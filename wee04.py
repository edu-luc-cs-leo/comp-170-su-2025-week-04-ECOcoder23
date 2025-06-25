words = ["the", "bright", "sun", "was", "extinguish'd", "and", "stars", "did","wander", "darkling", "in", "eternal", "space"]

# Function to find longest word in list of strings

def longest_word(words: list[str]) -> str: 
 # Create a variable named "longest" and assign is to the first string is the list "words"
  
  i = 0
  longest = words[i]

 # While statement (in order to run the following loop until no strings are left "unexamined")
 
  while i < len(words):
 
 # If there is a string in the list with more characters than the current one 
 # assinged "longest", the variable "longest" now gets assigned to that string   
   
    if len(words[i]) > len(longest):
      longest = words[i]
 
 # Moves on to string number n+1 until i = list length (meaning 
 # no more strings are left to examine)   
    
    i = i + 1   
  return longest 

print(longest_word(words))





# Function to find the shortest word in a list of strings

def shortest_word(words: list[str]) -> str:
  # Create a variable named "shortest" and assign is to the first string is the list "words"
 
  i = 0
  shortest = words[i]
 
 # While statement (in order to run the following loop until no strings are left "unexamined")
 
  while i < len(words):
 
 # If there is a string in the list with less characters than the current one 
 # assinged "shortest", the variable "shortest" now gets assigned to that string
   
    if len(words[i]) < len(shortest):
      shortest = words[i]
 
 # Moves on to string number n+1 until i = list length 
 # (meaning no more strings are left to examine) 
 
    i = i + 1 
  return shortest  

print(shortest_word(words))





# Function to return a list of words with a length = odd number

def odd_words(words: list[str]) -> list[str]: 
 
# Create an empty list named "list_of_odd_words"
 
  list_of_odd_words = list()
 
# Starting from the first string, divide the character length value of each string by 2
 
  i = 0 
  while i < len(words): 
    if len(words[i]) % 2 != 0:
      
# If there is a remainder after the division (meaning it's an odd number) add the string
# to the list "list_of_odd_words"      
  
      list_of_odd_words.append(words[i])

# Moves on to string number n+1 until i = list length and there are no strings left to examine

    i = i + 1
  return list_of_odd_words  

print(odd_words(words))





# Function to find words whose lenth deviates +/- 1 from the Avg word length

def list_avg(words: list[str]) -> int:
 
 # Ensures that we begin from the first string
 
 i = 0

# Creates a variable named "sum" and assigns the value "0" to it

 sum = 0
 
# For each string more than "0" characters long, add its character
# length value to the value of the variable "sum"
 
 while i < len(words): 
    if len(words[i]) > 0:
      sum = sum + len(words[i]) 
      
# Create a variable named "avg" with a value equivalent to the current
# sum value divided by the length of the list "words"      
      
      avg = sum / len(words)
   
# Moves on to string number n+1 until none are left (i = list length)   
   
    i = i + 1
 return int(avg)
  
def average_words(words: list[str]) -> list[str]: 
 
# Creates a variable named "deviation", which is a range of values [-1 -> 2)
 
  deviation = range(-1, 2, 1)
 
# Creates an empty list named "list_of_avg_words" 
 
  list_of_avg_words = list()

# Starting from the first string, subtracts the length of the nth string
# from the average string length value (found using "list_avg" function above)

  i = 0 
  while i < len(words):
    if (list_avg(words) - len(words[i])) in deviation: 
     
# If the remainder of the subtractive operation is found in the range "deviation"
# (meaning the string is +/- 1 from the avg string length) add string to the
# empty list "list_of_avg_words"    
     
      list_of_avg_words.append(words[i])
   
# Moves on to string number n+1 until none are left (i = list length) 
   
    i = i + 1 
  return list_of_avg_words     

print(average_words(words))

foo = ["free", "orange", "oreos"]

bar = ["beyond", "all", "reason"]

# Function to find if an intersection between two lists exists

def intersect(foo: list[str], bar: list[str]) -> bool: 
  
# Ensures that we begin from the first string 
  
  i = 0
 
# Before we've reached the end of the list "foo", if the nth string
# in the list is also in the list "bar", then return "True"
 
  while i < len(foo): 
    if foo[i] in bar:
      return True

# If the nth string is not in the list "bar", go to string number n+1

    elif foo[i] not in bar:
      i = i + 1 

# If we've exhaused the list "foo" and its final string is not found
# in the list "bar", then return "False" (no strings shared by the lists)

  else: 
     if i == len(foo) and foo[-1] not in bar:
      return False 

print(intersect(foo, bar))














#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
