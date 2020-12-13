import csv
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
d = pd.read_csv("data.csv")
plt.style.use('seaborn-darkgrid')
 
# create a color palette
palette = plt.get_cmap('Set1')
print(d.head())
print(d['hospitalCases'])
i = 1
a = []
a = d['hospitalCases']
print(a)
datee = d['date']
def date(i):
  datee[i] = datee[i].replace('-', ' ')
  date=str(datee[i])
  day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
  day = datetime.datetime.strptime(date, '%Y %m %d').weekday()
  c = day_name[day]  
  return c
x=[]
while i<len(a)-2:
  c = date(i)
  if c == 'Monday':
    a[i] = a[i]+0.25*a[i]
  elif c == 'Tuesday':
    a[i] = a[i]+0.40*a[i]
  elif c == 'Wednesday':
    a[i] = a[i]+0.15*a[i]
  elif c == 'Sunday':
    a[i] = a[i]+0.15*a[i]
  x.append((a[i-1]+a[i]+a[i+1])/3)
  i+=1
print(x)
x = pd.DataFrame(x)

plt.plot(x, color = 'orange', linewidth = 1)
plt.plot(d['hospitalCases'], color = 'grey', linewidth = 0.25)
plt.savefig('covid.png')
plt.show()
