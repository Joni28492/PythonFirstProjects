cabecera = """
 ______                            _______  _______          
(  __  \ |\     /|       |\     /|(  ___  )(  ____ \|\     /|
| (  \  )| )   ( |       | )   ( || (   ) || (    \/| )   ( |
| |   ) || |   | | _____ | (___) || (___) || (_____ | (___) |
| |   | || |   | |(_____)|  ___  ||  ___  |(_____  )|  ___  |
| |   ) || |   | |       | (   ) || (   ) |      ) || (   ) |
| (__/  )| (___) |       | )   ( || )   ( |/\____) || )   ( |
(______/ (_______)       |/     \||/     \|\_______)|/     \|

"""

def duHash(obj):
    return hash(obj)

if __name__ == '__main__':
    print(cabecera)
    s = input("introduce cadena a hashear\n")
    print("la cadena hasheada es: \n", duHash(s))


