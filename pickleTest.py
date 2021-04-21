import pickle

def string2list(input):
    a = input.strip('][')
    a = a.split(',')
    #print(a)

    for i in range(len(a)):
        try:
            x = complex(a[i])
            if x.imag != 0:
                a[i] = x
            elif x.imag == 0:
                try:
                    x = float(a[i])
                    if x.is_integer():
                        x = int(a[i])
                        a[i] = x
                    else:
                        a[i] = x
                    
                except:
                    continue
        except:
            x = str(a[i])
            x = x.strip(" '")
            a[i] = x
    return a

resultList = []
while 1:
    a = str(input('Enter a list: '))
    if a == '':
        print('Empty list')
        break
    else:
        a = string2list(a)
        print(a)
        resultList.append(a)

print(resultList)

with open('list_yay2.pk1', 'wb') as handle:
    pickle.dump(resultList, handle)

with open('list_yay2.pk1', 'rb') as handle:
    mynewlist = pickle.load(handle)

print("Get data via pickle.load")
#print(mynewlist)
#print(type(mynewlist))

for i in mynewlist:
    print(i)