import random
List=[]
a=int(input("Enter the no.of inputs:"))
for i in range(0,a):
    e=int(input())
    List.append(e)
print(List)
temperature=random.choice(List)
humudity=random.choice(List)
print(temperature,humudity)
if temperature>100:
    if humudity>80:
        print("DANGEROUS")
    else:
        print("HIGH TEMPERATURE")
elif temperature==100:
    print("No risk")
else:
    print("Good")
