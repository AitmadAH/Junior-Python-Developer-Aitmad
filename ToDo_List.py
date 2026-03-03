def todo_app():
    # An array of tasks: each element is [task_name, status]
    # Status: 0 for "To Do", 1 for "Done"
    tasks = [
        ["Buy groceries", 0],
    ]

    while True:
        print("ToDo List")
        
        # Rendering the list from the array
        if not tasks:
            print("The list is empty!")
        else:
            for i in range(len(tasks)):
                status_icon = "✅" if tasks[i][1] == 1 else "⏳"
                print(f"{i + 1}. {status_icon} {tasks[i][0]}")

        print("Commands: (A)dd, (D)one, (R)emove, (E)xit")
        choice = input("What's the move? ").strip().lower()

        if choice == 'a':
            new_item = input("Enter new task: ").strip()
            if new_item:
                tasks.append([new_item, 0]) # Adding a new sub-array
        
        elif choice == 'd':
            try:
                idx = int(input("Task number to complete: ")) - 1
                tasks[idx][1] = 1 # Updating the 'status' index in the sub-array
                print("Task marked as finished!")
            except (ValueError, IndexError):
                print("Oops, that index doesn't exist in our array.")

        elif choice == 'r':
            try:
                idx = int(input("Task number to delete: ")) - 1
                removed = tasks.pop(idx) # Removing the array element
                print(f"Removed '{removed[0]}' from the list.")
            except (ValueError, IndexError):
                print("Invalid number.")

        elif choice == 'e':
            print("Closing the app. Goodbye!")
            break

todo_app()
