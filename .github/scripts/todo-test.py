
import unittest
import io
from contextlib import redirect_stdout

from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        # Create a fresh TaskPool before every test
        self.pool = TaskPool()

    def test_add_task(self):
        # Create and add a new task
        task = Task("Test task")
        self.pool.add_task(task)

        # Check that the task was added
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        # Add sample tasks
        self.pool.populate()

        open_tasks = self.pool.get_open_tasks()

        # Check that unfinished tasks are returned
        self.assertEqual(len(open_tasks), 3)

        for task in open_tasks:
            self.assertEqual(task.status, "ToDo")

    def test_get_done_tasks(self):
        # Add sample tasks
        self.pool.populate()

        done_tasks = self.pool.get_done_tasks()

        # Check that completed tasks are returned
        self.assertEqual(len(done_tasks), 3)

        for task in done_tasks:
            self.assertEqual(task.status, "Done")


# Run the tests
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(
        TestTaskPool
    )

    output = io.StringIO()

    runner = unittest.TextTestRunner(
        stream=output,
        verbosity=2
    )

    result = runner.run(suite)

    # Display a simplified test result
    for line in output.getvalue().splitlines():
        if "test_" in line:
            print(line)

    if not result.wasSuccessful():
        exit(1)
