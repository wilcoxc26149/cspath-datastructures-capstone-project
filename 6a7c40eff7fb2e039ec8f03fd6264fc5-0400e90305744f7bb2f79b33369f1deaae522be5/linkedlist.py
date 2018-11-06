from node import Node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  
  def get_size(self):
    current_node = self.head_node
    size = 0
    while current_node:
      size += 1
      current_node = current_node.get_next_node()      
    return size
  
  def stringify_list(self):
    string_list = "["
    current_node = self.head_node
    while current_node:
      string_list += str(current_node.value) + ", "
      current_node = current_node.get_next_node()
    string_list += "]"  
    return string_list
  
  def exists(self, value_to_check):
    current_node = self.head_node
    while current_node:
      if current_node.value == value_to_check:
        return 1
      current_node = current_node.get_next_node()
    return None
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == node_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node

