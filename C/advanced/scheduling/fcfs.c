/*
    This is the simplest scheduling algorithm
    Queues processes in the order they arrive in the ready queue
    Execute one at a time, in order

    Burst Time: Time it takes for the process to complete task
    Completion Time: Time at which process completes its execution.
    Turn Around Time: Time Difference between completion time and arrival time. Turn Around Time = Completion Time – Arrival Time
    Waiting Time(W.T): Time Difference between turn around time and burst time. 
    Waiting Time = Turn Around Time – Burst Time

    Implementation:
    1-  Input the processes along with their burst time (bt).
    2-  Find waiting time (wt) for all processes.
    3-  As first process that comes need not to wait so 
    waiting time for process 1 will be 0 i.e. wt[0] = 0.
    4-  Find waiting time for all other processes i.e. for
     process i -> 
       wt[i] = bt[i-1] + wt[i-1] .
    5-  Find turnaround time = waiting_time + burst_time 
    for all processes.
    6-  Find average waiting time = 
                 total_waiting_time / no_of_processes.
    7-  Similarly, find average turnaround time = 
                 total_turn_around_time / no_of_processes.
*/

#include<stdio.h>
// Function to find the waiting time for all processes
void findWaitingTime(int processes[], int n, 
                          int bt[], int wt[])
{
    // waiting time for first process is 0
    wt[0] = 0;
   
    // calculating waiting time
    for (int  i = 1; i < n ; i++ )
        wt[i] =  bt[i-1] + wt[i-1] ;
}
   
// Function to calculate turn around time
void findTurnAroundTime( int processes[], int n, 
                  int bt[], int wt[], int tat[])
{
    // calculating turnaround time by adding
    // bt[i] + wt[i]
    for (int  i = 0; i < n ; i++)
        tat[i] = bt[i] + wt[i];
}
   
//Function to calculate average time
void findavgTime( int processes[], int n, int bt[])
{
    int wt[n], tat[n], total_wt = 0, total_tat = 0;
   
    //Function to find waiting time of all processes
    findWaitingTime(processes, n, bt, wt);
   
    //Function to find turn around time for all processes
    findTurnAroundTime(processes, n, bt, wt, tat);
   
    //Display processes along with all details
    printf("Processes   Burst time   Waiting time   Turn around time\n");
   
    // Calculate total waiting time and total turn 
    // around time
    for (int  i=0; i<n; i++)
    {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        printf("   %d ",(i+1));
        printf("       %d ", bt[i] );
        printf("       %d",wt[i] );
        printf("       %d\n",tat[i] );
    }
    
    int s=(float)total_wt / (float)n;
    int t=(float)total_tat / (float)n;
    printf("Average waiting time = %d",s);
    printf("\n");
    printf("Average turn around time = %d ",t);
}
   
// Driver code
int main()
{
    //process id's
    int processes[] = { 1, 2, 3};
    int n = sizeof processes / sizeof processes[0];
   
    //Burst time of all processes
    int  burst_time[] = {10, 5, 8};
   
    findavgTime(processes, n,  burst_time);
    return 0;
}
// This code is contributed by Shivi_Aggarwal