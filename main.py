
#1 using join() method :-

name = ["My", "name", "is", "Legendary"]
print(" ".join(name)) # My name is Legendary


#2 using join() method and map() function :-

age= ["my", "age", "is", 25]
print(" ".join(map(str,age))) # my age is 25



#3 using a loop :-

#converter function
def converter(list):
# initialize an empty string
    string= ""
# loop overthe string
    for element in list:
        string+= str(element) 
# return string
    return string

year = ['year', 'of', 2022]
print(converter(year)) # yearof2022



#4 List Comprehension :-
month = ['we', 'are', 'in', 'the' ,12, 'month']
print(" ".join([str(element) for element in month])) # we are in the 12 month


#4.1 enumerate with list comprehension:-
day = ['today', 'is', 8, 'december']
print(" ".join([str(element) for i,element in enumerate(day )])) # today is 8 december


