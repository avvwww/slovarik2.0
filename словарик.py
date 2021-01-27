from random import *
def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(f,list):
    fail=open(f,'w',encoding="utf-8-sig")
    for k in list:
        fail.write(k+"\n")
    fail.close()
    return list

def salvesta_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+'\n')
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def uued_sonad(): 
    rus_sona=input("Введи слово на русском ==> ")
    ee_sona=input("Sisesta sõna eesti keeles ==> ")
    list_rus=salvesta_failisse('rus.txt',rus_sona)
    list_ee=salvesta_failisse('ee.txt',ee_sona)
    return list_rus, list_ee

def tolkimine(list_rus,list_ee):
    slovo=input("Введите слово для перевода ==> ")
    if slovo in list_rus:
        ind=list_rus.index(slovo)
        print(f"{slovo}-{list_ee[ind]}")
    elif slovo in list_ee:
        ind=list_ee.index(slovo)
        print(f"{slovo}-{list_rus[ind]}")
    else:
        print(f"{slovo.upper()} отсутствует в словаре")
        v=input("Желаете добавить слово в словарь? ")
        if v.lower()=="да": uued_sonad()

def oshibka(list_rus, list_ee):
    viga=input("Введите слово с ошибкой ==> ")
    if viga in list_rus:
        ind=list_rus.index(viga) #index
        print(f"Будет исправлена пара слов {viga}-{list_ee[ind]}")
        list_rus.pop(ind)
        list_ee.pop(ind)
        list_rus=list_failisse("rus.txt",list_rus)
        list_ee=list_failisse("ee.txt",list_ee)
        uued_sonad()
    elif viga in list_ee:
        ind=list_ee.index(viga)
        print(f"Будет исправлена пара слов {viga}-{list_rus[ind]}")
        list_rus.pop(ind)
        list_ee.pop(ind)
        list_rus=list_failisse("rus.txt",list_rus)
        list_ee=list_failisse("ee.txt",list_ee)
        uued_sonad()
    else:
        print(f"{viga.upper()} отсутствует в словаре")
    return list_rus, list_ee
 

def proverka():
    keel=input("На какой язык хотите переводить? 1- на эстонский, 2- на русский ==> ")
    s=int(input("Сколько Вы слов хотите перевевести? "))
    while type(s) !=int and s<1 or s>50:
        try:
            s=input("Сколько Вы слов хотите перевести? ")
            
        except:
            print("Нельзя столько!")
            ValueError
    que=0    
    if keel=="1":
        print("Перевод с русского на эстонский: \n ")
        for i in range (s):
            ind=randint(0,len(list_rus)-1)
            list_rus[ind]
        


list_rus=loe_failist("rus.txt")
list_ee=loe_failist("ee.txt")
print(list_rus)
print(list_ee)

while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4 ==> ")
    if v=='1':
        tolkimine(list_rus, list_ee)
    elif v=='2':
        list_rus,list_ee= uued_sonad()
    elif v=="3":
        print(list_rus,list_ee)
        oshibka(list_rus, list_ee)
        print(list_rus,list_ee)

    elif v=="4":
        proverka()



