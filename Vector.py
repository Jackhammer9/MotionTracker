import math

def clamp(number , smallest , largest):
    return sorted((smallest, number, largest))[1]

class Quaternion(object):

    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z

    def x(self):
        return self.x

    def y(self):
        return self.y

    def z(self):
        return self.z

    def setx(self , r):
        self.x = r

    def sety(self , r):
        self.y = r

    def setz(self , r):
        self.z = r

    def __str__(self):
        return f'({self.x} , {self.y} , {self.z})'

    def __eq__(self , quaternion):
        if type(quaternion) != Quaternion:
            raise TypeError(f'Illegal action with type {type(quaternion)} use Quaternion')
        if self.x == quaternion.x and self.y == quaternion.y and self.z == quaternion.z:
            return True
        else:
            return False

class Vector3(object):

    def __init__ (self , i , j , k):
        self.i = i
        self.j = j
        self.k = k

    def i(self):
        return self.i

    def j(self):
        return self.j

    def k(self):
        return self.k

    def Magnitude(self):
        return (self.i**2 + self.j**2 + self.k**2)**0.5

    def __add__(self,vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        return Vector3(self.i + vector.i , self.j + vector.j , self.k + vector.k)

    def __sub__(self,vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        return Vector3(self.i - vector.i , self.j - vector.j , self.k - vector.k)

    def __str__(self):
        return f'({self.i}î {self.j}ĵ {self.k}k̂)'

    def __gt__(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        if self.Magnitude() > vector.Magnitude():
            return True
        else:
            return False

    def __lt__(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        if self.Magnitude() < vector.Magnitude():
            return True
        else:
            return False

    def __le__(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        if self.Magnitude() <= vector.Magnitude():
            return True
        else:
            return False

    def __ge__(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        if self.Magnitude() >= vector.Magnitude():
            return True
        else:
            return False

    def __eq__(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        if self.Magnitude() == vector.Magnitude() and self.dir == vector.dir:
            return True
        else:
            return False

    def __mul__(self , scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError(f'Illegal action with type {type(scalar)} use int or float')
        return Vector3(self.i * scalar , self.j * scalar , self.k * scalar)

    def __truediv__(self , scalar):
        if type(scalar) != int and type(scalar) != float:
            raise TypeError(f'Illegal action with type {type(scalar)} use int or float')
        return Vector3(self.i / scalar , self.j / scalar , self.k / scalar)

    def Normalize(self):
        Magnitude = self.Magnitude()
        self.i /= Magnitude
        self.j /= Magnitude
        self.k /= Magnitude

    def Dot(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        return self.i * vector.i + self.j * vector.j + self.k * vector.k

    def Cross(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        i = self.j*vector.k - self.k*vector.j
        j = self.i*vector.k - self.k*vector.i
        k = self.i*vector.j - self.j*vector.i
        return Vector3(i , j*-1 , k)

    def Angle(self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        self.Normalize()
        vector.Normalize()
        return math.acos(clamp(self.Dot(vector) , -1 , 1)) * 180 / math.pi

    def Towards(self , vector , MaxDist):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        target = vector - self
        sqd = target.Magnitude()**2
        if sqd == 0 or MaxDist >= 0 and sqd <= MaxDist**2:
            return vector
        dist = target.Magnitude()
        return Vector3(self.i + target.i / dist * MaxDist,
        self.j + target.j / dist * MaxDist, self.k + target.k / dist * MaxDist)

    def Distance (self , vector):
        if type(vector) != Vector3:
            raise TypeError(f'Illegal action with type {type(vector)} use Vector3')
        return (vector-self).Magnitude()

    def One():
        return Vector3(1 , 1 , 1)

    def Zero():
        return Vector3(0 , 0 , 0)