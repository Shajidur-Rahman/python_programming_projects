import time
def mili_gram_to_grame():
    mili_gram2 = float(input("what is the amount of mili_gram: "))
    a =  print(mili_gram2/1000, "grame")
    return a
def grame_to_mili_grame():
    grame1 = float(input("what is the amount of grame: "))
    result1 = print(grame1*1000, "mili gram")
    return result1
def grame_to_kg():
    grame2 = float(input("what is the amount of grame: "))
    result2 = print(grame2/1000, "kg")
    return result2
def kg_to_grame():
    kg = float(input("what is the amount of kg: "))
    result = print(kg*1000, "grame")
    return result
def kg_to_quintal():
    kg = float(input("what is the amount of kg: "))
    result = print(kg/100, "quintal")
    return result
def quintal_to_kg():
    quintal = float(input("what is the amount of quintal: "))
    result = print(quintal*100, "kg")
    return result
def kg_to_ton():
    kg = float(input("what is the amount of kg: "))
    result = print(kg/1000,'ton')
    return result
def ton_to_kg():
    ton  = float(input('what is the amount of ton: '))
    result = print(ton*1000)
    return result

#user input part

grame_list = ['grame', 'kg', 'ton', 'quintal']
print('......1.......' ,grame_list)
user_input = int(input("which number have you chosen? :: "))
if user_input == 1:
    print('1.. mili grame to grame')
    print('2.. grame to mili grame')
    print('3.. kg to grame')
    print('4.. grame to kg')
    print('5.. kg to quintal')
    print('6.. quintal to kg')
    print('7.. ton to kg ')
    print('8.. kg to ton')

grame_chosen = int(input("which number have you chosen? :: "))
if grame_chosen == 1:
    mili_gram_to_grame()
if grame_chosen == 2:
    grame_to_mili_grame()
if grame_chosen == 3:
    kg_to_grame()
if grame_chosen == 4:
    grame_to_kg()
if grame_chosen == 5:
    kg_to_quintal()
if grame_chosen == 6:
    quintal_to_kg()
if grame_chosen == 7:
    ton_to_kg()
if grame_chosen == 8:
    kg_to_ton()
time.sleep(5)    
