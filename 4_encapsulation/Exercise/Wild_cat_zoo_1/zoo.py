from animal import Animal
from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet
from worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, new_animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(new_animal)
            self.__budget -= price
            return f"{new_animal.name} the {new_animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, new_worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(new_worker)
            return f"{new_worker.name} the {new_worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{w.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        money_for_all_salaries = sum([w.salary for w in self.workers])
        if money_for_all_salaries <= self.__budget:
            self.__budget -= money_for_all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_tending = sum([a.money_for_care for a in self.animals])
        if money_for_tending <= self.__budget:
            self.__budget -= money_for_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        zoo_information = f"You have {len(self.animals)} animals" + "\n"
        lions = [lio for lio in self.animals if lio.__class__.__name__ == "Lion"]
        tigers = [tig for tig in self.animals if tig.__class__.__name__ == "Tiger"]
        cheetah = [cheet for cheet in self.animals if cheet.__class__.__name__ == "Cheetah"]
        lion_info = '\n'.join([f"{Animal.__repr__(lio)}" for lio in lions])
        tiger_info = '\n'.join([f"{Animal.__repr__(tig)}" for tig in tigers])
        cheetah_info = '\n'.join([f"{Animal.__repr__(cheet)}" for cheet in cheetah])
        animal_info = f"----- {len(lions)} Lions:" + "\n" + f"{lion_info}" + "\n" + f"----- {len(tigers)} Tigers:" \
                      + "\n" + f"{tiger_info}" + "\n" + f"----- {len(cheetah)} Cheetahs:" + "\n" + f"{cheetah_info}"

        return zoo_information + animal_info

    def workers_status(self):
        workers_information = f"You have {len(self.workers)} workers" + "\n"
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        keepers_info = '\n'.join([f"{Worker.__repr__(k)}" for k in keepers])
        caretakers_info = '\n'.join([f"{Worker.__repr__(c)}" for c in caretakers])
        vets_info = '\n'.join([f"{Worker.__repr__(v)}" for v in vets])

        return workers_information + f"----- {len(keepers)} Keepers:" + "\n" + f"{keepers_info}" + "\n" \
               + f"----- {len(caretakers)} Caretakers:" + "\n" + f"{caretakers_info}" + "\n" + f"----- {len(vets)}" \
                + f" Vets:" + "\n" + f"{vets_info}"


if __name__ == "__main__":
    zoo = Zoo("Zootopia", 3000, 5, 8)

    # Animals creation
    animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
               Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

    # Animal prices
    prices = [200, 190, 204, 156, 211, 140]

    # Workers creation
    workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
               Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
               Vet("Sam", 29, 220)]

    # Adding all animals
    for i in range(len(animals)):
        animal = animals[i]
        price = prices[i]
        print(zoo.add_animal(animal, price))

    # Adding all workers
    for worker in workers:
        print(zoo.hire_worker(worker))

    # Tending animals
    print(zoo.tend_animals())

    # Paying keepers
    print(zoo.pay_workers())

    # Fireing worker
    print(zoo.fire_worker("Adam"))

    # Printing statuses
    print(zoo.animals_status())
    print(zoo.workers_status())
