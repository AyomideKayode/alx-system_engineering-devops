#!/usr/bin/python3

"""
Script that uses JSONPlaceholder API to get information about an employee
and exports TODO list to CSV.

Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""

import csv
import requests
import sys


def fetch_employee_info(employee_id):
    """Fetch employee information from JSONPlaceholder API."""
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    json_data = response.json()
    username = json_data.get('username')
    return username


def fetch_todo_list(employee_id):
    """Fetch TODO list for a specific employee from JSONPlaceholder API."""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    return response.json()


def export_to_csv(employee_id, username, todo_list):
    """Export TODO list data to a CSV file."""
    filename = f'{employee_id}.csv'
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Write CSV header
        employee_writer.writerow(
            ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        # Write TODO list data
        for task in todo_list:
            employee_writer.writerow(
                [employee_id, username, task.get('completed'),
                 task.get('title')])

    print(f'TODO list data exported to {filename}')


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print('Usage: python3 1-export_to_CSV.py <employee_id>')
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Fetch employee information
    username = fetch_employee_info(employee_id)

    # Fetch TODO list for the employee
    todo_list = fetch_todo_list(employee_id)

    # Export TODO list data to CSV
    export_to_csv(employee_id, username, todo_list)
