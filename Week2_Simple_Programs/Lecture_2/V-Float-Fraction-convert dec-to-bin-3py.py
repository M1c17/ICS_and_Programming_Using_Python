'''
Write code to convert any number to its binary form 
and print out the summary
'''
num = 19

str_num = str(num)

is_decimal = '.' in str_num

is_negative = num < 0

if is_negative:

    num = abs(num)
    
if is_decimal:

    decimal_num = num - int(num)
    decimal_summary = '.'
    while True:
        decimal_num = decimal_num * 2
        str_num = str(decimal_num)
        decimal_summary = decimal_summary + str_num[0]
        if decimal_num > 1:
            decimal_num = decimal_num - 1
        if decimal_num == 1:
            break   # Break the moment number becomes whole number 1
        if len(decimal_summary) == 12:  # Break after max of 11 decimal digits. 
            break
num = int(num)

summary = ''

if num == 0:

    summary = '0'
while num > 0:

    summary = str(num%2) + summary
    num = num//2
if is_decimal:

    summary = summary + decimal_summary
if is_negative:

    summary = '-' + summary
print(summary)