# coding: utf-8
import re
import json
from unidecode import *
import treelib

def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
            

def read_json(filename: str = "json_data.json"):
    
    return json.load(open(filename, "rb"))
                        
def sep():
    print("====================")
    
    
def trimspaces(data):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    #return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), str(unidecode(json.dumps(data))))
    data_s=json.dumps(data)
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), data_s)

# Define the prompt_for_instance function that takes a class name as a string as input
def prompt_for_instance(cls):
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)


def print_list(list):
     for item in list:
        print(item)

class TreeExt(treelib.Tree):
    def __init__(self):
        super().__init__()
    
    """def get_terminal_nodes(self):
        terminal_nodes = []
        for node in self.all_nodes():
            if not self.children(node.identifier):
                terminal_nodes.append(node.identifier)
        return terminal_nodes"""
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

    