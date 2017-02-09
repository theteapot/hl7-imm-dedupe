import test_data_gen as rand_data
import peewee
from peewee import *


db = MySQLDatabase('python_test', user='python_test',passwd='password')

db.connect()

class Address(peewee.Model):
	addr_type = peewee.CharField()
	country = peewee.CharField()
	state = peewee.CharField()
	street = peewee.TextField()

	class Meta:
		database = db

class Patient_Identifier(peewee.Model):
	assigning_authority = peewee.TextField()
	id_type = peewee.TextField()
	identifier = peewee.TextField()
	
	class Meta:
		database = db
	
try:
	db.create_table(Address)
	db.create_table
except:
	print('table exists')

for i in range(5):
	rand_addr = rand_data.rand_addr(rand_data.address_obj)
	print(rand_addr)
	db_addr = Address(addr_type = rand_addr.address_type, country = rand_addr.country, state = rand_addr.state, street = rand_addr.street)
	db_addr.save()

for addr in Address:
    print(addr)
   
db.close()
