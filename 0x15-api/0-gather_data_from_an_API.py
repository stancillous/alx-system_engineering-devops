#!/usr/bin/python3
""" script that, using a REST API, for a given employee ID,
returns information about his/her todo list progress."""

if __name__ == "__main__":
    from requests import request
    import sys

    user_id = sys.argv[1]
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    tasks_response = (request("GET", task_url))
    user_response = request("GET", user_info_url)

    employee_name = user_response.json().get('name')

    completed_tasks = 0
    total_tasks = len(tasks_response.json())
    completed_tasks_list = []

    for item in tasks_response.json():
        if item.get('completed'):
            completed_tasks_list.append(item.get('title'))
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, completed_tasks, total_tasks))
    for task in completed_tasks_list:
        print(f"\t{task}")
