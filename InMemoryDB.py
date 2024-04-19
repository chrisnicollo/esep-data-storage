class InMemoryDB:
    def __init__(self):
        self.dictionary = dict() # The permanent dictionary that has a complete transaction information
        self.temp = dict() # The temporary dictionary to be used during transactions
        self.in_progress = False
      
    def begin_transaction(self):
        # I'm not sure what should happen if this is called when another transaction is already in progress, so I will assume that I can clear the existing transaction data
        # FIXME: Contact someone about this
        self.temp.clear()
        self.in_progress = True
    
    def put(self, key: str, value: int):
        if not self.in_progress: raise Exception("can only update keys during an in-progress transaction")
        self.temp[key] = value
      
    def get(self, key: str) -> int:
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return None
        
    def commit(self):
        if not self.in_progress: raise Exception("can only commit during an in-progress transaction")
        for key, value in self.temp.items():
            self.dictionary[key] = value
        self.temp.clear()
        self.in_progress = False
    
    def rollback(self):
        if not self.in_progress: raise Exception("can only rollback during an in-progress transaction")
        self.temp.clear()
        self.in_progress = False
