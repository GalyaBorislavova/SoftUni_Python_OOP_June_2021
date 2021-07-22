class Trainer:
    trainer_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.trainer_id
        Trainer.trainer_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.trainer_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

