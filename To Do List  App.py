def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        # Using the Day 13 requirement: with open() as f
        with open(filename, "r") as f:
            for line in f:
                # .strip() removes whitespace and the invisible newline character (\n)
                tasks.append(line.strip())
    except FileNotFoundError:
        print(f"[*] No existing '{filename}' found. A new one will be created.")
        
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    # Using the Day 13 requirement for writing files
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    print("\n--- My ToDo List ---")
    if not tasks:
        print("Your list is currently empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("--------------------")

def main():
 
    todo_list = load_tasks()
    
    while True:
        display_tasks(todo_list)
        print("Options: Add Task  Remove Task  Exit")
        
        choice = input("What would you like to do?: ").strip()
        
        if choice == "1":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                todo_list.append(new_task)
                print(f"[*] '{new_task}' added successfully!")
                
        elif choice == "2":
            try:
                # Using Error Handling (Day 18) to catch bad user input
                task_num = int(input("Enter the number of the task to remove: "))
                
                if 1 <= task_num <= len(todo_list):
                    removed_item = todo_list.pop(task_num - 1)
                    print(f"[*] Removed '{removed_item}'.")
                else:
                    print("[!] Invalid number. Please select a valid task.")
            except ValueError:
                # Triggers if the user types text instead of a number
                print("[!] Invalid input. Please enter a numerical value.")
                
        elif choice == "3":
            # Save the file right before the loop breaks to persist data
            save_tasks(todo_list)
            print("[*] Tasks saved! Goodbye.")
            break
            
        else:
            print("[!] Unrecognized command. Please enter 1, 2, or 3.")

# Ensures no code exists in the global scope (Day 8 constraint)
if __name__ == "__main__":
    main()
