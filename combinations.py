def factorial (a) :
      factorial=1
      for i in range (a,1,-1) :
            factorial*=i
      return factorial
def combination (n,r) :
      n_fact=factorial(n)
      r_fact=factorial(r)
      n_r_fact=factorial(n-r)
      return(n_fact//(r_fact*n_r_fact))
x=int(input('Enter n :'))
y=int(input('Enter r :'))
print(f'The total no. of combinations of n taken r at a time is :{combination(x,y)}')
