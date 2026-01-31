# ---------- ENQUEUE ----------
def IsFull(Q,n,REAR):
    return REAR == n-1
def ENQUEUE(Q,n,FRONT,REAR,value):
    if IsFull(Q,n,REAR):
        print("QUEUE is FULL")
    else:
        if FRONT == -1:
            FRONT = 0
        REAR += 1
        Q[REAR] = value
    print('UPDATED QUEUE is:',Q)
    return FRONT,REAR
n = 6
Q = [None] * n
FRONT = -1
REAR = -1
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'V')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'I')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'V')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'I')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'D')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'H')
FRONT,REAR = ENQUEUE(Q,n,FRONT,REAR,'V')
print("FRONT =", FRONT, "REAR =", REAR)

#---------- DEQUEUE ----------

def IsEmpty(Q,FRONT,REAR):
    return FRONT==-1 or FRONT>REAR
def dequeue(Q,n,FRONT,REAR):
    if IsEmpty(Q,FRONT,REAR):
        print('QUEUE is EMPTY')
        return FRONT,REAR,None
    else:
        value = Q[FRONT]
        FRONT+=1
        print("Deleted Element:",value)
        if FRONT > REAR:
            FRONT = -1
            REAR = -1
        return FRONT,REAR,value
n = 5
Q = ['V','I','V','I','D','H']
FRONT = 0
REAR = 5
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
FRONT, REAR, val = dequeue(Q, n, FRONT, REAR)
print("Final FRONT =", FRONT, "REAR =", REAR)

