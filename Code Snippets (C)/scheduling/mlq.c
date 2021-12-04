/*
    Multi-Level Queueing
    Processes in the ready queue are divided into different classes where each class has its own scheduling needs.
        For example, a common division is a foreground(interactive) process and a background(batch) process, which each have different scheduling needs

    Ready Queue is divided into separate queues for each class of processes.
        For example, you have 3 types of processes: System, interactive, and batch.
        All 3 have their own queue.

    Each queue has its own scheduling algorithm.
        For example, queues 1 and 2 use RR and queue 3 uses FCFS

    To determine the scheduling among queue levels you can use one of two ways:
        1. Fixed priority preemptive scheduling method – 
            Each queue has absolute priority over the lower priority queue. 
            Let us consider following priority order queue 1 > queue 2 > queue 3.
            According to this algorithm, no process in the batch queue(queue 3) can run unless queues 1 and 2 are empty. 
            If any batch process (queue 3) is running and any system (queue 1) or Interactive process(queue 2) entered the ready queue the batch process is preempted.
        
        2. Time slicing – 
        In this method, each queue gets a certain portion of CPU time and can use it to schedule its own processes. 
        For instance:
            queue 1 takes 50 percent of CPU time 
            queue 2 takes 30 percent
            queue 3 gets 20 percent of CPU time.

    Advantages:
    The processes are permanently assigned to the queue, so there is low scheduling overhead

    Disadvantages:
    Some processes may starve for CPU fi some higher priorities queues are never becoming empty
    Inflexible
*/