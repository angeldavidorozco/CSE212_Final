from collections import deque

class CallController:
    def __init__(self):
        self.queue = deque()

    def NewClient(self, name):
        self.queue.append(name)
        if (len(self.queue)-1 == 0):
            print("You are next")
        else:
            print(f"There are {len(self.queue)-1} clients in front of you.")
        

    def TakeCall(self):
        if len(self.queue) == 0:
            print("No clients in the queue.")
        else:
            name = self.queue.popleft()
            print(f"Connecting to {name}")


################################
## Testing
################################

CC = CallController()

CC.NewClient("Jorge") ##Jorge is the first in the queue, and should be the next client
CC.TakeCall()
CC.NewClient("Susy") ##Susy is the first in the queue, and should be the next client
CC.NewClient("Jhon")
CC.NewClient("Doe")
CC.TakeCall()
CC.TakeCall()
CC.TakeCall()
CC.TakeCall() ## Should print "No clients in the queue"