#Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst ,reverse=True)
print(lst_sorted)




#You will be sorting the following list by each element’s second letter, a to z.
#Create a function to use when sorting, called second_let.
 #It will take a string as input and return the second letter of that string.
 #Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it.
 #Do not use lambda
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(x):
    return x[1]

sorted_by_second_let = sorted(ex_lst ,key=second_let)
print(sorted_by_second_let)




#Below, we have provided a list of strings called nums.
#Write a function called last_char that takes a string as input, and returns only its last character.
#Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(s):
    return s[-1]

nums_sorted =sorted(nums ,key=last_char)
print(nums_sorted)





#Once again, sort the list nums based on the last digit of each number from highest to lowest.
#However, now you should do so by writing a lambda function.
#Save the new list as nums_sorted_lambda.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums ,key=lambda x: x[-1])
print(nums_sorted_lambda)




#Sort this dictionary by values:
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
d={}
for i in L:
    d[i] = d.get(i , 0) + 1

sort =  sorted(d ,key=lambda i:d[i])
print(d)
print(sort)




#Sort the following dictionary based on the keys so that they are sorted a to z.
#Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary)
print(sorted_keys)



#Below, we have provided the dictionary groceries, whose keys are grocery items,
#and values are the number of each item that you need to buy at the store.
#Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1,
             'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1,
             'peanut butter': 2, 'spinach': 9}

grocery_keys_sorted=sorted(groceries)
print(grocery_keys_sorted)





#Sort the following dictionary’s keys based on the value from highest to lowest.
#Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary ,key=lambda x: dictionary[x] ,reverse =True)
print(sorted_values)



####################################################################

#Coursera Assighnment Final Exam:
#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"

sorted_letters = sorted(letters ,reverse=True)
print(sorted_letters)






#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra',
      'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)
print(animals_sorted)





#The dictionary, medals, shows the medal count for six countries during the Rio Olympics.
#Sort the country names so they appear alphabetically.
#Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical =sorted(medals)
print(alphabetical)





#Given the same dictionary, medals, now sort by the medal count.
#Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top = sorted(medals ,key=lambda i : medals[i] ,reverse =True)
print(top[:3])








#We have provided the dictionary groceries.
#You should return a list of its keys, but they should be sorted by their values, from highest to lowest.
#Save the new list as most_needed.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2,
'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15,
'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

most_needed = sorted(groceries ,key=lambda i : groceries[i] ,reverse=True)
print(most_needed)








#Create a function called last_four that takes in an ID number and returns the last four digits.
#For example, the number 17573005 should return 3005.
#Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest.
#Save this sorted list in the variable, sorted_ids.
#Hint: Remember that only strings can be indexed, so conversions may be needed.
def last_four(x):
    x=str(x)
    return x[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids =sorted(ids , key=last_four)
print(sorted_ids)








#Sort the list ids by the last four digits of each id.
#Do this using lambda and not using a defined function.
#Save this sorted list in the variable sorted_id
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id =sorted(ids , key=lambda x :str(x)[-4:] )
print(sorted_id)







#Sort the following list by each element’s second letter a to z.
#Do so by using lambda. Assign the resulting value to the variable lambda_sort
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst ,key=lambda x: x[1])
print(lambda_sort)
