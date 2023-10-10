# With Comments


at = [1,1,2,3]
bt = [6,8,7,3]


def SRTF(at,bt):
    if(len(at) != len(bt)):return False
    # Intializing requirements i.e rt,ct,ata,wt,completed,t,minrt,minIdx,found
    n = len(at)
    pid = ["P"+str(i+1) for i in range(n)]
    rt = [i for i  in bt]
    ct = [0 for i in range(n)]
    tat = [0 for i in range(n)]
    wt = [0 for i in range(n)]
    completed = 0
    t = 0
    minrt = 999999999
    minIdx = 0
    found = False


    # Repeat upto all all tasks completed
    while(completed != n):
        # check if any smaller rt available 
        for j in range(n):
            # Checking at , bt , rt
            if(at[j]<=t and rt[j]<minrt and rt[j]>0):
                minrt = rt[j]
                minIdx = j
                found = True
        # If min rt available
        if(found):
            rt[minIdx] -= 1
            if(rt[minIdx] == 0):
                minrt = 9999999999
                completed += 1
                found = False


                finished = t+1
                tat[minIdx] = finished - at[minIdx] 
                curr_wt = tat[minIdx] - bt[minIdx]
                wt[minIdx] = 0 if (curr_wt < 0) else curr_wt;
        
        #Increase time quantum
        t+=1
    return pd.DataFrame({"PId":pid,"AT":at,"BT":bt,"TAT":tat,"WT":wt})
SRTF(at,bt)
