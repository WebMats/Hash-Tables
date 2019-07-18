

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

# '''
# Research and implement the djb2 hash function
# '''``
def hash(string, max):
    hash = 5381
    for i in range(len(string)):
        hash = ((hash << 5) + hash) + ord(string[i])
    return hash % max

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index, new_node = hash(key, hash_table.capacity), LinkedPair(key, value)
    stored_node = hash_table.storage[index]
    if stored_node is None:
        hash_table.storage[index] = new_node
    elif stored_node is not None and stored_node.key == key:
        stored_node.value = value
    else:
        while stored_node.next:
            if stored_node.next.key == key:
                stored_node.next.value = value
                return
            stored_node = stored_node.next
        stored_node.next = new_node
    

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        print('Warning: key being used does not have a value')
    elif hash_table.storage[index].key == key and hash_table.storage[index].next is not None:
        hash_table.storage[index] = hash_table.storage[index].next
    elif hash_table.storage[index].key == key:
        hash_table.storage[index] = None
    else:
        cur_node = hash_table.storage[index]
        next_node = hash_table.storage[index].next
        searching = True
        while searching and next_node is not None:
            if next_node.key == key:
                searching = False
                cur_node.next = next_node.next
            else:
                cur_node, next_node = next_node, next_node.next



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    value = None
    index = hash(key, hash_table.capacity)
    cur_node = hash_table.storage[index]
    searching = True
    while searching and cur_node is not None:
        if cur_node.key == key:
            searching = False
            value = cur_node.value
        else:
            cur_node = cur_node.next
    return value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    sec_half = [ None ] * hash_table.capacity
    hash_table.storage = [*hash_table.storage, *sec_half]
    hash_table.capacity = hash_table.capacity * 2
    return hash_table
    


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


# Testing()
