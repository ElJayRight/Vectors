class vector:
    def __init__(self,*args): #class magic
        self.vect = []
        for i in args:
            self.vect.append(i)

    def scalar(self,multiple):
        new = []
        for i in self.vect:
            i = i*multiple
            new.append(i)
        self.vect = new

    def __str__(self): #class magic for testing
        return str(self.vect)
    def __add__(self,other):
        if type(other) == type(self):
            if len(other.vect)==len(self.vect):
                new = []
                print(len(other.vect))
                for i in range(len(other.vect)):
                    new.append(self.vect[i]+other.vect[i])
                return vector(*new)
    def __sub__(self,other):
        if type(other) == type(self):
            if len(other.vect)==len(self.vect):
                new = []
                print(len(other.vect))
                for i in range(len(other.vect)):
                    new.append(self.vect[i]-other.vect[i])
                return vector(*new)

        else:
            raise 'invalid data type'
    def __mul__(self,other):
        if type(other) == type(self):
            if len(other.vect)==len(self.vect):
                result = 0
                for i in range(len(other.vect)):
                    result = result + other.vect[i]*self.vect[i]
                print('dot product is',str(result))
            else:
                raise 'not of same dimensions'
        elif type(other)==int:
            self.scalar(other)
            print(self.vect)
        else:
            raise 'invalid data type'
            
#testing
one = vector(1,2,3)
two = vector(2,3,4)
one*two
three = one+two
three*2
