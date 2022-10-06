exi = 'hello this is'
listi = [1,2,3,7,6,5,1]
listi2 = listi
tupli = (1,2,3,7,6,5,1)
seti = {1,2,3,7,6,5,1}
dicti = {1:'one', 2:'two', 7:'seven', 6:'six', 5:'five'}




#Set**************************************************************************************************
seti.add(10)
seti.update([100,200])

temp = seti.pop()
print('temp -- {}'.format(temp))
seti.remove(7)
seti.discard(200)
seti1 = {6,7,8,9}

print(seti)
print(seti.union(seti1))
print(seti.intersection(seti1))
print(seti-seti1)
print(seti^seti1)





