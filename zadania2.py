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


# lista2=[x for x in range(1,11) if (x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 9 != 0)]
# print(lista2)


numdivs=[(number, [div for div in range (2,10) if number%div==0]) for number in range (1,1001)]

print(numdivs)

not_dividable=[]
for pair in numdivs:
    if not len(pair[1])>=1:
        not_dividable.append(pair[0])
print(not_dividable)

#no niby działa ale po mongolsku, pewnie da się lepiej xD
 
# Zadanie 3 - trudne
# Stworz funkcję która usunie ("wyplaszczy") zagnieżdzone listy

# l = [4, 1, [ 2, [7] ], 3]

# wyplaszcz(l)

# [4, 1, 2, 7, 3]

# Podpowiedź: sprawdź co robi funkcja wbudowana type
# lista =[4, 1, [5], [ 2, [7], 8 ], 3]

# def wyplaszcz(lista):
#     l2=[]
#     for i in lista:
#         if type(i) is not list: #jak jeden element to odrazu append do płaskiej listy
#             l2.append(i)
#         elif type(i) is list:
#             if len(i)==1:
#                 l2=l2+i #jednoelementowe listy dodajemy od buta
#             else:
#                 for l in i: 
#                     if type(l) is not list: 
#                         l2.append(l)
#                     else:
#                         for x in l:
#                             l2.append(x)
                        
#     print(l2)


#wyplaszcz(lista)