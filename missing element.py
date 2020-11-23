


def find_missing_element(list1,list2):


    missing=[]
    newlist1=list1

    while len(list2)>0:
        
        for i in range(len(newlist1)):
            if newlist1[i] in list2:
                list2.remove(newlist1[i])
                #print (list2)
                #print (f'exists{newlist1[i]}')
            else:
                missing.append(newlist1[i]) 
        
    print (f'missing element(s) {missing}')
    
find_missing_element([5,5,5,5,7],[5,5,7])
