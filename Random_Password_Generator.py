import random 

chars = ' ASDSHUIWELJVLURGERLJGIUYalkjghoierguhasggjklhqu73333341678917809!@#$%&*(*())'

pass_len = int(input ("Enter ur password length :"))
pass_count = int (input ("how many passwords do u want:"))
 
for x in range (0,pass_count ):
    password = "" .join (random.sample ( chars , pass_len ))
    print ("Ur password is  " ,{password})


