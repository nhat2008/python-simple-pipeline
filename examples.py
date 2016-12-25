from pipeline.pipeline import Pipe

person = {
    'basic_information':
        {
            'name': 'Nguyen Minh Nhat',
            'year': '1900',
            'address': {
                'city': 'Ho Chi Minh',
                'ward': '6',
                'distrist': 'Tan Binh',
                'street': 'Nghia Phat Street'
            }
        }
}


def get_information_from_persion(person):
    return person.get('basic_information') or None


def get_address(basic_information):
    return basic_information.get('address') or None


def get_street(address):
    return address.get('street') or None


def test():
    pass


if __name__ == '__main__':
    pipe_adress = Pipe(get_information_from_persion, get_address, get_street)
    value = pipe_adress(person)
    print value

    pipe_adress = Pipe(get_information_from_persion, get_address, get_street, test)
    value = pipe_adress(person)
    print value

