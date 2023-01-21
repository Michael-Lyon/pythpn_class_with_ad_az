consoles = [
    "PS2", "PS3", "PS4",
]

# ADD ITEMS TO A LIST using append

print(f"Before adding items to the list: {consoles}")
new_console1 = input("Enter a new console: ")
consoles.append(new_console1)
print(f"After adding items to the list: {consoles}")

consoles.append("XBOX1")
print(consoles)


# ADD ITEMS TO A LIST using INSERT

value = input("Enter a new console: ")
position = int(input("Enter the position for this values: "))

if position > 0 and position <= len(consoles):
    position -= 1

    consoles.insert(position, value)
    print(consoles)
else:
    print("You have entered a value too high.\nIt would be added to the end of the list\nEnter yes to continue.")
    ans = input(">>> ")
    print(ans.lower())
    if ans.lower() == "yes":
        consoles.append(value)
        print(consoles)
    else:
        print("Bye.")