#Make 3 commits with descriptive messages

import random

#places to visit
destinations =  ['Orlando', 'San Francisco', 'Las Vegas', 'Seattle', 'Minneapolis', 'New York City'] 

#randomly select desitination
def select_destination (destination):
    return destination

place_selected = select_destination (random.choice(destinations))

print ("Welcome to the Day Trip Generator. We hope to make your travel planning as easy as possible. Let's start with a location. How about " + place_selected + "? Does that sound like a good idea? type yes or no"  )
place_answer = input()

while place_answer == "no":
    place_selected = select_destination (random.choice(destinations))
    print("We want to make sure you are satisfied. Let's try another place.")
    print("How about " + place_selected + " ?")
    place_answer = input()

    if place_answer != "yes" and place_answer != "no":
        print("You must enter yes or no")
        place_answer = input()
    
    else:
        destination = place_selected

#places to eat
restaurants = ['Carrabas', 'On The Border', 'Texas Roadhouse', 'Joes Crab Shack', 'PF Changs'] 

#randomly select restaurant
def select_restaurant (restaurant):
    return restaurant

restaurant_selected = select_restaurant (random.choice(restaurants))

if place_answer == "yes":
    print("Now that you have a destination, you can pick a restaurant. How does " + restaurant_selected + " sound?")
    rest_answer = input("Please type yes or no." )

while rest_answer == "no":
    restaurant_selected = select_restaurant (random.choice(restaurants))
    print("Not what you're in the mood for. Let's try something else.")
    print("How about " + restaurant_selected + " ?")
    rest_answer = input()

    if rest_answer != "yes" and rest_answer != "no":
        print("You must enter yes or no")
        rest_answer = input()
    
    else:
        restaurant = restaurant_selected

#methods of transportation
trans_methods = ['Boat', 'Train', 'Car', 'Plane'] 

#randomly select transportation
def select_transportation (transportation):
    return transportation

transportation_selected = select_transportation (random.choice(trans_methods))

if rest_answer == "yes":
    print("How do you prefer to get to your destination? Would a " + transportation_selected + " work?")
    trans_answer = input("Please type yes or no." )

while trans_answer == "no":
    transportation_selected = select_restaurant (random.choice(trans_methods))
    print("Not what you had in mind?")
    print("How about a " + transportation_selected + " ?")
    trans_answer = input()

    if trans_answer != "yes" and trans_answer != "no":
        print("You must enter yes or no")
        trans_answer = input()
    
    else:
        transportation = transportation_selected

#forms of entertainment
ent_forms = ['Dance Club', 'Comedy Bar', 'Playhouse Theater', 'Cinema', 'Escape Room'] 

#randomly select entertainment
def select_entertainment (entertainment):
    return entertainment

entertainment_selected = select_entertainment (random.choice(ent_forms))
print(entertainment_selected)

if trans_answer == "yes":
    print("What type of entertainment are you looking for? Would a " + entertainment_selected + " be on your agenda?")
    ent_answer = input("Please type yes or no." )

while ent_answer == "no":
    entertainment_selected = select_entertainment (random.choice(ent_forms))
    print("Not what you were thinking?")
    print("How about a " + entertainment_selected + " instead?")
    ent_answer = input()

    if ent_answer != "yes" and ent_answer != "no":
        print("You must enter yes or no")
        ent_answer = input()
    
    else:
        entertainment = entertainment_selected

print(place_selectedn, restaurant_selected, transportation_selected, entertainment_selected)

#if I don't like it I can select again

#review that the day trip is complete

#display completed trip

#functions single responsibility





# print(trans_methods)

# print(ent_forms)

