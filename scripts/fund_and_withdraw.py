from brownie import FundMe
from scripts.helpfulScripts import get_account

def fund():
    fund_me = FundMe[-1]
    account =get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(" entrace fee is ",entrance_fee)
    print("funding...")
    fund_me.fund({"from":account ,"value":entrance_fee} ,)
    
def with_draw():
        fund_me = FundMe[-1]
        account =get_account()
        print("withdrawing...")
        fund_me.withdraw({"from":account } ,)

        
    
    
    
def main():
    fund()
    with_draw()