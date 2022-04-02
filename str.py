

import operator
def most_frequent(string):
    dict={}
    for i in string:
        char = dict.keys()
        if i in char:
            dict[i] +=1
        else:
            dict[i]=1
    return dict

str1=input("please enter the string:")
n=most_frequent(str1)


#itemgetter(n) builds a callable object that assumes it as iterable
#dict.items() used to get items
#key parameter takes the function as its value,transforms elements before being sorted

sorted_dic = sorted(dict.items(n),key=operator.itemgetter(1),reverse=True)
print(sorted_dic)


        
    
