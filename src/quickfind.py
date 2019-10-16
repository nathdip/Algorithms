import numpy as np 

class QuickFind(object):
    """
    Initializes an unconnected object
    """
    def __init__(self, obj_size=10):
        self.obj_size = obj_size
        self.obj = [x for x in range(self.obj_size)]    
    
    def boolean_connected(self, p, q):
        """
        Check if p and q are connected
        """
        return self.obj[p]==self.obj[q]
    def union(self, p, q):
        """
        Change all indices connected to index p with value corresponding
        index q 
        """
        pid = self.obj[p]
        qid = self.obj[q]

        for i in range(self.obj_size):
            if self.obj[i]==pid:
                self.obj[i] = qid
    def get_object(self):
        return self.obj

class QuickUnion(object):
    """
    Initializes an unconnected object.
    Connected Objects are represented as trees
    """
    def __init__(self, obj_size=10):
        self.obj_size = obj_size
        self.obj = [x for x in range(self.obj_size)]   

    def __get_root(self, p):
        """
        Get the root of the id
        """
        while p!=self.obj[p]:
            p = self.obj[p]
        return p

    def boolean_connected(self, p, q):
        """
        Check if p and q have the same root
        """
        return self.__get_root(p)==self.__get_root(q)
    
    def union(self, p, q):
        """
        Change root of p to point to root of q
        """
        p_root = self.__get_root(p)
        q_root = self.__get_root(q)
        self.obj[p_root] = q_root
    def get_obj(self):
        return self.obj

class WeightedQuickUnion(object):
    """
    Initializes an unconnected object.
    Connected Objects are represented as trees
    Each connected object is connected to a root w
    """
    def __init__(self, obj_size=10):
        self.obj_size = obj_size
        self.obj = [x for x in range(self.obj_size)]   
        self.size = [1 for x in range(self.obj_size)]#size of the root

    def __get_root(self, p):
        """
        Get the root of the id
        """
        while p!=self.obj[p]:
            p = self.obj[p]
        return p

    def boolean_connected(self, p, q):
        """
        Check if p and q have the same root
        """
        return self.__get_root(p)==self.__get_root(q)
    
    def union(self, p, q):
        """
        Change root of p to point to root of q
        """
        p_root = self.__get_root(p)
        q_root = self.__get_root(q)
        if self.size[p_root] == self.size[q_root]:
            self.obj[p_root] = q_root
            self.size[q_root]+=self.size[p_root]
        elif self.size[p_root] > self.size[q_root]:
            self.obj[q_root] = p_root
            self.size[p_root]+=self.size[q_root]
        elif self.size[p_root] < self.size[q_root]:
            self.obj[p_root] = q_root
            self.size[q_root]+=self.size[p_root]
    def get_obj(self):
        return self.obj, self.size

if __name__=="__main__":
    connected = QuickFind()

    connected.boolean_connected(2,3)