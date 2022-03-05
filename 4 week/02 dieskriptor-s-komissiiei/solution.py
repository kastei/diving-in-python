class Value():

    def __init__(self):
        self.value = None
        
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = (1 - instance.commission) * value