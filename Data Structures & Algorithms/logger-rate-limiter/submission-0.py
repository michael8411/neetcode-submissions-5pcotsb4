class Logger:

    def __init__(self):
        self.mapping = {}
      


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print("message: ", message, "timestamp: ", timestamp)
        if message not in self.mapping:   
            self.mapping[message] = timestamp
            return True

        if timestamp >= self.mapping[message] + 10:
            self.mapping[message] = timestamp
            return True
        else:
            return False        
    
            
            
       
        

        

        



# Your Logger object will be instantiated and called as such:
