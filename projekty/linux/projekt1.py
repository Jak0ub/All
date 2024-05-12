import random
import math
import os
import time
i = 0
status = []
chybas = []
vypocet = []
answer = []
casy = []
lima = []
chyby = 0
chybys = 0
otz = "nic"
while True:
	otz = input("Vítej v testeru tvých matematických schopností, pro pokračování stiskni ENTER: ")
	if otz == "":
		break
os.system("clear")
input("Pokud chceš příklad přeskočit. Klikni na ENTER a budeš mít nový příklad\n\t!budeš mít ale ke konečnému času přičtenou sekundu!")
os.system("clear")
input("Pokud si nebudeš vůbec vědět rady, a budeš chtít test uknočit\n\t\t\tNAPIŠ 'KONČIM'")
while True:
	os.system("clear")
	olas = input("Kolik chceš příkladů?\n|1-20|: ")
	try:
		olas = int(olas)
	except ValueError:
		os.system("clear")
		print("ZADEJ ČÍSLO")
		time.sleep(1)
		continue
	if type(olas) == int:
		if olas >= 1 and olas <= 20:
			break
		else:
			os.system("clear")
			print("1-20!")
			time.sleep(1)
os.system("clear")
while True:
	osm = input("Jakou chceš obtížnost?\nLehká -> čísla od 1-10\nStřední -> čísla od 10-100\nTěžká -> čísla od 100-1000\n|Lehká|Střední|Těžká|: ")
	if osm.lower() == "lehká" or osm.lower() == "l" or osm.lower() == "lehka":
		obtiznost = 10
		omo = "lehká"
		break
	elif osm.lower() == "těžká" or osm.lower() == "t" or osm.lower() == "tezka":
		obtiznost = 1000
		omo = "těžká"
		break
	elif osm.lower() == "střední" or osm.lower() == "s" or osm.lower() == "stredni" or osm.lower() == "středni" or osm.lower() == "strední":
		obtiznost = 100
		omo = "střední"
		break
	else:
		os.system("clear")
		print("Zadej jednu z obtížností!")
		time.sleep(2)
		os.system("clear")
konec = False
	
os.system("clear")	
skips = 0
print("3")
time.sleep(1)
os.system("clear")
print("2")
time.sleep(1)
os.system("clear")
print("1")
time.sleep(1)
os.system("clear")
start = time.time()
while i != olas:
	chyby = 0
	priklados = time.time()
	jedna = random.randint(1, obtiznost)
	dva = random.randint(1, obtiznost)
	seznam = ["+", "-", "*"]
	znamenko = random.choice(seznam)
	if znamenko == "*":
		dva = random.randint(1, 10)
	stringa = f"{jedna} {znamenko} {dva}"
	olaso = eval(stringa)
	answer.append(olaso)
	status.append(stringa)
	while True:
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
				os.system("clear")
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
		
	string = f"{jedna} {znamenko} {dva}"
	vysledek = eval(string)
	custom = f"{jedna} {znamenko} {dva} = {vysledek}"
	if odpoved == vysledek:
		pass
	else:
		chybas.append(custom)
		chyby += 1
		chybys += 1
		os.system("clear")
		print(f"Chyby: {chybys}")
		while True:
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
				else:
					print("Musíš zadat číslo!")
					time.sleep(1)
					os.system("clear")
			if odpoved == vysledek:
				break
			chyby += 1
			chybys += 1
			os.system("clear")
			print(f"Chyby: {chybys}")
		if odpoved == vysledek:
			pass
		else:
			continue
	konecos = time.time()
	i += 1
	os.system("clear")
	jednotlivec = round(konecos - priklados, 2)
	casy.append(jednotlivec)
	vypocet.append(chyby)
	print(f"Skvěle, máš {i}/{olas} příkladů")
if konec == True:
	print("Nevadí, zkus trochu lehčí obtížnost :)")
else:
	konec = time.time()
	final = round(konec - start, 2)
	konec = final + skips
	os.system("clear")
	if skips > 0:
		print(f"KONEČNÉ VÝSLEDKY:\nObtížnost: {omo}\nPříklady: {olas}\nChyby: {chybys}\nČas bez přeskočení: {final}\nKonečný čas: {konec} s\nPřeskočení: {skips} ")
	else:
		print(f"KONEČNÉ VÝSLEDKY:Obtížnost: {omo}\nPříklady: {olas}\nChyby: {chybys}\nKonečný čas: {konec}")

	losos = input("\n\nchceš zobrazit statistiky?\nA|N: ")
	if losos.lower() == "a":
		y = 0
		os.system("clear")
		while y != len(status):
			os.system("clear")
			if vypocet[y] == "skip":
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nPřeskočil jsi\nčas: {casy[y]}")
			elif vypocet[y] == 0:
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nVypočteno bez chyby\nčas: {casy[y]}")
			else:
				print(f"{y+1}.příklad:\n\n{status[y]} = {answer[y]}\nPočet chyb: {vypocet[y]}\nčas: {casy[y]}")
			input()
			y += 1
	elif losos.lower() == "n":
		os.system("clear")
		print("nevadí")
		time.sleep(1)
	else:
		print("nerozumím")
		time.sleep(1)




#Kroufek dne 22.3.2024		
#Upraveno dne 28.4.2024
