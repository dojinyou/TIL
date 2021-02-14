# https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline

class Tree :
	class Node:
		def __init__(self,value,left=None,right=None):
			self.value = value
			self.left = left
			self.right = right

	def __init__(self):
		self.root = None
		self.dic = {}

	def add(self, value, left, right):
		if self.root != None :
			parent = self.dic[value]
		else :
			parent = self.Node(value)
			self.root = parent
			self.dic[value] = parent

		if left != '.':
			leftNode = self.Node(left)
			parent.left = leftNode
			self.dic[left] = leftNode
			
		if right != '.':
			rightNode = self.Node(right)
			parent.right = rightNode
			self.dic[right] = rightNode

	def preorder(self,node=None):
		if node == None :
			node = self.root
		print(node.value,end='')
		if node.left != None :
			self.preorder(node.left)
		if node.right != None :
			self.preorder(node.right)

	def inorder(self,node=None):
		if node == None :
			node = self.root
		if node.left != None :
			self.inorder(node.left)
		print(node.value,end='')
		if node.right != None :
			self.inorder(node.right)

	def postorder(self,node=None):
		if node == None :
			node = self.root
		if node.left != None :
			self.postorder(node.left)
		if node.right != None :
			self.postorder(node.right)
		print(node.value,end='')

n = int(input())
tree = Tree()

for _ in range(n):
	root, left, right = input().split()
	tree.add(root,left,right)

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()

# # list로 tree 구현
# # 메모리 초과로 에러
# def preorder(nodeIndex):
# 	print(tree[nodeIndex],end='')
# 	if tree[2*nodeIndex+1] :
# 		preorder(2*nodeIndex+1)
# 	if tree[2*nodeIndex+2] :
# 		preorder(2*nodeIndex+2)
# def inorder(nodeIndex):
# 	if tree[2*nodeIndex+1] :
# 		inorder(2*nodeIndex+1)
# 	print(tree[nodeIndex],end='')
# 	if tree[2*nodeIndex+2] :
# 		inorder(2*nodeIndex+2)
# def postorder(nodeIndex):
# 	if tree[2*nodeIndex+1] :
# 		postorder(2*nodeIndex+1)
# 	if tree[2*nodeIndex+2] :
# 		postorder(2*nodeIndex+2)
# 	print(tree[nodeIndex],end='')

# n = int(input())
# tree = [0]*(2**n-1)

# for _ in range(n):
# 	root, left, right = input().split()
# 	if root == 'A' :
# 		tree[0] = root
# 		if left != '.':
# 			tree[1] = left
# 		if right != '.':
# 			tree[2] = right
# 	else :
# 		rootIndex = tree.index(root)
# 		if left != '.':
# 			tree[2*rootIndex+1] = left
# 		if right != '.':
# 			tree[2*rootIndex+2] = right

# preorder(0)
# print()
# inorder(0)
# print()
# postorder(0)