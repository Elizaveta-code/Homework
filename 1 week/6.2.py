def vector_mul(self, other):
    assert isinstance(other, Vector)
    return Vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
def area(x, y, z):
    return(abs((x-y).vector_mul(x-z))/2)
def max_area(l):
    max = 0
    res = ()
    for i in l:
        for k in l:
            t = area(i, j, k)
            if t > max:
                max = t
                res = (i, j, k)
    return(max, res)