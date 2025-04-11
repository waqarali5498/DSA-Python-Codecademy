class Node:
  def __init__(self,value,next_node=None):
    self.value=value
    self.next_node=next_node



  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self,next_node):
    self.next_node=next_node


n1=Node(1)
n2=Node(2)
n3=Node(3)
n1.set_next_node(n3)
# n2.set_next_node(n2)

print(n2.get_next_node())