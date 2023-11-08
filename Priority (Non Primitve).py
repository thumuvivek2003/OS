
from pandas import DataFrame
#Criteria : Priority 
#Mode : Non-Primitive 

pid = ["P1","P2","P3","P4","P5"]
at = [0,1,2,3,4]
n = len(at)
bt = [4,3,1,5,2]
pr = [2,3,4,5,5]
tat = [0,0,0,0,0]
wt = [0,0,0,0,0]
ct =[0 for i in range(n)]
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if at[i]>at[i+1] or (at[i]==at[i+1] and pr[i]>pr[i+1]):
            at[i],at[i+1] = at[i+1],at[i]
            bt[i],bt[i+1] = bt[i+1],bt[i]
            pid[i],pid[i+1] = pid[i+1],pid[i]
            swapped = True

for i in range(n):
    if i == 0:
        ct[0] = at[0]+bt[0]
    else:
        maxIdx = i
        for j in range(i+1,n):
            if(at[j]<=ct[i-1] and pr[j]>pr[maxIdx]):
                maxIdx = j
        at[maxIdx],at[i] = at[i],at[maxIdx]
        bt[maxIdx],bt[i] = bt[i],bt[maxIdx]
        pr[maxIdx],pr[i] = pr[i],pr[maxIdx]
        pid[maxIdx],pid[i] = pid[i],pid[maxIdx]
        ct[i] = bt[i]+max(ct[i-1],at[i])
    tat[i] = ct[i]-at[i]
    wt[i] = tat[i]-bt[i]
df3 = DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct,"TAT":tat,"WT":wt,"Priority":pr})
# df3 = pd.DataFrame({"PId":pid,"AT":at,"BT":bt,"CT":ct})
df3
