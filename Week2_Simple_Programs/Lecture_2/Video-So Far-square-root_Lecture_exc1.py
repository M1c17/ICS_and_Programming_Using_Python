#square root

ans = 0
neg_flag = False
x = int(input("Enter an Iteger:"))

if x < 0:
    neg_flag = True
    if neg_flag:
        print("Just checking ... did you mean ", -x ,"?")
        neg_ans = input("Y/N: ")
        if neg_ans == "Y":
            x =- x              # change the negative value for positive 
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of: ", x," is ", ans)
else:
    print(x, " is not a perefect square root")