#IT210 Least Frequently Used Algorithm 
#Hamza Ahmed
from collections import defaultdict
primary_memory = [1,2,1,4,4,7,7,9]
frame = []
limit = 3
frequency = defaultdict(int)
#Least Frequenty used
def LFU():
    global frame
    for i in primary_memory:
        print(frame)
        if i in frame:
            #Counts the frequenct of the value
            frequency[i] += 1
        else:
            #Checks if frame is greater than limit
            if len(frame) < limit:
                frame.append(i)
                frequency[i] += 1
            else:
                # finds lowest Frequency Page
                lowest_frequency = min(frame, key=lambda x: frequency[x])
                frame.remove(lowest_frequency)
                #Deletes the frequency value of the lowest Frequency
                del frequency[lowest_frequency]
                frame.append(i)
                frequency[i] += 1
LFU()