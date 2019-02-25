
# coding: utf-8


def Red(N):
    if (N<0)|(N>1):
        return False
    elif (N<=1/6)&(N>=0)|(N>=5/6)&(N<=1):
        return 1
    elif (N>=1/6)&(N<=1/3):
        return -6*N+2
    elif (N>=2/3)&(N<=5/6):
        return 6*N-4
    else:
        return 0

def Green(N):
    if (N<0)|(N>1):
        return False
    elif (N>=1/6)&(N<=1/2):
        return 1
    elif (N<=1/6)&(N>=0):
        return 6*N
    elif (N>=1/2)&(N<=2/3):
        return -6*N+4
    else:
        return 0

def Blue(N):
    if (N<0)|(N>1):
        return False
    elif (N<=5/6)&(N>=1/2):
        return 1
    elif (N<=1/2)&(N>=1/3):
        return 6*N-2
    elif (N>=5/6)&(N<=1):
        return -6*N+6
    else:
        return 0
    
def chromatography(N):
    if (N<0)|(N>1):
        return False
    else:
        return (Red(N),Green(N),Blue(N))

