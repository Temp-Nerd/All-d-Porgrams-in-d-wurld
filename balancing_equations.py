import math
def balance(equation) :

    '''equation format: 'H2+O2=H2O' '''

    eqn=equation.split('=')
    
    lft=eqn[0].split('+')
    rt=eqn[1].split('+')
    lft_elmnts=rt_elmnts={}
    coeff_list=[]

    '''
    spliting the lists
    '''
    for g in lft :
        i=g.strip().upper()
        for k in range(len(i)) :
            coeff_list.append(1)
            coeff=1
            '''
            if required this can be used when given partially balanced equation
            '''
            if i[k].isdigit() :
                  n,coeff=0,0
                  try :
                      while i[k+n].isdigit() :
                            coeff=10*num+i[k+1]
                            n+=1
                  except IndexError :
                        cooeff=1
            if i[k].isalpha():
                elmnt=i[k]
                n,num=1,0
                try :
                      while i[k+n].isdigit() :
                            num=10*num+int(i[k+1])
                            n+=1
                except IndexError :
                      num==1
            lft_elmnts[elmnt]=coeff*num
    '''same thing for the right list'''
    for g in rt :
        g=i.strip().upper()
        for k in range(len(i)) :
            coeff=1
            '''same here'''
            if i[k].isdigit() :
                  n,coeff=0,0
                  try :
                      while i[k+n].isdigit() :
                            coeff=10*num+int(i[k+1])
                            n+=1
                  except :
                        coeff=1
            if i[k].isalpha():
                elmnt=i[k]
                n,num=1,0
                try :
                      while i[k+n].isdigit() :
                            num=10*num+int(i[k+1])
                            n+=1
                except IndexError:
                      num==1
            rt_elmnts[elmnt]=coeff*num

    while lft_elmnts != rt_elmnts :
        # lft_nos=lft_elmnts.values()
        # rt_nos=rt_elmnts.values()
        '''idk what is the problem here'''
        '''creating list of keys and values coz idk why the shit abv didnt work'''
        lft_nos=lft_val=[]
        for i in lft_elmnts :
            lft_nos.append(i[lft_elmnts])
            lft_val.append(i)


        '''checking for lowest left number'''
        low_no=lft_nos[0]
        for i in lft_nos :
            if i < low_no :
                low_no_lft=i
        low_elmnt_lft=lft_val[lft_nos.index(low_no_lft)]

        '''(for right)creating list of keys and values coz idk why the shit abv didnt work'''
        rt_nos=rt_val=[]
        for i in rt_elmnts :
            rt_nos.append(i[rt_elmnts])
            rt_val.append(i)
        low_no=rt_nos[0]

        '''checking for lowest right number'''
        for i in rt_nos :
            if i < low_no :
                low_no_rt=i
        low_elmnt_rt=rt_val[rt_nos.index(low_no_rt)]

        if low_no_lft != low_no_rt :
            gcd=math.gcd(low_elmnt_rt,low_elmnt_lft)
            lcm=low_elmnt_lft*low_elmnt_rt/gcd
            ###Need change
            lft_elmnts[low_elmnt_lft],rt_elemnts[low_elmnt_rt]=lcm,lcm
        print(lft_elmnts,rt_elemnts)
        """printing the final result"""
    for i in lft_elmnts :
        ###Need Change
        print(i,lft_elmnts[i])


equation=input('Enter your equation :')
balance(equation)
