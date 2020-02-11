# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        hashed = self._hash_mod(hash(key))
        if self.storage[hashed]:
            node = self.storage[hashed]
            while node.next:
                node = node.next
            node.next = LinkedPair(key, value)
        else:
            self.storage[hashed] = LinkedPair(key, value)



    def remove(self, key):
        hashed = self._hash_mod(hash(key))
        node = self.storage[hashed]
        prev = None
        while node:
            if node.key == key:
                if node.next:
                    if prev:
                        prev.next = node.next
                        node = None
                    else:
                        node = None
                else:
                    node = None
            else:
                prev = node
                node = node.next
        del node
        return(None)


    def retrieve(self, key):
        hashed = self._hash_mod(hash(key))
        node = self.storage[hashed]
        while node:
            if node.key == key:
                return node.value
            else:
                node = node.next
        return(None)


    def resize(self):
        self.capacity *= 2
        old = self.storage
        self.storage = [None] * self.capacity

        for link in old:
            if link:
                self.insert(link.key, link.value)
                link = link.next
                while link:
                    self.insert(link.key, link.value)
                    link = link.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")


# test = HashTable(10)
#
# test.insert('w', 'what')
# test.insert('t', 'too')
# test.insert('s', 'see')
# test.insert('z', 'zee')
#
# test.retrieve('z')
#
# test.remove('w')
#
# test.resize()
#
# test.capacity
