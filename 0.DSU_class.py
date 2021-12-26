
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: ZhujingZhe 


""" -------------------------- Implementation of parallel search set ---------------------------------


      Join query set is a typical tree data structure, which is used to deal with some non intersecting 
  merging and query problems. A set sum is represented by an element in the set, which is called a set
  The representative yuan of the contract; 

        All elements in a set are organized into a tree structure with the representative element as the
    root. In this way, to judge whether the two elements belong to the same set, you only need to judge 
    whether the representative elements of the two elements belong to the same set Equal, merging two 
    disjoint sets only needs to change the representative element.

class UnionFindSet(object):

    * Dictionary parent: for each element x, parent [x] is the parent node of X in the tree structure. 
      If x is the root node, make parent [x] = X;

    * Dictionary rank: rank [x] is the height of the element in the current tree structure (from 
      bottom to top) int set_ Counts: count the number of sets in the query set
    
def find(self, d):

    * For the search function, assuming that it is necessary to determine the representative elements 
      of the set, it can move upward in the tree structure along the parent [x] until it reaches the root 
      node;

    * Path compression: in order to speed up the search, the parent node of the child node is changed to
      the root node in the process of finding the root node
    
def union(self, a, b):

    * For the merge function, assuming that the representative elements of the two sets to be merged 
      are x and Y respectively, only parent [x] = y or parent [y] = x is required, and rank can be 
      used during the period To determine which one to use;

    * After merging two sets, check the number of sets in the set_ count -= 1
    
"""

class UnionFindSet(object):

    def __init__(self, data_list: list[int]) -> None:
      
        self.parent = {}
        self.rank = {}
        
        # Judge and check the total number of sets in the set. Initialization is independent by default
        
        self.set_count = len(data_list)  
        
        # Initialize parent dictionary and rank dictionary
        
        for d in data_list:
          
            # The parent node of the initialization node is itself
            self.parent[d] = d  
            
            # Initialize the rank of each node to 1
            self.rank[d] = 1    

    def find(self, d: int) -> int:
      
        # Use path compression to find the root node
        # Path compression: when finding the parent node, move the current node under the parent node
        father = self.parent[d]
        if d != father:
            father = self.find(father)
        self.parent[d] = father
        return father

    # Check whether the two nodes are in a collection
    
    def is_same_set(self, a: dict, b: dict) -> bool:
        return self.find(a) == self.find(b)

    # Define a function to merge two sets
    
    def union(self, a: dict, b:dict) -> None:

        # If a set is empty, we don't need to do anything
        
        if not a or not b:
            return
          
        a_head = self.find(a)
        b_head = self.find(b)

        if a_head != b_head:
          
            a_rank = self.rank[a_head]
            b_rank = self.rank[b_head]
            
            if a_rank >= b_rank:
              
                self.parent[b_head] = a_head
                if a_rank == b_rank:
                    self.rank[a_rank] += 1
            else:
                self.parent[a_head] = b_head

        self.set_count -= 1


"""------------------------------------ main(some tests) --------------------------------------"""

if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    
    ufs = UnionFindSet(a)
    
    ufs.union(1, 2)
    
    print(ufs.set_count)
    print(ufs.is_same_set(2, 5))  # True
    print(ufs.parent)
    print(ufs.rank)


# from collections import defaultdict

# dicts = defaultdict(list)
# for i in range(1, len(u.parent) + 1):
#     dicts[u.parent[i]].append(i)
# max_res = 0
# for i in range(1, len(dicts) + 1):
#     max_res = max(max_res, len(dicts[i]))
# print(max_res)
