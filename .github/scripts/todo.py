
class Task:
    # Create a new task
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

        if status == "Done":
            self.completed = True

    # Mark the task as completed
    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    # Return a short representation of the task
    def __repr__(self):
        return self.title + " - " + self.status

    # Return a user-friendly representation
    def __str__(self):
        return "Task: " + self.title + ", Status: " + self.status


class TaskPool:
    # Create an empty task list
    def __init__(self):
        self.tasks = []

    # Populate the pool with six example tasks
    def populate(self):
        task1 = Task("Add Login UI", status="Done")
        task2 = Task("Fix UI Bug", status="Done")
        task3 = Task("Write tests", status="ToDo")
        task4 = Task("Update Login UI", status="ToDo")
        task5 = Task("Update Documentation", status="ToDo")
        task6 = Task("Deploy to Production", status="ToDo")

        # Mark the first three tasks as completed
        task1.mark_completed()
        task2.mark_completed()
        task3.mark_completed()

        self.tasks = [
            task1, task2, task3,
            task4, task5, task6
        ]

    # Add a new task
    def add_task(self, task):
        self.tasks.append(task)

    # Return tasks that are not completed
    def get_open_tasks(self):
        return [task for task in self.tasks
                if task.status == "ToDo"]

    # Return completed tasks
    def get_done_tasks(self):
        return [task for task in self.tasks
                if task.status == "Done"]


# Main program
def main():
    pool = TaskPool()

    # Populate the task pool
    pool.populate()

    # Display ToDo tasks
    print("ToDo Tasks:")

    for task in pool.get_open_tasks():
        print(task.title)

    # Display completed tasks
    print("Done Tasks:")

    for task in pool.get_done_tasks():
        print(task.title)


if __name__ == "__main__":
    main()
