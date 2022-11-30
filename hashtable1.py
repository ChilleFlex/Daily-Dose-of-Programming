class hashable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        ascii = 0
        for chars in key:
            ascii += ord(chars)
        return ascii%self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        
if __name__ == "__main__":
    t = hashable()
    t['march 6'] = 130
    t['march 9'] = 55
    t['march 1'] = 100
    
    print(t.arr)
    print(t['march 6'])
    del t['march 1']
    print(t.arr)