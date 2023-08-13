class Doctor:
    def __init__(self, ID, Name, Specialization, WorkingTime, Qualification, RoomNumber):
        self.Id = ID
        self.Name = Name
        self.Specialization = Specialization
        self.WorkingTime = WorkingTime
        self.Qualification = Qualification
        self.RoomNumber = RoomNumber

    def formatDrInfo(self):
        return f"{self.Id}_{self.Name}_{self.Specialization}_{self.WorkingTime}_{self.Qualification}_{self.RoomNumber}"

    def tableDrInfo(self):
        return f"{self.Id:8}{self.Name:20}{self.Specialization:20}{self.WorkingTime:20}{self.Qualification:20}{self.RoomNumber:8}"


    def read_and_display_doctors(self):
        with open("doctors.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    table_info = doctor.tableDrInfo()
                    print(table_info)
                else:
                    print("Invalid format in line:", line)


    def search_doctor_by_name(self, doctor_name):
        with open("doctors.txt", "r") as file:
            found = False
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[1] == doctor_name:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    table_info = doctor.tableDrInfo()
                    header = Doctor(doctors.Id, doctors.Name, doctors.Specialization, doctors.WorkingTime, doctors.Qualification, doctors.RoomNumber)
                    table_header = header.tableDrInfo()
                    print(table_header)
                    print(table_info)
                    found = True
                    return

            if not found:
                print("Doctor with name", doctor_name, "not found.")


    def search_doctor_by_id(self, doctor_id):
        with open("doctors.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[0] == doctor_id:
                    doctor = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    table_info = doctor.tableDrInfo()
                    header = Doctor(doctors.Id, doctors.Name, doctors.Specialization, doctors.WorkingTime, doctors.Qualification, doctors.RoomNumber)
                    table_header = header.tableDrInfo()
                    print(table_header)
                    print(table_info)
                    return
            print("Doctor with ID", doctor_id, "not found.")


    def edit_doctor_info(self):
        doctor_id = input("Enter the ID of the doctor you want to edit: ")

        with open("doctors.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("doctors.txt", "w") as file:
            for line in lines:
                parts = line.strip().split("_")
                if len(parts) == 6 and parts[0] == doctor_id:
                    found = True
                    new_name = input("Enter new Name: ")
                    new_specialization = input("Enter new Specialization: ")
                    new_working_time = input("Enter new Working Time: ")
                    new_qualification = input("Enter new Qualification: ")
                    new_room_number = input("Enter new Room Number: ")
                    new_line = f"{doctor_id}_{new_name}_{new_specialization}_{new_working_time}_{new_qualification}_{new_room_number}\n"
                    file.write(new_line)
                    print("Doctor information updated successfully!")
                else:
                    file.write(line)

        if not found:
            print("Doctor with ID", doctor_id, "not found.")


    def add_doctor(self):
        doctor_id = input("Enter the ID: ")
        doctor_name = input("Enter the Name: ")
        doctor_specialization = input("Enter the Specialization: ")
        doctor_working_time = input("Enter the Working Time: ")
        doctor_qualification = input("Enter the Qualification: ")
        doctor_room_number = input("Enter the Room Number: ")

        with open("doctors.txt", "a") as file:
            new_doctor = f"{doctor_id}_{doctor_name}_{doctor_specialization}_{doctor_working_time}_{doctor_qualification}_{doctor_room_number}\n"
            file.write("\n")
            file.write(new_doctor)
            print("Doctor added successfully!")


class Facilities:
    def __init__(self):
        self.facilities_list = []
        self.loadFacilities()

    def loadFacilities(self):
        file = open('facilities.txt', 'r')
        self.facilities_list = [line.strip() for line in file.readlines()]

    def addFacility(self, facility):
        self.facilities_list.append(facility)
        self.writeFacilities()

    def displayFacilities(self):
        print("The Hospital Facilities are:")
        for facility in self.facilities_list:
            print(facility)

    def writeFacilities(self):
        file = open('facilities.txt', 'w')
        for facility in self.facilities_list:
            file.write(facility)
            file.write("\n")

class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def formatLabInfo(self):
        return f"{self.lab_name}_{self.cost:}"

    def tableLabInfo(self):
        return f"{self.lab_name:25}{self.cost:25}"


    def read_and_display_labs(self):
        with open("laboratories.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 2:
                    lab = Laboratory(parts[0], parts[1])
                    table_info = lab.tableLabInfo()
                    print(table_info)
                else:
                    print("Invalid format in line:", line)


    def add_lab_to_file(self, lab_name, cost):
        with open("laboratories.txt", "a") as file:
            lab_info = f"{lab_name}_{cost}\n"
            file.write(lab_info)
            print("Lab added successfully!")

class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.Id = pid
        self.Name = name
        self.Disease = disease
        self.Gender = gender
        self.Age = age

    def formatPatientInfo(self):
        return f"{self.Id}_{self.Name}_{self.Disease}_{self.Gender}_{self.Age}"

    def tablePatientInfo(self):
        return f"{self.Id:8} {self.Name:20}{self.Disease:20}{self.Gender:8}{self.Age:3}"


    def read_and_display_patients(self):
        with open("patients.txt", "r") as file:
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 5:
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    table_info = patient.tablePatientInfo()
                    print(table_info)
                else:
                    print("Invalid format in line:", line)


    def search_patient_by_id(self, patient_id):
        with open("patients.txt", "r") as file:
            found = False
            for line in file:
                parts = line.strip().split("_")
                if len(parts) == 5 and parts[0] == patient_id:
                    patient = Patient(parts[0], parts[1], parts[2], parts[3], parts[4])
                    table_info = patient.tablePatientInfo()
                    header = Patient(patients.Id, patients.Name, patients.Disease, patients.Gender, patients.Age)
                    table_header = header.tablePatientInfo()
                    print(table_header)
                    print(table_info)
                    found = True
                    return

            if not found:
                print("Patient with ID", patient_id, "not found.")


    def edit_patient_info(self):
        patient_id = input("Enter the ID of the patient you want to edit: ")

        with open("patients.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("patients.txt", "w") as file:
            for line in lines:
                parts = line.strip().split("_")
                if len(parts) == 5 and parts[0] == patient_id:
                    found = True
                    new_name = input("Enter new Name: ")
                    new_disease = input("Enter new Disease: ")
                    new_gender = input("Enter new Gender: ")
                    new_age = input("Enter new Age: ")
                    new_line = f"{patient_id}_{new_name}_{new_disease}_{new_gender}_{new_age}\n"
                    file.write(new_line)
                    print("Patient information updated successfully!")
                else:
                    file.write(line)

        if not found:
            print("Patient with ID", patient_id, "not found.")


    def add_patient(self):
        patient_id = input("Enter the ID: ")
        patient_name = input("Enter the Name: ")
        patient_disease = input("Enter the Disease: ")
        patient_gender = input("Enter the Gender: ")
        patient_age = input("Enter the Age: ")

        with open("patients.txt", "a") as file:
            new_patient = f"{patient_id}_{patient_name}_{patient_disease}_{patient_gender}_{patient_age}"
            file.write("\n")
            file.write(new_patient)
            print("Patient added successfully!")

doctors = Doctor("Id", "Name", "Speciality", "Timing", "Qualification", "Room Number")
facilities = Facilities()
labs = Laboratory("lab_name", "cost")
patients = Patient("Id", "Name", "Disease", "Gender", "Age")

def doctor_menu():
    while True:
        print("\nDoctors Menu:")
        print("1 - Display Doctors list")
        print("2 - Search for doctor by ID")
        print("3 - Search for doctor by name")
        print("4 - Add doctor")
        print("5 - Edit doctor info")
        print("6 - Back to the Main Menu")
        choice = input()

        if choice == '1':
            doctors.read_and_display_doctors()
        elif choice == '2':
            doctor_id = input("Enter the doctor ID: ")
            doctors.search_doctor_by_id(doctor_id)
        elif choice == '3':
            doctor_name = input("Enter the doctor name:")
            doctors.search_doctor_by_name(doctor_name)
        elif choice == '4':
            doctors.add_doctor()
        elif choice == '5':
            doctors.edit_doctor_info()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def facilities_menu():
    while True:
        print("Facilities Menu:\n 1 - Display Facilities List\n 2 - Add Facility\n 3 - Back to the Main Menu")
        choice = input()
        if choice == "1":
            facilities.displayFacilities()
        elif choice == "2":
            facilities.addFacility(input("Enter a new facility to add: "))
        elif choice == "3":
            break
        else:
            print("Invalid entry")

def laboratory_menu():
    while True:
        print("\nLaboratories Menu:")
        print("1 - Display laboratories list")
        print("2 - Add laboratory")
        print("3 - Back to the Main Menu")
        choice = input()

        if choice == '1':
            labs.read_and_display_labs()
        elif choice == '2':
            lab_name = input("Enter Laboratory name: ")
            cost = input("Enter Laboratory cost: ")
            labs.add_lab_to_file(lab_name, cost)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def patient_menu():
    while True:
        print("\nPatients Menu:")
        print("1 - Display Patients list")
        print("2 - Search for patient by ID")
        print("3 - Add patient")
        print("4 - Edit patient info")
        print("5 - Back to the Main Menu")
        choice = input()

        if choice == '1':
            patients.read_and_display_patients()
        elif choice == '2':
            patient_id = input("Enter the patient ID: ")
            patients.search_patient_by_id(patient_id)
        elif choice == '3':
            patients.add_patient()
        elif choice == '4':
            patients.edit_patient_info()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

class DisplayMenu:

    def __innit__(self):
        pass

    def mainMenu(self):
        while True:
            print("\nWelcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 0 to stop:")
            print("1 - Doctors")
            print("2 - Facilities")
            print("3 - Laboratories")
            print("4 - Patients")
            print("0 - Quit")
            choice = input()

            if choice == '1':
                doctor_menu()
            elif choice == '2':
                facilities_menu()
            elif choice == '3':
                laboratory_menu()
            elif choice == '4':
                patient_menu()
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

init = DisplayMenu()
init.mainMenu()
input()