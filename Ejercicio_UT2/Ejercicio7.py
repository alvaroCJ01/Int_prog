import string
import random
a=list(string.ascii_letters)
b=random.sample(a,4)
c="".join(b)
d=random.randrange(0,10)
lista=["!","#","$","%","&","*"]
e=random.sample(lista, k=2)
f="".join(e)
print(f"{c}{d}{f}")