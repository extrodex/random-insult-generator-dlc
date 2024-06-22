import random
i1=[""]
i2=[""]
i3=[""]
with open('ins1.txt', 'r') as file:
  for line in file:
    i1.append(line.strip())
with open('ins2.txt', 'r') as file:
  for line in file:
    i2.append(line.strip())
with open('ins3.txt', 'r') as file:
  for line in file:
    i3.append(line.strip())
a=random.randint(0,len(i1)-1)
b=random.randint(0,len(i2)-1)
c=random.randint(0,len(i3)-1)
print(f"You are a {i1[a]} {i2[b]} {i3[c]}")
while True:
    another_insult = input("Do you want another insult? (yes/no): ")
    if another_insult.lower() == "yes":
        a = random.randint(0,len(i1)-1)
        b = random.randint(0,len(i2)-1)
        c = random.randint(0,len(i3)-1)
        print(f"You are a {i1[a]} {i2[b]} {i3[c]}")
    else:
        break
