# coding: utf-8
import re
import json
from unidecode import *

def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
            

def read_json(filename: str = "json_data.json"):
    
    return json.load(open(filename, "rb"))
                        
def sep():
    print("====================\n")
    
    
def trimspaces(data):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    #return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), str(unidecode(json.dumps(data))))
    data_s=json.dumps(data)
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), data_s)


# Define a function that prompts the user to enter values for a given class
def prompt_for_instance(cls):
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)