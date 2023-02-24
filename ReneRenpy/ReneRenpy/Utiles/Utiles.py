def esFuncion(a):
    tipoStr=str(type(a))
    return tipoStr=="<class 'function'>" or tipoStr=="<type 'function'>"
def esInt(a):
    if isinstance(a,bool):
        return False
    return isinstance(a, int)
def esIntAll(a,i0=0):
    for i,n in enumerate(a[i0:]):
        if not esInt(n):
            return False
    return True
def esString(a):
    return isinstance(a,str) or isinstance(a,unicode)

def isNoneAll(*a):
    for e in a:
        if e is not None:
            return False
    return True
