/*
    Earliest Deadline First
    Optimal dynamic priority scheduling algorithm used in real-time systems
    Uses priorities to the jobs for scheduling.
        Assigns these priorities based on the absolute deadline.
        The task whose deadline is closests gets the highest priority.

    Priorities are assigned and changed in a dynamic fashion
    Very efficient compared to other algorithms in real-time systems 
        Can make the CPU utilization to ~100% while guaranteeing task deadlines

    EDF includes the kernel overload. 
    In EDF, if the CPU usage is less than 100%, then it means that all the tasks have met the deadline. 
    EDF finds an optimal feasible schedule.
    The feasible schedule is one in which all the tasks in the system are executed within the deadline. 
    If EDF is not able to find a feasible schedule for all the tasks in the real-time system, then it means that no other task scheduling algorithms in real-time systems can give a feasible schedule. 
    All the tasks which are ready for execution should announce their deadline to EDF when the task becomes runnable. 

    EDF scheduling algorithm does not need the tasks or processes to be periodic and also the tasks or processes require a fixed CPU burst time. 
    In EDF, any executing task can be preempted if any other periodic instance with an earlier deadline is ready for execution and becomes active. 
    Preemption is allowed in the Earliest Deadline First scheduling algorithm.

    Limitations:
    Transient Overload Problem
    Resource Sharing Problem
    Efficient Implementation Problem
*/