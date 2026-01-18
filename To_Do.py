import json
import os
from datetime import datetime

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(task):
    todos = load_todos()
    todo = {
        'id': len(todos) + 1,
        'task': task,
        'completed': False,
        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✓ Added: {task}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos found. Add one with 'add <task>'")
        return
    
    print("\n📋 Your To-Do List:")
    print("-" * 60)
    for todo in todos:
        status = "✓" if todo['completed'] else "○"
        print(f"{status} [{todo['id']}] {todo['task']}")
    print("-" * 60)

def complete_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            save_todos(todos)
            print(f"✓ Completed: {todo['task']}")
            return
    print(f"Todo with ID {todo_id} not found")

def delete_todo(todo_id):
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            task = todo['task']
            todos.pop(i)
            # Reindex remaining todos
            for j, t in enumerate(todos):
                t['id'] = j + 1
            save_todos(todos)
            print(f"✗ Deleted: {task}")
            return
    print(f"Todo with ID {todo_id} not found")

def show_help():
    print("""
  To-Do List CLI

Commands:
  add <task>       - Add a new todo
  list             - List all todos
  complete <id>    - Mark a todo as complete
  delete <id>      - Delete a todo
  help             - Show this help message
  exit             - Exit the application

Examples:
  add Buy groceries
  complete 1
  delete 2
    """)

def main():
    print("Welcome to To-Do List CLI! Type 'help' for commands.")
    
    while True:
        try:
            command = input("\n> ").strip().split(' ', 1)
            
            if not command or command[0] == '':
                continue
            
            action = command[0].lower()
            
            if action == 'exit':
                print("Goodbye!")
                break
            elif action == 'help':
                show_help()
            elif action == 'list':
                list_todos()
            elif action == 'add':
                if len(command) < 2:
                    print("Usage: add <task>")
                else:
                    add_todo(command[1])
            elif action == 'complete':
                if len(command) < 2:
                    print("Usage: complete <id>")
                else:
                    try:
                        complete_todo(int(command[1]))
                    except ValueError:
                        print("Please provide a valid todo ID")
            elif action == 'delete':
                if len(command) < 2:
                    print("Usage: delete <id>")
                else:
                    try:
                        delete_todo(int(command[1]))
                    except ValueError:
                        print("Please provide a valid todo ID")
            else:
                print(f"Unknown command: {action}. Type 'help' for commands.")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
