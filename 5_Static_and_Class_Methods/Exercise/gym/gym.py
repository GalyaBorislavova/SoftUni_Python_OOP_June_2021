from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def get_object(obj_id, list_with_objects):
        return [o for o in list_with_objects if o.id == obj_id][0]

    def subscription_info(self, subscription_id: int):
        subscription: Subscription = Gym.get_object(subscription_id, self.subscriptions)
        customer_id, trainer_id, plan_id = subscription.customer_id, subscription.trainer_id, subscription.exercise_id
        customer: Customer = Gym.get_object(customer_id, self.customers)
        trainer: Trainer = Gym.get_object(trainer_id, self.trainers)
        plan: ExercisePlan = Gym.get_object(plan_id, self.plans)
        equipment: Equipment = Gym.get_object(plan.equipment_id, self.equipment)

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

