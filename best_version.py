person = {
    'basic_information':
    {
        'name': 'Nguyen Minh Nhat',
        'year' : '1900',
        'address' : {
            'city' : 'Ho Chi Minh',
            'ward' : '6',
            'distrist': 'Tan Binh',
            'street': 'Nghia Phat Street'
        }
    }
}
# Monads ways
def bind(value, function): 
    if value:
        return function(value)
    else:
        None

def data_pipe(value, functions):
    c_value = value
    for function in functions:
        c_value = bind(c_value, function)
    return c_value

 # Flatten out
def get_information_from_persion(person):
    return person.get('basic_information') or None

def get_address(basic_information):
    return basic_information.get('address') or None

def get_street(address):
    return address.get('street') or None


if __name__ == '__main__':
    value = data_pipe(person , [get_information_from_persion, get_address, get_street])
    print value


