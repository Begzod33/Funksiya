# a = int(input("1-son kirit "))
# b = int(input("2-son kirit "))
# def add():
#     print(a+b)
# add()  
# def add():
#     print(a-b)
# add() 
# def add():
#     print(a*b)
# add()
# def add():
#     print(a/b)
# add()   

# def add():
#     a = int(input("1-sonni kirit "))
#     b = int(input("2-sonni kirit "))
#     print(f"{a} va {b} ning yig'indisi {a+b} ga teng")
# add()
# add()
# add()

# def full_name(name,familya):
#     print(f"{name} {familya}")
# full_name("Ali","Zafarov")   
# full_name("Doston","Murodov")

# def full_name(name='Farux',familya='Murodov'):
#     print(f"{name} {familya}")
# full_name()    
# full_name("Ali","Zafarov")   
# full_name("Doston","Murodov")

# def yosh_hisobla(tugilgan_yil=2007, joriy_yil=2024):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla() 

# def son(son=5):
#     print(f'{son}ning kvadrati{son**2}ga teng, kubi{son**3}ga teng')
# son()

# def juftmi(son):
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")

# juftmi(25)
# juftmi(242)

# def solishtir(x,y):
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{y}>{x}")
#     else:
#         print(f"{x}={y}")

# solishtir(6,30)
# solishtir(-7,16)
# solishtir(1223*1,5**4)

# def daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")

# daraja(5,2)
# daraja(3,3)
# daraja(94,2)

def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(10)