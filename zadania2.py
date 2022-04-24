# Zadanie 1 - łatwe
#Posortować dluga_lista po wartości bezwględnej elementów listy interpretowanych jako wartość całkowita 

dluga_lista = [ str(i) for i in range(21)] + [ str(i) for i in range(-1, -21, -1)]

print(dluga_lista)

def abs_val(n):
    return abs(int(n))

dluga_lista.sort(key=abs_val)
print(str(dluga_lista))