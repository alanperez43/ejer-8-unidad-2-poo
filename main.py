from claseconjuntos import conjunto
from menu import Menu
if __name__ == "__main__":
    a=conjunto()
    b=conjunto()
    num=input("ingesar valor positivo para cargar el promer conjunto: ")
    if(any(chr.isdigit() for chr in num)== False):
        print("error usted ingreso una cadena")
        num=input("ingesar valor positivo para cargar el promer conjunto: ")
    while(num != "fin"):
        num=int(num)
        if(type(num)==int):
            a.agregar(num)
            num=input("ingesar valor positivo para cargar el promer conjunto <finalizar con<fin>>: ")
        else:
            print("error numero mal ingresado")
        
        if(type(num)==str): 
            num=num.lower()   
    num=input("ingesar valor positivo para cargar el segundo conjunto: ") 
    if(any(chr.isdigit() for chr in num)== False):
        print("error usted ingreso una cadena")
        num=input("ingesar valor positivo para cargar el promer conjunto: ")  
    while(num != "fin"):
        num=int(num)
        if(type(num)==int):
            b.agregar(num)
            num=input("ingesar valor positivo para cargar el segundo conjunto <finalizar con<fin>>: ")
        if(type(num)==str):
            num=num.lower()
    MenU=Menu()
    op=None
    while(op!=4):
        print("|------------------------------------------------------|")
        print("|1 para: sumar los objetos ingresados                  |")
        print("|2 para: restar los objetos ingresados                 |")
        print("|3 para: ver cual objeto es mayor                      |")
        print("|------------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        MenU.opcion(op,a,b)