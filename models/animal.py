class Animal():
    """
    animal class definition for the animals in the kennel
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.

    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id

#this class is place holder that is a representation of what we see in the database
#think of the animals skeleton structured to match whats in the db