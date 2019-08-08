
# FLOATS & FRACTIONS
# HOW WE COULD CONVERT A DECIMAL INT INTO A BINARY REPRESENTATIONS
num = 3

if num < 0:
    isNeg = True     
    num = abs(num)
else:
    isNeg = False
result = '' 
if num == 0:
    result = '0'
    print(result)
while num > 0: 
    result = str(num % 2) + result
    num = num//2
    print(num)
    print(result)
if isNeg:
    result = '-' + result
print(result)




