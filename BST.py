#!/usr/bin/env python
# coding: utf-8

# In[13]:


class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        
    #insertion
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    #search
    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")
                
    #preorder
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    #INorder
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
            
    #postorder
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
        
    #delete
    def delete(self,data):
        if self.key is None:
            print("tree is empty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Node is not present in tree")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Node is not present in tree")
        else:
            #for 0 child or 1 child
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            #for 2 child
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
    
    #Minimum & maximum
    def min(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("minimum ",current.key)
        
    def max(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("maximum ",current.key)
            
            
        
        
                
root=BST(10)
list1=[2,34,1,55,7,8]
for i in list1:
    root.insert(i)


# In[4]:


root.search(34)


# In[7]:


root.search(50)


# In[10]:


print(root.lchild.key)


# In[7]:


root.preorder()


# In[8]:


root.inorder()


# In[9]:


root.postorder()


# In[11]:


root.delete(7)
root.postorder()


# In[12]:


root.delete(100)
root.postorder()


# In[14]:


root.min()
root.max()


# In[ ]:




