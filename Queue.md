# Queues

## Definition and Use Cases

A Queue is a linear data structure that follows a particular order in which operations are performed. The order is First In First Out (FIFO). We can think about it as the line of any grocery store, clients get added at the back of line (end of the queue) And the first client in line (start of the queue) will be served first.

Queues normally don't allow things to be added in the middle, this property of Queues make it useful in following certain kind of scenarios.

* CPU Scheduling: The processes in a computer system are scheduled according to a queue. The process at the front of the queue is the next one to be executed.

* Traffic Management: In networking, packets of data are often lined up in a queue for transmission over the internet. The packet at the front of the queue is sent first.

* Keyboard Buffer: When you type on a computer, sometimes the computer is busy and can’t keep up with your typing. The keystrokes are placed in a queue so that they can be processed in the order they were typed.

![queue representation](images/queue.JPG "Queue Representation")

## Common Operations

* enqueue(): Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.

* dequeue(): Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.

* size(): Return the size of the queue.

* empty(): Returns true if the length of the queue is zero.

## Common Implementations

Queues in Python can be implemented using different ways:

* list: List is a Python’s built-in data structure that can be used as a queue. we can replicate the common operations like enqueue() and dequeue() with append() and pop(0).

* collections.deque: Queue in Python can be implemented using deque class from the collections module. Deque stands for "Double Ended Queue", this module includes functions like append() and popleft() whic replicates the common operations

## Which one should you pick?

Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. However, if the size of the array is small, the differences in performance between deque and list will be almost negligible, for big amounts of data it's advisable that a deque is implemented instead of a list.


## Time Complexity (Big O Notation) For lists

* Enqueue (Insertion): O(1)
* Dequeue (Deletion): O(n)
* Size (Get size): O(1)
* Empty (Check if empty): O(1)

## Time Complexity (Big O Notation) For Deque

* Enqueue (Insertion): O(1)
* Dequeue (Deletion): O(1)
* Size (Get size): O(1)
* Empty (Check if empty): O(1)

## Example of implementation 

* Implement a class that handles the calls in a call center, when a call enters the system, it should be placed in a queue with a function called NewClient(name) which also prints a message that says "There are ${number} clients in front of you" or "You are next" in case the queue was empty. The operator needs the ability to take a call with the function TakeCall(), which connects the operator with the client and eliminates the client from the queue, the connection whould be done by printing a message that says "Connecting to ${name}" or "No clients in the queue" in case the queue is empty.

## Answer

```python
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
```

## Exercise

* For the code above, implement a new feature,  add a way to handle clients and no clients, clients should take priority on the queue and go first no matter how many no clients are there, the message now should print the number of clients and no clients in the queue, and when a TakeCall() is called, it should print the name and if it's a client or not

* Tip: In the class, handle the queues as 2 different queues 

* [Take a look at one possible solution for this](Queue_exercise.py)


[Back to welcome page](welcome.md)