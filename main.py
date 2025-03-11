import numpy as np

class Link:
    
    def __init__(self,type:str, length:float, *args, **kargs):
        self.type = type
        self.length = length


class Machin:
    
    def __init__(self, *links:Link):
        self.links = links

    def give_constans(self):
        pass

    def rel(self, a:Link, b:Link):
        pass

    def give_cords(self):
        pass



