# enums

# Encapsulation "what varies from what stays the same"
class GuitarSpec:

    def __init__(self, builder=None, model=None, type=None, back_wood=None, top_wood=None, numStrings=None):
        self.__builder = builder
        self.__model = model
        self.__type = type
        self.__back_wood = back_wood
        self.__top_wood = top_wood
        self.__numStrings = numStrings

    @property
    def builder(self):
        return self.__builder

    @property
    def model(self):
        return self.__model

    @property
    def type(self):
        return self.__type

    @property
    def back_wood(self):
        return self.__back_wood

    @property
    def top_wood(self):
        return self.__top_wood

    @property
    def numStrings(self):
        return self.__numStrings

    # Delegation
    def matches(self, specs):
        # Match provided attributes &  ignore the rest
        for spec, value in vars(specs).items():
            curr_attr = getattr(self, spec)
            if curr_attr is not None and value != curr_attr:
                return False
        return True


class Guitar:

    def __init__(self, serial_number, price, spec):
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = spec

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def price(self):
        return self.__price

    @property
    def spec(self):
        return self.__spec


class Inventory:

    def __init__(self, guitars=None):
        self.__guitars = guitars if isinstance(guitars, list) and all(
            [isinstance(guitar, Guitar) for guitar in guitars]) else []

    @property
    def guitars(self):
        return self.__guitars

    def add_guitar(self, guitar):

        if isinstance(guitar, Guitar):
            self.__guitars.append(guitar)
            return True
        else:
            print("the object added must be a Guitar instance")
            return False

    def search(self, guitar_spec):
        result = []
        for guitar in self.guitars:
            if guitar.matches(guitar_spec):
                result.append(guitar)
        return result
