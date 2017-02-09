import patient_class_def as pcd
import json
import random
import string

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

address_obj = json.loads(open("address-data.json", "r").read())
patient_identifer_obj = json.loads(open("patient-identifier-data.json", "r").read())

def rand_pid(pid_json):
	result = {}
	for key in pid_json.keys():
		if key == "identifier":
			id_len = pid_json[key][random.randrange(len(pid_json[key]))]
			if id_len != "N/P":
				result[key] = id_generator(int(id_len), string.ascii_uppercase + string.digits + string.ascii_lowercase)
			else:
				result[key] = "N/P"
		else:
			result[key] = pid_json[key][random.randrange(len(pid_json[key]))]
	return result


def id_generator(size, chars):
	return ''.join(random.choice(chars) for _ in range(size))

def rand_addr(addr_json):
	result = {}
	for key in addr_json.keys():
		if isinstance(addr_json[key], dict):
			result[key] = rand_bfs(addr_json[key], [])
		else:
			result[key] = addr_json[key][random.randrange(len(addr_json[key]))]
		#Randomise country by removing it sometimes
		if (random.randrange(3)) == 1:
			result["country"][0] = "N/P"
	return pcd.address(result["address_type"], result["street"], result["country"][2], result["country"][1], result["country"][0])

