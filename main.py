import numpy as np

class Link:
    TYPE_CHOICES = ('rev','pri')

    def __init__(self, type:str, X, Y, Z=0):

        if type not in self.TYPE_CHOICES:
            raise ValueError(f"Invalid type: {type}. Must be one of {self.TYPE_CHOICES}")
        
        self.type = type
        self.head = np.array((X,Y,Z))

class Cordinate:
    def __init__(self):
        self.XAxis = np.array((0,0,0))
        self.YAxis = np.array((0,0,0))
        self.ZAxis = np.array((0,0,0))


class Robot:
    
    def __init__(self, *links:Link):
        self.links = links

    def normalized(self, vector):
        norm = np.linalg.norm(vector)
        if norm == 0:  
            return vector
        return vector / norm




    def give_constans(self):
        cord = [Cordinate]*len(self.links)
        for index, link in enumerate(self.links[:-1]):
            if link.type == 'pri':
                cord[index].ZAxis = self.normalized(self.links[index+1].head - self.links[index].head)
            else:
                pass

    def rel(self, a:Link, b:Link):
        pass

    def give_cords(self):
        pass
