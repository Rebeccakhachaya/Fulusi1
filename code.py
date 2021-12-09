# Number1

def str_arr(arr):
    left=arr[0]
    right=arr[1]
    for i in left:
        if i in left and i in right:
            print(i, end=' ') 
        else:
            pass
            # print(False)
str_arr(["1,3,4,7,13","1,2,4,13,15"])
output=1,4,13


# Number2

def dif (n):
    add=0
    count=0
    square=0
    for i in range(n):
        if count <=10:
            add +=i
            square += i*i
            count +=1
    dif=add*add -square
    print(dif)  
dif(100)    


  

# Number 3

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
            
        else:
            number = (3 * number + 1)
            print(number)

collatz(12)