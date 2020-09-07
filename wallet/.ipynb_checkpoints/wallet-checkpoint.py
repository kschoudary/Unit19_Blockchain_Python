# Homework-19, Blockchain with Python
# This file contains the Python code used in the Homework-19
# Developer - Subbaiah Choudary Kotha (KS)
# Date: September-7th, 2020

# Import Libraries
import constants from constants.py
import subprocess
import json
import os

# Set Folder where HD-WALLET is installed
os.chdir(r'C:\Users\kscho\SW')

# Display current directory for verification
pwd()

# Define the function - derive_wallets and use JSON Format

def derive_wallets(mnemonic, coin, numderive):
  
    command = 'php derive -g --mnemonic="' + mnemonic + '" --cols=path,address,privkey,pubkey --coin="' + coin + '" --numderive="' + str(numderive) + '" --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    
    keys = json.loads(output)
    return keys
    
# Set Variables
#
mnemonic = "crazy kitten zoo also rack load praise between decrease fringe opinion erosion"
#coin = "btc"
numderive = 3

# Call the Function with variable for ETH
coin='eth'
coins_eth=derive_wallets(mnemonic,coin,numderive)   
print("ETH Details")
print(coins_eth)

# Call the Function with variable for BTC-TEST
coin='btc-test'
coins_btc_test=derive_wallets(mnemonic,coin,numderive)  
print("BTC-TEST Details")
print(coins_btc_test)
