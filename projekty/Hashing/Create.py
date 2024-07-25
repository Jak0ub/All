import hashlib
import random
import sys
import time
import platform
import os
platform_system = platform.system()
if platform_system == "Windows":
	def cisto():
		os.system("cls")
else:
	def cisto():
		os.system("clear")
while True:
	cisto()
	print(r"""     
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |
   | |\__,_|_|\_\___/ \__,_|_.__/ 
  _/ |                            
 |__/ 
""")
	print("**************************************")
	print("Typy hashování:\n|md5|\t\t|sha1|\t\t|sha224|\n|sha256|\t|sha384|\t|sha512|\n|sha3_224|\t|sha3_256|\t|sha3_384|\n|sha3_512|\n")
	print("|Q| == |QUIT|")
	str2hash = input("Zadej text, který chceš zahashovat: ")
	if str2hash.lower() == "q":
		sys.exit()
	hashing = input("Zadej hashovací algoritmus: ")
	if hashing.lower() == "q":
		sys.exit()
	if hashing == "md5":
	    result = hashlib.md5(str2hash.encode())
	elif hashing == "sha1":
	    result = hashlib.sha1(str2hash.encode())
	elif hashing == "sha224":
	    result = hashlib.sha224(str2hash.encode())
	elif hashing == "sha256":
	    result = hashlib.sha256(str2hash.encode())
	elif hashing == "sha384":
	    result = hashlib.sha384(str2hash.encode())
	elif hashing == "sha512":
	    result = hashlib.sha512(str2hash.encode())
	elif hashing == "sha3_224":
	    result = hashlib.sha3_224(str2hash.encode())	
	elif hashing == "sha3_256":
	    result = hashlib.sha3_256(str2hash.encode())
	elif hashing == "sha3_384":
	    result = hashlib.sha3_384(str2hash.encode())
	elif hashing == "sha3_512":
	    result = hashlib.sha3_512(str2hash.encode())
	else:
		print("neznámý typ hashování!")
		input()
		continue
	print(f"Hash {hashing} slova {str2hash} = {result.hexdigest()}")
	choice = input("chcete hash uložit do souboru?Y/n")
	if choice.lower() == "y":
		while True:
			name = input("|Pojmenuj si soubor s hashem|: ")
			try:
				with open(f"{name}.txt", "r", encoding="utf-8") as file:
					test = file.readlines()
			except FileNotFoundError:
				f = open(f"{name}.txt", "a")
				f.write(f"{result.hexdigest()}")
				f.close()
				input("uloženo")
				break
			print("\t|soubor již existuje|")
			continue
	

input()
