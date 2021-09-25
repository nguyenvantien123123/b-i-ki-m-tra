

A=[ 1,1,2,3,5,8,13,21,34]
B=[ 1,3,5,4,7,88,66,59,40,54]
print("list A:",A)
print("list B:",B)
C= list( set (A) & set (B))

print( "các phần tủ trùng nhau trong 2 mảng là  ", C)

# E=[ num for  num in A if A !=C]
# D=set (A) ^ set (B)
D= list( set (A) ^ set (C))
print("các phần tử của list A không trùng với B là: :",D)
E= list( set (B) ^ set (C))
print("các phần tử của list B không trùng với A là:  :",E)
