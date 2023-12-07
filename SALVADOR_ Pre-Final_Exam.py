import random

primen = []
respo = ["PROGRAM TERMINATED...",
         "YOU HAVE BEEN TERMINATED...",
         "CONNECTION TERMINATED...",
         "PROGRAM BREACHED..."]

print("CS112 COMPROG 1 -- PREFINAL EXAMINATION\n"
      "CREATED BY: Mon Nikolai R. Salvador\n"
      "")

while True:
    respo1 = int(input("Enter a number [Start]: "))
    if respo1 == 0:
        print(random.choice(respo))
        exit()
    elif respo1 < 0:
        print("Enter a positive number")
    else:
        break

while True:
    respo2 = int(input("Enter a number [End]: "))
    if respo2 == 0:
        print(random.choice(respo))
        exit()
    elif respo2 <= respo1:
        print("Please enter a number greater than [Start]")
    else:
        break

for i in range(respo1, respo2):
    if i > 1:
        for x in range(2, int(i**0.5) + 1):
            if i % x == 0:
                break
        else:
            primen.append(i)

print(f"The prime numbers between {respo1} and {respo2} are:\n"
      f"{primen}")
