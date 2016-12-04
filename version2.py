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


#  Inspire from Monad's style
class Perhaps(object):
    def __init__(self, value):
        self.value = value

    def bind(self, fn):
        if self.value is None:
            return self
        return fn(self.value)

    def get_value(self):
        return self.value


def get_information(person):
    return Perhaps(person.get('basic_information') or None)

def get_address(basic_information):
    return Perhaps(basic_information.get('address') or None)

def get_street(address):
    return Perhaps(address.get('street') or None)

def get_street_from_person(person):
    return (Perhaps(person)
        .bind(get_information)
        .bind(get_address)
        .bind(get_street)
        .get_value())

if __name__ == '__main__':
    
    value = get_street_from_person(person)
    print value
