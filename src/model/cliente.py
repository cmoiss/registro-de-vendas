class Cliente:
    def __init__(self, name):
        self.name = name
        
    
    def to_list(self):
        return [
            self.name
        ]