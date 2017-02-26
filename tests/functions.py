def get_information_from_persion(person):
    return person.get('basic_information') or None


def get_address(basic_information):
    return basic_information.get('address') or None


def get_street(address):
    return address.get('street') or None

