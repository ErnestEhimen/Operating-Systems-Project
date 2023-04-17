import numpy as np

def check(i):
    for j in range(resc):
        if(need[i][j]>avl[j]):
            return 0
    return 1
 
proc = int(input("Enter the number of processes:"))
resc = int(input("Enter the number of resources:"))
 
 #Gets user input for the maximum resources
 
print("Enter the Maximum number of resources needed for each process (separated by space): ")

entries = list(map(int, input().split()))
 
max= np.array(entries).reshape([proc, resc])
print(max)

#Gets user input for the available resources

print("Enter the Available resources single line (separated by space): ")

entries_avl = list(map(int, input().split()))
 
avl= np.array(entries_avl)

#Gets user input for allocated resources

print("Enter the Allocated resources for each process in a single line (separated by space): ")

entries_all = list(map(int, input().split()))
 
all= np.array(entries_all).reshape([proc, resc])
print(all)

## Calculates the Need of the processes

need=max-all;

print("");
print("The Processes needs resources as below:")
print(need);

## Checking if executing a process causes deadlock

Seq = np.zeros((proc,),dtype=int)
vis = np.zeros((proc,),dtype=int)

count = 0
i= 0;
while( count < proc ):
    temp=0
    for i in range( proc ):
        if( vis[i] == 0 ):
            if(check(i)):
                Seq[count]=i;
                count+=1
                vis[i]=1
                temp=1
                for j in range(resc):
                    avl[j] += all[i][j] 
    if(temp == 0):
        break
##Declares if a deadlock occurs

if(count < proc):
    print('The system is Unsafe')
else:
    print("The system is Safe")
    print("The Safe Sequence is: ",Seq)
    print("The total Available resources are:",avl)


