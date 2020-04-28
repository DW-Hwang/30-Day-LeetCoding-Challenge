"""
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key 
if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
*.*.*.*.*.*

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

	def __init__(self, capacity):
		self.capacity = capacity
		self.table = {}
		self.head = Node(-1, -1)
		self.tail = Node(-1, -1)
		self.head.next = self.tail
		self.tail.prev = self.head


	def get(self, key):
		if key in self.table:
			node = self.table[key]
			self.delete(node)
			self.put_to_first(node.key, node.value)
			return node.value
		return -1


	def put(self, key, value):
		# for available capacity and key in table
		if key in self.table:
			node = self.table[key]
			self.delete(node)

		# for full capacity and key not in table
		elif len(self.table) >= self.capacity:
			self.delete(self.tail.prev)

		self.put_to_first(key, value)


	def put_to_first(self, key, value):
		# make node
		node = Node(key, value)
		self.table[key] = node
		node.next, node.prev = self.head.next, self.head
		# update linked list
		self.head.next.prev, self.head.next = node, node
			

	def delete(self, node):
		node.prev.next, node.next.prev = node.next, node.prev
		self.table.pop(node.key)


class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None


if __name__ == "__main__":
	cache = LRUCache(2)
	print 'make cache with capacity 2 :: LRUCache(2)'
	print 'put(1, 1) in cache :: cache.put(1, 1)', cache.put(1, 1)
	print 'put(2, 2) in cache :: cache.put(2, 2)', cache.put(2, 2)
	print 'get (1) in cache :: cache.get(1)', cache.get(1)
	print 'put (3, 3) in cache :: cache.put(3, 3)', cache.put(3, 3)
	print 'get (2) in cache :: cache.get(2)', cache.get(2)
	print 'put(4, 4) in cache :: cache.put(4, 4)', cache.put(4, 4)
	print 'get (1) in cache :: cache.get(1)', cache.get(1)
	print 'get (3) in cache :: cache.get(3)', cache.get(3)
	print 'get (4) in cache :: cache.get(4)', cache.get(4)



    
