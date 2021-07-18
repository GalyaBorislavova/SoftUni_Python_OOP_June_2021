from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if MovieWorld.CUSTOMER_CAPACITY > 0:
            MovieWorld.CUSTOMER_CAPACITY -= 1
            self.customers.append(customer)
        return

    def add_dvd(self, dvd: DVD):
        if MovieWorld.DVD_CAPACITY > 0:
            self.dvds.append(dvd)
            MovieWorld.DVD_CAPACITY -= 1
        return

    def extract_customer_and_dvd(self, customer_id, dvd_id):
        customer: Customer = [c for c in self.customers if c.id == customer_id][0]
        dvd: DVD = [d for d in self.dvds if d.id == dvd_id][0]
        return customer, dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer, current_dvd = MovieWorld.extract_customer_and_dvd(self, customer_id, dvd_id)
        if current_dvd.is_rented:
            if current_dvd in current_customer.rented_dvds:
                return f"{current_customer.name} has already rented {current_dvd.name}"
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer, current_dvd = MovieWorld.extract_customer_and_dvd(self, customer_id, dvd_id)
        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        customer_info = '\n'.join([repr(c) for c in self.customers])
        dvds_info = '\n'.join([repr(d) for d in self.dvds])
        return customer_info + "\n" + dvds_info


if __name__ == "__main__":

    c1 = Customer("John", 16, 1)
    c2 = Customer("Anna", 55, 2)

    d1 = DVD("Black Widow", 1, 2020, "April", 18)
    d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

    movie_world = MovieWorld("The Best Movie Shop")

    movie_world.add_customer(c1)
    movie_world.add_customer(c2)

    movie_world.add_dvd(d1)
    movie_world.add_dvd(d2)

    print(movie_world.rent_dvd(1, 1))
    print(movie_world.rent_dvd(2, 1))
    print(movie_world.rent_dvd(1, 2))

    print(movie_world)