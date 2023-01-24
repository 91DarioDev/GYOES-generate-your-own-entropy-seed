# GYOES: **G**enerate **Y**our **O**wn **E**ntropy **S**eed

This project permits to generate your own **BIP39 seed** using your own entropy of 256 bit. So that you don't have to trust any RNG to generate your mnemonic.

This is a python script that accepts as a parameter a string of 256 bits ( 01 ) created with your own entropy and generates a bip39 mnemonic seed.

## Usage example:
Pass your entropy as parameter. It should be a string of 256 bits (0 and 1 chars):

```
python3 main.py 001100...00110
```

## How to generate your own entropy:
The easier way to generate your own entropy to pass to the script is flipping a coin 256 times ( head=1, tail=0 ).

For better security run this script on a secure environment.

## Considerations:
Use this project at your own risk. 

I DON'T have any responsability of how you will use it and eventual money loss.

Don't use this project for your actual wallet if you don't know what you are doing!!
