class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, key, value):
        self.name = str
        self.phonenumber = str
        self.next = None
   
    

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.key!r}, {self.value!r})"   
    
    

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size
  
  # Hash
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size   
    
  # Insert method
    def insert(self, key, value):
        index = self.hash_function(key)

        current =  self.data[index] # Get the linked list value(s) for index
		
    # If there are no values currently at that position
        if current is None:
            self.data[index] = Node(key, value)
            return

        while current:
            if current.key == key:         
                current.value = value
                return
            if current.next is None:       
                break
            current = current.next

        current.next = Node(key, value) # Add to the end of the list
    
  # Search method
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
        current = current.next
    
        return None
    

    def print_table(self):
        # Readable print for the table
        for i, head in enumerate(self.data):
            chain = []
            cur = head
            while cur:
                chain.append(f"{cur.key}:{cur.value}")
                cur = cur.next
            print(f"[{i}] -> " + " -> ".join(chain) if chain else f"[{i}] -> ∅")

    def __repr__(self):
        #  print(table) 
        rows = []
        for i, head in enumerate(self.data):
            parts = []
            cur = head
            while cur:
                parts.append(f"{cur.key}:{cur.value}")
                cur = cur.next
            rows.append(f"[{i}] {' -> '.join(parts) if parts else '∅'}")
        return "<HashTable>\n" + "\n".join(rows)

# Test your hash table implementation here.  

# Main
if __name__ == "__main__":
  
    #Test hash table function - insert
    table = HashTable(size=15)
    table.insert("Jim", "900-234-0987")
    table.insert("Dave", "800-456-4567")
    table.insert("John", "700-123-4321")
    table.insert("Alice", "600-123-4576")

    table.print_table()

    #table.insert("Alice", Contact("Alice", "555-0101"))
    #table.insert("Bob", Contact("Bob", "555-0202"))

    # Update an existing key/number
    table.insert("Jim", "999-999-9999")

    # Lookups
    print("Jim ->", table.search("Jim"))    # "999-999-9999"
    print("Alice ->", table.search("Alice"))
    
    table.print_table()