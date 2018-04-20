# Small adventure game. Had to fix a few bugs and add code as part of the challenge.
# The goal is for the user to navigate the map and try to visit all of the locations.

locations = {0: {"desc": "[Alarm Clock rings] It was all a dream...",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at fork in the road, go explore!",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill. What is that all the way over there!?...",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a small, dark, quiet shack...",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a raging stream...",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the lush forest, watch your step...",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }
 
# These values are used to reference the locations dictionary in the event that the user spells out the direction fully
vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
 
loc = 1
while True:
    
    # Tells the user their current location
    availableExits = ", ".join(locations[loc]["exits"].keys()) + "...Which direction do you want to go?: "
    print(locations[loc]["desc"])
 
    if loc == 0:    # quit option
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])
 
    # Prompts the user to enter a direction
    direction = input("Available exits are " + availableExits).upper()
    print()
 
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split() # splits every 
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break
 
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")