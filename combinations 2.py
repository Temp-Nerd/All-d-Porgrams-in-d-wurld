def combination (n,r) :
      def factorial (a) :
            factorial=1
            for i in range (a,1,-1) :
                  factorial*=i
            return factorial
      return(factorial(n)//(factorial(r)*factorial(n-r)))
x=int(input('Enter n :'))
y=int(input('Enter r :'))
print(f'The total no. of combinations of n taken r at a time is :{combination(x,y)}')
