#To count the occurrence of a specific element in a list.
list1=[1,2,3,2,4,5,2,6,6,6,8,6]
element=int(input("Enter the element:"))
count_of_element=list1.count(element)
print(count_of_element)
#we can also do this question in another way
count=0
for i in list1:
    if i==element:
        count+=1
print(count)        