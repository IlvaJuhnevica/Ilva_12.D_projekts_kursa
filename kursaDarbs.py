import random
import math
from turtle import*
print(" Kursa darbs: Darbošanās ar skaitļiem, vārdiem un burtiem- dažādas darbības un spēles.")
print("NOTEIKSIM, VAI SKAITLIS IR PĀRA VAI NEPĀRA")
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
print("NOTEIKSIM, IEVADĪTĀ INTERVĀLA PĀRA UN NEPĀRA SKAITĻUS")
saraksts=[]
s=int(input("Ievadi intervāla sākuma vērtību:"))
b=int(input("Ievadi intervāla beigu vērtību:"))
for i in range(s,b):
  saraksts.append(i)
print("Skaitļu saraksts:", saraksts)
para=[]
nepara=[]
for i in range(len(saraksts)):
  if(saraksts[i]%2==0):
    para.append(saraksts[i])
  else:
    nepara.append(saraksts[i])
print("Pāra skaitļu saraksts:", para)
print("Nepāra skaitļu saraksts:", nepara)
print("UZSPĒLĒSIM SKAITĻU MINĒŠANAS SPĒLI!")
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
print("UZSPĒLĒSIM -AKMENS, ŠĶĒRES PAPĪRĪTS- SPĒLI!")
def play():
    Darbība = input("Kāda ir tava izvēle? 'a' ir akmens, 'p' ir papīrs, 's' ir šķēres \n")
    Dators = random.choice(['a', 'p', 's'])
    if Darbība == Dators:
        return 'Neizšķirts'
    # a > s, s > p, p > a
    if is_win(Darbība, Dators):
        return 'Tu uzvarēji!'
    return 'Tu zaudēji!'
def is_win(player, opponent):
    # return true if player wins
    # a > s, s > p, p > a
    if (player == 'a' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'a'):
        return True
print(play())
def trijsturis(b):
    a=(2*b)-2
    for i in range (b, -1, -1):
        for j in range (a, 0,-1):
            print(end="")
        a=a+1
        for j in range (0, i+1):
            print( "* ",end="")
        print("\r")
b=int(input("Ievadi līniju skaitu: "))
trijsturis(b)
print("FAILS IZVADA, KĀDS SKAITLIS IR KATRĀ VIŅA LĪNIJĀ")
linijas = []
with open('cipari.txt') as f:
    linijas = f.readlines()
count = 0
for line in linijas:
    count += 1
    print(f'line {count}: {line}')    

print("NOVĒLĒJUMS NO ŠĪ BURTU MIKŠĻA")
v="SEKUNDILAIAPSTĀTOSJAUKANEPDIENATIKSKOP!ŠPAVASARA"
print(v.lower())
print(v[7:10])
print(v[18:23])
print(v[26:31])
print(v[38:39])
#Noslēpumainākais matemātikas simbols
bgcolor('black')
color('cyan')
speed(15)
right(45)
for i in range(150):
    circle(30)
    if 7 < i < 62:
        left(5)
    if 80 < i < 133:
        right(5)
    if i < 80:
        forward(10)
    else:
        forward(5)
done()

