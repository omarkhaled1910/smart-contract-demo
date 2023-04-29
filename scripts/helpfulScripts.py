

from brownie import network ,accounts,config ,MockV3Aggregator
from web3 import Web3

descimals = 8
starting_price = 200000000
LOCAL_DEVELOPMENT_ENIROMENT=["development" ,"ganahe-local"]
FORKED_LOCAL_ENV = ["mainnet-fork"]

def get_account():
    if network.show_active() in  LOCAL_DEVELOPMENT_ENIROMENT or network.show_active() in  FORKED_LOCAL_ENV :
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])

def get_price_feed():
    if(network.show_active() not in LOCAL_DEVELOPMENT_ENIROMENT):
        return config["networks"][network.show_active()]["eth_use_rice_feed"]
    else:
        if(len(MockV3Aggregator)<=0):
            print("deploying mocks sucess ....")
            MockV3Aggregator.deploy(descimals,Web3.toWei(starting_price ,"ether") ,{"from":get_account()})
        print("deploying mocks sucess at" ,MockV3Aggregator[-1].address)
        return MockV3Aggregator[-1].address

 