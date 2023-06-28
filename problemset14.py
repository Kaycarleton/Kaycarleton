import pandas_datareader as pdr
import sys
import time
import yfinance as yf
import os

watchlist_file=open('files/watchlist.txt')
watchlist_file.write(main)
watchlist_file.close()

watchlist_file=open('files/watchlist.txt')
categories=watchlist_file.readlines()
print(categories)

for index, word in enumerate(categories):
    print(f'{word}')

def display_menu():
    print("""
    1. Track Watchlist  
    2. Edit watchlist
    """)

def default():
  pass

def pharma():
    pass

def retail():
    print("Edit your list")

def technology():
    pass

def automotive():
    pass

watchlist={"1":default,"2":pharma,"3":retail, "4":technology, "5":automotive}

def main():
    while True:
        display_menu()
        choice=input("Enter a symbol here: ")
        if choice in "1234":
            watchlist[choice]()
        elif choice =='5':
            time.sleep(1)
            sys.exit()
        else:
            print("Enter a valid selection ")

if __name__=="__main__":
    main()