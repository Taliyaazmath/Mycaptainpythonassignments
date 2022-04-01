#all positive numbers in a range
list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
'''
len_list1 =len(list1)
len_list2 =len(list2)

n1= len_list1+1
'''
pos_list1=[]
pos_list2=[]
for n1 in list1:
    if n1>0:
        pos_list1.append(n1)
        
for n2 in list2:
    if n2>0:
        pos_list2.append(n2)

print("positive element of the list1:")
print(pos_list1)

print("positive element of the list2:")
print(pos_list2)
