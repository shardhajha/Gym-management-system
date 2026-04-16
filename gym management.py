# ---------------------------
# Gym Management System using Data Structures (Separated Menus)
# ---------------------------

# Data Structures
members = {}   # key = member_id, value = dict with member info
trainers = {}  # key = trainer_id, value = dict with trainer info

# Membership plans stored in dictionary
plans = {
    1: {"name": "Basic Plan", "duration": "1 Month", "price": 1000},
    2: {"name": "Standard Plan", "duration": "3 Months", "price": 2500},
    3: {"name": "Premium Plan", "duration": "6 Months", "price": 4500}
}

# ---------------------------
# Member Functions
# ---------------------------

def add_member():
    member_id = input("Enter Member ID: ")
    if member_id in members:
        print("Member already exists!")
        return

    name = input("Enter Member Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")

    print("\nAvailable Plans:")
    for pid, pinfo in plans.items():
        print(f"{pid}. {pinfo['name']} - ₹{pinfo['price']} ({pinfo['duration']})")

    plan_id = int(input("Choose Plan ID: "))
    if plan_id not in plans:
        print("Invalid Plan ID!")
        return

    members[member_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "plan": plans[plan_id]["name"],
        "trainer": None
    }
    print(f"Member '{name}' added successfully!")


def view_members():
    if not members:
        print("No members found.")
        return
    print("\n--- Gym Members List ---")
    for mid, info in members.items():
        print(f"ID: {mid} | Name: {info['name']} | Plan: {info['plan']} | Trainer: {info['trainer']}")


def delete_member():
    member_id = input("Enter Member ID to delete: ")
    if member_id in members:
        del members[member_id]
        print("Member deleted successfully.")
    else:
        print("Member not found.")


def assign_trainer():
    member_id = input("Enter Member ID: ")
    if member_id not in members:
        print("Member not found!")
        return

    if not trainers:
        print("No trainers available. Add trainers first.")
        return

    print("\nAvailable Trainers:")
    for tid, info in trainers.items():
        print(f"{tid}. {info['name']} ({info['speciality']})")

    trainer_id = input("Enter Trainer ID to assign: ")
    if trainer_id not in trainers:
        print("Trainer not found!")
        return

    members[member_id]["trainer"] = trainers[trainer_id]["name"]
    print(f"Trainer '{trainers[trainer_id]['name']}' assigned to member '{members[member_id]['name']}'.")


# ---------------------------
# Trainer Functions
# ---------------------------

def add_trainer():
    trainer_id = input("Enter Trainer ID: ")
    if trainer_id in trainers:
        print("Trainer already exists!")
        return

    name = input("Enter Trainer Name: ")
    speciality = input("Enter Speciality (e.g. Yoga, Strength, Cardio): ")

    trainers[trainer_id] = {
        "name": name,
        "speciality": speciality
    }
    print(f"Trainer '{name}' added successfully!")


def view_trainers():
    if not trainers:
        print("No trainers found.")
        return
    print("\n--- Gym Trainers List ---")
    for tid, info in trainers.items():
        print(f"ID: {tid} | Name: {info['name']} | Speciality: {info['speciality']}")


def delete_trainer():
    trainer_id = input("Enter Trainer ID to delete: ")
    if trainer_id in trainers:
        del trainers[trainer_id]
        print("Trainer deleted successfully.")
    else:
        print("Trainer not found.")


# ---------------------------
# Sub-Menus
# ---------------------------

def member_menu():
    while True:
        print("\n===== Member Management Menu =====")
        print("1. Add Member")
        print("2. View All Members")
        print("3. Assign Trainer to Member")
        print("4. Delete Member")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            assign_trainer()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")


def trainer_menu():
    while True:
        print("\n===== Trainer Management Menu =====")
        print("1. Add Trainer")
        print("2. View All Trainers")
        print("3. Delete Trainer")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_trainer()
        elif choice == "2":
            view_trainers()
        elif choice == "3":
            delete_trainer()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.")


# ---------------------------
# Main Menu
# ---------------------------

def main_menu():
    while True:
       
        print("\n===== Welcome =====")
        print("1. Member Section")lcome =====")
        print("2. Trainer Section")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            member_menu()
        elif choice == "2":
            trainer_menu()
        elif choice == "3":
            print("Exiting... Thank you for using Gym Management System!")
            break
        else:
            print("Invalid choice! Try again.")


# ---------------------------
# Run the System
# ---------------------------
if __name__ == "__main__":
    main_menu()
