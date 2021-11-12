from math import e
# e es el numero de euler

def ReLu(x):
    """Calcula el resultado de la funcion matematica ReLu"""
    return max(0, x)

def sigmoid(x):
    """Calcula el resultado de la funcion matematica Sigmoide"""
    return 1 / (1+e**(-x))

def sinh(x):
    """Calcula el resultado de la funcion matematica Sinh"""
    return ( e**x - (e**(-x))  ) / 2

def cosh(x):
    """Calcula el resultado de la funcion matematica Cosh"""
    return ( e**x + (e**(-x))  ) / 2

def tanh(x):
    """Calcula el resultado de la funcion matematica Tanh"""
    return sinh(x)/cosh(x)

#Main
if __name__ == '__main__':
    header = """
    .-------.    ,---.   .--.   ____       .-'''-.  
|  _ _   \   |    \  |  | .'  __ `.   / _     \ 
| ( ' )  |   |  ,  \ |  |/   '  \  \ (`' )/`--' 
|(_ o _) /   |  |\_ \|  ||___|  /  |(_ o _).    
| (_,_).' __ |  _( )_\  |   _.-`   | (_,_). '.  
|  |\ \  |  || (_ o _)  |.'   _    |.---.  \  : 
|  | \ `'   /|  (_,_)\  ||  _( )_  |\    `-'  | 
|  |  \    / |  |    |  |\ (_ o _) / \       /  
''-'   `'-'  '--'    '--' '.(_,_).'   `-...-'   
"""
    print(header)
    s = float(input("Introduce el numero: \n"))
    print("Funcion ReLu ->", ReLu(s))
    print("Funcion Sigmoid ->",sigmoid(s))
    print("Funcion Tanh ->",tanh(s))