#IT210 Page Replacement
#Least Recently Used Algorithm
#Hamza Ahmed
primary_memory = [1,2,1,4,4,7,7,9]
frame = []
limit = 3

#Least Recently Used 
def LRU():
    for i in primary_memory:
        print(frame)
        #Checks if the same value is in the frame
        if i in frame:
            frame.remove(i)

            frame.append(i)
        else:
            #Replaces if the frame reached its size limit
            if(len(frame) <  limit):
                frame.append(i)
            else:
                frame.remove(frame[0])
                frame.append(i)
LRU()
