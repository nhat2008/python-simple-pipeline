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


def get_city_from_persion(person):
    basic_information = person.get('basic_information')
    if basic_information:
        address = basic_information.get('address')
        if address:
            street = address.get('street')
            if street:
                return street
    return None

if __name__ == '__main__':
    value = get_city_from_persion(person)
    print value