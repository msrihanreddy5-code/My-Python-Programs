n=int(input("Enter a number: "))
count=0
arm=0
num=n
while num>0:
    rem = num % 10
    arm  = arm + rem**3
    num = num // 10
if arm ==n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number") 
