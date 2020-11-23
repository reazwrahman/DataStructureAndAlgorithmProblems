list1=[1,2,3,4,5,5,5,6,6,6,7]
list2=[3,7,2,1,4,5,5]

count={}
for i in list1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for j in list2:
    if j in count:
        count[j]-=1
    else:
        count[j]=1

for k in count:

    if count[k] !=0:
        print (f'{k} is missing {count[k]} times')
    
    else:
        print ('no elements are missing')
               
