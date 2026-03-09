class Node:  
  def __init__(self, data):  
    self.data = data  
    self.next = None  
  
class LinkedList:  
      
  def __init__(self):  
    self.head = None  
    
  def push(self, new_data):  
      new_node = Node(new_data)  
      new_node.next = self.head  
      self.head = new_node  
      print("Node inserted! Next?")  
  
  def append(self, new_data):  
      new_node = Node(new_data)  
        
      if self.head is None:  
          self.head = new_node  
          print("Welcome to the list, new node!")  
          return  
  
      last = self.head  
      while (last.next):  
          last = last.next  
        
      last.next = new_node  
      print("Node Appeneded")  
  
  def insert_after(self, prev_node_data, new_data):  
    prev_node = self.head  
      
    while prev_node:  
        if prev_node.data == prev_node_data:  
            break  
        prev_node = prev_node.next  
    else:  
        print("Node not found in the list.")  
        return  
  
    new_node = Node(new_data)  
    new_node.next = prev_node.next  
    prev_node.next = new_node  
    print("Node inserted")  
  
  def delete_head(self):  
      if self.head is None:  
          print("Nothing to delete, List is Empty ")  
          return  
  
      temp = self.head  
      self.head = self.head.next  
      temp = None  
      print("Head removed!")  
  
  def delete_tail(self):  
      if self.head is None:  
          print("Lists is Empty! Nothing to Delete.")  
          return  
  
      if self.head.next is None:  
          self.head = None  
          print("Tail Removed from the List!")  
          return  
            
      temp = self.head  
      while temp.next.next:  
          temp = temp.next  
            
      tail = temp.next  
      temp.next = None  
      tail = None  
      print("Tail Node Is Updated")  
  
  def delete_node(self, key):  
      if self.head is None:  
          print("No Node with Value Found!!")  
          return  
  
      if self.head.data == key:  
          self.head = self.head.next  
          print("Target node eliminated from the head!")  
          return  
  
      temp = self.head  
      while temp.next:  
          if temp.next.data == key:  
              break  
          temp = temp.next  
  
      if temp.next is None:  
          print("Node not Found")  
      else:  
          prev = temp.next  
          temp.next = prev.next  
          prev = None  
          print("Node Deleted Succesfully. ")  
            
  def traverse(self):  
      temp = self.head  
      if temp is None:  
          print("This list is...empty. ")  
      else:  
          print("Data in the list:")  
          while temp:  
              print(temp.data, end=" ")  
              temp = temp.next  
          print()  
            
  def search(self, key):  
      temp = self.head  
      index = 0  
      while temp:  
          if temp.data == key:  
              print(f"There it is! Your data is at node {index}")  
              return  
          temp = temp.next  
          index += 1  
      print("Data Not Found.")  
  
llist = LinkedList()  
while True:  
    print("1. Push")   
    print("2. Append")  
    print("3. Insert After")  
    print("4. Delete Head")  
    print("5. Delete Tail")  
    print("6. Delete By Value")  
    print("7. Traverse")  
    print("8. Search")  
    print("0. Exit")  
      
    choice = int(input("Your move: "))  
      
    if choice == 1:  
        data = int(input("Enter the data for the node to push: "))  
        llist.push(data)  
          
    elif choice == 2:  
        data = int(input("Enter the data for the node to append: "))  
        llist.append(data)  
          
    elif choice == 3:  
        data = int(input("Enter the node data to insert after: "))  
        item = int(input("Enter the data for the new node: "))  
        llist.insert_after( data, item)  
          
    elif choice == 4:  
        llist.delete_head()  
          
    elif choice == 5:  
        llist.delete_tail()  
          
    elif choice == 6:  
        data = int(input("Enter the node data to delete: "))  
        llist.delete_node(data)  
          
    elif choice == 7:  
        llist.traverse()  
          
    elif choice == 8:  
        data = int(input("Enter the data to search: "))  
        llist.search(data)  
          
    elif choice == 0:  
        break  
          
    else:  
        print("Invalid choice, try again rangerrrr!")  
