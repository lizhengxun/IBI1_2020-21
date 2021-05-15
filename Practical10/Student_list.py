class student:
    def __init__(self,last_name,first_name,programme):
        self.last_name = last_name
        self.first_name = first_name
        self.programme = programme
    def information(self):
        return (self.last_name+self.first_name , self.programme)

#example
print(student('Li','Zhengxun','BMS').information())
