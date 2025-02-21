number = int(input("please give the number.\n"))
def calculation(number) :
    for i in range(number+1):
            if not i==0 and number%i==0:
                print(i)
answer = calculation(number)
