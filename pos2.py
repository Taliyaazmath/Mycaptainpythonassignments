#incase we were suppose to input a list as i didn't understand the question

list1=[]
n=int(input("enter the number of element to upload:"))
for i in range(n):
    element=int(input("enter the element to be added "))
    list1.append(element)
print(list1)


pos_list1=[]
for n1 in list1:
    if n1>0:
        pos_list1.append(n1)

print("the postive numbers are:")
print(pos_list1)
