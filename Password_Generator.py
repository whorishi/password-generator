import random as r

def pass_generator(l=8):
    l1=["@","#","$","%","&","*","!"]
    upper = chr(r.randint(65,90))
    lower = chr(r.randint(97,122))
    special = r.choice(l1)
    digit1 = str(r.randint(10000,99999))
    digit2 = str(r.randint(10000,99999))
    digit3 = str(r.randint(100,999))
    
    password = upper+lower+special+digit1+digit2+digit3
    l2 = r.sample(password,l)
    password = ("").join(l2)
    return password

num = int(input("enter password length(max:- 16):"))
PASS = pass_generator(num)
print(PASS)

