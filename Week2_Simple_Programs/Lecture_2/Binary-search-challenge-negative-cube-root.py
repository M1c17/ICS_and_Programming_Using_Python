
cube = -125
epsilon = 0.01
high = cube
low = 0
guess = abs((high + low)/2)
num_guesses = 0


while abs(guess**3 -abs(cube)) >= epsilon and guess <= abs(cube):
    print('guess =', guess)
    if guess ** 3 > abs(cube):
        high = guess
    elif guess ** 3 < abs(cube):
        low = guess        
    num_guesses += 1
    guess = (high + low)/2

print('num_guesses =', num_guesses)
if abs(guess**3 -abs(cube)) >= epsilon :
    print('Failed on cube root of :', cube)

else:
    if cube < 0:
        guess = - guess
    print(guess, 'is close to the cube root of :', cube) 