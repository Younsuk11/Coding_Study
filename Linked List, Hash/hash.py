




# Create a function that takes a list nums and returns its majority element
def majorityelement(nums):
    hash_table = {}
    
    max = 0
    ans = 0
    for num in nums:
        if num in hash_table:
            hash_table[num] +=1

            # if hash_table[num] >= len(nums)//2: # majority
            #     return num
        else:
            hash_table[num] = 1
        if hash_table[num] >=max:
                max = hash_table[num]
                ans = num
    return ans



#Hash table : using Linked List
class LinkedNode:
    def __init__(self, key, value):
         self.key = key
         self.value = value
         self.next = None

class HashTable:
    def __init__(self, modulo):
        self.modulo = modulo
        self.table = [None for _ in range(self.modulo)] #LinkedNode를 담을 예정
        self.size = 0 # number of elements

    def hash_function(self, key):
        return key % self.modulo
    
    def insert(self, key, value):
        '''
        inserts a new (key, value) to hash table
        if the key already exists, replace the value
        collision is handled using a SLL
        '''
        
        #idx : hash function
        idx = self.hash_function(key)

        #check existance
        if self.table[idx] is None:
            self.table[idx] = LinkedNode(key, value)
            self.size +=1

        else: #해당 값에 이미 값들이 있다면 linkednode를 타고 가서 마지막에 달기.
            curr = self.table[idx] # linkednode
            #linked list traversal
            while(curr) :

                ##같은 key가 있다면 value replace
                if curr.key == key:
                    curr.value = value
                    return
                curr = curr.next

            # 아예 없는 거라면 chain의 맨 앞에 넣기.(addfront)
            newnode = LinkedNode(key, value)
            newnode.next = self.table[idx]
            self.table[idx] = newnode
            self.size +=1
        
        # resizing
        if self.size / self.modulo > 0.8 :  # N/M
            self.rehash()



    def search(self, key):
        
        idx = self.hash_function(key)
        curr = self.table[idx]
        while(curr):
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def remove(self, key):
        '''
        remove the (key, value) from hash table
        찾고 -> 있으면 지우고, 없으면 그냥 Return
        '''
        idx = self.hash_function(key)

        curr = self.table[idx]
        prev = None
        while(curr):
            if curr.key == key:
                
                if curr == self.table[idx]:
                    self.table[idx]= curr.next
                else:
                    prev.next = curr.next
                
                self.size -=1
                return True
            prev = curr
            curr = curr.next
        return False

    def __len__(self):
        return self.size
    
    def rehash(self):
        '''
        load of the hash table = (#N, size) / (# of buckets , modulo)
        rehasing when load >=0.8
        when rehashing, double the original modulus and create a new hash table
        '''
        print("rehashing!", end = "")
        self.modulo *= 2
        self.size = 0
        self.old_table = self.table

        self.table =[None for _ in range(self.modulo)]

        for node in self.old_table: # 모든 table element를 순회하면서 옮기기
            while node:
                self.insert(node.key, node.value) # 여기서 size 갱신
                node = node.next

        



def main():
    L = [3, 3, 3, 2, 1, 3, 2, 1]
    print("Majority Element of list L : ", majorityelement(L))

    # Test code for given cases; run without modification
    ht = HashTable(13)
    print("Created hash table with modulo = 13\n")

    print("Size of hashtable:",len(ht),"/ Expected: 0") 
    ht.insert(10, "apple") 
    print("Inserted apple with key = 10")
    print("Value for key = 10:", ht.search(10),"/ Expected: apple\n")

    ht.insert(10,"banana") 
    print("Inserted banana with key = 10")
    print("Value for key = 10:", ht.search(10), "/ Expected: banana\n")
    print("Size of hashtable:",len(ht),"/ Expected: 1") 

    ht.insert(23, "pineapple")
    print("Inserted pineapple with key = 23")
    print("Size of hashtable:",len(ht),"/ Expected: 2") 
    ht.remove(23)
    print("Removed key = 23")
    print("Value for key = 23:", ht.search(23), "/ Expected: None")

if __name__ == "__main__":
    main()