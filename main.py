import random
from art import text2art

author = text2art("IAMTHEROOT")
title = text2art("PASSWORD GENERATOR")
notice = ("This program generate unique and strong passwords")

print(author)
print(title)
print(notice)


chars = "abcdefghijklmnopqrstuwxyz1234567890()=^:/-#~&^@=+*!;<>."

for x in range(1):
    password = '' 
    password_lengh = int(input("Choisissez le nombres de caracteres que votre mot de passe fera :"))
    print("")
    for x in range (password_lengh):
        password += random.choice(chars)
    print("Le mot de passe généré est: ")
    print("")
    print(password)
    password_lengh = len(password)
    print("")
    print("Votre mot de passe fait " + str(password_lengh) + " caracteres")
    print("")
