exi = 'hello this is'
listi = [1,2,3,7,6,5,1]
tupli = (1,2,3,7,6,5,1)
seti = {1,2,3,7,6,5,1}
dicti = {1:'one', 2:'two', 7:'seven', 6:'six', 5:'five'}

#List**************************************************************************************************
listi1 =  [1,2,3,7,6,5,1]
listi2 = listi
print(listi is listi1)
print(listi is listi2)
print(1 in listi)

print(id(listi))
listi.append(8)
listi.extend([9,10])
listi.pop(2)
listi.remove(1)
listi.insert(0,1)
listi.sort()
listi.sort(reverse=True)
rlisti = reversed(listi)
listi.reverse()
listi.count(1)
listi1 = listi
listi2 = listi.sort()
listi4 = sorted(listi, reverse=True)        #another way to sort and store in diff variable
temp = listi.index(1)
listi3 = listi.copy()

#find item's index 
enter_item = 5
listi_len = len(listi)
i=0
index_listi = []

print(listi)
while i <= listi_len:
    try:
        res = listi.index(enter_item,i,listi_len)
    except ValueError:
        break
    i+=1
    index_listi.append(res)
print('found--{}'.format(set(index_listi)))
print(min(listi))





print(id(listi1))   #id doesnot change
print(id(listi2))   #id will change
print(id(listi3))   #id will change

print("string ---{}".format(exi))
print("list ---- {}".format(listi))
print("tuple --- {}".format(tupli))
print("set ----- {}".format(seti))
print("dict ---- {}".format(dicti))
