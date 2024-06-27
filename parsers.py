import argparse
import functions

# global parser
parser = argparse.ArgumentParser(prog='Todo_List', usage='%(prog)s [options]' )
# sub parser - task commands
subparsers = parser.add_subparsers(
    title='subcommands', help='Commands for tasks'
)

# view tasks parser
view_tasks_parser = subparsers.add_parser('view', help='View tasks')
view_tasks_parser.add_argument(dest='view', action='store_true')
# create optional argument for filter - completed / outstanding
view_tasks_parser.add_argument('-f', '--f', choices=['completed', 'outstanding'], help='filter tasks')
view_tasks_parser.set_defaults(func=functions.view)

# add task parser
add_task_parser = subparsers.add_parser('add', help='Add new task')
add_task_parser.add_argument(dest='add', nargs='?', help='Task to be added')
add_task_parser.set_defaults(func=functions.add)

# delete task
del_task_parser = subparsers.add_parser('delete', help='Delete a task')
del_task_parser.add_argument(dest='delete', nargs='?', help='Pick a task to delete')
# create optional filter to delete all tasks
del_task_parser.add_argument('-a', '--all', action='store_true', help='Delete all tasks')
del_task_parser.set_defaults(func=functions.del_task)

# set task to either completed or outstanding
mark_task_parser = subparsers.add_parser('set', help='Set status for task')
mark_task_parser.add_argument(dest='task', nargs='?', help='Task to set')
mark_task_parser.add_argument(dest='status', choices=['completed', 'outstanding'])
mark_task_parser.set_defaults(func=functions.mark_task)
