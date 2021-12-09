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

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            
        else:
            n = (3 * n + 1)
            print(n)

collatz(12)