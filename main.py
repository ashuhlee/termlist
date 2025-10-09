from imports import *

# PROJECT TO-DO

# - add progress bar (?)
# - mark as complete
# - prettify

tasks: list[dict] = []
MAX_STORAGE: int = 5

emojis: list[str] = ['💫', '✨', '🌈', '🚀']

last_updated: type[datetime] = datetime.datetime

# clears console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# add a new task - DONE
def add_task():
    global last_updated

    if len(tasks) >= MAX_STORAGE:
        print('\033[33m' + 'Task list is full!' + '\033[0m')

    else:
        task: str = input('\n\033[34mEnter task: \033[0m').capitalize()
        tasks.append({'task': task, 'done': False})

        emoji: str = random.choice(emojis)
        print('\n\033[1m' + 'Task added!' + '\033[0m ' + emoji)

        last_updated = datetime.datetime.now() # update last modified time

# modify existing task - DONE
def edit_task():
    global last_updated

    if len(tasks) == 0:
        print('\033[33m' + 'No tasks to edit.' + '\033[0m')
        return
    else:

        show_tasks(header=False)

        try:
            edit_index: int = int(input(f'\nEnter task number: '))

            if 1 <= edit_index <= len(tasks):
                updated: str = input('\n\033[34mEnter updated task: \033[0m').capitalize()
                tasks[edit_index - 1]['task'] = updated

                print('\n\033[1;92m' + f'Task {edit_index} has been modified.' + '\033[0m ')

                last_updated = datetime.datetime.now()  # update last modified time

            else:
                print('Task does not exist.')

        except ValueError:
            print('Please enter a valid number.')

# remove existing task - DONE
def remove_task():
    global last_updated

    if len(tasks) == 0:
        print('\033[33m' + 'No tasks to remove.' + '\033[0m')
        return
    else:
        show_tasks(header = False)

        try:
            remove_index: int = int(input(f'\nEnter task number: '))

            if 1 <= remove_index <= len(tasks):
                tasks.pop(remove_index - 1)

                print('\n\033[1;92m' + 'Task removed.' + '\033[0m ')

                last_updated = datetime.datetime.now()  # update last modified time

            else:
                print('Task does not exist.')

        except ValueError:
            print('Please enter a valid number.')

# display all tasks - DONE
def show_tasks(header: bool = True):
    if len(tasks) == 0:
        print('\033[33m' + 'No tasks yet.' + '\033[0m')

    else:
        if header:
            print('\nYour tasks:\n')
        else:
            print('\nChoose a task to modify/remove: \n')

        i: int = 1
        for task_info in tasks:

            if task_info['done']:
                checkbox = '[✓]'
            else:
                checkbox = '[ ]'
            print(f"{i}. {checkbox} {task_info['task']}")
            i += 1

        print('\n\033[1m' + 'Total tasks: ' + str(len(tasks)) + '\033[0m')

        if last_updated:
            formatted: str = last_updated.strftime('%A at %-I:%M%p')
            print('\n\033[1m' + f'🕔 Last updated: {formatted}' + '\033[0m')

# mark specific tasks as done - NOT DONE
def mark_done():
    print('Mark complete feature coming soon!')

# show help manual in terminal - DONE
def help_manual(header: bool = True):

    console = Console()

    if header:
        console.print('\n--- HELP DESK ---\n', style = 'bold magenta', justify = 'left')
    else:
        pass

    ### DISPLAY MAIN TABLE

    table = Table(show_header = False, border_style = 'magenta', style = 'grey70', min_width = 50)

    # define columns - content inside aligned left
    table.add_column('OPTION', justify ='center', style = 'bold magenta', no_wrap = True)
    table.add_column('DESCRIPTION', justify = 'left')

    # header rows
    header_option = Align.center(Text('OPTION', style = 'bold magenta'))
    header_description = Align.center(Text('DESCRIPTION', style = 'bold magenta'))

    table.add_row(header_option, header_description, end_section = True)

    # table rows
    table.add_row('1', 'Add a new task')
    table.add_row('2', 'Edit an existing task')
    table.add_row('3', 'Remove an existing task')
    table.add_row('4', 'Show all tasks')
    table.add_row('5', 'Mark task as done')

    ### DISPLAY MANUAL

    manual = Table(show_header=False, border_style=Style(color='red'), min_width=50)

    # Define columns (no headers)
    manual.add_column('', justify='center', style='bold red')
    manual.add_column('', justify='left')

    # add manual rows
    manual.add_row('(Q)', 'Quit the app')
    manual.add_row('(H)', 'Show this help manual')

    console.print(table)
    console.print(manual)

# main function
def todo_list():

    print('\n\033[1;36m' + 'To-Do List App' +'\033[0m\n')
    time.sleep(0.5)

    help_manual(header = False)

    actions = {
        '1': add_task,
        '2': edit_task,
        '3': remove_task,
        '4': show_tasks,
        '5': mark_done
    }

    while True:

        choice = input('\n\033[1m' + 'Enter your choice: ' + '\033[0m').strip().lower()

        if choice in actions:
            actions[choice]()

        elif choice in ('h', 'help', '-help', '--help'):
            clear_screen(), help_manual()

        elif choice in ('q', 'quit', '-quit', '--quit'):
            clear_screen()
            print('Exiting app...')

            time.sleep(1)
            break

        else:
            print('\033[31m' + 'Invalid choice. Please try again or H for help' + '\033[0m')

        time.sleep(0.5)


todo_list()