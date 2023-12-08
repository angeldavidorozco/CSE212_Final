class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, data):
        if not self.head:
            self.head = Node(data)
            self.current = self.head
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def back(self):
        if self.current != self.head:
            self.current = self.current.prev
            return self.current.data
        
        return 'This is the start of the list'

    def forward(self):
        if self.current.next != None:
            self.current = self.current.next
            return self.current.data
        
        return 'This is the end of the list'

    def remove_song(self, songName):
        curr = self.head
        while curr is not None:
            if curr.data == songName:
                if curr == self.tail:
                    self.tail.prev.next = None  
                    self.tail = self.tail.prev
                elif curr == self.head:
                    self.head.next.prev = None  
                    self.head = self.head.next 
                else:
                    curr.next.prev = curr.prev 
                    curr.prev.next = curr.next     
                return 
            curr = curr.next
    

    def insert_after(self, song, newSong):

        if song == None:
            new_node = Node(newSong)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while curr is not None:
            if curr.data == song:

                if curr == self.tail:
                    self.add_song(newSong)   

                else:
                    new_node = Node(newSong)
                    new_node.prev = curr     
                    new_node.next = curr.next 
                    curr.next.prev = new_node  
                    curr.next = new_node      
                return
            curr = curr.next 


    def print_playlist(self):
        curr = self.current
        while curr is not None:
            print(curr.data)
            curr = curr.next

################################
## Testing
################################

playlist = MusicPlaylist()

print('------Adding songs-------')

playlist.add_song('Song 1')
playlist.add_song('Song 2')
playlist.add_song('Song 3')
playlist.print_playlist()

print('------Removing song 2-------')

playlist.remove_song('Song 2')
playlist.print_playlist()

print('------Adding songs-------')

playlist.add_song('Song 4')
playlist.add_song('Song 5')
playlist.print_playlist()

print('------Adding a song at the start-------')

playlist.insert_after(None, 'Favorite Song')
playlist.back()
playlist.print_playlist()

print('------Reproducing 2 songs-------')

playlist.forward()
playlist.forward()
playlist.print_playlist()

print('------Going back to the start of the list-------')

playlist.back()
playlist.back()
playlist.back()
playlist.print_playlist()
