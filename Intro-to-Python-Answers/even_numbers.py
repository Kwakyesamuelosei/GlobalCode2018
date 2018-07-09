
#Printing even numbers between 12 and 20

#for i in range(13,20):
#    if i%2== 0:
#       print("Even numbers : {0}".format(i))
    

#function for  even numbers given range of numbers

#def even(number_from, to):
#    for i in range(number_from,to):
#        if i%2 == 0:
#           print("Even numbers : {0}".format(i))
            
#even(13,20)
        
def even(number_from, to):
    for i in reversed(range(number_from,to)):
        if i%2 == 0:
            print("Even numbers : {0}".format(i))
            
even(13,20)
