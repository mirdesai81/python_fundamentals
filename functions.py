def describe_pet(type='dog',name='rocky'):
    '''
    Method with default value if not provided
    :param type:  type f pet
    :param name:  name of pet
    :return:  void
    '''
    print('I have a animal of type '+type)
    print('My animal name is '+name)


describe_pet('cat','puffy')
describe_pet(type='dog',name='rocky')
describe_pet(name='mini',type='cat')
describe_pet()


def get_formatted_name(first,last,middle=''):
    '''
    Returns full name along with middle as optional
    :param first: first name
    :param last: last name
    :param middle: optional middle name
    :return:
    '''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name

name = get_formatted_name('mihir','desai')
print(name)

def build_person(first,last,middle=''):
    '''
    Returns dictionary of person information
    :param first:
    :param last:
    :param middle:
    :return:
    '''
    person = {'fname' : first, 'lname' : last}
    if middle:
        person['middle'] = middle

    return person

info = build_person('mihir','desai','rohit')
for key,value in info.items():
    print(key+" : "+value)

print(info)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

def make_pizza(*toppings):
    for topping in toppings:
        print("- " + topping)


make_pizza('chicken','cheese','olives')

def print_items(items):
    for key,value in items.items():
        print(key + " : " + value)


def build_profile(fname,lname,**user_info):
    profile = {}
    profile['fname'] = fname
    profile['lname'] = lname
    for key,value in user_info.items():
        profile[key] = value

    return profile

user = build_profile('mihir','desai',city = 'san jose',field = 'IT')
print_items(user)
