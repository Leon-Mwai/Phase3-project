from lib.db.models import session, Patient, Medication
from lib.db.seed import seed

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Invalid input. Please enter a number.")

def get_patient_by_id():
    pid = get_valid_int("Enter patient ID: ")
    patient = session.get(Patient, pid)
    if not patient:
        print(" Patient not found.")
    return patient

def menu():
    while True:
        print("""
         MediTrack CLI 
        1. Add Patient
        2. View All Patients
        3. Delete Patient
        4. Add Medication
        5. View Patient's Medications
        6. Delete Medication
        7. Exit
        """)
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = get_valid_int("Enter age: ")
            session.add(Patient(name=name, age=age))
            session.commit()
            print(" Patient added.")

        elif choice == '2':
            patients = session.query(Patient).all()
            if patients:
                for p in patients:
                    print(f"{p.id}. {p.name}, Age {p.age}")
            else:
                print("No patients found 🫤")

        elif choice == '3':
            patient = get_patient_by_id()
            if patient:
                session.delete(patient)
                session.commit()
                print(" Patient deleted.")

        elif choice == '4':
            patient = get_patient_by_id()
            if patient:
                name = input("Medication name: ")
                dosage = input("Dosage (e.g., 500mg): ")
                time = input("Time to take (e.g., 8AM): ")
                session.add(Medication(name=name, dosage=dosage, time_to_take=time, patient=patient))
                session.commit()
                print(" Medication added.")

        elif choice == '5':
            patient = get_patient_by_id()
            if patient:
                if patient.medications:
                    for med in patient.medications:
                        print(f"{med.id}. {med.name} - {med.dosage} @ {med.time_to_take}")
                else:
                    print("This patient has no meds.")

        elif choice == '6':
            mid = get_valid_int("Enter medication ID to delete: ")
            med = session.get(Medication, mid)
            if med:
                session.delete(med)
                session.commit()
                print("Medication deleted.")
            else:
                print("Medication not found.")

        elif choice == '7':
            print("Goodbye! Stay medicated.")
            break

        else:
            print(" Invalid option. Try again.")

# Only runs when `python -m lib.cli` is used
if __name__ == '__main__':
    from lib.db.models import Base, engine
    Base.metadata.create_all(engine)
    seed()
    menu()
