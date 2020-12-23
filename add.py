# class myclass:
#     def __init__(self,value1,value2):
#         self.v1 = value1
#         self.v2 = value2
#         self.result = value1 + value2 
#     def add(self):
#         print("The result is =",self.result)

# a = int(input("enter value of a"))
# b = int(input("enter value of b"))
# obj1 = myclass(a,b)
# obj1.add()



class myclass:
    def __init__(self,value1,value2):
        self.v1 = value1
        self.v2 = value2
        self.add_res = value1 + value2
        self.sub_res = value1 - value2 
        self.mul_res = value1 * value2 
        self.div_res = float(value1) / float(value2)  
    def add(self):
        print("The addition is =",self.add_res)
    def sub(self):
        print("The subtaction is = ",self.sub_res)
    def mul(self):
        print("The Multiplication is = ",self.mul_res)
    def div(self):
        print("The divide is = ",self.div_res)
while(True):
    a = int(input("enter value of a=\t"))
    b = int(input("enter value of b\t"))
    con = input("press \n+ for add\n- for Subtract\n*for multiply\n/ for divide\n")
    if con == "+":
        obj1 = myclass(a,b)
        obj1.add()
        break
    elif con == "-":
        obj1 = myclass(a,b)
        obj1.sub()
        break
    elif con == "*":
        obj1 = myclass(a,b)
        obj1.mul()
        break
    elif con == "/":
        obj1 = myclass(a,b)
        obj1.div()
        break
    else:
        print("choose correct sign")
        continue
