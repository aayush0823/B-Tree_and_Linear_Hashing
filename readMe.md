# B-TREE AND LINEAR HASHING

#PROGRAMMER
	AAYUSH GOEL

#Q1 B+ TREE
	* To run the python code enter:
		python3 q1.py inputFileName

	* The B+ Tree is implemented in which each node can max store 3 values stored in variable Max_Val at start of code

	* No output for Insert queries as given in sample

	* Find and Count queries are also implemented using Range query with Count(x) as Range(x,x) and Find checking the value of Range(x,x)

	* Range query is implemented by going to the leftmost leaf with the value in the range and then traversing the nodes and then subsequent leafs 

	* The complexity is nlogn as in any standard B+  tree

#Q2 LINEAR HASHING
	* To run the python code enter:
		python3 q2.py inputFileName

	* Linear Hashing is implemented in which each bucket can max store 40 values stored in variable Bucket_Size at start of code

	* No output for queries with number already present and no value is inserted

	* Count variable stores the number of values in the hash table and it's value along with the entire hash table can be seen by uncommenting the last 2 lines

	* The implemented Linear Hashing is unsupervised and a new bucket is inserted after any bucket overflows

	* It assumes that the size of all buckets is approximately same and when one bucket overflows other buckets will also overflow in near future.

## Thanks
