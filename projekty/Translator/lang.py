import platform
import os
import random
import time
#proměnné
spravne = 0
chyby = 0
#konec proměnných a definice
def main():
	print(r'''    
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |
   | |\__,_|_|\_\___/ \__,_|_.__/ 
  _/ |                            
 |__/                            
''')
#Konec definic a kontrola systému
platform_system = platform.system()
if platform_system == "Windows":
	def cisto():
		os.system("cls")
else:
	def cisto():
		os.system("clear")
#Konec Detekce systému a kontrola slovíček
try:
	with open("words_configFile.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
except FileNotFoundError:
	f = open("words_configFile.txt", "a")
	f.close()
#Konec kontroly a ůvodní načítání	
cisto()
main()
time.sleep(0.6)
cisto()
print(r'''    
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_) 
  _/ |                            
 |__/                             
''')
time.sleep(0.6)
cisto()
print(r'''     
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _    _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)
  _/ |                            
 |__/                            
''')
time.sleep(0.6)
cisto()
print(r'''    
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _    _    _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)  (_)
  _/ |                            
 |__/                             
''')
time.sleep(0.6)
cisto()
#Konec úvodního načtení a main loop
while True:
	main()
	choice = input("Zadej číslo akce:\n |1| -> |Přidání slovíček|\n |2| -> |Odebrání slovíček| \n |3| -> |Začít procvičovat|\n |4| -> |Hledání dostupnosti slovíček| \n |5| -> |Vypsání aktuálních slovíček| \n\t")
	try:
		choice = int(choice)
	except ValueError:
		print("\t\tZadej ČÍSLO z nabídky!")
		time.sleep(1)		
		cisto()
		continue		
	if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
		print("\t\t1, 2, 3, 4 nebo 5!")
		time.sleep(1)		
		cisto()
		continue
	if choice == 1:
		cisto()
		main()
		print("|Q| -> |ukončení loopu|\n")
		while True:
			add = input("Zadej slovo: ")
			if add.lower() == "q":
				cisto()				
				break
			add1 = input("Zadej překlad slova: ")
			if add1.lower() == "q":
				cisto()				
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				radky.append(f"{add}:{add1},")
			with open("words_configFile.txt", "w", encoding="utf-8") as file:
				file.writelines(radky)
			print("\tZapsáno✔️\n")
	elif choice == 2:
		while True:
			cisto()
			main()
			radky2 = []
			success = False
			print("|Q| -> |ukončení loopu|\n")
			delete = input("Zadej slovo pro odstranění: ")
			if delete.lower() == "q":
				cisto()	
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				for i in range(len(radky)):
					sloupce = radky[i].strip().split(",")
					for sloup in sloupce:
						slup = sloup.split(":")
						try:
							one = slup[0]
							two = slup[1]
							if one.lower() == delete.lower() or two.lower() == delete.lower():
								pass
								success = True
							else:
								radky2.append(f"{one}:{two},")
						except IndexError:
							pass
				radky = radky2
			if success == True:
				with open("words_configFile.txt", "w", encoding="utf-8") as file:
					file.writelines(radky2)
				input("\tSmazáno✔️\n\t\tEnter pro pokračování")
			else:
				input("\tNenalezeno✖️\n\t\tEnter pro pokračování")					
	elif choice == 3:
		cisto()
		main()
		print("překlad slova:")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			for radek in radky:
				sloupy = radek.strip().split(",")
				cisla = []
				while len(cisla) != len(sloupy):
					cislo = random.randint(0, len(sloupy) - 1)
					if cislo in cisla:
						pass
					else:
						cisla.append(cislo)
				for i in range(len(cisla)):
					verify = cisla[i]
					sloup = sloupy[verify]
					hlavni = sloup.split(":")
					if len(hlavni) != 2:
						pass
					else:
						nahodne = random.randint(0, 1)
						if nahodne == 1:
							vedlejsi = hlavni[0]
							hlavni = hlavni[1]
						else:
							vedlejsi = hlavni[1]
							hlavni = hlavni[0]
						quest = input(f"|{hlavni}|: ")
						if quest.lower() == vedlejsi:
							print("\t✔️")
							spravne += 1
						else:
							print("\t✖️")
							chyby += 1
		if spravne == 0 and chyby == 0:
			cisto()
			main()
			input("Nejsou zadaná slova\n\tEnter pro pokračování")
			cisto()
		else:
			input(f"\n|Správně| -> |{spravne}|\n|Chyby| -> |{chyby}|")
			spravne = 0
			chyby = 0
			cisto()
	elif choice == 4:
		while True:
			cisto()
			main()
			print("|Q| -> |ukončení loopu|\n")
			search = input("Vyhledej slovíčko... ")
			if search.lower() == "q":
				cisto()
				break
			nalezeno = False
			while True:
				with open("words_configFile.txt", "r", encoding="utf-8") as file:
					radky = file.readlines()
					for i in range(len(radky)):
						sloupce = radky[i].strip().split(",")
						for sloupec in sloupce:
							try:
								jeden = sloupec.split(":")[0].strip()
								druhej = sloupec.split(":")[1].strip()
								if jeden.lower() == search.lower() or druhej.lower() == search.lower():
									nalezeno1 = jeden
									nalezeno2 = druhej
									nalezeno = True
							except IndexError:
								pass
				if nalezeno == False:
					input("\tNenalezeno✖️\n\t\tEnter pro pokračování")
					break
				else:
					input(f"\tNalezeno✔️: |{nalezeno1}| -> |{nalezeno2}|\n\t\tEnter pro pokračování")
					break
			cisto()
	elif choice == 5:
		cisto()
		main()
		print("Aktuální slovíčka\n")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			for i in range(len(radky)):
				sloupce = radky[i].strip().split(",")
				for sloupec in sloupce:
					try:
						jeden = sloupec.split(":")[0].strip()
						druhej = sloupec.split(":")[1].strip()
						print(f"|{jeden}| -> |{druhej}|")
					except IndexError:
						pass
		input("\nEnter pro pokračování")
		cisto()

#Jak0ub dne 04.09.2024
		
