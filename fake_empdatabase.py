from random import *
alphabets = 'abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRST'
digit = '1234567890'
cities = ['Hydrabad', 'Chennai', 'Banglore', 'Pune', 'Delhi', 'Mumbai']
designations = ['Software Engineer', 'Senior Software Engineer',
                'Team Leader', 'project leader', 'Project Manager']


def gen_name():
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name = name+choice(alphabets)
    return name


def gen_num():
    eno = 'e-'
    for i in range(4):
        eno = eno+choice(digit)
    return eno


def emp_sal():
    for i in range(5):
        sal = float(uniform(10000, 50000))
    return sal


def emp_city():
    city = choice(cities)
    return city


def emp_num():
    emno = choice('6789')
    for i in range(2, 11):
        emno = emno+choice(digit)
    return emno


def emp_desi():
    desi = choice(designations)
    return desi


def get_fake_emp_data():

    print("The name of the Employee: ", gen_name())
    print("The number of the Employee: ", gen_num())
    print("City of the Employee: ", emp_city())
    print("Designation of the Employee: ", emp_desi())
    print("Salary of the Employee:{:.2f} ".format(emp_sal()))
    print("The phone number of the Employee: ", emp_num())
    print('\n')


for i in range(5):
    get_fake_emp_data()
