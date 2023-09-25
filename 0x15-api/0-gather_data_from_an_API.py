#!/usr/bin/python3
import sys
from requests import request

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


print(f"Employee {employee_name} is done \
with tasks ({completed_tasks}/{total_tasks})")
for task in completed_tasks_list:
    print(f"\t{task}")
