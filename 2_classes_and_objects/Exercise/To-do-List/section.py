from task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def task_in_section(self, task_to_check: Task):
        if isinstance(task_to_check, Task):
            for t in self.tasks:
                if t.name == task_to_check.name:
                    return True
            return False
        for t in self.tasks:
            if t.name == task_to_check:
                return t
        return None

    def add_task(self, new_task: Task):
        if self.task_in_section(new_task):
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        current_task: Task = self.task_in_section(task_name)
        if current_task:
            current_task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        only_not_completed = [t for t in self.tasks if not t.completed]
        return f"Cleared {len(self.tasks) - len(only_not_completed)} tasks."

    def view_section(self):
        task_details = [t.details() for t in self.tasks]
        return f"Section {self.name}:" + "\n" + '\n'.join(task_details)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
