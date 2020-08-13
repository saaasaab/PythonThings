def find_available(prev,total,row,size,start,tryte):
    newRow = row#Reset Row
    newTotal = list(total)
    optionColor=prev[1]
    optionSize=int(prev[0])
    newAvailable=list(start)

    for num,combo in enumerate(newAvailable):
        
        for i in tryte:
            if i == combo:
                newAvailable[num]="0"+newAvailable[num][1]
        
        if newTotal[newRow]!=0:
            if combo[1]==optionColor:
                newAvailable[num]="0"+newAvailable[num][1]
            if int(combo[0])+newTotal[newRow]>size:
                newAvailable[num]="0"+newAvailable[num][1]
                
    #print(prev,total,row,newAvailable)
    return(newAvailable)


trytes=[[]]
size=3
tot = [0 for i in range(size)]
#tot=[0,0,0] #Including the addition of the prev option
row = 0
#start= ["1w","1b","1r","2w","2b","1r"]
#start= ["1w","2w","3w","1b","2b","3b"]
#start= ["1w","2w","3w","1b","2b","3b","1r","2r","3r"]
#start= ["1w","2w","1b","2b","1r","2r","1g","2g","1p","2p"]
start= ["1w","2w","3w",
        "1b","2b","3b",
        "1r","2r","3r"]
tryte=0


for i in start:
    trytes[tryte].append([i])#Appends the option
    tot = [0 for i in range(size)] #Including the addition of the prev option
    row=0
    tot[row]+=int(i[0])
    if tot[row]>=size: ##CHANGE THE SIZE OF THE TRYTE
        row+=1

    available = find_available(i,tot,row,size,start,trytes[tryte][0])
    trytes[tryte].append([tot])
    trytes[tryte].append([row])
    
    tryte+=1
    trytes.append([])



group = list(trytes)
for i in trytes:
    print(i)
tryte=0
trytes=[[]]

running = True
count =0
finished=[]
while running:
    for i in range(len(group)-1):
        if sum(group[i][1][-1])<size*size and group[i][2][-1]<size:
            option = group[i][0][-1]
            tot = group[i][1][-1]
            row = int(group[i][2][-1])
            
            available = find_available(option,tot,row,size,start,group[i][0])
            for j in range(len(available)):
                newtot=list(tot)
                newRow=row
                choice=available[j] 
                if(int(choice[0])!=0):
                    #print(trytes[tryte])
                    trytes[tryte].append(list(group[i][0]))
                    #print(trytes[tryte][1])
                    trytes[tryte][0].append(choice)
                    newtot[newRow]+=int(choice[0])
                    
                    if newtot[newRow]==size:#CHANGE WITH THE SIZE
                        newRow+=1
                    trytes[tryte].append([newtot])
                    trytes[tryte].append([newRow])
                    
                    tryte+=1
                    try: 
                        trytes.append([])
                    except:
                        print(len(finished))

                    
        else:
            #print(True)
            finished.append(group[i])
            count+=1

        if(count >= len(group)-1):
           running=False

    if running:
        group = list(trytes)
        tryte=0
        trytes=[[]]

for i in trytes:
    finished.append(i)


for i in range(len(finished)-1):
    print(finished[i][0])
print(len(finished))
#[[1], ['1w', '0w', '0w', '1b', '0b'], [[1, 0]], [0]]            
            
    
#print(trytes[i])#trytes[i][1]
#for i in trytes:
#    print(i)
#print(trytes)
