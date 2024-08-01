import random
import math
import os
import time
import platform
import sys
os.system("title Matematika")
i = 0
seznam = []
list_pocet = []
post = 0
numero = 0
okos = 0
znovu = False
status = []
chybas = []
vypocet = []
answer = []
jop = []
casy = []
lima = []
platform_system = platform.system()
if platform_system == "Windows":
	operacni_system = "Windows"
	def cisto():
		os.system("cls")
else:
	operacni_system = "Linux_based"
	def cisto():
		os.system("clear")
#Úvodní načtení
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
time.sleep(0.6)
cisto()
print(r"""     
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_) 
  _/ |                            
 |__/                              
""")
time.sleep(0.6)
cisto()
print(r"""     
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _    _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)
  _/ |                            
 |__/                             
""")
time.sleep(0.6)
cisto()
print(r"""     
    _       _               _     
   (_)     | |             | |    
    _  __ _| | _____  _   _| |__  
   | |/ _` | |/ / _ \| | | | '_ \ 
   | | (_| |   < (_) | |_| | |_) |   _    _    _
   | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)  (_)
  _/ |                            
 |__/                             
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
		f.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		f.close()
		with open("config.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			radky[0] = "Konfigurace:\n"
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
			radky[13] = "End=Nevadí, zkus trochu lehčí obtížnost :)\n"
			radky[14] = "Minus=ON\n"
			radky[15] = "+=ON\n"
			radky[16] = "-=ON\n"
			radky[17] = "**=ON\n"
			radky[18] = "*=ON\n"
			radky[19] = "√=ON\n"
		with open("config.txt", "w", encoding="utf-8") as file:
			file.writelines(radky)
		animace_zmeny()
		sys.exit()
	print("Pro defaultní nastavení souboru napiště při chybovém hlášení:|REMAKE|: ")
	time.sleep(2)
	sys.exit()
def animace_distrib():
	cls()
	print(r"Pracuji |")
	time.sleep(0.5)
	cls()
	print("Pracuji \\ ")
	time.sleep(0.5)
	cls()
	print(r"Pracuji -")
	time.sleep(0.5)
	cls()
	print("Pracuji /")
	time.sleep(0.5)
	cls()
	print(r"Pracuji |")
	time.sleep(0.5)
	cls()
	print("Pracuji \\ ")
	time.sleep(0.5)
	cls()
	print(r"Pracuji -")
	time.sleep(0.5)
	cls()
	print("Pracuji /")
	time.sleep(0.5)
	cls()
	print("Hotovo")
	time.sleep(0.5)
def cls():
	cisto()
#Kontrola pro funkci distribuce
def kontrola():
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
				ok14 = radky[13]
				ok15 = radky[14]
				ok16 = radky[15]
				ok17 = radky[16]
				ok18 = radky[17]
				ok19 = radky[18]
				ok20 = radky[19]
			except IndexError:
				soubor_poskozen()
			if ok1.lower().strip() != "konfigurace:":
				soubor_poskozen()
			try:
				one = radky[1].strip().split("PEN:")[1]
			except IndexError:
				soubor_poskozen()
			try:
				one = int(one)
			except ValueError:
				soubor_poskozen()
			try:
				two = radky[2].strip().split("UV:")[1]
				three = radky[3].strip().split("UV:")[1]
				four = radky[4].strip().split("UV:")[1]
			except IndexError:
				soubor_poskozen()
			try:
				five = radky[5].strip().split("1:")[1]
				six = radky[6].strip().split("2:")[1]
				seven = radky[7].strip().split("3:")[1]
			except IndexError:
				soubor_poskozen()
			if five != "ON" and five != "OFF":
				soubor_poskozen()
			elif six != "ON" and six != "OFF":
				soubor_poskozen()
			elif seven != "ON" and seven != "OFF":
				soubor_poskozen()
			try:
				eight = radky[8].strip().split("1=")[1]
				nine = radky[9].strip().split("2=")[1]
			except IndexError:
				soubor_poskozen()
			try:
				eight = int(eight)
				nine = int(nine)
			except ValueError:
				soubor_poskozen()
			if eight > nine:
				soubor_poskozen()
			elif eight <= 0:
				soubor_poskozen()
			try:
				ten = ok11.strip().split("=")[1]
				eleven = ok12.strip().split("=")[1]
				twelve = ok13.strip().split("=")[1]
			except IndexError:
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
				soubor_poskozen()
			if ten_2 < ten_1:
				soubor_poskozen()
			elif ten_2 <= 0 or ten_1 <= 0:
				soubor_poskozen()
			if eleven_2 <= eleven_1:
				soubor_poskozen()
			elif eleven_2 <= 0 or eleven_2 <= 0:
				soubor_poskozen()
			if twelve_2 <= twelve_1:
				soubor_poskozen()
			elif twelve_2 <= 0 or twelve_1 <= 0:
				soubor_poskozen()
			if ok14.strip() == "":
				soubor_poskozen()
			try:
				ok14_1 = ok14.strip().split("=")[0]
			except IndexError:
				soubor_poskozen()
			if ok14_1.lower() != "end":
				soubor_poskozen()
			try:
				radek15 =  ok15.lower().strip().split("=")[1]
			except IndexError:
				soubor_poskozen()
			if radek15 != "on" and radek15 != "off":
				soubor_poskozen()
			if ok16.strip().split("=")[0] != "+":
				soubor_poskozen()
			if ok16.lower().strip().split("=")[1] != "on" and ok16.lower().strip().split("=")[1] != "off":
				soubor_poskozen()
			if ok17.strip().split("=")[0] != "-":
				soubor_poskozen()
			if ok17.lower().strip().split("=")[1] != "on" and ok17.lower().strip().split("=")[1] != "off":
				soubor_poskozen()
			if ok18.strip().split("=")[0] != "**":
				soubor_poskozen()
			if ok18.lower().strip().split("=")[1] != "on" and ok18.lower().strip().split("=")[1] != "off":
				soubor_poskozen()
			if ok19.strip().split("=")[0] != "*":
				soubor_poskozen()
			if ok19.lower().strip().split("=")[1] != "on" and ok19.lower().strip().split("=")[1] != "off":
				soubor_poskozen()
			if ok20.strip().split("=")[0] != "√":
				soubor_poskozen()
			if ok20.lower().strip().split("=")[1] != "on" and ok20.lower().strip().split("=")[1] != "off":
				soubor_poskozen()
			if ok16.lower().strip().split("=")[1] != "on" and ok17.lower().strip().split("=")[1] != "on" and ok18.lower().strip().split("=")[1] != "on" and ok19.lower().strip().split("=")[1] != "on" and ok20.lower().strip().split("=")[1] != "on":
				soubor_poskozen() 

				
	except FileNotFoundError:
		soubor_poskozen()
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


#Kontrola Konfiguračního souboru pro spuštění programu
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
			ok14 = radky[13]
			ok15 = radky[14]
			ok16 = radky[15]
			ok17 = radky[16]
			ok18 = radky[17]
			ok19 = radky[18]
			ok20 = radky[19]
		except IndexError:
			hlaseni = "Někde něco kompletně chybí! "
			soubor_poskozen()
		if ok1.lower().strip() != "konfigurace:":
			hlaseni = "Soubor neobsahuje 'Konfigurace:' na prvním řádku"
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
			hlaseni = f"Něco je kompletně špatně na 10/11 nebo 12.řádce, VZOR:|EASY=1-10|"
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
			hlaseni = f"10/11 nebo 12.řádek neobsahuje číslo za =, VZOR:|EASY=1-10|"
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
		if ok14.strip() == "":
			hlaseni = "14.řádek neobsahuje nic, VZOR:|end=text|"
			soubor_poskozen()
		try:
			ok14_1 = ok14.strip().split("=")[0]
		except IndexError:
			hlaseni = "14.řádek je kompletně špatně, VZOR:|end=text|"
			soubor_poskozen()
		if ok14_1.lower() != "end":
			hlaseni = "14.řádek nezačíná na end, VZOR:|end=text|"
			soubor_poskozen()
		try:
			radek15 =  ok15.lower().strip().split("=")[1]
		except IndexError:
			hlaseni = "15.řádek je kompletně špatně, VZOR:|Minus=ON|"
			soubor_poskozen()
		if radek15 != "on" and radek15 != "off":
			hlaseni = "15.řádek neobsahuje ON/OFF, VZOR:|Minus=ON|"
			soubor_poskozen()
		if ok16.strip().split("=")[0] != "+":
			hlaseni = "16.řádek nezačíná na +, VZOR:|+=ON|"
			soubor_poskozen()
		if ok16.lower().strip().split("=")[1] != "on" and ok16.lower().strip().split("=")[1] != "off":
			hlaseni = "16.řádek nekončí na on/off, VZOR:|+=ON|"
			soubor_poskozen()
		if ok17.strip().split("=")[0] != "-":
			hlaseni = "17.řádek nezačíná na -, VZOR:|-=ON|"
			soubor_poskozen()
		if ok17.lower().strip().split("=")[1] != "on" and ok17.lower().strip().split("=")[1] != "off":
			hlaseni = "17.řádek nekončí na on/off, VZOR:|-=ON|"
			soubor_poskozen()
		if ok18.strip().split("=")[0] != "**":
			hlaseni = "18.řádek nezačíná na **, VZOR:|**=ON|"
			soubor_poskozen()
		if ok18.lower().strip().split("=")[1] != "on" and ok18.lower().strip().split("=")[1] != "off":
			hlaseni = "18.řádek nekončí na on/off, VZOR:|**=ON|"
			soubor_poskozen()
		if ok19.strip().split("=")[0] != "*":
			hlaseni = "19.řádek nezačíná na *, VZOR:|*=ON|"
			soubor_poskozen()
		if ok19.lower().strip().split("=")[1] != "on" and ok19.lower().strip().split("=")[1] != "off":
			hlaseni = "19.řádek nekončí na on/off, VZOR:|*=ON|"
			soubor_poskozen()
		if ok20.strip().split("=")[0] != "√":
			hlaseni = "20.řádek nezačíná na √, VZOR:|√=ON|"
			soubor_poskozen()
		if ok20.lower().strip().split("=")[1] != "on" and ok20.lower().strip().split("=")[1] != "off":
			hlaseni = "20.řádek nekončí na on/off, VZOR:|√=ON|"
			soubor_poskozen()
		if ok16.lower().strip().split("=")[1] != "on" and ok17.lower().strip().split("=")[1] != "on" and ok18.lower().strip().split("=")[1] != "on" and ok19.lower().strip().split("=")[1] != "on" and ok20.lower().strip().split("=")[1] != "on":
			hlaseni = "16/17/18/19 a 20.řádek obsahují OFF, minimálně jeden z nich musí obsahovat ON"
			soubor_poskozen() 
			
except FileNotFoundError:
	print("Konfigurační soubor nebyl nalezen")
	oka = input("Přejete si soubor vytvořit?\nA|N: ")
	if oka.lower() == "a":
		f = open("config.txt", "a")
		f.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		f.close()
		with open("config.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			radky[0] = "Konfigurace:\n"
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
			radky[13] = "End=Nevadí, zkus trochu lehčí obtížnost :)\n"
			radky[14] = "Minus=ON\n"
			radky[15] = "+=ON\n"
			radky[16] = "-=ON\n"
			radky[17] = "**=ON\n"
			radky[18] = "*=ON\n"
			radky[19] = "√=ON\n"
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
while True:
	if testrun == True:
		break
	if post == 0:
		post += 1
		cls()
		dev_tools = input("Vítejte v developerském menu, zadejte příkaz\n\n|Pro navigační menu napište(dev.tools:menu)|\n|Pro ukončení napište(končim)|\n|Pro vytvoření distribuovatelného souboru napište(dev.tools:distrib)|\n ")
	elif post > 0:
		dev_tools = input()
	if dev_tools.lower() == "koncim" or dev_tools.lower() == "končim":
		sys.exit()
	elif dev_tools.lower() == "dev.tools:distrib":
		cls()
		print("Jste si jisti?")
		ano_ne = input("A|N: ")
		if ano_ne.lower() == "a":
			cls()
			print("Provádím kontrolu souboru...")
			time.sleep(2)
			hlaseni = "Spusťe program znovu pro podrobnější infomace"
			kontrola()
			with open("config.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				var1 = radky[1].strip().split(":")[1]
				var1 = int(var1)
				var2 = []
				if radky[5].strip().split(":")[1].lower() == "on":
					var2_1 = radky[2].strip().split(":")[1]
					var2.append(var2_1)
				if radky[6].strip().split(":")[1].lower() == "on":
					var2_1 = radky[3].strip().split(":")[1]
					var2.append(var2_1)
				if radky[7].strip().split(":")[1].lower() == "on":
					var2_1 = radky[4].strip().split(":")[1]
					var2.append(var2_1)
				if radky[14].strip().lower().split("=")[1] == "on":
					var3 = "on"
				else:
					var3 = "off"
				seznam2 = []
				var4 = radky[8].strip().split("=")[1]
				var4 = int(var4)
				var5 = radky[9].strip().split("=")[1]
				var5 = int(var5)
				var6_name = radky[10].strip().split("=")[0]
				var6_num = radky[10].strip().split("=")[1]	
				var7_name = radky[11].strip().split("=")[0]
				var7_num = radky[11].strip().split("=")[1]
				var8_name = radky[12].strip().split("=")[0]
				var8_num = radky[12].strip().split("=")[1]
				var9 = radky[13].strip().split("=")[1]
				jeden = radky[15].strip().split("=")[1]
				druhej = radky[16].strip().split("=")[1]
				treti = radky[17].strip().split("=")[1]
				ctvrtej = radky[18].strip().split("=")[1]
				patej = radky[19].strip().split("=")[1]
				if jeden.lower() == "on":
					seznam2.append("+")
				if druhej.lower() == "on":
					seznam2.append("-")
				if treti.lower() == "on":
					seznam2.append("**")
				if ctvrtej.lower() == "on":
					seznam2.append("*")
				if patej.lower() == "on":
					seznam2.append("√")
			try:
				with open("distribution.py", "r", encoding="utf-8") as file:
					pass
			except FileNotFoundError:
				with open("distribution.py", "w", encoding="utf-8") as file:
					file.write(f"""
import random
import math
import os
import time
import platform
import sys
#Proměnné
i = 0
list_pocet = []
post = 0
numero = 0
okos = 0
znovu = False
status = []
chybas = []
vypocet = []
answer = []
jop = []
casy = []
lima = []
chyby = 0
chybys = 0
rak = 0
otz = "nic"
zpet = False
seznam = {seznam2}
skios = {var1}
minusko = "{var3}"
jednicka = {var4}
dvojka = {var5}
zpravy = {var2}
ob1 = "{var6_name}"
ci1 = "{var6_num}"
ob2 = "{var7_name}"
ci2 = "{var7_num}"
ob3 = "{var8_name}"
ci3 = "{var8_num}"
konec_zprava = "{var9}"
				""")
					file.write(r"""

os.system("title Matematika")
platform_system = platform.system()
if platform_system == "Windows":
	operacni_system = "Windows"
	def cisto():
		os.system("cls")
else:
	operacni_system = "Linux_based"
	def cisto():
		os.system("clear")
#Úvodní načtení
cisto()
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
#Konec úvodního načítání
def cls():
	cisto()
if len(zpravy) > 0:
	for prvek in zpravy:
		cls()
		print(prvek)
		input("\nEnter pro pokračování")
cls()
while True:
	cls()
	olas = input(f"Kolik chceš příkladů? |{jednicka}-{dvojka}|: ")
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

if minusko == "on":
	enabled_minus = "Povoleno"
elif minusko == "off":
	enabled_minus = "Zakázáno"
if ob1.lower()[0] != ob2.lower()[0] and ob2.lower()[0] != ob3.lower()[0] and ob1.lower()[0] != ob3.lower()[0]:
	Enabled_first_lttr = "Povoleno"
else:
	Enabled_first_lttr = "Zakázáno"	
while True:
	osm = input(f"Jakou chceš obtížnost?\n{ob1} -> čísla od {ci1}\n{ob2} -> čísla od {ci2}\n{ob3} -> čísla od {ci3}\n\n|Možnost specifikování obtížnosti pomocí prvního písmene| |{Enabled_first_lttr}|\n|Možnost mínusového výsledku| |{enabled_minus}|\n")
	if Enabled_first_lttr == "Povoleno":
		if osm.lower() == ob1.lower() or osm.lower() == ob1.lower()[0]:
			num1 = ci1.strip().split("-")[0]
			num2 = ci1.strip().split("-")[1]
			obtiznost = int(num2)
			omo = f"{ob1}"
			odm = 10
			jedos = int(num1)
			break
		elif osm.lower() == ob3.lower() or osm.lower() == ob3.lower()[0]:
			num1 = ci3.strip().split("-")[0]
			num2 = ci3.strip().split("-")[1]
			obtiznost = int(num2)
			odm = 30
			jedos = int(num1)
			omo = f"{ob3}"
			break
		elif osm.lower() == ob2.lower() or osm.lower() == ob2.lower()[0]:
			num1 = ci2.strip().split("-")[0]
			num2 = ci2.strip().split("-")[1]
			obtiznost = int(num2)
			omo = f"{ob2}"
			odm = 20
			jedos = int(num1)
			break
		else:
			cls()
			print("Zadej jednu z obtížností!")
			time.sleep(2)
			cls()
	elif Enabled_first_lttr == "Zakázáno":
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
	znamenko = random.choice(seznam)
	if znamenko == "*":
		dva = random.randint(1, 10)
	if znamenko == "-" and minusko == "off" and dva > jedna:
		dva = random.randint(1, jedna)
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
if konec == True and konec_zprava != "":
	cls()
	print(konec_zprava)
	time.sleep(1)
elif konec == True and konec_zprava == "":
		pass
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
			input("\n\nEnter pro pokračování")
			y += 1
	elif losos.lower() == "n":
		cls()
		print("nevadí")
		time.sleep(1)
	else:
		print("nerozumím")
		time.sleep(1)
						""")
				
				animace_distrib()
				input()
				sys.exit()
			cls()
			print("Soubor již existuje!\n|Smažte soubor 'distribution.py' před použitím této funkce|\n")
			input()
			post = 0
		else:
			post = 0

	elif dev_tools.lower() == "dev.tools:menu":
		while True:
			post = 0
			cls()
			menu = input("Zadejte jednu z možností:\n\n|Testovací spuštění -> dev.tools:testrun|\n|Úprava obtížností -> dev.tools:diff|\n|Úprava penalizace za přeskočení -> dev.tools:skip|\n|Úprava možnosti počtu příkladů -> dev.tools:count|\n|Vypnutí/Úprava jednotlivých informačních zpráv -> dev.tools:inform|\n|Úprava zprávy při předčasném ukončení programu -> dev.tools:ending|\n|Úprava možnosti mínusových výsledků -> dev.tools:minus|\n|Vypnutí/Zapnutí znamének -> dev.tools:signs|\n|exit z menu -> exit|\n")
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
					if ob1.lower()[0] != ob2.lower()[0] and ob2.lower()[0] != ob3.lower()[0] and ob1.lower()[0] != ob3.lower()[0]:
						tetok = "Povoleno"
					else:
						tetok = "Zakázáno"
					print(f"Aktuální obtížnosti\n|{ob1} -> {ci1}|\n|{ob2} -> {ci2}|\n|{ob3} -> {ci3}|\n\nInformace\n|Specifikace pomocí prvního písmene obtížnosti| -> |{tetok}|")
					inp = input("\n\nOperace:\n|cislo:nickname -> změna pojmenování obtížnosti|\n|cislo:range -> změna rozmezí|\n|exit -> zpět do menu|\n")
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
							if oks.lower()[0] != ob2.lower()[0] and ob2.lower()[0] != ob3.lower()[0] and oks.lower()[0] != ob3.lower()[0]:
								break
							else:
								cls()
								print("Pozor, nějaké obtížnosti začínají na stejné písmeno. Funkce specifikování názvu obtížnosti je tedy zakánána!!\n|Back| -> |znovuspecifikování obtížnosti|\n|Enter| -> |pokračovat|\n")
								dehok = input()
								if dehok.lower() == "back":
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
							if ob1.lower()[0] != oks.lower()[0] and oks.lower()[0] != ob3.lower()[0] and ob1.lower()[0] != ob3.lower()[0]:
								break
							else:
								cls()
								print("Pozor, nějaké obtížnosti začínají na stejné písmeno. Funkce specifikování názvu obtížnosti je tedy zakánána!!\n|Back| -> |znovuspecifikování obtížnosti|\n|Enter| -> |pokračovat|\n")
								dehok = input()
								if dehok.lower() == "back":
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
							if ob1.lower()[0] != ob2.lower()[0] and ob2.lower()[0] != oks.lower()[0] and ob1.lower()[0] != oks.lower()[0]:
								break
							else:
								cls()
								print("Pozor, nějaké obtížnosti začínají na stejné písmeno. Funkce specifikování názvu obtížnosti je tedy zakánána!!\n|Back| -> |znovuspecifikování obtížnosti|\n|Enter| -> |pokračovat|\n")
								dehok = input()
								if dehok.lower() == "back":
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
			elif menu.lower() == "dev.tools:signs":
				while True:
					cls()
					with open("config.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						jeden = radky[15].strip().split("=")[1]
						druhej = radky[16].strip().split("=")[1]
						treti = radky[17].strip().split("=")[1]
						ctvrtej = radky[18].strip().split("=")[1]
						patej = radky[19].strip().split("=")[1]
					print(f"Hodnoty\n1.|+| -> |{jeden}|\n2.|-| -> |{druhej}|\n3.|**| -> |{treti}|\n4.|*| -> |{ctvrtej}|\n5.|√| -> |{patej}|")
					if jeden.lower() == "off" and druhej.lower() == "off" and treti.lower() == "off" and ctvrtej.lower() == "off" and patej.lower() == "off":
						cls()
						print("|VAROVÁNÍ: všechna znaménka jsou vypnutá, bez toho nebude program funkční, proto jsem automaticky zapnul jedno znaménko|")
						input("\nEnter pro pokračování")
						radky[15] = "+=ON\n"
						with open("config.txt", "w", encoding="utf-8") as file:
							file.writelines(radky)
						continue
					sign = input("\n\nMoznosti\n|Automaticke prepnuti na z ON na OFF nebo z OFF na ON| -> |cislo:edit|\n|zpět do menu| -> |exit|\n")
					if sign.lower() == "exit":
						break
					elif sign.lower() == "1:edit":
						if jeden.lower() == "on":
							radky[15] = "+=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
						else:
							radky[15] = "+=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
					elif sign.lower() == "2:edit":
						if druhej.lower() == "on":
							radky[16] = "-=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
						else:
							radky[16] = "-=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
					elif sign.lower() == "3:edit":
						if treti.lower() == "on":
							radky[17] = "**=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
						else:
							radky[17] = "**=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
					elif sign.lower() == "4:edit":
						if ctvrtej.lower() == "on":
							radky[18] = "*=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
						else:
							radky[18] = "*=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
					elif sign.lower() == "5:edit":
						if patej.lower() == "on":
							radky[19] = "√=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
						else:
							radky[19] = "√=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
								animace_zmeny()
								continue
					else:
						cls()
						print("Neznám")
						time.sleep(2)						
			elif menu.lower() == "dev.tools:minus":
				while True:
					cls()
					with open("config.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						hlavni = radky[14].strip().lower().split("=")[1]
					print(f"Aktuální stav: |{hlavni}|\n")
					question = input("Možnosti\n|Úprava -> edit|\n|zpět do menu -> exit|\n|získání informací k tomuto nástroji -> inform|\n")
					if question.lower() == "exit":
						break
					elif question.lower() == "edit":
						cls()
						if hlavni == "on":
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[14] = "Minus=OFF\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
						elif hlavni == "off":
							with open("config.txt", "r", encoding="utf-8") as file:
								radky = file.readlines()
								radky[14] = "Minus=ON\n"
							with open("config.txt", "w", encoding="utf-8") as file:
								file.writelines(radky)
							animace_zmeny()
					elif question.lower() == "inform":
						cls()
						print("|Jedná se o nástroj pro vypnutí nebo zapnutí možnosti mínusových výsledků|\n|Při možnosti edit se automaticky možnost změní na opačnou možnost než je možnost aktuální|\n")
						input("\nEnter pro pokračování")
					else:
						cls()
						print("Neznám")
						time.sleep(2)


				
			elif menu.lower() == "dev.tools:ending":
				while True:
					cls()
					with open("config.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						konec_zprava_edit = radky[13].strip().split("=")[1]
						print(f"Aktuální konečná zpráva\n|{konec_zprava_edit}|")
						choice_1 = input("\n\nMožnosti\n|Úprava zprávy -> edit|\n|Zpět do menu -> exit|\n|Získání informací k tomuto nástroji -> inform|\n")
					if choice_1.lower() == "edit":
							cls()
							editace_1 = input("Zadej novou zprávu(může být prázdné pro nevypsání ničeho): ")
							with open("config.txt", "w", encoding="utf-8") as file:
									radky[13] = f"end={editace_1}\n"
									file.writelines(radky)
									animace_zmeny()
									continue
					elif choice_1.lower() == "exit":
							cls()
							break
					elif choice_1.lower() == "inform":
							cls()
							print("Informace:\n|Jedná se o zprávu, která se vypíše, když uživatel zadá příkaz končim nebo koncim, při loopu počítání příkladů|\n|Pokud pouze stisknete Enter pri editaci zpravy, tak se nic nevypíše při předčasném skončení počítání|\n")
							input("\n\nEnter pro pokračování")
							cls()
							continue
					else:
						cls()
						print("Neznám")
						time.sleep(2)
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
					else:
						cls()
						print("Neznám")
						time.sleep(2)
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
							break
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
				print(f"{uvodni_text}")
				input("\nEnter pro pokračování")
cls()
while True:
	cls()
	with open("config.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
		jednicka = radky[8].strip().split("1=")[1]
		dvojka = radky[9].strip().split("2=")[1]
	olas = input(f"Kolik chceš příkladů?\n|{jednicka}-{dvojka}| ")
	if olas.lower() == "dev.tools:turn_on":
		with open("config.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			radky[0] = "ANO\n"
		with open("config.txt", "w", encoding="utf-8") as file:
			file.writelines(radky)
			animace_zmeny()
			sys.exit()
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
with open("config.txt", "r", encoding="utf-8") as file:
	radky = file.readlines()
	minusko = radky[14].strip().split("=")[1].lower()
if minusko == "on":
	enabled_minus = "Povoleno"
elif minusko == "off":
	enabled_minus = "Zakázáno"
if ob1.lower()[0] != ob2.lower()[0] and ob2.lower()[0] != ob3.lower()[0] and ob1.lower()[0] != ob3.lower()[0]:
	Enabled_first_lttr = "Povoleno"
else:
	Enabled_first_lttr = "Zakázáno"	
while True:
	osm = input(f"Jakou chceš obtížnost?\n{ob1} -> čísla od {ci1}\n{ob2} -> čísla od {ci2}\n{ob3} -> čísla od {ci3}\n\n|Možnost specifikování obtížnosti pomocí prvního písmene| |{Enabled_first_lttr}|\n|Možnost mínusového výsledku| |{enabled_minus}|\n")
	if Enabled_first_lttr == "Povoleno":
		if osm.lower() == ob1.lower() or osm.lower() == ob1.lower()[0]:
			obtiznost = os1
			omo = f"{ob1}"
			odm = 10
			jedos = int(num1)
			break
		elif osm.lower() == ob3.lower() or osm.lower() == ob3.lower()[0]:
			obtiznost = os3
			odm = 30
			jedos = int(num3)
			omo = f"{ob3}"
			break
		elif osm.lower() == ob2.lower() or osm.lower() == ob2.lower()[0]:
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
	elif Enabled_first_lttr == "Zakázáno":
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
with open("config.txt", "r", encoding="utf-8") as file:
	radky = file.readlines()
	konec_zprava = radky[13].strip().split("=")[1]
	jeden = radky[15].strip().split("=")[1]
	druhej = radky[16].strip().split("=")[1]
	treti = radky[17].strip().split("=")[1]
	ctvrtej = radky[18].strip().split("=")[1]
	patej = radky[19].strip().split("=")[1]
	if jeden.lower() == "on":
		seznam.append("+")
	if druhej.lower() == "on":
		seznam.append("-")
	if treti.lower() == "on":
		seznam.append("**")
	if ctvrtej.lower() == "on":
		seznam.append("*")
	if patej.lower() == "on":
		seznam.append("√")
if len(seznam) == 0:
	cls()
	print("Žádná znaménka nejsou aktivní")
	time.sleep(2)
	sys.exit()
while i != olas:
	chyby = 0
	priklados = time.time()
	jedna = random.randint(jedos, obtiznost)
	dva = random.randint(jedos, obtiznost)
	znamenko = random.choice(seznam)
	if znamenko == "*":
		dva = random.randint(1, 10)
	if znamenko == "-" and minusko == "off" and dva > jedna:
		dva = random.randint(1, jedna)
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
if konec == True and konec_zprava != "":
	cls()
	print(konec_zprava)
	time.sleep(1)
elif konec == True and konec_zprava == "":
		pass
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
			input("\n\nEnter pro pokračování")
			y += 1
	elif losos.lower() == "n":
		cls()
		print("nevadí")
		time.sleep(1)
	else:
		print("nerozumím")
		time.sleep(1)




#Kroufek dne 22.3.2024		
#Upraveno dne 29.7.2024
#Dne 12.5.2024 -> přidána funkce mocnin a odmocnin
#Dne 15.5-X.X.2024 -> přidána funkce dev.tools!
#Dne 27.5.2024 -> Přidána Kontrola Souboru
#Dne 30.5.2024 -> přidána úvodní obrazovka
#Dne 11.6.2024 -> přidáno rozšíření pro všechny systémy, již není potřeba instalovat projekt jednotlivě na různé systémy, stačí jeden soubor na všechny systémy
#Dne 22.7.2024 -> Úprava načítacího loga
#Dne 23.7.2024 -> Přidána funkce specifikování obtížnosti pomocí prvního písmene
#Dne 24.7.2024 -> Přidána funkce úpravy zprávy při použití příkazu koncim uzivatelem & Úprava vypínání a zapínání developera. Nyní se zapína při zprávě kolik chceš příkladů
#Dne 25.7.2024 -> Přidána funkce pro vypnutí a zapnutí mínusových výsledků
#Dne 29.7.2024 -> Pozměněn soubor, toto je soubor pro developera, a lze pomoci funkce dev.tools:distrib distribuovat soubor s nastaveními ktere provedl developer a to vse v samostatnem souboru!!
