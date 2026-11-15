from project.worker import Worker

from project.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_tend_animals = sum(a.money_for_care for a in self.animals)
        if money_to_tend_animals <= self.__budget:
            self.__budget -= money_to_tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def __print_status(self, collection: list[Worker | Animal], *args) -> str:
        elements = {arg: [] for arg in args}
        for item in collection:
            elements[type(item).__name__].append(repr(item))

        result = [f"You have {len(collection)} {str(collection[0].__class__.__bases__[0].__name__).lower()}s"]

        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)

    def animals_status(self) -> str:
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self) -> str:
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

