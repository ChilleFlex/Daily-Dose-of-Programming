class hashable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        ascii = 0
        for chars in key:
            ascii += ord(chars)
        return ascii%self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,ele in enumerate(self.arr[h]):
            if len(ele)==2 and ele[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                del self.arr[h][idx]
        
if __name__ == "__main__":
    t = hashable()
    t['march 6'] = 130
    t['march 6'] = 55
    t['march 8'] = 78
    t['march 17'] = 100
    print(t.arr)
    print(t['march 6'])
    del(t['march 17'])
    print(t.arr)
    