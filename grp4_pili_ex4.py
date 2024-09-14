#Script that runs a condition in an if statement
con = 6 > 10
if con:
    print("Condition is True")
else:
    print("Condition is False")

#Script that has List, Tuples, Sets, and Dictionaries also uses String, int, and boolean data types in each collection.

the_list=["Lakers", 17, True] #17 championships, True because they are playing in the 2023-2024 playoffs
print("List:",the_list)

the_tuple=("Boston Celtics",18,True) #18 championships, True because they are playing in the 2023-2024 playoffs
print("Tuple:",the_tuple)

the_set={"Golden State Warriors", 5, False} #5 championships, False because they are not playing in the 2023-2024 playoffs
print("Set:",the_set)

my_dict = {
"NBA Team":"San Antonio Spurs",
"championships":5, #5 championships
"available":False  #False because they are not playing in the 2023-2024 playoffs
}
print("Dictionary:",my_dict)