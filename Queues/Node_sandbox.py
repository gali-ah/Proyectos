class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node 
    
    def set_next_node(self, next_node):
        if not isinstance(next_node, (Node, dict, type(None))):
            raise TypeError("next_node debe ser de tipo Node, dict, o None")
        self.next_node = next_node