#!/usr/bin/python3
""" script to export data in the JSON format."""

if __name__ == "__main__":
    import json
    from requests import request

    all_employees_url = f"https://jsonplaceholder.typicode.com/users"

    filename = "todo_all_employees.json"  # to store the json data

    all_employees = request("GET", all_employees_url).json()

    """
    iterate over all the employees
    during each iteration, get current employee's tasks
    """

    for employee in all_employees:
        # everything inside this for loop will happen for
        # the current iterated employee, including writing/appending
        # to the json file
        employee_name = employee.get('username')
        employee_id = employee.get('id')  # use id to get tasks
        employee_tasks_url = ("https://jsonplaceholder.typicode.com/" +
                              f"users/{employee_id}/todos")
        tasks_response = (request("GET", employee_tasks_url)).json()

        user_tasks_list = []
        for task in tasks_response:
            # for each task of a user, append a dict of
            # the task's details into the above array
            user_tasks_list.append({
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        with open(filename, 'a') as jsonFile:
            # write the data, key is the user_id and
            # value is an array of dicts of each task
            user_json_data = {
                employee_id: user_tasks_list
            }
            jsonFile.write(json.dumps(user_json_data))
