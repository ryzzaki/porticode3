import research as rs

class Start:

    def __init__(self):
        self.topic = input("Enter Topic: ")
    
    def research(self):
        rs.download()
