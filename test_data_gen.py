import patient_class_def as pcd
import json
import random
import string

def rand_bfs(dict_obj):
    """Iterate through python-ed json structure
    args:
        dict_obj -- the object (probably json.loads(...)) to 
        iterate over. Assumes a structure of nested dictionaries.
    returns:
        list of the names of the random keys chosen at each level, and
        the random value chosen at the lowest level.
        e.g. [key1, key2, key3, value]
        
    """
    
    result = []
    nodes = dict_obj.keys()
    # if the python object you are at is a dictionary (nested) then you
    # are not at the lowest level of the json object (a python list) and
    # should continue
    if isinstance(dict_obj[nodes[0]], dict):
        rand_node = nodes[random.randrange(0, len(nodes))]
        result.append(rand_node)
        rand_bfs(dict_obj[rand_node])
        return result
    else:
        rand_node = nodes[random.randrange(0, len(nodes))]
        result.append(rand_node)
        rand_leaf = dict_obj[rand_node][random.randrange(len(dict_obj[rand_node]))]
        result.append(rand_leaf)
        return result

address_obj = json.loads(open("address-data.json", "r").read())
patient_identifier_obj = json.loads(open("patient-identifier-data.json", "r").read())

def rand_pid(pid_json):
    """Generates a random person_identifier in HL7 format given dict
    args:
        pid_json: a python-ed json file, e.g. json.loads(file_obj) with
        data relevant to HL7 person_identifiers.
    returns:
        person_identifier object (defined by patient_class_def.py) with
        random values taken from pid_json.  
            
    """
    
    result = {}
    for key in pid_json.keys():
        # The 'identifier' should be randomly generated??
        # Maybe I should use a big dict so there are overlaps??
        if key == "identifier":
            id_len = pid_json[key][random.randrange(len(pid_json[key]))]
            if id_len != "N/P":
                result[key] = id_generator(int(id_len))
            else:
                result[key] = "N/P"
        else:
            result[key] = pid_json[key][random.randrange(len(pid_json[key]))]
    return pcd.person_identifier(result["assigning_authority"], result["id_type"], result["identifier"])


def id_generator(size):
    """Generates random string of upper/lowercase/digits of len size
    """
    
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def rand_addr(addr_json):
    """Generates a random address in HL7 format given dict
    args:
        addr_json: a python-ed json file, e.g. json.loads(file_obj)
        with data relevant to HL7 address.
    returns:
        address object (defined by patient_class_def.py) with
        random values taken from addr_json.  
            
    """
    
    result = {}
    for key in addr_json.keys():
        if isinstance(addr_json[key], dict):
            result[key] = rand_bfs(addr_json[key])
        else:
            result[key] = addr_json[key][random.randrange(len(addr_json[key]))]
        #Randomise country by removing it sometimes
        if (random.randrange(3)) == 1:
            result["country"][0] = "N/P"
    return pcd.address(result["address_type"], result["street"], result["country"][2], result["country"][1], result["country"][0])
