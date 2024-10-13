#List Reverse numbers/string
sentence=input('enter any sentence: ')
print('original sentence: \n',sentence)
nsen=sentence.split()
nsen.reverse()
print('Reversed Sentence: \n',nsen)

a=[1,2,3,4,5,6]
print(list(reversed(a)))
a.reverse()
print(a)

b=['Ahmad','Rahim','Shafiq','Qadir','Umair']
print('Original String: ',b)
print('\nString Reversed using [reversed()function]: \n', list(reversed(b))) # use of reversed() function
b.reverse() #use of reverse() function
print('\nString Reversed using [reverse()function]: \n', b)
print('Reverse String Slicing:\n',sentence[::-1])
