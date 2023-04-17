#IT210 First Come First Se
#Hamza Ahmed
primary_memory = [1,2,1,4,4,7,7,9]
frame = []
limit = 3
#First come first serve
def FIFS():
    for i in range(8):
        frame.append(primary_memory[i])
        print(frame)
        #Checks of frame length is greater than limit
        if len(frame) >= limit:
            frame.remove(frame[0])
FIFS()






    


