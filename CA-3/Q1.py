import sys
import functools

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MainEmu():
    def __init__(self):
        self.items = dict()

    def start_program(self):
        for line in sys.stdin:
            line = Utils.delete_end_char(line)
            action, line = Utils.parse_line(line)
            actionPointer = Utils.get_attribute_pointer(self, action)
            actionPointer(line)

    def make(self, line):
        itemType, line = Utils.parse_line(line)
        itemName, line = Utils.parse_line(line)
        self.items[itemName] = classDict[itemType]()

    def call(self, line):
        itemName, line = Utils.parse_line(line, '.')
        funcName, line = Utils.parse_line(line, '(')
        argsLine, line = Utils.parse_line(line, ')')
        args = Utils.get_args(argsLine)
        attribute = Utils.get_attribute_pointer(self.items[itemName],
                                                   funcName)

        Utils.run_function(attribute, args)

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class MinHeap:
    def __init__(self):
        self.list =[]
        self.number =0
    
    class Node:
        def __init__(self,val):
            self.val = val
            
    def bubble_up(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        
        if not self.number:
            raise Exception('empty')
        
        if index < 0 or index >= self.number:
            raise Exception('out of range index')
    
        while (index > 0):
            if (index-1)//2 >=0 and self.list[(index-1)//2].val > self.list[index].val:
                self.list[(index-1)//2].val,self.list[index].val=self.list[index].val,self.list[(index-1)//2].val
            else: break
            index =(index-1)//2

    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        
        if not self.number:
            raise Exception('empty')
        
        if index < 0 or index >= self.number:
            raise Exception('out of range index')


        minimum = index
        while (2*index < self.number):
            if 2*index+1 < self.number and self.list[minimum].val > self.list[2*index+1].val:
                minimum = 2*index+1
            if 2*index+2 < self.number and self.list[minimum].val > self.list[2*index+2].val:
                minimum = 2*index+2
            if minimum != index:
                self.list[minimum].val,self.list[index].val=self.list[index].val,self.list[minimum].val
                index = minimum
            else: break
    
    def heap_push(self, value):
        new = self.Node(value)
        self.list.append(new)
        self.number += 1
        self.bubble_up(self.number-1)
        
        
    def heap_pop(self):
        if not self.number:
            raise Exception('empty')
        
        popped = self.list[0].val
        self.list[0].val = self.list[self.number-1].val
        self.number -=1
        self.list.pop()
        if self.number:self.bubble_down(0)
        return popped

    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        
        if index < 0 or index >= self.number:
            raise Exception('out of range index')
        
        if not self.number:
            raise Exception('empty')

        if 2*index < self.number:
            minimum = 2 *  index + 1
            if self.list[2*index+1].val > self.list[2*index+2].val:
                 minimum = 2 * index + 2
        return minimum            

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)

class HuffmanTree:
    def __init__(self):
        self.nodes =[]
        self.totalcost = 0
        

    @fix_str_arg    
    def set_letters(self,*args):
        for i in args:
            new_node = self.Node(0)
            self.nodes.append(new_node)
        

    @fix_str_arg    
    def set_repetitions(self,*args):
        j = 0
        for i in args:
            self.nodes[j].repeats = i
            j+=1

    class Node:
        def __init__(self,repeats):
            self.repeats = repeats
            self.cost = ""
            self.left = None
            self.right = None
        
    def build_huffman_tree(self):
        while len(self.nodes) != 1:
            self.nodes.sort(key = lambda x:x.repeats)
            node1 = self.nodes.pop(0)
            node2 = self.nodes.pop(0)
            new_node = self.Node(node1.repeats+node2.repeats)
            new_node.left = node2
            node1.cost = '1'
            node2.cost = '0'
            new_node.right = node1
            self.nodes.append(new_node)
    
    def traverse_put(self, root,cost):
        if root == None:
            return
        cost = root.cost + cost
        self.traverse_put(root.left,cost)
        self.traverse_put(root.right,cost)
        if root.left == None and root.right == None:
            self.totalcost += root.repeats * len(cost)

    def get_huffman_code_cost(self):
        self.traverse_put(self.nodes[0],"")
        return self.totalcost
    

    @fix_str_arg
    def text_encoding(self, text):
        w_dict= dict()
        for i in range(len(text)):
            if text[i] in w_dict:
                w_dict[text[i]] +=1
            else:
                w_dict[text[i]] = 1
        for i in w_dict:
            new_node = self.Node(w_dict[i])
            self.nodes.append(new_node)
        self.build_huffman_tree()

@for_all_methods(fix_str_arg)
@for_all_methods(print_raised_exception)
class Bst() :
    def __init__(self):
        self.list = list()
        self.size = 0
    
    class Node:
        def __init__(self, _val, _right_child, _left_child, _parent):
            self.val = _val
            self.right_child = _right_child
            self.left_child = _left_child
            self.parent = _parent
    
    def insert(self,key):
        if(self.size == 0):
            self.list.append(self.Node(key, -1, -1, -1))
            self.size += 1
            return
        
        node = self.list[0]

        while(node != -1):
            parent = node
            if(key < node.val):
                node = node.left_child
            else:
                node = node.right_child
        new_node = self.Node(key, -1, -1, parent)
        if(key < parent.val):
            parent.left_child = new_node
        else:
            parent.right_child = new_node
        self.list.append(new_node)
        self.size += 1
        
    def inorder(self,key = 0):
        if(key == 0):
            key = self.list[0]
        if(key == -1):
            return
        self.inorder(key.left_child)
        print(key.val, end = ' ')
        self.inorder(key.right_child)

classDict = { "min_heap": MinHeap, "bst": Bst, "huffman_tree": HuffmanTree}
    
if __name__ == "__main__":
    mainEmu = MainEmu()
    mainEmu.start_program()