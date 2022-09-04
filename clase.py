class Persona:
    __name = None
    __years = None
    __phone = None
    def __init__(self):
        pass


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

mi_persona = Persona()
mi_persona.set_name('John')
mi_persona.set_years(28)
mi_persona.set_phone("11437235")
print(f"La persona se llama {mi_persona.get_name()} tiene {mi_persona.get_years()} años y su numero de celular es {mi_persona.get_phone()}")