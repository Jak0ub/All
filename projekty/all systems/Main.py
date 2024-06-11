import random
import math
import os
import time
import platform
import sys
os.system("title Matematika")
i = 0
list_pocet = []
post = 0
numero = 0
okos = 0
znovu = False
uvod_list = []	
status = []
chybas = []
vypocet = []
answer = []
jop = []
casy = []
lima = []
platform_system = platform.system()
if platform_system == "Windows":
	def cisto():
		os.system("cls")
else:
	def cisto():
		os.system("clear")
#Úvodní načtení
cisto()
print("""     
__________        ___          __  ___     _________     __     __    ______
\_______  |      /   \        |  |/  /    /   ___   \   |  |   |  |  |   __ \ 
       |  |     /  _  \       |  |  /     |  |   |  |   |  |   |  |  |  |__| |
       |  |    /  /_\  \      |    /      |  |   |  |   |  |   |  |  |    __/
       |  |   /  _____  \     |    \      |  |   |  |   |  |   |  |  |   _  \ 
 ____  /  |  /  /     \  \    |  |  \     |  |   |  |   |  |   |  |  |  | \  \      
 \   \/  /  /  /       \  \   |  |\  \    |  |___|  |   |  \___/  |  |  |__|  |     
  \_____/  /__/         \__\  |__| \__\   \_________/   \_________/  |_______/     
       
""")
time.sleep(0.6)
cisto()
print("""     
__________        ___          __  ___     _________     __     __    ______
\_______  |      /   \        |  |/  /    /   ___   \   |  |   |  |  |   __ \ 
       |  |     /  _  \       |  |  /     |  |   |  |   |  |   |  |  |  |__| |
       |  |    /  /_\  \      |    /      |  |   |  |   |  |   |  |  |    __/
       |  |   /  _____  \     |    \      |  |   |  |   |  |   |  |  |   _  \ 
 ____  /  |  /  /     \  \    |  |  \     |  |   |  |   |  |   |  |  |  | \  \       __
 \   \/  /  /  /       \  \   |  |\  \    |  |___|  |   |  \___/  |  |  |__|  |     /  \ 
  \_____/  /__/         \__\  |__| \__\   \_________/   \_________/  |_______/      \__/
       
""")
time.sleep(0.6)
cisto()
print("""     
__________        ___          __  ___     _________     __     __    ______
\_______  |      /   \        |  |/  /    /   ___   \   |  |   |  |  |   __ \ 
       |  |     /  _  \       |  |  /     |  |   |  |   |  |   |  |  |  |__| |
       |  |    /  /_\  \      |    /      |  |   |  |   |  |   |  |  |    __/
       |  |   /  _____  \     |    \      |  |   |  |   |  |   |  |  |   _  \ 
 ____  /  |  /  /     \  \    |  |  \     |  |   |  |   |  |   |  |  |  | \  \     __    __
 \   \/  /  /  /       \  \   |  |\  \    |  |___|  |   |  \___/  |  |  |__|  |   /  \  /  \ 
  \_____/  /__/         \__\  |__| \__\   \_________/   \_________/  |_______/    \__/  \__/
       
""")
time.sleep(0.6)
cisto()
print("""     
__________        ___          __  ___     _________     __     __    ______
\_______  |      /   \        |  |/  /    /   ___   \   |  |   |  |  |   __ \ 
       |  |     /  _  \       |  |  /     |  |   |  |   |  |   |  |  |  |__| |
       |  |    /  /_\  \      |    /      |  |   |  |   |  |   |  |  |    __/
       |  |   /  _____  \     |    \      |  |   |  |   |  |   |  |  |   _  \ 
 ____  /  |  /  /     \  \    |  |  \     |  |   |  |   |  |   |  |  |  | \  \     __    __    __
 \   \/  /  /  /       \  \   |  |\  \    |  |___|  |   |  \___/  |  |  |__|  |   /  \  /  \  /  \ 
  \_____/  /__/         \__\  |__| \__\   \_________/   \_________/  |_______/    \__/  \__/  \__/ 
       
""")
time.sleep(0.6)
cisto()
#Konec úvodního načítání
chyby = 0
chybys = 0
rak = 0
editace = False
testrun = False
hlaseni = "NIC NEOBSAHUJE"
developer = False
otz = "nic"
zpet = False
#definice
def soubor_poskozen():
	OLA = input(f"Konfigurační soubor je poškozen!\n\n|Hlášení|:{hlaseni} ")
	if OLA.lower() == "remake":
		f = open("config.txt", "a")
		f.write("\n\n\n\n\n\n\n\n\n")
		f.close()
		with open("config.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			radky[0] = "ANO\n"
			radky[1] = "PEN:2\n"
			radky[2] = "UV:TEXT1\n"
			radky[3] = "UV:TEXT2\n"
			radky[4] = "UV:TEXT3\n"
			radky[5] = "1:ON\n"
			radky[6] = "2:ON\n"
			radky[7] = "3:OFF\n"
			radky[8] = "1=10\n"
			radky[9] = "2=20\n"
			radky[10] = "Lehká=1-10\n"
			radky[11] = "Střední=10-100\n"
			radky[12] = "Těžká=100-1000\n"
		with open("config.txt", "w", encoding="utf-8") as file:
			file.writelines(radky)
		animace_zmeny()
		sys.exit()
	print("Pro defaultní nastavení souboru napiště při chybovém hlášení:|REMAKE|: ")
	time.sleep(2)
	sys.exit()
def cls():
	cisto()
def animace_zmeny():
	cls()
	print("Zapisuji změny")
	time.sleep(0.5)
	cls()
	print("Zapisuji změny.")
	time.sleep(0.5)
	cls()
	print("Zapisuji změny..")
	time.sleep(0.5)
	cls()
	print("Zapisuji změny...")
	time.sleep(0.5)
	cls()
	print("Změny byly zapsány")
	time.sleep(0.5)
def kontrola_konec(var):
	if var.lower() == "koncim" or var.lower() == "končim":
		sys.exit()
#Kontrola Konfiguračního souboru
try:
	with open("config.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
		try:
			ok1 = radky[0]
			ok2 = radky[1]
			ok3 = radky[2]
			ok4 = radky[3]
			ok5 = radky[4]
			ok6 = radky[5]
			ok7 = radky[6]
			ok8 = radky[7]
			ok9 = radky[8]
			ok10 = radky[9]
			ok11 = radky[10]
			ok12 = radky[11]
			ok13 = radky[12]
		except IndexError:
			hlaseni = "Někde něco kompletně chybí! "
			soubor_poskozen()
		try:
			if radky[0].lower().strip() == "ano":
				developer = True
			elif radky[0].lower().strip() == "ne":
				developer = False
			else:
				hlaseni = f"Na první řádce není ANO nebo NE"
				soubor_poskozen()
		except IndexError:
			hlaseni = f"První řádek neobsahuje ANO nebo NE! "
			soubor_poskozen()
		try:
			one = radky[1].strip().split("PEN:")[1]
		except IndexError:
			hlaseni = f"2.řádek -> není pojmenován PEN:(Číslo[penalizace])"
			soubor_poskozen()
		try:
			one = int(one)
		except ValueError:
			hlaseni = f"2.řádek -> není zde číslo pro penalizaci -> PEN:(Číslo)"
			soubor_poskozen()
		try:
			two = radky[2].strip().split("UV:")[1]
			three = radky[3].strip().split("UV:")[1]
			four = radky[4].strip().split("UV:")[1]
		except IndexError:
			hlaseni = f"3/4 nebo 5.řádek nezačíná UV:(Úvodní zpráva)"
			soubor_poskozen()
		try:
			five = radky[5].strip().split("1:")[1]
			six = radky[6].strip().split("2:")[1]
			seven = radky[7].strip().split("3:")[1]
		except IndexError:
			hlaseni = f"6/7 nebo 8.řádek nezačíná 1/2/3:(6.řádek má být 1:, 7. 2: atd)"
			soubor_poskozen()
		if five != "ON" and five != "OFF":
			hlaseni = f"6.řádek neobsahuje ON nebo OFF pro identifikaci zaplé uvítací zprávy"
			soubor_poskozen()
		elif six != "ON" and six != "OFF":
			hlaseni = f"7.řádek neobsahuje ON nebo OFF pro identifikaci zaplé uvítací zprávy"
			soubor_poskozen()
		elif seven != "ON" and seven != "OFF":
			hlaseni = f"8.řádek neobsahuje ON nebo OFF pro identifikaci zaplé uvítací zprávy"
			soubor_poskozen()
		try:
			eight = radky[8].strip().split("1=")[1]
			nine = radky[9].strip().split("2=")[1]
		except IndexError:
			hlaseni = f"9. nebo 10.řádek nezačíná 1/2="
			soubor_poskozen()
		try:
			eight = int(eight)
			nine = int(nine)
		except ValueError:
			hlaseni = f"9. nebo 10.řádek neobsahuje číslo"
			soubor_poskozen()
		if eight > nine:
			hlaseni = f"9.řádek nesmí být větší číslo než 10.řádek"
			soubor_poskozen()
		elif eight <= 0:
			hlaseni = f"9.řádek nesmí být menší nebo rovno nule!"
			soubor_poskozen()
		try:
			ten = ok11.strip().split("=")[1]
			eleven = ok12.strip().split("=")[1]
			twelve = ok13.strip().split("=")[1]
		except IndexError:
			hlaseni = f"Něco je kompletně špatně na 10/11 nebo 12.řádce (takto má vypadat|EASY=1-10|)"
			soubor_poskozen()
		ten = ten.split("-")
		eleven = eleven.split("-")
		twelve = twelve.split("-")

		try:
			ten_1 = int(ten[0])
			ten_2 = int(ten[1])
			eleven_1 = int(eleven[0])
			eleven_2 = int(eleven[1])
			twelve_1 = int(twelve[0])
			twelve_2 = int(twelve[1])
		except ValueError:
			hlaseni = f"10/11 nebo 12.řádek neobsahuje číslo za =(takto to má vypadat|EASY=1-10|)"
			soubor_poskozen()
		if ten_2 < ten_1:
			hlaseni = f"10.řádek má první číslo větší nebo rovno druhému, VZOR:|EASY=1-10|"
			soubor_poskozen()
		elif ten_2 <= 0 or ten_1 <= 0:
			hlaseni = f"10.řádek nesmí obsahovat číslo menší nebo rovno nule VZOR:|EASY=1-10|"
			soubor_poskozen()
		if eleven_2 <= eleven_1:
			hlaseni = f"11.řádek má první číslo větší nebo rovno druhému, VZOR:|EASY=1-10|"
			soubor_poskozen()
		elif eleven_2 <= 0 or eleven_2 <= 0:
			hlaseni = f"11.řádek nesmí obsahovat číslo menší nebo rovno nule VZOR:|EASY=1-10|"
			soubor_poskozen()
		if twelve_2 <= twelve_1:
			hlaseni = f"12.řádek má první číslo větší nebo rovno druhému, VZOR:|EASY=1-10|"
			soubor_poskozen()
		elif twelve_2 <= 0 or twelve_1 <= 0:
			hlaseni = f"12.řádek nesmí obsahovat číslo menší nebo rovno nule VZOR:|EASY=1-10|"
			soubor_poskozen()
		
		
		
		
except FileNotFoundError:
	print("Konfigurační soubor nebyl nalezen")
	oka = input("Přejete si soubor vytvořit?\nA|N: ")
	if oka.lower() == "a":
		f = open("config.txt", "a")
		f.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		f.close()
		with open("config.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			radky[0] = "ANO\n"
			radky[1] = "PEN:2\n"
			radky[2] = "UV:TEXT1\n"
			radky[3] = "UV:TEXT2\n"
			radky[4] = "UV:TEXT3\n"
			radky[5] = "1:ON\n"
			radky[6] = "2:ON\n"
			radky[7] = "3:OFF\n"
			radky[8] = "1=10\n"
			radky[9] = "2=20\n"
			radky[10] = "Lehká=1-10\n"
			radky[11] = "Střední=10-100\n"
			radky[12] = "Těžká=100-1000\n"
		with open("config.txt", "w", encoding="utf-8") as file:
			file.writelines(radky)
		animace_zmeny()
		sys.exit()
	sys.exit()
with open("config.txt", "r", encoding="utf-8") as file:
	radky = file.readlines()
	penalizace_1 = [radek.strip() for radek in radky if radek.startswith("PEN:")]
	for penal in penalizace_1:
		skios = (penal.split("PEN:")[1].strip())
		skios = int(skios)
if developer == True:
	while True:
		if testrun == True:
			break
		elif post == 0:
			post += 1
			cls()
			dev_tools = input("Vítejte v developerském menu, zadejte příkaz\n\n|Pro navigační menu napište(dev.tools:menu)|\n|Pro vypnutí dev.tools napište(dev.tools:turn_off)|\n|Pro ukončení napište(končim)|\n ")
		elif post > 0:
			dev_tools = input()
		if dev_tools.lower() == "dev.tools:turn_off":
			with open("config.txt", "r", encoding="utf-8") as dev:
				radky = dev.readlines()
			radky[0] = "NE\n"
			with open("config.txt", "w", encoding="utf-8") as dev:
				dev.writelines(radky)
			animace_zmeny()
			input("Pro zapnutí napište při uvítací zprávě(dev.tools:turn_on)")
			sys.exit()	
		elif dev_tools.lower() == "koncim" or dev_tools.lower() == "končim":
			sys.exit()
		elif dev_tools.lower() == "dev.tools:menu":
			while True:
				post = 0
				cls()
				menu = input("Zadejte jednu z možností:\n\n|Testovací spuštění -> dev.tools:testrun|\n|Úprava obtížností -> dev.tools:diff|\n|Úprava penalizace za přeskočení -> dev.tools:skip|\n|Úprava možnosti počtu příkladů -> dev.tools:count|\n|Vypnutí/Úprava jednotlivých informačních zpráv -> dev.tools:inform|\n|exit z menu -> exit|\n")
				kontrola_konec(menu)
				if menu.lower() == "dev.tools:diff":
					while True:
						cls()
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							ob1 = radky[10].strip().split("=")[0]
							ci1 = radky[10].strip().split("=")[1]
							ob2 = radky[11].strip().split("=")[0]
							ci2 = radky[11].strip().split("=")[1]
							ob3 = radky[12].strip().split("=")[0]
							ci3 = radky[12].strip().split("=")[1]
						print(f"Aktuální obtížnosti\n|{ob1} -> {ci1}|\n|{ob2} -> {ci2}|\n|{ob3} -> {ci3}|")
						inp = input("\n\nZadejte operaci:\n|cislo:nickname -> změna pojmenování obtížnosti|\n|cislo:range -> změna rozmezí|\n|exit -> zpět do menu|\n")
						if inp.lower() == "exit":
							break
						elif inp.lower() == "1:nickname":
							while True:
								cls()
								oks = input(f"Zadejte nové pojmenování obtížnosti |{ob1}|: ")
								if oks.lower().strip() == ob2.lower() or oks.lower().strip() == ob3.lower():
									cls()
									print("Toto jméno je již používáno(Nezáleží na CapsLocku-> AHOJ=ahoj)")
									time.sleep(3)
									continue
								else:
									break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[10] = f"{oks}={ci1}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif inp.lower() == "2:nickname":
							while True:
								cls()
								oks = input(f"Zadejte nové pojmenování obtížnosti |{ob2}|: ")
								if oks.lower().strip() == ob1.lower() or oks.lower().strip() == ob3.lower():
									cls()
									print("Toto jméno je již používáno(Nezáleží na CapsLocku-> AHOJ=ahoj)")
									time.sleep(3)
									continue
								else:
									break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[11] = f"{oks}={ci2}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif inp.lower() == "3:nickname":
							while True:
								cls()
								oks = input(f"Zadejte nové pojmenování obtížnosti |{ob3}|: ")
								if oks.lower().strip() == ob2.lower() or oks.lower().strip() == ob1.lower():
									cls()
									print("Toto jméno je již používáno(Nezáleží na CapsLocku-> AHOJ=ahoj)")
									time.sleep(3)
									continue
								else:
									break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[12] = f"{oks}={ci3}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()

						elif inp.lower() == "1:range":
							while True:
								cls()
								inp2 = input("Zadejte první číslo >|1|< - 10: ")
								try:
									inp2 = int(inp2)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp2) == int:
									if inp2 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									else:
										break
							while True:
								cls()
								inp3 = input("Zadejte druhé číslo 1- >|10|<: ")
								try:
									inp3 = int(inp3)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp3) == int:
									if inp3 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									elif inp3 <= inp2:
										cls()
										print(f"2.Číslo nesmí být menší nebo rovno prvnímu číslu!|{inp2}| !")
										time.sleep(1)
										cls()
										continue
							
									else:
										break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[10]= f"{ob1}={inp2}-{inp3}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif inp.lower() == "2:range":
							while True:
								cls()
								inp2 = input("Zadejte první číslo >|1|< - 10: ")
								try:
									inp2 = int(inp2)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp2) == int:
									if inp2 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									else:
										break
							while True:
								cls()
								inp3 = input("Zadejte druhé číslo 1- >|10|<: ")
								try:
									inp3 = int(inp3)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp3) == int:
									if inp3 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									elif inp3 <= inp2:
										cls()
										print(f"2.Číslo nesmí být menší/rovno prvnímu číslu!|{inp2}| !")
										time.sleep(1)
										cls()
										continue
							
									else:
										break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[11]= f"{ob2}={inp2}-{inp3}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif inp.lower() == "3:range":
							while True:
								cls()
								inp2 = input("Zadejte první číslo >|1|< - 10: ")
								try:
									inp2 = int(inp2)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp2) == int:
									if inp2 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									else:
										break
							while True:
								cls()
								inp3 = input("Zadejte druhé číslo 1- >|10|<: ")
								try:
									inp3 = int(inp3)
								except ValueError:
									cls()
									print("Zadejte číslo!")
									time.sleep(1)
									cls()
									continue
								if type(inp3) == int:
									if inp3 <= 0:
										cls()
										print("Číslo nesmí být menší než 0!")
										time.sleep(1)
										cls()
										continue
									elif inp3 <= inp2:
										cls()
										print(f"2.Číslo nesmí být menší/rovno prvnímu číslu!|{inp2}| !")
										time.sleep(1)
										cls()
										continue
							
									else:
										break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[12]= f"{ob3}={inp2}-{inp3}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						else:
							cls()
							print("neznám")
							time.sleep(1)
							cls()
							continue
				elif menu.lower() == "dev.tools:testrun":
					cls()
					print("Jdeme na to!")
					time.sleep(1)
					cls()
					testrun = True
					break
				elif menu.lower() == "dev.tools:count":
					while True:
						cls()
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							jednicka = radky[8].strip().split("1=")[1]
							dvojka = radky[9].strip().split("2=")[1]
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							print(f"Aktuální rozmezí příkladů -> |{jednicka}-{dvojka}|")
						moz = input("\n\nMoznosti:\n|Úprava -> edit|\n|zpět do menu -> exit|\n")
						if moz.lower() == "edit":
							cls()
							while True:
								cls()
								jep = input("Zadejte první číslo >|1|< -10: ")
								try:
									jep = int(jep)
								except ValueError:
									cls()
									print("celé číslo a jen číslo!")
									time.sleep(2)
									cls()
									continue
								if type(jep) == int:
									break
							while True:
								cls()
								jes = input("Zadejte druhé číslo 1- >|10|<: ")
								try:
									jes = int(jes)
								except ValueError:
									cls()
									print("Celé číslo a jen číslo")
									time.sleep(2)
									cls()
									continue
								if type(jes) == int:
									if jes < jep:
										print("druhé číslo nesmí být menší než první!")
										time.sleep(2)
										cls()
										continue
									else:
										break
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[8] = f"1={jep}\n"
								radky[9] = f"2={jes}\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif moz.lower() == "exit":
							cls()
							break
						else:
							cls()
							print("neznám")
							time.sleep(2)
							cls()
							continue
				elif menu.lower() == "dev.tools:skip":
					while True:
						cls()
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							penalizace = [radek.strip() for radek in radky if radek.startswith("PEN:")]
							for penal in penalizace:
								uvodni_text = (penal.split("PEN:")[1].strip())
						choi = input(f"Stará penalizace za přeskočení |{uvodni_text}s|\n|edit -> nastavíte novou penalizaci|\n|exit -> vrátíte se zpět do menu|\n")
						if choi.lower() == "exit":
							break
						elif choi.lower() == "koncim" or choi.lower() == "končim":
							sys.exit()
						elif choi.lower() == "edit":
							while True:
								cls()
								pen = input("Zadejte novou penalizaci: ")
								try:
									pen = int(pen)
								except ValueError:
									cls()
									print("Celým číslem a pouze číselně")
									time.sleep(2)
									continue
								if type(pen) == int:
									with open ("config.txt", "r", encoding="utf-8") as file:
										radky = file.readlines()
										radky[1] = f"PEN:{pen}\n"	
									with open("config.txt", "w", encoding="utf-8") as file:
										file.writelines(radky)
									cls()
									input(f"Pokud máš v úvodních zprávách zmíněn čas přičtený za přeskočení\nUpdatuj tu změnu, aby uživatel vědel kolik je skutečná penalizace")
									animace_zmeny()
									break
				elif menu.lower() == "dev.tools:inform":
					cls()
					while True:
						cls()
						print("Aktuální uvítací zprávy:")
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							uvody = [radek.strip() for radek in radky if radek.startswith("UV:")]
							jop.append(radky[5].strip())
							jop.append(radky[6].strip())
							jop.append(radky[7].strip())
							for uvod in uvody:
								okos += 1
								list_pocet.append(okos)
								uvodni_text = (uvod.split("UV:")[1].strip())
								print(f"|{uvodni_text}| |{jop[-1+okos]}|")
						print("")
						while True:
							choice = input("Moznosti:\n|editace -> cislo:edit|\n|Vypnutí jednnotlivých zpráv -> cislo:turn_on/turn_off|\n|Zpět do menu -> exit|\n")
							if choice.lower() == "1:turn_on" or choice.lower() == "1:turn_off":
								with open("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									if choice.lower() == "1:turn_on":
										if radky[5].strip() == "1:ON":
											cls()
											print("text 1 už je zapnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[5] = "1:ON\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
									elif choice.lower() == "1:turn_off":
										if radky[5].strip() == "1:OFF":
											cls()
											print("text 1 už je vypnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[5] = "1:OFF\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
							elif choice.lower() == "2:turn_on" or choice.lower() == "2:turn_off":
								with open("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									if choice.lower() == "2:turn_on":
										if radky[6].strip() == "2:ON":
											cls()
											print("text 2 už je zapnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[6] = "2:ON\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
									elif choice.lower() == "2:turn_off":
										if radky[6].strip() == "2:OFF":
											cls()
											print("text 2 už je vypnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[6] = "2:OFF\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
							elif choice.lower() == "3:turn_on" or choice.lower() == "3:turn_off":
								with open("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									if choice.lower() == "3:turn_on":
										if radky[7].strip() == "3:ON":
											cls()
											print("text 3 už je zapnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[7] = "3:ON\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
									elif choice.lower() == "3:turn_off":
										if radky[7].strip() == "3:OFF":
											cls()
											print("text 3 už je vypnut")
											time.sleep(2)
											cls()
											znovu = True
										else:
											with open("config.txt", "r", encoding="utf-8") as file:
												radky = file.readlines()
												radky[7] = "3:OFF\n"
											with open("config.txt", "w", encoding="utf-8") as file:
												file.writelines(radky)
												animace_zmeny()
												znovu = True
							elif choice.lower() == "1:edit":
								cls()
								osloa = input("zadejte novou zprávu:\n ")
								with open ("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									radky[2] = f"UV:{osloa}\n"	
								with open("config.txt", "w", encoding="utf-8") as file:
									file.writelines(radky)
								cls()
								animace_zmeny()
								break
							elif choice.lower() == "2:edit":
								cls()
								osloa = input("zadejte novou zprávu:\n ")
								with open ("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									radky[3] = f"UV:{osloa}\n"	
								with open("config.txt", "w", encoding="utf-8") as file:
									file.writelines(radky)
								cls()
								animace_zmeny()
								break
							elif choice.lower() == "3:edit":
								cls()
								osloa = input("zadejte novou zprávu:\n ")
								with open ("config.txt", "r", encoding="utf-8") as file:
									radky = file.readlines()
									radky[4] = f"UV:{osloa}\n"	
								with open("config.txt", "w", encoding="utf-8") as file:
									file.writelines(radky)
								cls()
								animace_zmeny()
								break
							elif choice.lower() == "koncim":
								sys.exit()
							elif choice.lower() == "exit":
								break
							else:
								cls()
								print("neznám")
								time.sleep(2)
								cls()
							if znovu == True:
								znovu = False
								break
						
						if choice.lower() == "exit":
							break
						elif znovu == True:
							znovu = False
							continue
							
								
							
				elif menu.lower() == "exit":
					zpet = True
					break

				else:
					cls()
					print("neznám")
					time.sleep(2)
					cls()
					continue
				
			if zpet == True:
				continue
		else:
			cls()
			print("neznám")
			post = 0
			time.sleep(2)
			cls()
			continue	

if developer == False or testrun == True:
	with open("config.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
		uvody = [radek.strip() for radek in radky if radek.startswith("UV:")]
		for uvod in uvody:
			numero += 1
			with open("config.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				if radky[4+numero].strip() == f"{numero}:ON":
					cls()
					uvodni_text = (uvod.split("UV:")[1].strip())
					mozne = input(f"{uvodni_text}")
					if mozne == "dev.tools:turn_on":
						with open("config.txt", "r", encoding="utf-8") as file:
							radky = file.readlines()
							radky[0] = "ANO\n"
						with open("config.txt", "w", encoding="utf-8") as file:
							file.writelines(radky)
							animace_zmeny()
							sys.exit()
cls()
while True:
	cls()
	with open("config.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
		jednicka = radky[8].strip().split("1=")[1]
		dvojka = radky[9].strip().split("2=")[1]
	olas = input(f"Kolik chceš příkladů?\n|{jednicka}-{dvojka}| ")
	jednicka = int(jednicka)
	dvojka = int(dvojka)
	try:
		olas = int(olas)
	except ValueError:
		cls()
		print("ZADEJ ČÍSLO")
		time.sleep(1)
		continue
	if type(olas) == int:
		if olas >= jednicka and olas <= dvojka:
			break
		else:
			cls()
			print(f"{jednicka}-{dvojka}!")
			time.sleep(1)
cls()
with open("config.txt", "r", encoding="utf-8") as file:
	radky = file.readlines()
	ob1 = radky[10].strip().split("=")[0]
	ci1 = radky[10].strip().split("=")[1]
	ob2 = radky[11].strip().split("=")[0]
	ci2 = radky[11].strip().split("=")[1]
	ob3 = radky[12].strip().split("=")[0]
	ci3 = radky[12].strip().split("=")[1]
	num1 = ci1.split("-")[0]
	num2 = ci2.split("-")[0]
	num3 = ci3.split("-")[0]
	os1 = int(radky[10].strip().split("-")[1])
	os2 = int(radky[11].strip().split("-")[1])
	os3 = int(radky[12].strip().split("-")[1])
	
while True:
	osm = input(f"Jakou chceš obtížnost?\n{ob1} -> čísla od {ci1}\n{ob2} -> čísla od {ci2}\n{ob3} -> čísla od {ci3}\n|{ob1}|{ob2}|{ob3}|: ")
	if osm.lower() == ob1.lower():
		obtiznost = os1
		omo = f"{ob1}"
		odm = 10
		jedos = int(num1)
		break
	elif osm.lower() == ob3.lower():
		obtiznost = os3
		odm = 30
		jedos = int(num3)
		omo = f"{ob3}"
		break
	elif osm.lower() == ob2.lower():
		obtiznost = os2
		omo = f"{ob2}"
		odm = 20
		jedos = int(num2)
		break
	else:
		cls()
		print("Zadej jednu z obtížností!")
		time.sleep(2)
		cls()
konec = False
k = 1
odmocniny = []
for j in range(1, odm):
	k += 1
	odmocniny.append(k ** 2)
cls()	
skips = 0
print("3")
time.sleep(1)
cls()
print("2")
time.sleep(1)
cls()
print("1")
time.sleep(1)
cls()
start = time.time()

while i != olas:
	chyby = 0
	priklados = time.time()
	jedna = random.randint(jedos, obtiznost)
	dva = random.randint(jedos, obtiznost)
	seznam = ["+", "-", "*", "**", "√"]
	znamenko = random.choice(seznam)
	if znamenko == "*":
		dva = random.randint(1, 10)
	if znamenko == "**":
		dva = 2	
		if obtiznost == 10:
			jedna = random.randint(1, 10)
		elif obtiznost == 100:
			jedna = random.randint(1, 20)
		elif obtiznost == 1000:
			jedna = random.randint(1, 30)
		stringa = f"{jedna} ** 2"
	elif znamenko == "√":
		jedna = random.choice(odmocniny)
		stringa2 = f"√{jedna}"
		status.append(stringa2)
		olaso = math.sqrt(jedna)
		answer.append(olaso)
	else:	
		stringa = f"{jedna} {znamenko} {dva}"
	if znamenko != "√":
		olaso = eval(stringa)
		answer.append(olaso)
		if znamenko == "**":
			stringa = f"{jedna}²"
		status.append(stringa)
	while True:
		if znamenko == "**":
			odpoved = input(f"{jedna}²= ")
		elif znamenko == "√":
			odpoved = input(f"√{jedna}= ")
		else:
			odpoved = input(f"{jedna} {znamenko} {dva} = ")
		try:
			odpoved = float(odpoved)
		except ValueError:

			if odpoved == "":
				skips += 1
			elif odpoved.lower() == "koncim" or odpoved.lower() == "končim":
				konec = True
				break
			else:
				print("Musíš zadat číslo!")
				time.sleep(1)
				cls()
				chybys += 1
				chyby += 1
				print(f"Chyby: {chybys}")
				continue
		if odpoved == "" or type(odpoved) == float:
			break
	if konec == True:
		break
	if odpoved == "":
		konecos = time.time()
		jednotlivec = round(konecos - priklados, 2)
		casy.append(jednotlivec)
		vypocet.append("skip")
		continue
	if znamenko != "√":
		string = f"{jedna} {znamenko} {dva}"
		vysledek = eval(string)
		if znamenko != "²" or znamenko != "√":
			custom = f"{jedna} {znamenko} {dva} = {vysledek}"
		elif znamenko == "²":
			custom = f"{jedna}² = {vysledek}"
	elif znamenko == "√":
		vysledek = math.sqrt(jedna)
		custom = f"√{jedna} = {vysledek}"
		
	if odpoved == vysledek:
		pass
	else:
		chybas.append(custom)
		chyby += 1
		chybys += 1
		cls()
		print(f"Chyby: {chybys}")
		while True:
			if znamenko == "**":
				odpoved = input(f"{jedna}²= ")
			elif znamenko == "√":
				odpoved = input(f"√{jedna}= ")
			else:
				odpoved = input(f"{jedna} {znamenko} {dva} = ")
			try:
				odpoved = int(odpoved)
			except ValueError:
				if odpoved == "":
					skips += 1
					konecos = time.time()
					jednotlivec = round(konecos - priklados, 2)
					casy.append(jednotlivec)
					vypocet.append("skip")
					break
				elif odpoved.lower() == "koncim" or odpoved.lower() == "končim":
					sys.exit()
				else:
					print("Musíš zadat číslo!")
					time.sleep(1)
					cls()
			if odpoved == vysledek:
				break
			chyby += 1
			chybys += 1
			cls()
			print(f"Chyby: {chybys}")
		if odpoved == vysledek:
			pass
		else:
			continue
	konecos = time.time()
	i += 1
	cls()
	jednotlivec = round(konecos - priklados, 2)
	casy.append(jednotlivec)
	vypocet.append(chyby)
	print(f"Skvěle, máš {i}/{olas} příkladů")
if konec == True:
	print("Nevadí, zkus trochu lehčí obtížnost :)")
else:
	konec = time.time()
	final = round(konec - start, 2)
	konec = final + (skips * skios)
	cls()
	if skips > 0:
		print(f"KONEČNÉ VÝSLEDKY:\nObtížnost: {omo}\nPříklady: {olas}\nChyby: {chybys}\nČas bez přeskočení: {final}\nKonečný čas: {konec} s\nPřeskočení: {skips} ")
	else:
		print(f"KONEČNÉ VÝSLEDKY:\nObtížnost: {omo}\nPříklady: {olas}\nChyby: {chybys}\nKonečný čas: {konec}")

	losos = input("\n\nchceš zobrazit statistiky?\nA|N: ")
	if losos.lower() == "a":
		y = 0
		cls()
		while y != len(status):
			cls()
			if vypocet[y] == "skip":
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nPřeskočil jsi\nčas: {casy[y]}")
			elif vypocet[y] == 0:
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nVypočteno bez chyby\nčas: {casy[y]}")
			else:
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nPočet chyb: {vypocet[y]}\nčas: {casy[y]}")
			input()
			y += 1
	elif losos.lower() == "n":
		cls()
		print("nevadí")
		time.sleep(1)
	else:
		print("nerozumím")
		time.sleep(1)




#Kroufek dne 22.3.2024		
#Upraveno dne 12.5.2024
#Dne 12.5.2024 -> přidána funkce mocnin a odmocnin
#Dne 15.5-X.X.2024 -> přidána funkce dev.tools!
#Dne 27.5.2024 -> Přidána Kontrola Souboru
#Dne 30.5.2024 -> přidána úvodní obrazovka
