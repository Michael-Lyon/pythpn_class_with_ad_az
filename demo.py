

games = [
    
        "COD" , "PUBG", "FORTNITE", "SUBWAY-SURF", "CANDY CRUSH",
        "NEED FOR SPEED", "PUBG",
        "COD COLD WAR", "ROBLOX",
        "BLUR", "DEATHRACE"
    ]


consoles = [
    "PS2", "PS3", "PS4",
]

#  How to select itmes from a list
#  0 1 2 3 4
#  -1 -2 -3 -4 -5
game_cod = games[0]
game_pubg = games[1]
game_candy_crush = games[-1]

# [start : stop] 1 3 -> 1 2
game_range = games[1:3]
game_range2 = games[1: ] # selects all from the starting pont

games_reversed = games[::-1]

# select by negative values
game_range_negative = games[-3 : -1]


# remove items from a list
num_item = len(games)
# print(num_item)

ind = int(input("Enter index of item to remove: "))

#  using pop with an index position
removed_item = games.pop(ind)
# print(removed_item)

#  using pop without an index position
removed_item2 = games.pop()
# print(removed_item2)

games.remove("COD")
# print(games)




