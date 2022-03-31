import random
import math
print(" Kursa darbs: Darbošanās ar skaitļiem-darbības un spēles ar skaitļiem")
print("Noteiksim, vai skaitlis ir pāra vai nepāra")
skaitlis = int(input("Ievadi skaitli: "))
if (skaitlis % 2) == 0:
   print("{0} ir Pāra skaitlis".format(skaitlis))
else:
   print("{0} ir Nepāra skaitlis".format(skaitlis))
summa = 0
i = 1
while i <= skaitlis:
    summa = summa + i
    i = i+1   
print("Skaitļu summa līdz ievadītajam skaitlim (ieskaitot) ir", summa) # summa = 1+2+3+...+n
print("Uzspēlēsim skaitļu minēšanas spēli!")
mazākais = int(input("Ievadi mazāko iespējamo intervāla vērtību:- "))
lielākais = int(input("Ievadi lielāko iespējamo intervāla vērību:- "))
# tiek ģenerēts nejaušs skaitlis starp lielāko un mazāko intervāla vētību
x = random.randint(mazākais, lielākais)
print("\n\tTev ir tikai ",
	round(math.log(lielākais - mazākais + 1, 2)),
	" iespējas, lai atminētu pareizo skaitli!\n")
skaits = 0
while skaits < math.log(lielākais - mazākais + 1, 2):
	skaits += 1
	minamais = int(input("Ievadi savu izvēlēto(minamo)skaitli:- "))
	if x == minamais:
		print("Apsveicu! Tu uzminēji ar  ",
			skaits, ". reizi")
		break
	elif x > minamais:
		print("Tavs izvēlētais skaitlis ir pārāk mazs!")
	elif x < minamais:
		print("Tavs izvēlētais skaitlis ir pārāk liels!")
if skaits >= math.log(lielākais - mazākais + 1, 2):
	print("\nPareizā atbilde ir skaitlis  %d" % x)
print("Paldies par darbu!")	
print("Jauku tev dienu! ")	
