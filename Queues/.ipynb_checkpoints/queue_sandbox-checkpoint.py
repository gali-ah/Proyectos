import logging
from Node_sandbox import Node
class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.is_empty():
            logging.warning("¡No hay nada que ver aqui!")
            return None
        else:
            return self.head.value

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0
    def enqueue(self, value):
        new_node = Node(value)
        if self.has_space():
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node
            self.size += 1
        else:
            logging.warning("¡Lo sentimos, no hay más espacio!")
            
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            logging.warning(f"¡Eliminando {item_to_remove.get_value()} de la cola!")
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next_node
            self.size -= 1
            return item_to_remove.get_value()
        else:
            logging.warning("¡Esta cola está totalmente vacía!")
            return None 