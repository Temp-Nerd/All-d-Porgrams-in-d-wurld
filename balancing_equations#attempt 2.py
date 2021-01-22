def Makelist(equation):
	global lft_list, rt_list, lft_elmnts, rt_elmnts,coeff
	eqn=equation.split('=')
	lft_list=eqn[0].split('+')
	rt_list=eqn[1].split('+')
	lft_elmnts=rt_elmnts={}
	coeff=[]

eqn=input('Enter equation:')
Makelist(eqn)
print(eqn,lft_list, rt_list, lft_elmnts, rt_elmnts,coeff)

def Getlist(list,get_list) :
	global lft_list, rt_list, lft_elmnts, rt_elmnts, coeff
	for g in list :
		i=g.strip().upper()
		for k in len(i) :
			coeff.append(1)
			if i[k].isdigit() :
				n,coeff=0,0
				while i[k+n].isdigit() :
					coeff=10*num+i[k+1]
					n+=1
			if i[k].isalpha():
				elmnt=i[k]
				n,num=1,0
				try :
					while i[k+n].isdigit() :
						num=10*num+i[k+1]
						n+=1
				except IndexError :
					num==1
			get_list[elmnt]=coeff*num

print(eqn,lft_list, rt_list, lft_elmnts, rt_elmnts,coeff)