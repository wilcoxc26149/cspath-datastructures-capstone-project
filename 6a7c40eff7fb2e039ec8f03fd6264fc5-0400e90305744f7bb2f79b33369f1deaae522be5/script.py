from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList
from stack import Stack

#Printing the Welcome Message
print_welcome()

# pretty_rest_print()
# Created a convenience method to ask the user if they want to see the restaurants. 
# If yes, print out the list of restaurants (a word I will never mispell again)
# associated with a food type in a pretty format. 
# Arguments:
#   food_type: str - The food type string which is used to map to the restaurant list.
#   rest_hashmap: HashMap - Restaurant data from a food_type hashmap of LinkedLists.
def pretty_rest_print(food_type, rest_hashmap):
  while True:
    yes_or_no = str(input("\nYour food type search returned %s. Would you like to see a list of %s restaurants? Enter 'y' for yes and 'n' for no.\n" % (food_type.capitalize(), food_type.capitalize()))).lower()
    if yes_or_no == 'y':
      rest_list = rest_hashmap.retrieve(food_type)
      current_node = rest_list.get_head_node()
      pretty_rest_print = "\n------------------------------\n"
      while current_node:
        restaurant = current_node.value
        pretty_rest_print += "\nName:\t %s\n" % restaurant[1]
        pretty_rest_print += "Price:\t %s\n" % restaurant[2]
        pretty_rest_print += "Rating:\t %s\n" % restaurant[3]
        pretty_rest_print += "Address: %s\n" % restaurant[4]
        pretty_rest_print += "\n------------------------------\n"
        current_node = current_node.get_next_node()
      print(pretty_rest_print)                           
      break
    elif yes_or_no == 'n':
      print("Maybe next time.")
      break
    else:
      print("Invalid input: %s. Try again." % yes_or_no)

# Utilizing a Stack to upload the restaurant list of lists in one go so that we don't
# have to iterate over it more than once which keeps us at O(N) asyptotic notation.
# The Stack module was not available in the project directory, so I had to create it
# from the lesson. I also added a "fill" class var that initializes the Stack from a list arg.
restack = Stack(fill=restaurant_data)
food_type_hashmap = HashMap(30)
restaurant_hashmap = HashMap(30)

# Unpack the stack
types.sort()
while not restack.is_empty():
  rest = restack.pop()
  # If the food_type hasn't been hashmap'd for a single char to a LinkedList, assign it, else insert.  
  if not food_type_hashmap.retrieve(rest[0][0]):
    ll_char = LinkedList(rest[0])
    food_type_hashmap.assign(rest[0][0], ll_char)
  else:
    fth_list = food_type_hashmap.retrieve(rest[0][0])
    if not fth_list.exists(rest[0]):
      fth_list.insert_beginning(rest[0])
  # If the food_type hasn't been hashmap'd for a two char to a LinkedList, assign it.
  # Future work: If we need to go beyond 2 chars, we'll insert here, and then grab a third.
  if not food_type_hashmap.retrieve(rest[0][:2]):  
    ll_char2 = LinkedList(rest[0])
    food_type_hashmap.assign(rest[0][:2], ll_char2)
      
  # Create the food type hashmap of LinkedListed restaurants. 
  if not restaurant_hashmap.retrieve(rest[0]):
    ll_rest = LinkedList(rest)
    restaurant_hashmap.assign(rest[0], ll_rest)
  else:
    resth_list = restaurant_hashmap.retrieve(rest[0])
    if not resth_list.exists(rest[1]):
      resth_list.insert_beginning(rest)

# User Interaction
# 1. Ask the user to type a few characters of the type of food they would like to eat, or 'q' to quit.
# 2. If the user types q, break. (no food type exists beginning with the letter q that I'm aware of)
# 3. If the user types more than 1 character, and the first two signifies a single food type, ask if they
#    want to see the list of restaurants. If so, pretty print them out. Grabs most permutations.
# 4. Else, get the single char list. Check to see if the list size is 1. If so, prety print the restaurant
#    LinkedList, else return the food type LinkedList choices that are possible from that one char.
# 5. If the user types in an invalid string, let them know the search did not return anything.
while True:
  char_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here, or type 'q' to quit.\n")).lower()
  #Search for user_input in food types data structure here
  if char_input == 'q':
    print("\nHave a great day, and come back again.\n")
    break
  # Data unique out-to 2 characters. Depending on future added types, might go to 3 or 4.  
  elif len(char_input) > 1 and food_type_hashmap.retrieve(char_input[:2]):
    print("Did we get here with char2 %s" % char_input[:2])
    ulist = food_type_hashmap.retrieve(char_input[:2])
    pretty_rest_print(ulist.get_head_node().value, restaurant_hashmap)
  elif food_type_hashmap.retrieve(char_input[0]):
    ulist = food_type_hashmap.retrieve(char_input[0])
    if ulist.get_size() > 1:
      print("With those beginning letters, your choices are %s.\n"
        % ulist.stringify_list())
      print("Try typing a few more characters, or the food type for a list of available restaurants.\n")
    else:  
      pretty_rest_print(ulist.get_head_node().value, restaurant_hashmap)                   
  else:
    print("\nA search for a food type using your input: %s, does not exist. Try again.\n" % (char_input))