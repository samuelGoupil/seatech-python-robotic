
from exo1 import Robot



class Human():   
    __sexe = "<undefined>"
    __name = "<unnamed>"
    
    def __init__(self, name, sexe):
        self.__name = name
        self.__sexe = sexe

    def set_sexe(self, sexe):
        self.__sexe = sexe

    def get_sexe(self):
        return self.__sexe
    
    def get_name(self):
        return self.__name
    
    def eat(self, aliment):
        if type(aliment) is str:
            print(self.__name + " mange " + aliment)
        elif type(aliment) is list:
            for i in aliment:
                print(self.__name + " mange " + i)
        



    def digest(self, aliment):
        if type(aliment) is str:
            print(self.__name + " digere " + aliment)
        elif type(aliment) is list:
            for i in aliment:
                print(self.__name + " digere " + i)



    
    
        
        

class Cyborg( Human,Robot):   

    def __init__(self, name, sexe, family_name):   
        Robot.__init__(self, name)
        Human.__init__(self, family_name, sexe)

    """ def get_name(self):
        print() """


if __name__ =="__main__":
    
    cyborg = Cyborg('DeuxExMachina', 'M', 'dupont')

    print(cyborg.get_name(), 'sexe', cyborg.get_sexe())
    print('Charging battery...')
    cyborg.recharge()
    cyborg.get_states()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest('banana')