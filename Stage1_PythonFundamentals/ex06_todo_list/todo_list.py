# Simple To-Do list program
tasks = []

while True:
    task = input("Enter a task (or 'quit' to stop): ")

    if task.lower() == "quit":
        break

    tasks.append(task)

# Display the to-do list
print("\nYour to-do list:")
for t in tasks:
    print(f"- {t}")
