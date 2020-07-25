import sys
# Get the player's name with input and store it in the name variable
name = input('What\'s your name?: ')
# Greet the player using string concatenation
print('Hi '+ name + '!')
# Print out some steps for player to choose from, for example:
# Next steps: 1) Look around 2) Chop down tree 3) Jump
todos = ['look around', 'chop tree', 'jump' ]
print('There is a few things you can do: ')
print(todos[0])
print(todos[1])
print(todos[2])
todo = input('Which would you like to do? ')

# Use an if statement to decide the next steps to print. For example, if they picked 1:
# You've spotted a suit of armor! 1) Put it on 2) Ignore it
if todo == 'jump':
    print('Well ' + name +', go ' + todo + ' to your hearts content!')
elif todo == 'chop tree':
    print('Go ' + todo + '\'s ' + name + '! ')
elif todo == 'look around':
    print(todo +' as much as you want ' + name + '! ')
else:
    print('You can\'t do that ' + name + '! ')
sys.exit
# Do this inside a loop until the user is done with the game