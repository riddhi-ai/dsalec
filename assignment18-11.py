class node:
    def __init__(self,p_id,name,priority):  #(self,data,priority)
        self.p_id=p_id                      #self.data=data
        self.name=name
        self.priority=priority
        self.next=None



class PriorityQueue():
    def __init__(self):
        self.front=None
        self.total=0

    def enqueue(self,p_id,name,priority):
        if priority not in (1,2,3,4):
            print("Enter a priority from 1 to 4 for CPU Scheduling as priority is invalid")
            return

        new_node= node(p_id,name,priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front          
            self.front = new_node             
        else:                                    
            temp = self.front    

            while temp.next and temp.next.priority <= priority:
                temp = temp.next                

            new_node.next = temp.next          
            temp.next = new_node  

        self.total +=1          #to count

    def dequeue(self):
        if self.front is None:
            print("No pending processes")
            return

        temp = self.front                 
        self.front = temp.next               
        self.total -= 1                      
        print("Executing the process:", temp.p_id, temp.name)  


    def display_next(self):                  
         if self.front is None:              
            print("No pending processes.")  
            return                          

         temp = self.front                 
         print("Next:", temp.p_id, temp.name, " Priority:", temp.priority)

    def display_all(self):                  
            if self.front is None:               
                print("No pending processes")   
            return                           

            temp = self.front                   
            while temp:                          
                print(temp.pid, temp.name, " Priority:", temp.priority)  
                temp = temp.next    


    def count(self):                       
            print("Pending processes:", self.total)  

pq = PriorityQueue()                     
pq.enqueue(101, "Backup", 3)            
pq.enqueue(102, "Keyboard input", 2)     
pq.enqueue(103, "System update", 1)      
pq.enqueue(104, "Cleanup", 4)       

pq.display_all()                        
pq.display_next()                       
pq.dequeue()                            
pq.count()                             
        