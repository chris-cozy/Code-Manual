/*
    Least Slack Time
    Dynamic priority driven scheduling algorithm used in real-time systems
    All tasks are assigned some priority according to their slack time
        Tasks with the least slack time has highest priority and vice versa
    Priorities are assigned dynamically

    Slack time is calculated by:
        slack_time = (D - t - e')
        D: task deadline
        t: Real time when the cycle starts
        e': remaining execution time of the task

    The task which has the minimal slack time is dispatched to the CPU for its execution as it has the highest priority.
    Hyper Period (HP) is the time period of the Gantt chart which is equal to the LCM of the periods of all the tasks in the system.
    At time t, the slack of a task is equivalent to ( d-t ) minus the time required to complete the remaining portion of the task.
    A complex algorithm, and works only when preemption is allowed.
        It can produce a feasible schedule if and only if a feasible schedule exists for the set of tasks that are runnable.

    It is different from the Earliest Deadline First because it requires execution times of the task which are to be scheduled. 
    Hence it is sometimes impractical to implement the Least Slack Time scheduling algorithm because the burst time of the tasks in real-time systems is difficult to predict.

    Unlike EDF (Earliest Deadline First) scheduling algorithm, LST may under-utilize the CPU, thus decreasing the efficiency and throughput.

    If two or more tasks which are ready for execution in LST, and the tasks have the same slack time or laxity value, then they are dispatched to the processor according to the FCFS (First Come First Serve) basis.
    

*/