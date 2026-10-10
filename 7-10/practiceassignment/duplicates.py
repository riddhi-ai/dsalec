#remove duplicates from the list
list =[1,1,3,1,3,4,6,8,9]
new_list=[]

for i in list:
    if i not in new_list: #checks the characters that are not duplicate
        new_list.append(i) #creates new list without duplicates

print("Original list is: ", list)
print("After removing duplicates from list:",new_list)