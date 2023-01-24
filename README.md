# GYOES: generate your own entropy seed

This project permits to generate your own **BIP39 seed** using your own entropy of 256 bit. So that you don't have to trust any RNG to generate your mnemonic.

This is a python script that accepts as a first argument a string of 256 bits ( 01 ) created with your own entropy and generates a bip39 mnemonic seed.

Example: `python3 main.py 001100...00110`

## HOW TO GENERATE YOUR ENTROPY:
The easier way to generate your own entropy to pass to the script is flipping a coin 256 times ( head=1, tail=0 ).

For better security run this script on a secure environment.

## CONSIDERATIONS:
Use this project at your own risk. 

I DON'T have any responsability of how you will use it and eventual money loss.

Don't use this project for your actual wallet if you don't know what you are doing!!
