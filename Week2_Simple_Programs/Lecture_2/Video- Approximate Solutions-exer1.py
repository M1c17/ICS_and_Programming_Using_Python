'''
#step colud be any small number 
#if too small, takes along time to find the solution
#if too large, might skip over answer without getting close enough
#in general will take x/step times through code to find the solution


#when i change increment = 0.01 by hundreds
# its off in infinite loop is because im checking only to see if i get 
#to place where its close enough. i've actually 
#gone right past the cube root
# i need to make sure that my guess is still small enough
'''

cube = float(input("Insert a number: "))
#set up some initial values 
epsilon = 0.01 # How close I want to get to the answer (my constant)
guess = 0.0    # Where i'm going to start 
increment = 0.0001  # the size in wich I'm going to increase my guess as move along.
num_guesses = 0 # How many times do i go through the loop as i do this 

while abs(guess**3 - cube) >= epsilon:
    if cube > 0:
        guess += increment
        num_guesses += 1
    else:
        guess -= increment
        num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)