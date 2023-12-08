class BrowserHistory:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.current = None
        

    def visit(self, url):
        if self.current is None:
            self.head = self.Node(url)
            self.current = self.head
        else:
            new_node = self.Node(url)
            new_node.prev = self.current
            self.current.next = new_node
            self.current = new_node

    def back(self):
        if self.current != self.head:
            self.current = self.current.prev
            return self.current.data
        
        return 'This is the first page visited'

    def forward(self):
        if self.current.next != None:
            self.current = self.current.next
            return self.current.data
        
        return 'This is the last page visited'
    
    
################################
## Testing
################################
    
history = BrowserHistory()
history.visit('www.google.com')
history.visit('www.wikipedia.org')
history.visit('www.github.com')
print(history.forward()) #Invalid
print(history.back()) #Wikipedia
print(history.back()) #Google
print(history.back()) #Invalid
print(history.forward()) #Wikipedia
print(history.forward()) #Github
