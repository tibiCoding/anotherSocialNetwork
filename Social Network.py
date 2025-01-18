friends_network = { "Alice": {"Bob", "Charlie"}, "Bob": {"Alice", "David"}, "Charlie": {"Alice", "Eve"}, "David": {"Bob"}, "Eve": {"Charlie"} }

def main():
  choice = int(input("\n======Main Program======\n[1]Add a user\n[2]Find common friends\n[3]Expand network\n[4]Exit\nMake a selection: "))
  if choice == 1:
    add_user()
  elif choice == 2:
    common_friends()
  elif choice == 3:
    expand()
  elif choice == 4:
    print("See you later!")
  else:
    print("Wrong input, try again!")
    main()    

# Issue: if user already exists, friends will be added to the existing person with the same name
def add_user():
  user = input("Name of the user: ").strip()
  if user:
    friends = set(input("Name of the friends to add: (seperated by comma's)").split(","))
    if friends:
      friends_network.update({user:friends})
    else:
      print("Incorrect input, try again")
      add_user() 
  else: 
    print("Incorrect input, try again")
    add_user()  
  print(f"{user} and their friends have been added to the social network.")
  main()

def common_friends():
  print(friends_network)
  person1 = input("Which person would you like to compare? ")
  if person1:
    person2 = input(f"With whom would you like to compare {person1}? ")
    if person2:
      friends1 = friends_network.get(person1)
      friends2 = friends_network.get(person2)
      commonFriends = friends1 & friends2
    else:
      print("Incorrect input, try again")
      common_friends() 
  else:
    print("Incorrect input, try again")
    common_friends() 
  print(f"The common friend(s) of {person1} and {person2} is/are {commonFriends}")
  main()

def expand():
  person1 = input("Who wants to add a friend? ")
  if person1:
    person2 = input(f"Whose friends does {person1} want to add? ")
    if person2:
      friends1 = friends_network.get(person1)
      friends2 = friends_network.get(person2)
      while person1 in friends2:
        friends2 -= {person1}
        continue
      newFriends = friends2 - friends1
      if newFriends:
        friends_network.update({person1:newFriends})
        print(f"{person1} added the friends {newFriends} of {person2} to his network")
      else: 
        print(f"No new friends were added to the {person1}'s network")
  main()

main()
