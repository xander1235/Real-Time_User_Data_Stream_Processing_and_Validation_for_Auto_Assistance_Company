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
freq2max=[]
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

	

def send(acc,count,index,half,header):
	if(count >=half):
		s="there may be a problem in a car "+header+" that occurs in future having accuracy of " + str(acc)
	else:
		s="there is no problem in future"
	print(s+"\n")



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
	with open('mean.csv','a') as f, open('std_dev.csv','a') as e: #for storing the headers 
		w=csv.writer(f,delimiter=',',lineterminator='\n')
		x=csv.writer(e,delimiter=',',lineterminator='\n')
		w.writerow(head)
		x.writerow(head)
	f.close()
	e.close()

	while(i<=n): #processing each header
		mn=df[headers[i]] #header i of column is stored
		j=1 	 #index used for the mn(mn is a header)
		k=1 	 #count for the trips
		r=1 	#is used for the buffer
		s=1 
		lk=1	 #it is used in the sampling index
		index=[] #used as the false positive index
		fp=0 	 #used as the false positive count
		tp=0 	 #used as the true positive count
		count=0 #count for the mean
		#lis1.clear()
		ind_num=[]
		inde=[]
		z.append(0)
		l=len(mn) #length of the header i
		print(headers[i]," ",j," ",l,"\n")
		while(j<=l):
			z.append([])
			z[j].append(mn[j])
			z[j].append(j)
			if(j==3600*k):
				#print("aa")
				#smpl=sampling(z,4)
				while(r<=3500*k):
					t=r
					while(t<r+100):
						me.append(z[t][0])
						inde.append(z[t][1])
						#print(me,k,t,r)
						t=t+1
						
					mea=np.mean(me)
					
					
					if(r==1):
						mx=mea
					#sd=np.std(me)
					if(mea<freq2[i-3]):
						count=count+1
					#print()
					lk=1
					c=1
					c1=1
					while(lk<100):
						if(me[lk]<=freq2[i-3] and mea>freq2[i-3]):
							if(c==1):
								fp= fp + 1
								index.append(inde[lk])
							c=c+1							
						else:
							if(c1==1):
								tp = tp + 1
							c1=c1+1
						lk = lk + 1
						#print(lk)
						#print(fp,tp)
			
					me.clear()
					inde.clear()
					r=r+1
				acc=100*(tp/(fp+tp))
				half=50
				send(acc,count,index,half,headers[i])
				
				
				#print(acc)
				fp=0
				tp=0

				trace = []
				for ind in index:
					trace.append(z[ind][0])
				#s=moment_generating(smpl,j,s,headers[i])
				#z.clear()
				print(index,"\n",trace)
				graph1(index,trace,headers[i])
				index.clear()
				trace.clear()
				smpl.clear()
				k=k+1
			j=j+1

		i=i+1
		z.clear()
	

def graph1(index,trace,header1):
	style.use('ggplot')
	plt.bar(index,trace,width=0.5,color="red")
	if(np.mean(trace)<5):
		plt.ylim(0,5)
	else:
		plt.ylim(0,60)
	plt.title('FALSE_POSITIVE')
	plt.ylabel(header1+"_VALUES")
	plt.xlabel('TIME')
	plt.xlim(0,3800)
	plt.show()




path='datasetnew2.csv'
print('information for 0-3 years\n')
#immediate(path)
future(path,freq2)



