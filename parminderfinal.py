# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 18:18:47 2021

@author: hp
"""

import parminder_covid
import parminder_heart
import parminder_stroke
import WSN
import random
import pandas as pd


iotdata = pd.read_csv('./vf.csv')

#func(array = ([[0.],[0.],[1.]]))
#parminder_covid.covid_func(array)
#parminder_stroke.stroke_func(array)
#parminder_mental_illness.mental_illness_func(array)


#parminder_covid.covid_func(array)
#print(array[0])
print("Welcome to QMS... press 1 for new data and any other key to reshuffle only")
new1 = input()

result=[]

#result=WSN.returner()
#print(result)
#new1=input()

print("Reshuffling ...")
print()
print()
print("Order of reshuffling:")
print("Covid-19")
print("Stroke")
print("Heart-patient")
print()
print()

if new1 == '1':
    print("Initializing sensors...")
    result=WSN.sensors()
    #print(random.random()*100)
    x=round(random.random()*100)
    print('Packet delivery ratio:',iotdata.loc[0]['Packet_Delivery_Ratio'])
    print('Delay:',iotdata.loc[1]['Delay'])
    #print(result)
    if result[0]==3:# or result[0]==2 or result[0]==1:
        print("Data of covid-19 patient detected::")
        array = ([[random.choice([0.0,1.0])],[random.choice([0.0,1.0])],[random.choice([0.0,1.0])]])
        df1,edf1=parminder_covid.covid_func(array,new1)
        array=[]
        new5='2'
        df2,edf2=parminder_stroke.stroke_func(array,new5)
        df3,edf3=parminder_heart.heart_func(array,new5)

    if result[1]==3:# or result[1]==2 or result[1]==1:
        print("Data of stroke patient detected::")
        array2=[]
        new2='2'
        df1,edf1=parminder_covid.covid_func(array2,new2)
        array = ([[random.choice([4.0,5.0])],[random.choice([4.0,5.0])],[random.choice([4.0,5.0])]]) 
        new1='1'
        df2,edf2=parminder_stroke.stroke_func(array,new1)
        array3=[]
        new3='3'
        df3,edf3=parminder_heart.heart_func(array3,new3)
        #print('Final queue')
        #print(df1.iloc[0]['id'])
        #print(df2.iloc[0]['id'])
        #print(df3.iloc[0]['id'])
    
    if result[2]==3:# or result[2]==2 or result[2]==1:
        print("Data of heart patient detected::")
        array4=[]
        new4='4'
        df1,edf1=parminder_covid.covid_func(array4,new4)
        df2,edf2=parminder_stroke.stroke_func(array4,new4)
        array = ([[random.choice([2.0,3.0])],[random.choice([2.0,3.0])],[random.choice([2.0,3.0])]])
        new1='1'
        df3,edf3=parminder_heart.heart_func(array,new1)
else:
    array = []
    df1,edf1=parminder_covid.covid_func(array,new1)
    df2,edf2=parminder_stroke.stroke_func(array,new1)
    df3,edf3=parminder_heart.heart_func(array,new1)
print()
print('Original queue')    
for i in range(edf1.shape[0]):
    if random.random()>0.5:
        print(edf1.iloc[i]['id'])
        print(edf2.iloc[i]['id'])
        print(edf3.iloc[i]['id'])
    else:
        print(edf3.iloc[i]['id'])
        print(edf2.iloc[i]['id'])
        print(edf1.iloc[i]['id'])
print()
print('Final queue')    
for i in range(df1.shape[0]):
        print(df1.iloc[i]['id'])
for i in range(df2.shape[0]):
        print(df2.iloc[i]['id'])
for i in range(df3.shape[0]):
        print(df3.iloc[i]['id'])
'''array = ([[0.],[0.],[1.]])
if array[0]==[0.0] or array[0]==[1.0]:
    parminder_covid.covid_func(array,new1)

array = ([[4.],[5.],[4.]])    
if array[0]==[4.0] or array[0]==[5.0]:
    parminder_stroke.stroke_func(array,new1)

array = ([[2.],[3.],[2.]])    
if array[0]==[2.0] or array[0]==[3.0]:
    parminder_mental_illness.mental_illness_func(array,new1)'''


#print("x = ",x)
#print("fx = ",fx)
#y = parminder_mental_illness.mental_illness_func()
#func(array = ([[2.],[2.],[3.]]))
#z = parminder_stroke.stroke_func()
#func(array = ([[4.],[4.],[5.]]))
#print(x,y,z)
#f

    