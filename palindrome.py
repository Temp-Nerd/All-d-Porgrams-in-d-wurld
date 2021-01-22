def reverse(a):
      rev=''
      for i in range (len(a)-1,-1,-1) :
            rev+=a[i]
      return(rev)
a=(input('enter :'))
b=reverse(a)
if b==a :
      fill=''
else :
      fill='not '
print(f'The string is {fill}a palindrome')
