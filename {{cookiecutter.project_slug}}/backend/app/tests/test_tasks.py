from app import tasks
import time


def test_example_task():
    task_output = tasks.example_task("Hello World")
    assert task_output == "test task returns Hello World"


def test_async_example_task():
    task_object = tasks.example_task.apply_async(
        ("Hello World",), ignore_result=False
    )

    time.sleep(1)
    task_output = task_object.get()
    assert task_output == "test task returns Hello World"
