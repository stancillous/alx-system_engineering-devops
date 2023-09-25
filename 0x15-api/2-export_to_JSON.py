#!/usr/bin/python3
""" script to export data in the JSON format."""

if __name__ == "__main__":
    import json
    from requests import request
    import sys

    user_id = sys.argv[1]
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    filename = "{}.json".format(user_id)  # to store the json data

    tasks_response = (request("GET", task_url)).json()
    user_response = request("GET", user_info_url).json()

    employee_name = user_response.get('username')

    user_tasks_list = []
    for task in tasks_response:
        # for each task of a user, append a dict of
        # the task's details into the above array
        user_tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    with open(filename, 'w') as jsonFile:
        # write the data, key is the user_id and
        # value is an array of dicts of each task
        user_json_data = {
            user_id: user_tasks_list
        }
        jsonFile.write(json.dumps(user_json_data))
