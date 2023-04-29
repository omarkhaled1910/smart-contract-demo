
from brownie import FundMe ,accounts,config 
from scripts.helpfulScripts import get_account ,get_price_feed

def deploy_fund_me():
    account = get_account()
    deployed_address = FundMe.deploy( get_price_feed(),{"from":account})
    print("contract deployed at adress >>", deployed_address)
    print(deployed_address.getVersion())


def main():
    print("start" ,get_account())
    deploy_fund_me()
    print("end")
