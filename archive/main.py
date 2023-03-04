# coding: utf-8

import json
from unidecode import unidecode
from classes.product_classes import *
import generator
import utils

def main():
    
    #########
    utils.sep()
   
    json_data= generator.read_json("json_data.json")
    json_data = generator.trimspaces(json_data)

    json_dict = json.loads(str(unidecode(json_data)))

    utils.sep()
    
    #########
    
    class_tree = generator.generate_tree_hierarchy(json_dict)
    
    product_classes = class_tree.get_penultimate_nodes()
  
    class_tree.show()

    utils.sep()

    utils.print_list(product_classes)

    
    # Get the immediate children nodes of node 'B'
    children_nodes = class_tree.get_children_nodes('Meubles')
    utils.print_list(children_nodes)

    #########
    
    #class_hierarchy_code = generator.generate_class_hierarchy(json_dict)

    utils.sep()

    #########

    #generator.write_content(class_hierarchy_code, "product_classes.py")

    #########

    #print(class_hierarchy_code)
                             

if __name__ == '__main__':

    
    main()

    #new_product = utils.prompt_for_instance(Product)

