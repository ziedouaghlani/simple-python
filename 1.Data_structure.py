#List:
L=[1,2,3,4,5]
print(L[0])

L.append(6)  #add content to list
print(L)

print(len(L))

L.index(6)

for i in L:
    print(i)

L1=["a","b","d"]
print(''.join(L1))  #join a list of string


#Dictionary

D={
    "number": 1,
    3 : "three",
    "key": "value",
}
print(D)
print(D[3])
print(D["key"])

D["bla"]="bluew"  #Add content to Dictionary

for key in D:
    print(key,type(key))
    print(D[key])

#Nested List and Dictionary
D1={
    "number": [1,2,3],
    "France" : {"cities": ["paris","lyon","lille"]},
}

print(D1["number"][0])
print(D1["France"]["cities"][0])