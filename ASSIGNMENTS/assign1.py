import json
import itertools

# No.1 store dictionary data into a json file

# Original dictionary:
dict1 = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
                {'firstName': 'Mervin', 'lastName': 'Friedland'},
                {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
         'teachers': [{'firstName': 'Amberly','lastName': 'Calico'},
                    {'firstName': 'Regine', 'lastName': 'Agtarap'}]} 

print(type(dict1))


with open("dictionary", "w") as first:
   json.dump(dict1, first, indent = 4, sort_keys = True)

print("\nJson file to dictionary:")
with open('dictionary') as first:
 data = json.load(first)
print(data)



#No2. Write a Python program to convert more than one list to nested dictionary.
# original lists
# [['S001', 'S002', 'S003', 'S004'] ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'] [85,98, 89, 92]]

def convert(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

list1 = ["S001", "S002", "S003", "S004"] 
list2 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
list3 = [85, 98, 89, 92]
print(list1)
print(list2)
print(list3)
print("\nNested dictionary:")
ch='a'
print(convert(list1, list2, list3))

# No3. Write a Python program to check a dictionary is empty or not
my_dict = {}
if not bool(my_dict):
    print("\nDictionary is empty")

# No4. Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.


my_dicts= {'x':['b','c'],'y':['d','e'],'z':['f','g']}
for allitems in itertools.product(*[my_dicts[k] for k in sorted(my_dicts.keys())]):
    print(''.join(allitems))
	

# No5. Write a program that takes in a list of numbers 
# and returns a set containing only the unique values in the list.
# option1 set
mylist = [1,2,3,4,2,5,6,7,6]
unique_numbers = list(set(mylist))
print(unique_numbers)

# other option iteration
def get_unique(mylist):
    unique = []
    for number in mylist:
        if number in unique:
            continue
        else:
            unique.append(number)
            return unique
print(get_unique(mylist))
            

# No6. Create a dictionary that maps the names of countries to their respective capital cities.
#  Allow the user to enter a country name and have the program output the capital.
countries = {'uganda':'kampala', 'kenya':'nairobi','tanzania':'dar-es-salaam'}
user = input("Enter country name: ")

if user in countries:
        print(countries[user] )
else:
        print(user, "does not exist in my database")



# random code
A = dict(zip('ab`cdef', list(range(6))))
for key in A:
    print(key, A[key])
    


