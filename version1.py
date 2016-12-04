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


 # Flatten out
def get_city_from_persion(person):
    return person.get('basic_information') or None

def get_address(basic_information):
    return basic_information.get('address') or None

def get_street(address):
    return address.get('street') or None

def get_street_from_person(person):
    return get_street(get_address(get_city_from_persion(person)))


if __name__ == '__main__':
    
    value = get_street_from_person(person)
    print value
