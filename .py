'''                     print("Let us define the logic of permutations")                  '''
from numbers import Number
def Fact(num):
        temp = 1
        for i in range(1,num+1):
            temp = temp * i
        return temp


class P:

    def __init__(self,n,r):
        self.n = n
        self.r = r 
        if(type(self.n)== int and type(self.r)== int):
            if(self.n >= self.r):
                if(self.n>=0 and self.r>=0):
                    pass
                else:
                    raise ValueError("Invalid Input!")
            else:
                raise ValueError("Invalid Input!")
        else:
             raise ValueError("Please, Enter an interger!")

    def Value(self):
        num  = Fact(self.n)
        den = Fact(self.n - self.r)
        val = (num / den)
        return val
        

    def __str__(self):
        return(f"P({self.n},{self.r}) = {self.Value()}")

         
    def __add__(self,other):
        if isinstance(other,Number):
            result = self.Value() + other
        elif isinstance(other,P):
             result = self.Value() + other.Value()
        else:
             return NotImplemented
        return result

    def __radd__(self,other):
        return self.__add__(other)

    def __sub__(self,other):

        if isinstance(other,Number):
            result = self.Value() - other
        elif isinstance(other,P):
            result = self.Value() - other.Value()
        else:
             return NotImplemented
        return result

    def __rsub__(self,other):
            if isinstance(other,Number):
                 return other - self.Value()
            else:
                 return NotImplemented

    def __mul__(self,other):
        if isinstance(other,Number):
            result = self.Value() * other
        elif isinstance(other,P):
            result = self.Value() * other.Value()
        else:
             return NotImplemented
        return result

    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __truediv__(self, other): 
        if isinstance(other,Number):
            result = self.Value() / other
        elif isinstance(other,P):
            result = self.Value() / other.Value()
        else:
             return NotImplemented
        return result
    
    def __rtruediv__(self,other):
            if isinstance(other, Number):
                return other/self.Value()
            else:
                return NotImplemented

    def __eq__(self, other):
        if isinstance(other,Number):
            return self.Value() == other
        elif isinstance(other,P):
             return self.Value() == other.Value()
        else:
            return NotImplemented