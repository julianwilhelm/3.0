# Zadanie 1 - łatwe
#Posortować dluga_lista po wartości bezwględnej elementów listy interpretowanych jako wartość całkowita 

    # dluga_lista = [ str(i) for i in range(21)] + [ str(i) for i in range(-1, -21, -1)]

    # print(dluga_lista)

    # def abs_val(n):
    #     return abs(int(n))

    # dluga_lista.sort(key=abs_val)
    # print(str(dluga_lista))

#Zadanie 2 - średnie
#Wygenerować listę liczb z zakresu 1-1000 które nie są podzielne przez żadną cyfrę od 2 do 9


# lista2=[x for x in range(1,1001) if (x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 9 != 0)]
# print(lista2)

#no niby działa ale po mongolsku, pewnie da się lepiej xD

# Zadanie 3 - trudne
# Stworz funkcję która usunie ("wyplaszczy") zagnieżdzone listy

# l = [4, 1, [ 2, [7] ], 3]

# wyplaszcz(l)

# [4, 1, 2, 7, 3]

# Podpowiedź: sprawdź co robi funkcja wbudowana type
l = [4, 1, [ 2, [7] ], 3]

def wyplaszcz(l):
    l2=[]
    for i in l:
        if len(i)==1:
            if type(i) is int:
                l2.append(i)
            elif type(i) is list:
                l2=l2+i
                for l in l2:
                    if type(l) is not int:
                        l2=l2+l
        print(l2)


wyplaszcz(l)