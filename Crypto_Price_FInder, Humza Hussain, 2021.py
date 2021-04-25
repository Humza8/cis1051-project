
import requests
import json
import os
import time

api_url = 'https://api.coingecko.com/api/v3/simple/price?ids='

#The api used is from https://www.coingecko.com/en/api#explore-api
#api_key = 1c88999c-b126-425c-9274-1be5025d92d3

crypto = ["BITCOIN", "ETHEREUM", "DOGECOIN","LITECOIN", "CHAINLINK", "CARDANO", "POLKADOT"]
lst = ["YES", "NO", "N","Y"]
currency= ["usd","eur", "jpy", "aud", "pkr","chf", "aed", "rub", "inr"] 

print("Welcome to Humza's Cryptocurrency finder!")
print("Supported Crypto's include: Bitcoin, Ethereum, Dogecoin, Litecoin, Chainlink,Cardano, and Polkadot")
print("")
coin = input("Which cryptocurrency would you like to search: ")
coin = coin.upper()
def validate_coin(coin):
     while coin not in crypto:
        coin = input("Invalid entry' what cryptocurrency would you like to look at: ")
        coin = coin.upper()
     else:
         return coin
coin = validate_coin(coin)

print("")
print("We can display price in usd, eur, jpy, aud, pkr, chf, aed, rub, inr")
cur = input("what fiat currency do you want to use?")
cur = cur.lower()

def validate_cur(cur):
    while cur not in currency:
            print("invalid option; please try again")
            cur = input("what fiat currency do you want to use")
            cur = cur.lower()
    else:
        return cur
cur = validate_cur(cur)
print("")

market = input("do you want to see the marketcap?")
market = market.upper()
def validate_market(market):
    while market not in lst:
        print("Invalid entry, please enter again.")
        market = input("Do you want to see marketcap?")
        market = market.upper()
    else:
        if market == "Y" or market == "YES":
            market = "true"
            return market
        elif market == "N" or market == "NO":
            market = "false"
            return market
market = validate_market(market)

change = input("Do you want to see the 24 hour change in price?")
change = change.upper()
def validate_change(change):
    while change not in lst:
        print("Invalid entry, please enter again.")
        change = input("Do you want to see the 24 hour change in price?")
        change = change.upper()
    else:
        if change == "Y" or change == "YES":
            change = "true"
            return change
        elif change == "N" or change == "NO":
            change = "false"
            return change

change = validate_change(change)

def get_change(coin,cur,change):
    if change == "true":
        coin = coin.lower()
        t = requests.get(api_url + coin + "&vs_currencies=" +cur+"&include_market_cap=false" + "&include_24hr_change=" + change).text
        t = json.loads(t)
        
        return(t[coin][cur +"_24h_change"])
    else:
        pass



def info(coin,cur,market):
    
    print("gathering information...")
    coin = coin.lower()
    return (get_coin(coin,cur,market))
        

def get_coin(coin,cur,market):
    response = requests.get(api_url + coin + "&vs_currencies=" +cur+"&include_market_cap="+market).text
    #response_json = response.json()
    response_json = json.loads(response)
    

    return response_json[coin][cur]

def get_marketcap(coin,cur,market):
    if market == "true":
        coin = coin.lower()
        t = requests.get(api_url + coin + "&vs_currencies=" +cur+"&include_market_cap="+market).text
        t = json.loads(t)
        
        return(t[coin][cur +"_market_cap"])
    else:
        pass
x = get_marketcap(coin,cur,market)

print("")
print("The price of", coin, "in", cur, "is", info(coin,cur,market))
print("")
if market == "true":
    print("The market cap of", coin, "in", cur, "is", x)
else:
    pass

print("")
if change == "true":
    y = float(get_change(coin,cur, change))
    form = "{:.2f}".format(y)
    print("The price of", coin, "has changed", form, "percent over the past 24 hours.")
else:
    pass

def validate_ans(ans):
    while ans not in lst:
        print("Invalid entry, enter again:")
        ans = input("Do you want to search another coin?")
        ans = ans.upper()
    else:
        return ans

ans = input("Do you want to search another coin? ")
ans = ans.upper()
while ans not in lst:
    ans = input("Invalid entry; would you like to look at another coin? ")
    ans = ans.upper()
else:
    while ans == "YES" or ans == "Y":
        coin = input("Enter another coin: ")
        coin = coin.upper()
        coin = validate_coin(coin)
        print("")
        cur = input("What fiat currency do you want to use? ")
        cur = cur.lower()
        cur = validate_cur(cur)
        print("")
        market = input("Do you want to see marketcap?")
        market = market.upper()
        market = validate_market(market)
        change = input("Do you want to see the 24 hour change in price?")
        change= change.upper()
        change = validate_change(change)
        print("")
        print("The price of", coin, "in", cur, "is", info(coin,cur,market))
        print("")
        x = get_marketcap(coin,cur,market)
        if market == "true":
            print("The market cap of", coin, "in", cur, "is", x)
        else:
            pass
        print("")
        if change == "true":
            y=float(get_change(coin,cur,change))
            form = "{:.2f}".format(y)
            print("The price of", coin, "has changed", form, "percent over the past 24 hours.")
        else:
            pass
        ans = input("Do you want to search another coin? ")
        ans = ans.upper()
        ans = validate_ans(ans)
    else:
        if ans =="N" or ans == "NO":
            print("Thank you for using this Humza's Crypto!")

#https://drive.google.com/file/d/1v10bIwSmtqG5V07Yq55djcWtAnAx7r4t/view

