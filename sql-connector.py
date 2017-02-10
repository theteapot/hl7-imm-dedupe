import test_data_gen as rand_data
import peewee
import random
from peewee import *


db = MySQLDatabase('python_test', user='python_test',passwd='password')

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Patient(BaseModel):
    patient_id = peewee.UUIDField()

class Address(BaseModel):
    patient_id = ForeignKeyField(Patient, related_name = 'patient_address')
    addr_type = peewee.CharField()
    country = peewee.CharField()
    state = peewee.CharField()
    street = peewee.TextField()

class Person_Identifier(BaseModel):
    patient_id = ForeignKeyField(Patient, related_name = 'patient_ident')
    assigning_authority = peewee.TextField()
    id_type = peewee.CharField()
    identifier = peewee.CharField()

# Try creating tables, if they already exist don't worry they'll add 
# anyway.
try:
    db.create_table(Patient)
    db.create_table(Address)
    db.create_table(Person_Identifier)
    
except:
    print('table exists')

""" Adding data to the tables """
for i in range(5):
    
    # make a patient and save it to db
    patient = Patient(patient_id = rand_data.id_generator(15))
    patient.save()
    
    # creating 0..* address for one patient_id
    for i in range(random.randrange(2)):
        rand_addr = rand_data.rand_addr(rand_data.address_obj)
        db_addr = Address(patient_id=patient, addr_type = rand_addr.address_type, country = rand_addr.country, state = rand_addr.state, street = rand_addr.street)
        db_addr.save()
    
    # creating 0..* person_identifier for one patient_id
    for i in range(random.randrange(3)):
        rand_pid = rand_data.rand_pid(rand_data.patient_identifier_obj)
        db_pid = Person_Identifier(patient_id=patient, assigning_authority = rand_pid.assigning_authority, id_type = rand_pid.id_type, identifier = rand_pid.identifier)
        db_pid.save()
   
db.close()
