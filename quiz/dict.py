exi = 'hello this is'
listi = [1,2,3,7,6,5,1]
listi2 = listi
tupli = (1,2,3,7,6,5,1)
seti = {1,2,3,7,6,5,1}
dicti = {1:'one', 2:'two', 7:'seven', 6:'six', 5:'five'}


#Dict*********************************************************************************************

temp = 10 in dicti          #check key exists
print(temp)

temp1 = dicti.get(10, 'error')
temp2 = dicti.get(1, 'error')
temp3 = dicti.get(1200)

print('temp1 ---{}'.format(temp1))
print('temp2 ---{}'.format(temp2))
print('temp3 ---{}'.format(temp3))

dicti[5] = 'sample'
dicti[15] = 'sample15'

del dicti[6]
keysi = dicti.keys()
valuesi = dicti.values()
itemsi = list(dicti.items())[0]
print(itemsi)
print(dicti)

temp4 = dicti.pop(1)
temp5 = dicti.popitem()     #recently added key is removed

print(dicti)

dicti.update({10:'ten'})
temp7 = dicti.setdefault(40, 'forty')
temp6 = dicti.setdefault(10, 'forty')           # returs the value if exists else saves the new value

print('*****')
print(temp7)
print(temp6)
print(dicti)
