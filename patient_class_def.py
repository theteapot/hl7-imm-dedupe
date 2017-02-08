class patient:
    def __init__(self, person, pat_cond, org_rl, rsp_prsrn, imm_his):
        self.person = person
        self.patient_conditions = pat_cont
        self.org_relationship = org_rl
        self.responsible_person = rsp_prsn
        self.immunization_his = imm_his

class person:
    def __init__(self, dob, gender, lang, birth_ord, birth_st, mom_maiden_name, birth_cntry, death_dt, ethn, mult_birth, occptn, race, addr_obj, prsn_name_obj, prsn_ident_obj, school_obj, rsp_prsn_obj):
        self.date_of_birth = dob
        self.gender = gender
        self.primary_language = lang
        self.birth_order = birth_ord
        self.birth_state = birth_st
        self.mothers_maiden_name = mom_maiden_name
        self.birth_country = birth_cntry
        self.death_date = death_dt
        self.ethnicity = ethn
        self.mult_birth = mult_birth
        self.occupation = occptn
        self.race = race
        #class objects
        
        self.address = addr_obj
        self.person_name = prsn_name_obj
        self.person_identifier = prsn_ident_obj
        self.school = school_obj
        self.responsible_person = rsp_prsn_obj

class address:
    """Specifies a persons address in HL7
        address-type -- string: home/work etc.
        street -- string: street name (in full) and number (e.g. '25 Bay Road')
        city -- string: the closest city
        state -- string: the state/territory/region of residence
        country -- string: the country of residence
    """
    
    def __init__(self, addr_type, street, city, state, country):
        self.address_type = addr_type
        self.street = street
        self.city = city
        self.state = state
        self.country = country
    
    def __repr__(self):
        print_string = "Address Type: {0}\nStreet: {1}\nCity: {2}\nState: {3}\nCountry: {4}".format(self.address_type, self.street, self.city, self.state, self.country)
        return print_string

class person_identifier:
    def __init__(self, ass_auth, id_type, ident):
        self.assigning_authority = ass_auth
        self.id_type = id_type
        self.identifier = ident

class person_name:
    def __init__(self, given_name, last_name, midd_name, name_suff, name_type):
        self.given_name = given_name
        self.last_name = last_name
        self.middle_name = midd_name
        self.name_suffix = name_suff
        self.name_type = name_type

class school:
    def __init__(self, dept_date, enrll_date, grade, name):
        self.depart_date = dept_date
        self.enroll_date = enrll_date
        self.grade = grade
        self.school_name = name

class responsible_person:
    def __init__(self, relationship, person):
        self.relationship = relationship
        self.person = person
