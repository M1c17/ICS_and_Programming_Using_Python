#Bisection search - cube root 

cube = 27 #start off 
epsilon = 0.01 # how close i am 
guess = 0 # keep tracking how often do i actually run through the loop just to compare it
low = 1
high = x
ans = (high + low)/2.0 #initialize a guess 

while abs(ans**3 - cube) >= epsilon:
    print('low =' + str(low) +'high =' + str(high) +'ans=' + str(ans))
    if ans**3 < cube:
        low = ans 
    else:
        high = ans
    ans = (high  + low)/2.0
    guess +=1
print('guesses=' + str(guess))
print(str(ans) + 'is close cube root of:' + str(cube))