import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
party='INC BJP  Indipendent OTHERS'.split()
state=['Madhya Pradesh','Rajastan','Chhattisgarh','Telangana','Mizoram']
seats=[[144,15,4,3],[99,74,3,14],[68,15,9,7],[88,19,1,11],[26,5,1,8]]
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
#patches,texts=spobj.pie(sales,colors=colrs,shadow=True)
patches,texts=spobj.pie(sales,colors=colrs,shadow=True,startangle=45)
print patches
print texts
plt.legend(patches,fruits,loc='best')
plt.show()
