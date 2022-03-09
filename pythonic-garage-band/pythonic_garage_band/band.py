
from abc import abstractmethod

class Musician: 

    def __init__(self ,name, instrument):
        self.name = name
        self.instrument =  instrument

    
    def get_instrument (self):
        return f'{self.instrument}'

    @abstractmethod
    def play_solo(self):
         pass

    def __str__ (self):
       return f'My name is {self.name} and I play {self.instrument}'

    @abstractmethod
    def __repr__(self):
        pass
    

class Guitarist(Musician):
    def __init__(self ,name):
        self.name = name
        self.instrument = "guitar"
        # self.play_solo=

    # def get_instrument (self):
    #     return self.instrument
    def play_solo(self):
        return "face melting guitar solo"

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    # def play_solo(self):
    #      return self.play_solo
    # def get_instrument (self):
    #     return self.instrument



class Bassist(Musician):
    def __init__(self ,name):
        self.name = name
        self.instrument = "bass"
        # self.play_solo="bom bom buh bom"

    def play_solo(self):
        return "bom bom buh bom"

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):
    def __init__(self ,name):
        self.name = name
        self.instrument = "drums"
        # self.play_solo= "rattle boom crash"

    def play_solo(self):
        return "rattle boom crash"
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

class Band:

    instances = []
    members = []

    def __init__(self , name , members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    
    
    def __str__ (self):
        pass


    def __repr__(self):
        pass
    

    def play_solos(self):
        solos=[]
        for i in self.members:
            solos.append(i.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


if __name__== "__main__":
    j = Drummer( "1")
    print(j.play_solo)
    the_nobodies = Band("The Nobodies", [])
    