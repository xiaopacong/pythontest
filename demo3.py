class Person():
    #成员变量
    name="张三"
    age=22
    address="长沙"

    def eat(self):
        print(self.name,"吃饭")


    def run(self):
        print("干活赚钱") 

    def love(self,):
        self.run()    

p=Person()
# print(p.name)
p.love()          