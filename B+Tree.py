import sys #take commandline file
import bisect #As a sorting tool

Max_Val=3

class btree_node:

	def __init__(self):

		self.values=[] # Values In The Node
		self.pointers=[] # Pointers In The Node
		self.leaf=True #Differentiate Leaf from Internal Node
		self.next=None #Leaf Node to Point To Next Node

	def splitnode(self):
		#Split Node On Overflow

		# Initialising new_pointer node
		new_node=btree_node()

		#splitting around middle element
		mid=int(len(self.values)/2)		
		mid_val=self.values[mid]

		# if Node to split is a leaf
		if(self.leaf == True):

            # Updating Parameters for both nodes
			new_node.leaf=True
			self.leaf = True

			new_node.values=self.values[mid:]
			self.values=self.values[:mid]

			new_node.pointers=self.pointers[mid:]
			self.pointers=self.pointers[:mid]

			new_node.next=self.next
			self.next = new_node

		else:

            # Updating Parameters for both nodes
			new_node.leaf=False
			self.leaf=False

			new_node.pointers=self.pointers[mid+1:]
			self.pointers=self.pointers[:mid+1]

			new_node.values=self.values[mid+1:]
			self.values=self.values[:mid]

		#returning middle val over which split and new split node 
		return [mid_val,new_node]


class b_tree(btree_node):

	# Initialize B_TREE with a root node
	def __init__(self):
		self.root = btree_node()
	
	def range(self,left,right):
        
		ans=0
		#largest node less than left
		start=self.start_node(left,self.root)

		while(start):

			count = 0
			if(len(start.values)==0):
				break

			for i in range(len(start.values)):
				if(left<=start.values[i]<=right):
					count+=1

			ans+=count

			if(start.values[len(start.values)-1]<=right):
				start=start.next
			else:
				break

		return ans



	def start_node(self,val,node):
		
		# Termination Condition
		if(node.leaf):
			return node

		for i in range(len(node.values)):
			# First Child
			if((val<=node.values[i]) and i==0):
				return self.start_node(val,node.pointers[0])
			#Last Child
			elif((val>node.values[i]) and i+1==len(node.values)):
				return self.start_node(val,node.pointers[i+1])
			# Intermediate Child 
			elif(val <= node.values[i+1] and node.values[i] <= val ):
				return self.start_node(val,node.pointers[i+1])

	def check_root(self,value):
		
		# Flag bool to check if split required
		flag,new_node=self.insert(value,self.root)
		
		if flag:
			new_root=btree_node()
			new_root.pointers=[self.root,new_node]
			new_root.values=[flag]
			new_root.leaf=False
			self.root = new_root



	def insert(self,value,node):
		# Returns value and node if node needs to get split

		if(node.leaf == True):
			# Tool to find location to add new value
			place = bisect.bisect(node.values,value)

			node.pointers.insert(place,value)
			node.values.insert(place,value)			

			#Check If Split Required
			if(len(node.values) > Max_Val):
				return node.splitnode()
			return [None,None]

		else:
			# Recursion For Non-Leaf To Reach Leaf
			for i in range(len(node.values)):
				# First Child
				if( value<node.values[i] and i==0):
					middle_val,new_pointer = self.insert(value,node.pointers[i])
				#Last Child
				elif((value>=node.values[i]) and (i+1==len(node.values))):
					middle_val,new_pointer = self.insert(value,node.pointers[-1])
				elif( (value<node.values[i+1]) and value>=node.values[i] ):
					# Case of Intermediate Value Lying In Range
					middle_val,new_pointer = self.insert(value,node.pointers[i+1])
				else:
					# Continue If the current val doesn't satisfy the range of val
					continue
				# Break if moves in a subnode and not else condition
				break

		# Recursively Splitting The Tree If Required
		if middle_val != None: #Value is returned only if split required else None

			place = bisect.bisect(node.values,middle_val)
			node.pointers.insert(place+1,new_pointer)
			node.values.insert(place,middle_val)
			
			if len(node.values) <= Max_Val:
				return [None,None]

			return node.splitnode()

		return [None,None]


if __name__=="__main__":

	if(len(sys.argv) != 2):
		print("CORRECT SYNTAX :- python3 q1.py inputFileName\n")
	else:

		# Initialize B+ tree
		bpt=b_tree()

		input_file=sys.argv[1]
		with open(input_file,'r') as f:
			for query in f:
				command = query.strip().split()
				if(command[0]=="INSERT"):
					bpt.check_root(int(command[1]))
				elif(command[0]=="FIND"):
					if(bpt.range(int(command[1]),int(command[1]))>0):
						print("YES")
					else:
						print("NO")
				elif(command[0]=="COUNT"):
					print(bpt.range(int(command[1]),int(command[1])))
				elif(command[0]=="RANGE"):
					print(bpt.range(int(command[1]),int(command[2])))
