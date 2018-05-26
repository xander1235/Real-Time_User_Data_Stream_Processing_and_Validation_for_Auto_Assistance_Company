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

def immediate(dataset):
	dataset = csv.reader(open(dataset, newline=''), delimiter= " ", quotechar="|")
	i=0
	prob=' '
	s=0
	#wq=0
	k=0
	tot=0
	row=['0','0','0','0','0','0','0','0','0','0','0']
	prev=[' ',' ',' ',' ',' ',' ',' ']
	#inp=input("attribute")
	for row in dataset:

		s=s+1
		if(i<=0):
			header=row[0].split(',')
			header.append(' ')
			header.append(' ')
			i=i+1
			s=0
		else:
			row=row[0].split(',')
			now=[row[1],row[1],row[1],row[1],row[1],row[1],row[1]]

						#0 to 3 years
			#engine oil checking
			if(header[3]=='ENGINE_OIL' and int(row[3])<=freq1[0] and (now[0]==' ' or now[0]!=prev[0])):
				prob= header[3]+', '
				tot=tot+cost1[0]
				prev[0]=row[1]

			#coolant checking
			if(header[4]=='COOLANT' and int(row[4])>=freq1[1] and (now[1]==' ' or now[1]!=prev[1])):
				prob= prob + ' ' + header[4]
				tot=tot+cost1[1]
				prev[1]=row[1]

			if(header[5]=='BATTERY' ):
				if(k<120):
					x.append(int(row[5]))
					k=k+1

			#battery checking
			if(header[5]=='BATTERY' and int(row[5])<=freq1[2] and (now[2]==' ' or now[2]!=prev[2])):
				prob= prob + ' ' + header[5]
				tot=tot+cost1[2]
				prev[2]=row[1]

			#lights checking
			if(header[6]=='LIGHTS' and int(row[6])<=freq1[3] and (now[3]==' ' or now[3]!=prev[3])):
				prob=prob +' ' + header[6]
				tot=tot+cost1[3]
				prev[3]=row[1]

			#left wheel alignment checking
			if(header[7]=='WHEEL_ALIGNMENT' and int(row[7])<=freq1[4] and (now[4]==' ' or now[4]!=prev[4])):
				prob=prob +' left-' + header[7]
				tot=tot+cost1[4]
				prev[4]=row[1]

			#right wheel alignment checking
			if(header[7]=='WHEEL_ALIGNMENT' and int(row[7])>=freq1[5] and (now[4]==' ' or now[4]!=prev[4])):
				prob=prob + ' right-' + header[7]
				tot=tot+cost1[4]
				prev[4]=row[1]

			#cleaning
			if(header[8]=='CLEANING' and int(row[8])>=freq1[6] and (now[5]==' ' or now[5]!=prev[5])):
				prob=prob + ' '+ header[8]
				tot=tot+cost1[5]
				prev[5]=row[1]

			#oil filter checking
			if(header[9]=='OIL_FILTER' and row[9]=='yes' and (now[6]==' ' or now[6]!=prev[6])):
				prob=prob+ ' ' + header[9]
				tot=tot+cost1[6]
				prev[6]=row[1]

							#3 to 6 years
			#rad check
			if(header[3]=='RAD_CHECK' and int(row[3])<freq2[0] and (now[0]==' ' or now[0]!=prev[0])):
				prob=prob + ' '+ header[3]
				tot=tot+cost2[0]
				prev[0]=row[1]

			#wiper blades
			if(header[4]=='WIPER_BLADES' and int(row[4])<=freq2[1] and (now[1]==' ' or now[1]!=prev[1])):
				prob=prob + ' '+ header[4]
				tot=tot+cost2[1]
				prev[1]=row[1]

			#suspension
			if(header[5]=='SUSPENSION' and float(row[5])<=freq2[2] and (now[2]==' ' or now[2]!=prev[2])):
				prob=prob + ' '+ header[5]
				tot=tot+cost2[2]
				prev[2]=row[1]

			#steer gear box check
			if(header[6]=='STEER_GEAR_BOX' and int(row[6])<=freq2[3] and (now[3]==' ' or now[3]!=prev[3])):
				prob=prob + ' '+ header[6]
				tot=tot+cost2[3]
				prev[3]=row[1]

			#fuel filters
			if(header[7]=='FUEL_FILTER' and float(row[7])<=freq2[4] and (now[4]==' ' or now[4]!=prev[4])):
				prob=prob + ' '+ header[7]
				tot=tot+cost2[4]
				prev[4]=row[1]

			#brake pads check
			if(header[8]=='BRAKE_PADS' and int(row[8])<=freq2[5] and (now[5]==' ' or now[5]!=prev[5])):
				prob=prob + ' '+ header[8]
				tot=tot+cost2[5]
				prev[5]=row[1]

							#6 to 9 years
			#Ignition checking
			if(header[3]=='IGNITION_TIMING' and int(row[3])>=freq3[0] and (now[0]==' ' or now[0]!=prev[0])):
				prob=prob+ ' ' + header[3]
				tot=tot+cost3[0]
				prev[0]=row[1]

			#fuel ejectors checking
			if(header[4]=='FUEL_EJECTORS' and int(row[4])>=freq3[1] and (now[1]==' ' or now[1]!=prev[1])):
                                prob=prob+ ' ' + header[4]
                                tot=tot+cost3[1]
                                prev[1]=row[1]

			#power steering check
			if(header[5]=='POWER_STEERING_FUEL' and int(row[5])>=freq3[2] and (now[2]==' ' or now[2]!=prev[2])):
                                prob=prob+ ' ' + header[5]
                                tot=tot+cost3[2]
                                prev[2]=row[1]

			#pcv valve check
			if(header[6]=='PCV_VALVE' and int(row[6])>=freq3[3] and (now[3]==' ' or now[3]!=prev[3])):
                                prob=prob+ ' ' + header[6]
                                tot=tot+cost3[3]
                                prev[3]=row[1]

			#transmission checking
			if(header[7]=='TRANSMISSION' and int(row[7])>=freq3[4] and (now[4]==' ' or now[4]!=prev[4])):
                                prob=prob+ ' ' + header[7]
                                tot=tot+cost3[4]
                                prev[4]=row[1]

							#9 to 15 years

			#seat belts
			if(header[3]=='SEAT_BELTS' and int(row[3])>=freq4[1] and  int(row[3])<=freq4[0] and (now[0]==' ' or now[0]!=prev[0])):
                                prob=prob+ ' ' + header[3]
                                tot=tot+cost4[0]
                                prev[0]=row[1]

			#engine idle settings
			if(header[4]=='ENGINE_IDLE' and int(row[4])>=freq4[2] and (now[1]==' ' or now[1]!=prev[1])):
                                prob=prob+ ' ' + header[4]
                                tot=tot+cost4[1]
                                prev[1]=row[1]

			#clutch plate
			if(header[5]=='CLUTCH' and int(row[5])>=freq4[3] and (now[2]==' ' or now[2]!=prev[2])):
                                prob=prob+ ' ' + header[5]
                                tot=tot+cost4[2]
                                prev[2]=row[1]

			#water pump
			if(header[6]=='TRANSMISSION' and int(row[6])>=freq4[4] and (now[3]==' ' or now[3]!=prev[3])):
                                prob=prob+ ' ' + header[6]
                                tot=tot+cost4[3]
                                prev[3]=row[1]
		
			ro=row[1]
			if(s>=12):
				s=0
				if(tot>0):
					prob1=row[0] + ' has a problems in '+ prob+ ' in ' + ro + ' of total cost RS.' +str(tot)
					print(prob1)
					print('\n')
					ch=input()
					if(ch=='\0'):
						continue
					tot=0
					prob1=' '
				prob=' '
				if(k>=120):
					graph(x)
					k=12
					x.clear()










def graph(x):
	style.use('ggplot')
	i=0
	for p in range(0,140):
		y.append(p)
	for l in x:
		if(l>=30):
			plt.bar(y[i],l,width= 1.3,color="red")
		else:
			plt.bar(y[i],l,width=1.3,color="green")
		i=i+1

	plt.ylim(0,250)
	plt.xlim(0,150)
	plt.title('TRIPS')
	plt.xlabel('TIME')
	plt.ylabel('ATTRIBUTE')
	plt.show()
	y.clear()


path='dataset1.csv'
print('information for 0-3 years\n')
immediate(path)
#future(path,freq2)