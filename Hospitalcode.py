from collections import deque

# 1 = emergency, 2 = regular
queue = deque()

def add_patient():
    name = input("Enter patient name: ")
    priority = int(input("Enter priority (1 = Emergency, 2 = Regular): "))
    if priority == 1:
        queue.appendleft((name, priority))
    else:
        queue.append((name, priority))
    print("Patient added!\n")

def serve_patient():
    if not queue:
        print("No patients in queue!\n")
    else:
        patient = queue.popleft()
        print(f"Serving Patient: {patient[0]} (Priority {patient[1]})\n")

def view_queue():
    if not queue:
        print("Queue is empty!\n")
        return
    print("\n--- Current Queue ---")
    for name, priority in queue:
        print(f"{name} (Priority {priority})")
    print()

def main():
    while True:
        print("1. Add Patient")
        print("2. Serve Patient")
        print("3. View Queue")
        print("4. Exit")
        ch = int(input("Choice: "))
        
        if ch == 1:
            add_patient()
        elif ch == 2:
            serve_patient()
        elif ch == 3:
            view_queue()
        elif ch == 4:
            break
        else:
            print("Invalid choice\n")

if name == "main":
    main()
