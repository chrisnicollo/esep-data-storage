class InMemoryDB:
    def __init__(self):
        self.dictionary = dict() # The permanent dictionary that has a complete transaction information
        self.temp = dict() # The temporary dictionary to be used during transactions
        self.in_progress = False
      
    # This will always clear the previous existing transaction data
    # If this is called while a transaction is already in progress, the transaction will be aborted, an exception will be raised, and no new transaction will start
    def begin_transaction(self):
        self.temp.clear()
        if self.in_progress:
            self.in_progress = False
            raise Exception("can only start a new transaction when there is not already an in-progress transaction")
        else:
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
