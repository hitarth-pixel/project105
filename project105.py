import csv
import math
with open("data.csv",newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
def getMean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean=total/n
    print(mean)
    return mean
sqrList=[]
for number in data:
    a=int(number)-getMean(data)
    a=a*a
    sqrList.append(a)
sum=0
for s in sqrList:
    sum=sum+s
    result=sum/(len(data)-1)
    std=math.sqrt(result)
print("standard deviation=== "+str(std))