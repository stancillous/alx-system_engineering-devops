#!/usr/bin/python3
""" script to export data in the CSV format."""

if __name__ == "__main__":
    import csv
    from requests import request
    import sys

    user_id = sys.argv[1]
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    filename = "{}.csv".format(user_id)  # to store the csv data
    user_tasks_list = []  # 2d list to store all tasks of a given user

    tasks_response = (request("GET", task_url)).json()
    user_response = request("GET", user_info_url).json()

    employee_name = user_response.get('username')

    # add each task, as an array, to our 2d list above
    for task in tasks_response:
        user_tasks_list.append(
            [user_id, employee_name, task.get('completed'), task.get('title')]
            )

    # write data to the csv file
    with open(filename, 'w', newline='') as csvfile:
        data = csv.writer(csvfile)
        data.writerows(user_tasks_list)
