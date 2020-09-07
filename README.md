# Unit19_Blockchain_Python
Homework Assignment Unit# 19 with Block Chain Transactions using Python
Developer: Subbaiah Choudary Kotha (KS)
Date Created: 8/30/2020


Dependencies: The following 3 SW libraries are already installed on this laptop as part of class work
-	PHP 
-	Bit (Python Bitcoin library) 
-	Web3 (Python Ethereum Library) 
Repo Folder: C:\Users\kscho\Documents\github_files\Unit19_Blockchain_Python
Create a new folder and name it as – wallet
Step-1:  Open GitBash and run the following commands:
-	cd C:/Users/kscho/Documents/github_files/Unit19_Blockchain_Python/wallet
-	git clone https://github.com/dan-da/hd-wallet-derive
-	cd hd-wallet-derive
-	php -r "readfile('https://getcomposer.org/installer');" | php
-	php -d pcre.jit=0 composer.phar install
Create sumlink – derive in the parent folder (wallet)
-	cd . (go to parent folder)
-	ln -s hd-wallet-derive/hd-wallet-derive.php derive

Step-2:  Generate Mnemonic 
-	Generate mnemonic with 12 words from https://iancoleman.io/bip39/
BIP39 Mnemonic
crazy kitten zoo also rack load praise between decrease fringe opinion erosion
BIP39 Seed: 
31e192d24866b0652d4b351389f63f7f1cc751f5e37e3c642820bbe7bf417e5c711ee9f4306032eac27cc963982e23a5a1e2e123e1a1b3357dc6434378a49f3a
Coin: Bit Coin
BIP32 Root Key
xprv9s21ZrQH143K3VmAQB2yu9KFkKRduE6E4qcEYX5pBJJFm7F3dpe6rppEJQFM9fv5nx4ZtM8scoDoMRBwj5ugb9RUDjZR1zv1FhJCs88FnkW

Step-3:  Add the above mnemonic words to the .env file
	MNEMONIC="crazy kitten zoo also rack load praise between decrease fringe opinion erosion"
Step-4:  Develop code in constants.py
Step-5:  Develop code in wallet.py
 
