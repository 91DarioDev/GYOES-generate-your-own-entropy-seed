# GYOES: **G**enerate **Y**our **O**wn **E**ntropy **S**eed

This project permits to generate your own **BIP39 seed** using your own entropy of 128 or 256 bit. So that you don't have to trust any RNG to generate your mnemonic.

This is a python script that accepts as a parameter a string of 128 or 256 bits ( 01 ) created with your own entropy and generates a bip39 mnemonic seed.

## 128 or 256 bit ?
An entropy of 128 bit will result in a seed of 12 words. A 256 bit entropy will result in a seed of 24 words.

**Despite 128 bit is still safe, I STRONGLY ADVICE TO GENERATE SEEDS 256 bit ENTROPY LENGTH because they are way more safe!!**

## Usage example:
Download the project as a zip, open a terminal in the directory and type:

```
python3 main.py
```

the follow the script instructions.

## Don't trust, verify!
The code is very minimal and simple so that can be reviewed. In order to avoid that you have to review the bip39 words list, it is in a separate file and you can just delete that one and download it again from https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt and save it as `english.txt`

## How to generate your own entropy:
The easier way to generate your own entropy to pass to the script is flipping a coin 256 times ( head=1, tail=0 ).

For better security run this script on a secure environment.

## Disclaimer:
Use this project at your own risk. 

I DON'T have any responsability of how you will use it and eventual money loss.

Don't use this project for your actual wallet if you don't know what you are doing!!
