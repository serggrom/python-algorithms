
def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")



book = dict()

book["apple"] = 0.67

book["milk"] = 1.49

book["avocado"] = 1.49

print(book)

print(book["avocado"])

phone_book = {}

phone_book["jenny"] = 711256

phone_book["emergency"] = 1

print(phone_book["jenny"])

voted ={}

check_voter("tom")

check_voter("kate")

check_voter("tom")
