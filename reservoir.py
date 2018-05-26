import csv
import math
import numpy as np
import random
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
x=[]
y=[]
freq1=[20,210,30,0,-1,1,1]
freq2=[20,0,1.9,25,58,7]
freq3=[1,2,3,4,5]
freq4=[600,1000,3,4]
cost1=[3000,5000,6000,2500,1500,2000,1000,1500]
cost2=[3000,1500,4000,7000,5000,4600]
cost3=[1700,2500,1300,3400,1500]
cost4=[7100,4200,3700,4000]
lis1=[]
lis2=[]
car={}
head=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','CAR_ID','ATTRIBUTE']
cl=['Car1','Car2','Car3','Car4','Car5','Car6','Car7','Car8','Car9','Car10','Car11','Car12','Car13','Car14','Car15']


def moment_generating(x,j,s,header):		
	w=[]
	m=np.mean(x)
	lis1.append(int(m))
	if(j==120*s):
		car[cl[s-1]]=lis1
		lis1.append(cl[s-1])
		lis1.append(header)
		with open('mean.csv','a') as f:
			w=csv.writer(f,delimiter=',',lineterminator='\n')
			w.writerow(lis1)
		f.close()
		#print(cl[s-1]," ",header," ",car[cl[s-1]],"\n")
		s=s+1
		lis1.clear()
	return s





def sampling(items,k):
	sample=items[0:k]
	for i in range(k,len(items)):
		j=random.randrange(1,i+1)
		if j<=k:
			sample.append(items[i])
	return sample	



def future(dataset2,freq2):
	df=pd.read_csv(dataset2)
	df.index=np.arange(1,len(df)+1)
	headers=df.columns
	n=len(headers)-1
	i=3 	#index for the headers
	z=[]	#for each header
	smpl=[] #used for the sampling 
	me=[]   #for calculating mean values are stored
	mns=0
	with open('mean.csv','a') as f: #for storing the headers 
		w=csv.writer(f,delimiter=',',lineterminator='\n')
		w.writerow(head)
	f.close()

	while(i<=n):  #processing each header
		mn=df[headers[i]] #header i of column is stored
		j=1 	 #index used for the mn(mn is a header)
		k=1 	 #count for the trips
		r=1 	#is used for the buffer
		s=1 	 #it is used in the sampling index
		index=[] #used as the false positive index
		fp=0 	 #used as the false positive count
		tp=0 	 #used as the true positive count
		count=0 #count for the mean
		#lis1.clear()
		z.append(0)
		l=len(mn) #length of the header i
		print(headers[i]," ",j," ",l,"\n")
		while(j<=l):
			z.append(mn[j])
			if(j==12*k):
				smpl=sampling(z,4)
				s=moment_generating(smpl,j,s,headers[i])
				z.clear()
				smpl.clear()
				k=k+1
			j=j+1
		i=i+1
	




path='dataset2.csv'
print('information for 0-3 years\n')
#immediate(path)
future(path,freq2)