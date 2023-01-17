import random

chiffre = random.randint(1,100)
question = int()
question = input("devinez le nombre que j'ai choisi")
question = int(question)
print (question)


if int(question) > chiffre:
    print("plus petit")


elif int(question) < chiffre:
    print("plus grand")
