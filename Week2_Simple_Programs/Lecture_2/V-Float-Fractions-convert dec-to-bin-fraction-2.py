
#CONVERT DECIMAL INTO A BINARY FRACTION
 
x = float(input('Enter a decimal between 0 and 1: '))

p = 0
#By exhaustive search (guess and check).
while ((2 ** p) * x) % 1 != 0: # ((2 ** 3) * 0.375)%1
    print('Remainder = ' + str((2 ** p)* x - int((2 ** p) * x)))
    print((2 ** p) * x)
    p += 1
   
num = int(x * (2 ** p)) #A number big enough to convert into a whole number
print(num)
result =''
#convert decimal integer into binary representation
if num == 0:
    result = '0'
    print(result)
    print(num)
while num > 0:
    result = str(num % 2) + result
    num = num // 2
    print(result)
    print(num)
#how many "0" he should add before the variable called "result",
# and then in the print statement used index to insert the binary point.
for i in range(p-len(result)):
    result = '0' + result
    print(result)
    print(p-len(result))
result = result[0:-p] + '.' + result[-p:]
print(p-len(result))
print(result[0:-p])
print(result[-p:])
print('The binary representation of the decimal ' + str(x) +' is ' + str(result))

#Now i can take any floating point number, and convert into something that 
#can be represent inside of the machine in binary form 