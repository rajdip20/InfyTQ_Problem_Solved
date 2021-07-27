'''  Care hospital wants to know the medical speciality visited by the maximum number of
    patients. Assume that the patient id of the patient along with the medical speciality visited by
    the patient is stored in a list. The details of the medical specialities are stored in a dictionary as
    follows:
    {
        "P":"Pediatrics",
        "O":"Orthopedics",
        "E":"ENT"
    }

    Write a function to find the medical speciality visited by the maximum number of patients and
    return the name of the speciality.
    
    Note:
        1. Assume that there is always only one medical speciality which is visited by maximum
        number of patients.
        2. Perform case sensitive string comparison wherever necessary.

        Sample Input                                            Expected Output
    [101,P,102,O,302,P,305,P]                                     Pediatrics
    [101,O,102,O,302,P,305,E,401,O,656,O]                         Orthopedics
    [101,O,102,E,302,P,305,P,401,E,656,O,987,E]                      ENT

'''

def max_patient_speciality(inp):
    speciality_dict = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
    count_dict = {"P": 0,"O": 0,"E": 0}
    for i in range(0, len(inp), 2):
        count_dict[inp[i + 1]] = count_dict[inp[i + 1]] + 1
    m_s = 'P'
    m_v = 0

    for s,v in count_dict.items():
        if v>m_v:
            m_v = v
            m_s = s
    return speciality_dict[m_s]


inp = [101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E']
print(max_patient_speciality(inp))
