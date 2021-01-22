def binsearch (L) :
      print(L)
      data=int(input('Enter the value to be searched'))
      beg=0
      end=len(L)-1
      mid=(beg+end)//2
      while beg != end :
            print('X',beg,mid,end)
            if data != L[mid] :
                  if data > L[mid] :
                        beg=mid+1
                        mid=(beg+end)//2
                        print('A',beg,mid,end)
                  else :
                        end=mid-1
                        mid=(beg+end)//2
                        print('B',beg,mid,end)
            else :
                  beg=end
                  print('C',beg,mid,end)
      print('Y',beg,mid,end)
      return mid

l=[5,9,12,18,20,24]
print(binsearch(l))
