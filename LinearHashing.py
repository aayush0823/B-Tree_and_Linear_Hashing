import sys
import math

Bucket_Size = 40

class Hash:
	def __init__(self,num_buckets):
		self.hash_table = []
		#Initialising number of buckets
		for i in range(num_buckets):
			self.hash_table.append([])
		self.buckets = num_buckets
		self.bits = math.ceil(math.log(self.buckets))
		self.point = 0 #Point the bucket to split

	def find(self,value):
		# Finding Bucket where value may be present
		bucket = value%(2**self.bits)
		# If bucket num is over the total buckets so consider one less bit
		if(bucket >= self.buckets):
			bucket = value%(2**(self.bits-1))

		for key in self.hash_table[bucket]:
			if(key==value):
				return True
		return False

	def insert(self,value):
		# Finding Bucket where value may be present
		bucket = value%(2**self.bits)
		# If bucket num is over the total buckets so consider one less bit
		if(bucket >= self.buckets):
			bucket = value%(2**(self.bits-1))

		self.hash_table[bucket].append(value)

		# If Bucket Overflows
		if(len(self.hash_table[bucket]) > Bucket_Size):
			self.buckets+=1
			self.hash_table.append([])
			self.bits = math.ceil(math.log(self.buckets,2))
			copy = self.hash_table[self.point].copy()
			# print(self.hash_table)
			self.hash_table[self.point].clear()
			# print(self.hash_table)
			# print(self.bits)
			# print(copy)
			for i in copy:
				bucket = i%(2**self.bits)
				self.hash_table[bucket].append(i)
			if(2**self.bits == self.buckets):
				self.point = 0
			else:
				self.point += 1
		print(value)


if __name__=="__main__":

	count = 0;	
	if(len(sys.argv) != 2):
		print("CORRECT SYNTAX :- python3 q1.py inputFileName\n")
	else:
		# Initialize Hash Table
		linear=Hash(2)
		
		input_file=sys.argv[1]
		with open(input_file,'r') as f:
			for query in f:
				command = query.strip().split()
				if (linear.find(int(command[0])) == True):
					continue
				else:
					linear.insert(int(command[0]))
					count +=1;
	# print(count)
	# print(linear.hash_table)
