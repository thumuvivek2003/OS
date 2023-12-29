#include<stdio.h>

int main() {
    int cnt, n, t, remain, flag = 0, tq;
    int wt = 0, tat = 0;

    n = 4;
    remain = n;

   int at[] = {0, 1, 2, 4};
    int bt[] = {5, 4, 2, 1};
    int rt[] = {5, 4, 2, 1};

    tq = 2;

    printf("\n\nProcess\t|Turnaround Time|Waiting Time\n\n");
    
    for(t = 0, cnt = 0; remain != 0;) {
        if(rt[cnt] <= tq && rt[cnt] > 0) {
            t += rt[cnt];
            rt[cnt] = 0;
            flag = 1;
        } else if(rt[cnt] > 0) {
            rt[cnt] -= tq;
            t += tq;
        }

        if(rt[cnt] == 0 && flag == 1) {
            remain--;
            printf("P[%d]\t|\t%d\t|\t%d\n", cnt + 1, t - at[cnt], t - at[cnt] - bt[cnt]);
            wt += t - at[cnt] - bt[cnt];
            tat += t - at[cnt];
            flag = 0;
        }

        if(cnt == n - 1)
            cnt = 0;
        else if(at[cnt + 1] <= t)
            cnt++;
        else
            cnt = 0;
    }

    printf("\nAverage Waiting Time= %f\n", wt * 1.0 / n);
    printf("Avg Turnaround Time = %f", tat * 1.0 / n);

    return 0;
}
