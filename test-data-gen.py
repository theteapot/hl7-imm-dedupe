import patient_class_def as pcd
import json
import random

resp_pers = pcd.responsible_person("Dad", "John Hope")
school = pcd.school("2008-04-17", "2009-11-17", "9", "Orewa College")
pers_name = pcd.person_name("Taylor", "Kettle", "David", "Mr", "Fullname")
pers_ident = pcd.person_identifier("Red Beach Dental", "PC760A8D", "tket350")
addr = pcd.address("Home", "295c Wainui rd", "Hibiscus Coast", "Auckland", "New Zealand")
persn = pcd.person("1995-04-17", "Male", "English", "3", "Healthy", "Sawyer", "New Zealand", "N/A", "NZ European", "1", "Student", "NZ European", addr, pers_name, pers_ident, school, resp_pers)

address_obj = json.loads(open("address-data.json", "r").read())

def rand_bfs(dict_obj, result):
	nodes = dict_obj.keys()
	if isinstance(dict_obj[nodes[0]], dict):
		rand_node = nodes[random.randrange(0, len(nodes))]
		result.append(rand_node)
		rand_bfs(dict_obj[rand_node], result)
		return result
	else:
		rand_node = nodes[random.randrange(0, len(nodes))]
		result.append(rand_node)
		rand_leaf = dict_obj[rand_node][random.randrange(len(dict_obj[rand_node]))]
		result.append(rand_leaf)
		return result

def rand_addr(addr_json):
	result = {}
	for key in addr_json.keys():
		if isinstance(addr_json[key], dict):
			result[key] = rand_bfs(addr_json[key], [])
		else:
			result[key] = addr_json[key][random.randrange(len(addr_json[key]))]
	return pcd.address(result["address_type"], result["street"], result["country"][2], result["country"][1], result["country"][0])
			

print rand_addr(address_obj)
			


	
	

