from Firewall import *
from utils import*

F1 = Firewall(10,5)
F2 = Firewall(10,5)

flag=1

for rule in F2.rules:
    p=Property(rule)
    if (satisfy(F1,p)==0):
        flag=0

if(flag==0):
    print("F1 and F2 are not same")
else:
    print("F1 and F2 are same")