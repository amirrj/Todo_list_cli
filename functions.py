import json

def load_data():
    return json.loads(open('data.json', 'r').read())


def save_data(data):
    json.dump(data, open('data.json', 'w'), indent=4)


# function for viewing tasks
def view(args, data):
    # check for tasks, if not tasks - display message
    if not data:
        print('No tasks to display')
    else:
        # define output message within a function
        def output(task):
            print('Task: %s -- Status: %s ' % (task['title'], task['status']))

        # check if filter is provided and display tasks
        match args.f:
            case None:
                for entry in data:
                    output(entry)
            case 'completed':
                for entry in data:
                    if entry['status'] == 'completed':
                        output(entry)
            case 'outstanding':
                for entry in data:
                    if entry['status'] == 'outstanding':
                        output(entry)


# add new task
def add(args, data):
    # generate task id
    task_id = len(data) + 1
    # create new task
    new_task = {
        'id': task_id,
        'title': args.add,
        'status': 'outstanding'
    }
    # add task to data
    data.append(new_task)
    # save data to json
    save_data(data)
    # print success message
    print(f'Task added {args.add}')


def del_task(args, data):

    # check to see if task if provided by user
    try:
        # check if user wants to delete all tasks
        if not args.all:
            task_id = [task['id'] for task in data if task['title'].lower() == args.delete.lower()]

            if task_id:
                for i, task in enumerate(data):
                    if task['id'] in task_id:
                        data.pop(i)
                        print('Task removed - %s' % (task['title']))
                        save_data(data)
            else:
                print('Task not found')
        # delete all tasks
        else:
            verify = input('Are you sure you wish to delete all tasks?(Yes/No)')
            if verify.lower() == 'yes':
                data.clear()
                save_data(data)
                print('All tasks deleted!')
            elif verify.lower() == 'no':
                print('No changes made')
            else:
                print('Please type "Yes" or "No"')
    except AttributeError:
        print('Please enter a task')


def mark_task(args, data):
    task = {}
    for task in data:
        if task['title'] == args.task:
            task = task

    if task:
        match args.status:
            case 'completed':
                if task['status'] == 'completed':
                    print('Task has already been completed')
                else:
                    task['status'] = 'completed'
                    save_data(data)
                    print('Task Updated')
            case 'outstanding':
                if task['status'] == 'outstanding':
                    print('Task has already been set as outstanding')
                else:
                    task['status'] = 'outstanding'
                    save_data(data)
                    print('Task Updated')
    else:
        print('Task not found')