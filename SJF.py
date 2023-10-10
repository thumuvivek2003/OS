SJF
import pandas as pd
pid = ["P1","P2","P3","P4","P5"]
at = [3,1,4,0,2]
bt = [1,4,2,6,3]
tat = []
wt = []
n = len(at)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if at[i]>at[i+1] or (at[i]==at[i+1] and bt[i]>bt[i+1]):
            at[i],at[i+1] = at[i+1],at[i]
            bt[i],bt[i+1] = bt[i+1],bt[i]
            pid[i],pid[i+1] = pid[i+1],pid[i]
            swapped = True


for i in range(n):
    if i == 0:
        ct[0] = at[0]+bt[0]
    else:
        minIdx = i
        min_val = 9999
        for j in range(i+1,n):
            if(at[j]<=ct[i-1] and bt[j]<min_val):
                min_val = bt[j]
                minIdx = j
        at[minIdx],at[i] = at[i],at[minIdx]
        bt[minIdx],bt[i] = bt[i],bt[minIdx]
        ct[i] = bt[i]+max(ct[i-1],at[i])
    tat.append(ct[i]-at[i])
    wt.append(tat[i]-bt[i])
df3 = pd.DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct,"TAT":tat,"WT":wt})
# df3 = pd.DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct})
df3
