###Creating Different Type of Lists

# list of fruits
['Apple', 'Mango', 'Banana']

#list of cities
Fav_cities = ['Banglore', 'Jaipur', 'Kanpur']

#list of numbers
numbers = [1,2,3,5]

#empty list
empty=[]

#list with mixed data type
mixed = [3,"Mango", 4.5]

#nested List
nested = ["Mango",[4,5,6],['a']]


###Accessing List Elements
print(Fav_cities[2]) #p (third elements)

##negative Indexing
print(Fav_cities[-1])

#List slicing in Python
List = ['p','r','o','g','r','a','m','i','z']
print(List[2:7])

#adding and changing the List elemets
even=[4,5,8,10]
even[1]=6
print(even)


# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]
print(my_list)