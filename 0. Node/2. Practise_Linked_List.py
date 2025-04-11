class Node:
    def __init__(self,value,link_node=None):
        self.value=value
        self.link_node=link_node
    
    def set_link_node(self,link_node):
        self.link_node=link_node

    def get_link_node(self):
        return self.link_node
    
    def get_value(self):
        return self.value
    


head_node=Node("Head Node")
mid_node=Node('Middle Node')
last_node=Node("Leaf Node")

head_node.set_link_node(mid_node)
print(head_node.get_link_node().get_value())

mid_node.set_link_node(last_node)
print(mid_node.get_link_node().get_value())

print(last_node.get_link_node())