from collections import deque

class CallController:
    def __init__(self):
        self.client_queue = deque()
        self.no_client_queue = deque()

    def NewClient(self, name, client):
        if client:
            self.client_queue.append(name)
        else:
            self.no_client_queue.append(name)
        
        if ((len(self.client_queue)-1 == 0) & client):
            print("You are the next client")
        elif((len(self.no_client_queue)-1 == 0) & (not client)):
            print("You are the next no client")
        else:
            print(f"There are {len(self.client_queue)} clients and {len(self.no_client_queue)} no clients in the queue.")
        

    def TakeCall(self):
        if len(self.client_queue) > 0:
            name = self.client_queue.popleft()
            print(f"Connecting to client {name}")
        elif len(self.no_client_queue) > 0:
            name = self.no_client_queue.popleft()
            print(f"Connecting to no client {name}")
        else:
            print("No calls in the queue.")

################################
## Testing
################################

CC = CallController()

CC.NewClient("Jorge", True) ##Jorge is the first in the queue, and should be the next client
CC.TakeCall()
CC.NewClient("Susy", True) ##Susy is the first in the queue, and should be the next client
CC.NewClient("Jhon", False) ##First no client
CC.NewClient("Doe", False)
CC.TakeCall() ##Takes susy
CC.TakeCall() ##Takes Jhon
CC.TakeCall() ##Takes Doe
CC.NewClient("Will", False)
CC.NewClient("Ana", False)
CC.NewClient("Jim", True)
CC.TakeCall() ## takes Jim
CC.TakeCall() ##Takes will
CC.TakeCall() ##Takes Ana
CC.TakeCall() ##Should print no clients