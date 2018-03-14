n= int(input("enter a number")) 
if n>1:
        for i in range(2,n):
            
            if n%i==0:
                print("{} is not a prime number".format(n))
                n= int(input("enter a number"))
        else:
            print("{} is a prime number".format(n))
