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
print("Jauku tev dienu!!!!")	
# Python 3 program to convert integer
# number to Roman values
import math

def integerToRoman(A):
	romansDict = \
		{
			1: "I",
			5: "V",
			10: "X",
			50: "L",
			100: "C",
			500: "D",
			1000: "M",
			5000: "G",
			10000: "H"
		}

	div = 1
	while A >= div:
		div *= 10

	div /= 10

	res = ""

	while A:

		# main significant digit extracted
		# into lastNum
		lastNum = int(A / div)

		if lastNum <= 3:
			res += (romansDict[div] * lastNum)
		elif lastNum == 4:
			res += (romansDict[div] +
						romansDict[div * 5])
		elif 5 <= lastNum <= 8:
			res += (romansDict[div * 5] +
			(romansDict[div] * (lastNum - 5)))
		elif lastNum == 9:
			res += (romansDict[div] +
						romansDict[div * 10])

		A = math.floor(A % div)
		div /= 10
		
	return res

# Driver code
print("Roman value for the integer is:"
				+ str(integerToRoman(3549)))

