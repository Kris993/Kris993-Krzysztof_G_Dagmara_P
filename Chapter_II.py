import argparse
import datetime

from psycopg2 import connect


def add_task(name, deadline, description=None):
    task_hash = hash((results.name, results.deadline, results.description))
    if deadline:
        cursor.execute(f'''INSERT INTO tasks
                            VALUES ('{name}', '{deadline}', '{description}', {task_hash}
                            );''')
    else:
        cursor.execute(f'''INSERT INTO tasks(name, description, task_hash)
                            VALUES ('{results.name}', '{description}', {task_hash}
                            );''')
    print(f"Task has been added to database with hash: {task_hash}")


def update_task(task_hash, name=None, deadline=None, description=None):
    cursor.execute(f'''SELECT * FROM tasks WHERE task_hash = '{task_hash}';''')
    task_to_update = cursor.fetchone()
    if task_to_update[1] or deadline is not None:
        cursor.execute(f'''UPDATE tasks
                    SET name = '{name if name else task_to_update[0]}',
                    deadline = '{deadline if deadline else task_to_update[1]}',
                    description = '{description if description else task_to_update[2]}'
                    WHERE task_hash = '{task_hash}'
                    ;''')
    else:
        cursor.execute(f'''UPDATE tasks
                            SET name = '{name if name else task_to_update[0]}',
                            description = '{description if description else task_to_update[2]}'
                            WHERE task_hash = '{task_hash}'
                            ;''')
    print(f"Task with hash {results.task_hash} has been updated to database")


def remove_task(task_hash):
    cursor.execute(f'''DELETE FROM tasks
                        WHERE task_hash = '{task_hash}'
                        ;''')
    print(f"Task with hash {task_hash} has been deleted from database")


def tasks_list(all_tasks=False, tasks_for_today=False):
    if all_tasks:
        cursor.execute('''SELECT * FROM tasks;''')
    elif tasks_for_today:
        cursor.execute(f'''SELECT * FROM tasks WHERE deadline = '{datetime.date.today()}';''')
    tasks = cursor.fetchall()
    print("All tasks:" if all_tasks else "Tasks for today:")
    if not tasks:
        print("You do not have any tasks.")
    for task in tasks:
        print(f"{task[0]} {task[1]} {task[2]} {task[3]}")


def valid_deadline(deadline):
    try:
        return datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        msg = f"{deadline} is not valid. Should have been YYYY-MM-DD"
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="commands", dest="command")

add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("--name", help="Name of an adding task", required=True)
add_parser.add_argument("--deadline", help="Deadline of an adding task", type=valid_deadline)
add_parser.add_argument("--description", help="Description of an adding task")

update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("--name", help="Name of an updating task")
update_parser.add_argument("--deadline", help="Deadline of an updating task", type=valid_deadline)
update_parser.add_argument("--description", help="Description of an updating task")
update_parser.add_argument("task_hash", help="Task hash")

remove_parser = subparsers.add_parser("remove", help="Remove a task")
remove_parser.add_argument("task_hash", help="Task hash")

list_parser = subparsers.add_parser("list", help="List contents")
list_parser = list_parser.add_mutually_exclusive_group(required=True)
list_parser.add_argument("--all", help="All of the list contents", action="store_true")
list_parser.add_argument("--today", help="List contents of today", action="store_true")

results = parser.parse_args()


cnx = connect(
    user="user",
    password="password",
    host="localhost",
    database="task_db")

cnx.autocommit = True
cursor = cnx.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                (name text NOT NULL,
                deadline date,
                description text,
                task_hash text NOT NULL
                );''')

if results.command == "add":
    add_task(results.name, results.deadline, results.description)
elif results.command == "update":
    update_task(results.task_hash, results.name, results.deadline, results.description)
elif results.command == "remove":
    remove_task(results.task_hash)
elif results.command == "list":
    tasks_list(results.all, results.today)
else:
    print("choose from 'add', 'update', 'remove', 'list'")

cnx.close()
