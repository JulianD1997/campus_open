class Person:
    
    def __init__(self,name,years,phone):
        self.__name = name
        self.__years = years
        self.__phone = phone


    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name

    def get_years(self):
        return self.__years


    def set_years(self, years):
        self.__years = years

    def get_phone(self):
        return self.__phone

        
    def set_phone(self, phone):
        self.__phone = phone


class Client(Person):
    
    def __init__(self,name,years,phone,credit):
        super().__init__(name,years,phone)
        self.__credit = credit
    

    def get_credit(self):
        return self.__credit


    def set_credit(self, credit):
        self.__credit = credit
    

    def __str__(self):
        return f"El nombre del cliente es : {self.get_name()} su edad es {self.get_years()} años,\
            \nsu numero de telefono es {self.get_phone()} y el credito actual es {self.get_credit()} pesos"


mi_cliente = Client("Jonh",28,"89685641",8600)
print(mi_cliente)


class Employee(Person):


    def __init__(self, name, years, phone,salary):
        super().__init__(name, years, phone)
        self.__salary = salary
    

    def get_salary(self):
        return self.__salary


    def set_salary(self, salary):
        self.__salary = salary


    def __str__(self):
        return f"El nombre del empleado es : {self.get_name()} su edad es {self.get_years()} años,\
            \nsu numero de telefono es {self.get_phone()} y su salario actual es {self.get_salary()} pesos"    


mi_empleado = Client("Julian",25,"11232434",95000)
print(mi_empleado)
