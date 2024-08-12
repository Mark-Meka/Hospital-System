class Patient:
    def __init__(self, name, condition, specialization):
        self.name = name
        self.condition = condition
        self.specialization = specialization

class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} has been added to the system.")

    def print_patients(self):
        print("List of all patients:")
        patients_by_priority = {'super urgent': [], 'urgent': [], 'normal': []}
        for patient in self.patients:
            if patient.condition == 'super urgent':
                patients_by_priority['super urgent'].append(patient)
            elif patient.condition == 'urgent':
                patients_by_priority['urgent'].append(patient)
            else:
                patients_by_priority['normal'].append(patient)
        for priority, patients in patients_by_priority.items():
            if patients:
                print(f"Priority: {priority}")
                for patient in patients:
                    print(f"Patient: {patient.name}, Specialization: {patient.specialization}")

    def get_next_patient(self):
        if not self.patients:
            print("There are no patients in the system.")
            return None
        else:
            patients_by_priority = {'super urgent': [], 'urgent': [], 'normal': []}
            for patient in self.patients:
                if patient.condition == 'super urgent':
                    patients_by_priority['super urgent'].append(patient)
                elif patient.condition == 'urgent':
                    patients_by_priority['urgent'].append(patient)
                else:
                    patients_by_priority['normal'].append(patient)
            for priority in ['super urgent', 'urgent', 'normal']:
                if patients_by_priority[priority]:
                    next_patient = patients_by_priority[priority][0]
                    self.patients.remove(next_patient)
                    print(f"The next patient is {next_patient.name}, Specialization: {next_patient.specialization}, Priority: {priority}")
                    return next_patient

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"Patient {patient.name} has been removed from the system.")
        else:
            print("Patient not found in the system.")

hospital = Hospital()

while True:
    print("1. Add new patient")
    print("2. Print all patients")
    print("3. Get next patient")
    print("4. Remove leaving patient")
    print("5. End the program")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter patient name: ")
        condition = input("Enter patient condition (super urgent, urgent, or normal): ")
        specialization = input("Enter patient specialization: ")
        patient = Patient(name, condition, specialization)
        hospital.add_patient(patient)

    elif choice == "2":
        hospital.print_patients()

    elif choice == "3":
        hospital.get_next_patient()

    elif choice == "4":
        name = input("Enter patient name to remove: ")
        patient = None
        for p in hospital.patients:
            if p.name == name:
                patient = p
                break
        if patient:
            hospital.remove_patient(patient)
        else:
            print("Patient not found in the system.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
