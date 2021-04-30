class Menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3
        }
    def opcion(self,op,a,b):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(a,b)
    def op1(self,a,b):
        suma=a+b
        
        print("resultado de la suma",suma)
    def op2(self,a,b):
        resta=a-b
        
        print("resultado de la resta",resta)
    def op3(self,a,b):
        a==b