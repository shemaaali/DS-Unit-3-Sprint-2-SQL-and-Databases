import functools
num_list = [10, 15, 8 , 4, 20, 5, 30, 50, 19, 60] 
  
# using reduce to compute sum of list 
print ("The sum of the list elements is:", end="") 
print (functools.reduce(lambda x,y : x*y,num_list)) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is:",end="") 
print (functools.reduce(lambda x,y : x if x > y else y, num_list)) 