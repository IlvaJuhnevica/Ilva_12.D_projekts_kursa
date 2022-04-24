sk = [] 
cipari = open("cipari.txt", "r")
for r in cipari:
    sk.append(r)
    print(r, end="")
print()
sum = 0
for i in range(len(sk)):
    k = int(sk[i]) 
    sum += k    
print("\n Summa = ", sum)
cipari = open("cipari.txt", "w", encoding="UTF-8")
cipari.write(f"Summa ir {str(sum)}")
cipari.close()