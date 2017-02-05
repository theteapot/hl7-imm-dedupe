import patient_class_def as pcd

resp_pers = pcd.responsible_person("Dad", "John Hope")
school = pcd.school("2008-04-17", "2009-11-17", "9", "Orewa College")
pers_name = pcd.person_name("Taylor", "Kettle", "David", "Mr", "Fullname")
pers_ident = pcd.person_identifier("Red Beach Dental", "PC760A8D", "tket350")
addr = pcd.address("Home", "295c Wainui rd", "Hibiscus Coast", "Auckland", "New Zealand")
persn = pcd.person("1995-04-17", "Male", "English", "3", "Healthy", "Sawyer", "New Zealand", "N/A", "NZ European", "1", "Student", "NZ European", addr, pers_name, pers_ident, school, resp_pers)

print(persn)

