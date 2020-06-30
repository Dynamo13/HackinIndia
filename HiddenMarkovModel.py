# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

transition=np.array([[.70,.101,0.033,.013,.0086,.0080,.0090,.0084],
                   [.673,.303,.004,.004,.004,.004,.004,.004],
                   [.153,.401,.381,.035,0.012,0.012,.005,.001],
                   [.101,.099,.100,.334,.103,.094,.101,.068],
                   [.105,.051,.155,.100,.186,.201,.193,.010],
                   [.305,.140,.105,.050,.00,.148,.102,.150],
                   [.401,.251,.145,.040,.00,.014,.139,.010],
                   [.501,.153,.152,.024,.00,.022,.012,.136]])

start=np.array([12.5,12.5,12.5,12.5,12.5,12.5,12.5,12.5])

res=start@transition

print('Enter 1 for yes and 0 for no as an answer to the following symptoms')
a=int(input('Do you have Fever or an infrequent temperature rise?'))
b=int(input('Did you lose taste/skipped meal?'))
c=int(input('Do you have a dry cough?'))
d=int(input('Do you have fatigueness ?'))
e=int(input('Do you have shortness of breath?'))
f=int(input('Did you have a sore throat?'))
g=int(input('Did you have a head ache?'))
h=int(input('Did you experience body chills recently?'))

covid=[a*(.20),b*(.20),c*(.10),d*(.10),e*(.10),f*(.10),g*(.1),h*(.1)]

final=res*covid

if(final.sum()>10):
  print('High chances of covid ')
elif(final.sum()>6):
  print('Moderate chance (test required)')
else:
  print('Covid negative')1
