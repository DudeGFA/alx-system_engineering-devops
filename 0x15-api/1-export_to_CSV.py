#!/usr/bin/python3
"""Returns information on todo list progress for an employee id"""
if __name__ == "__main__":
    import requests
    import sys
    import csv
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={'userId': sys.argv[1]}).json()
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]).json()
    filename = sys.argv[1] + ".csv"
    with open(filename, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csvwriter.writerow([sys.argv[1], user['username'],
                                todo['completed'], todo['title']])
    completed_tasks = [task for task in todos if task["completed"] is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(completed_tasks), len(todos)))
    [print("\t " + task["title"]) for task in completed_tasks]
