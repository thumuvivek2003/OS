
#SJF Algortithm
from pandas import DataFrame

pid = ["P1","P2","P3","P4","P5"]

# Test case 1 : 
# at = [3,1,4,0,2]
# bt = [1,4,2,6,3]


# Test case 2:
at = [1,3,6,7,9]
bt = [7,3,2,10,8]
n = len(pid)


ct = [0 for i in range(n)]
wt = [0 for i in range(n)]
tat = [0 for i in range(n)]

# Sort at,bt,pid lists based on arrival time 
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if at[i]>at[i+1] or (at[i]==at[i+1] and bt[i]>bt[i+1]):
            at[i],at[i+1] = at[i+1],at[i]
            bt[i],bt[i+1] = bt[i+1],bt[i]
            pid[i],pid[i+1] = pid[i+1],pid[i]
            swapped = True


# Calculate ct,tat,wt
for i in range(n):
    if i == 0:
        ct[0] = at[0]+bt[0]
    else:
        minIdx = i
        for j in range(i+1,n):
            if(at[j]<=ct[i-1] and bt[j]<bt[minIdx]):
                minIdx = j
        at[minIdx],at[i] = at[i],at[minIdx]
        bt[minIdx],bt[i] = bt[i],bt[minIdx]
        pid[minIdx],pid[i] = pid[i],pid[minIdx]
        ct[i] = bt[i]+max(ct[i-1],at[i])
    tat[i] = ct[i]-at[i]
    wt[i] = tat[i]-bt[i]
df3 = DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct,"TAT":tat,"WT":wt})
# df3 = pd.DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct})
df3
