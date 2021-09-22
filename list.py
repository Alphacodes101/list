# # Lists are used to store multiple items in a single variable.

# # Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
mylist = ["apple", "banana", "cherry"]
print(mylist)


# #LIST LENGTH 
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# #access items 
newlist = ["apple", "banana", "cherry"]
print(newlist[1])


# #range of indexing 
new1list=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(new1list[2:5])


# #check items 
new2list = ["apple", "banana", "cherry"]
if "apple" in new2list:
  print("Yes, 'apple' is in the fruits list")
  

# #change list items 
new3list = ["apple", "banana", "cherry"]
new3list[1] = "blackcurrant"
print(new3list)

# #insert items 
new4list = ["apple", "banana", "cherry"]
new4list.insert(2, "watermelon")
print(new4list)

# #append items 
new5list = ["apple", "banana", "cherry"]
new5list.append("orange")
print(new5list)

# #extend list 
fruitlist= ["apple", "banana", "cherry"]
fruitlist2=["mango","pineapple","papaya"]
fruitlist.extend(fruitlist2)
print(fruitlist)

# # remove list items
hellolist = ["apple", "banana", "cherry"]
hellolist.remove("banana")
print(hellolist)

# # remove the last items
ram = ["apple", "banana", "cherry"]
ram.pop()
print(ram)

# #remove the specified index
rahul= ["apple", "banana", "cherry"]
del rahul[0]
print(rahul)

# clear method to empities the list 
aman=["apple", "banana", "cherry"]
aman.clear()
print(aman)

# #loops through the list 
helloram=["apple", "banana", "cherry"]
for x in helloram:
    print(x)
    
# #loops through the index numbers 
rehyan=["apple", "banana", "cherry"]
for i in range(len(rehyan)):
    print(rehyan[i])
    
# #using a while loops
arjun= ["apple", "banana", "cherry"]
i=0
while i <len(arjun):
    print(arjun[i])
    i=i+1
    