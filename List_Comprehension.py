
#List Comprehension

a=["codegnan","python","course"]

'''for i in a:
    print(i.upper(),end=",")'''

#syntax

'''b=[i.upper() for i in a]
print(b)'''

'''a=["hello","python"]
b=[i.title() for i in a]
print(b)'''

'''a=[1,3,4,5,6,8,12,13]
#b=[i*i for i in a]
b=[i**2 for i in a]
print(b)'''


'''a=["apple","banana","grapes","kiwi","mango","blueberry"]

b=[i for i in a if 'a' not in i]
print(b)


b=[i for i in a if 'a' in i]
print(b)'''


#Range
'''a=[i for i in range(21) if i%2==0]
print(a)

a=[i**2 for i in range(21) if i%2==0]
print(a)

a=[i for i in range(21) if i%2!=0]
print(a)

a=[i**2 for i in range(21) if i%2!=0]
print(a)'''


#No elif usage in list comprehension

#if-else

'''a = [i**2 if i % 2 == 0 else i*5 for i in range(16)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#output[6,6,6,6,6]
#c=[a[0]+b[0] ,a[1]+b[1],a[2]+b[2],a[3]+b[3],a[4]+b[4]]

# List comprehension method
'''c=[a[i]+b[i] for i in range(5)] #method 1
c=[a[i]+b[i] for i in range(len(a))] #method 2
print(c)'''




































    
