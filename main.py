import random

chiffre = random.randint(1,100)
question = input("devinez le nombre que j'ai choisi")
print (question)

for
if int(question) > chiffre:
    print("plus petit")
    input("asseyez de nouveau")


elif int(question) < chiffre:
    print("plus grand")
    input("asseyez de nouveau")
