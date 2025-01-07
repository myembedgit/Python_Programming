

set1 = {'Raja','srini',"Dhivagar"}

set2 = {"Raja","jiya","Aakash"}

set3 = {1,2,3,"Raja"}

#set4 = set1.union(set2)  #->{'Raja', 'jiya', 'srini', 'Dhivagar', 'Aakash'}

#print(set4)

#print(set2.union(set1,set3))   #->{1, 2, 3, 'srini', 'Raja', 'Dhivagar', 'jiya', 'Aakash'}

#print(set1.union(set2))

#print(set1.union(('100','200')))  #-->{'Dhivagar', '100', '200', 'Raja', 'srini'}

# set Update function #

#set1.update(("1234","321"))
#print(set1)

#set2.update(["rajalingam",])   #->{'jiya', 'Aakash', 'rajalingam', 'Raja'}
#print(set2)

#print(set1.intersection(set2,set3))    #->{'Raja'}

#print(set1 & set2)    #->{'Raja'}  #{'Dhivagar', 'srini'}

print(set1.difference(set2))










