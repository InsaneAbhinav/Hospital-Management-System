# Importing Modules
import mysql.connector as sql
from random import randint

# Establishing a Connection to MySQL Server
print("Enter the details of your MySQL Server:")
x = input("Hostname: ")
y = input("User: ")
z = input("Password: ")
con = sql.connect(host=x,
                  user=y,
                  password=z)
con.autocommit = True
cur = con.cursor()

# Creation of Database and Tables
cur.execute("CREATE DATABASE IF NOT EXISTS Hospital;")
cur.execute("USE Hospital;")
cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        sex CHAR(1),
        ailment VARCHAR(255),
        contact CHAR(10)
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        specialization VARCHAR(100),
        availability VARCHAR(50)
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INT PRIMARY KEY,
        patient_id INT,
        doctor_id INT,
        date DATE,
        time VARCHAR(10),
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (doctor_id) REFERENCES doctors(id)
    );
""")


# Login Menu
def login_menu():
    print("WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM")
    print("1. Register Patient")
    print("2. Register Doctor")
    print("3. Patient Menu")
    print("4. Doctor Menu")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register_patient()
    elif choice == 2:
        register_doctor()
    elif choice == 3:
        patient_menu()
    elif choice == 4:
        doctor_menu()
    else:
        exit_prompt()


# Register Patient
def register_patient():
    print("Enter patient details:")
    patient_id = randint(1000, 9999)
    print(f"Generated Patient ID: {patient_id}")
    name = input("Name: ")
    age = int(input("Age: "))
    sex = input("Sex (M/F/O): ").upper()
    ailment = input("Ailment: ")
    contact = input("Contact Number: ")
    cur.execute(f"""
        INSERT INTO patients VALUES ({patient_id}, '{name}', {age}, '{sex}', '{ailment}', '{contact}');
    """)
    print("Patient registered successfully!")
    login_menu()


# Register Doctor
def register_doctor():
    print("Enter doctor details:")
    doctor_id = randint(1000, 9999)
    print(f"Generated Doctor ID: {doctor_id}")
    name = input("Name: ")
    specialization = input("Specialization: ")
    availability = input("Availability (e.g., Mon-Fri, 10 AM-5 PM): ")
    cur.execute(f"""
        INSERT INTO doctors VALUES ({doctor_id}, '{name}', '{specialization}', '{availability}');
    """)
    print("Doctor registered successfully!")
    login_menu()


# Patient Menu
def patient_menu():
    print("Patient Menu:")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Back to Main Menu")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_appointment()
    elif choice == 2:
        view_appointments()
    else:
        login_menu()


# Book Appointment
def book_appointment():
    print("Booking an Appointment:")
    patient_id = int(input("Enter your Patient ID: "))
    cur.execute(f"SELECT * FROM patients WHERE id = {patient_id};")
    if cur.fetchone():
        doctor_id = int(input("Enter Doctor ID: "))
        cur.execute(f"SELECT * FROM doctors WHERE id = {doctor_id};")
        if cur.fetchone():
            date = input("Enter Appointment Date (YYYY-MM-DD): ")
            time = input("Enter Appointment Time (e.g., 10:30 AM): ")
            appointment_id = randint(10000, 99999)
            cur.execute(f"""
                INSERT INTO appointments VALUES ({appointment_id}, {patient_id}, {doctor_id}, '{date}', '{time}');
            """)
            print(f"Appointment booked successfully! Your Appointment ID: {appointment_id}")
        else:
            print("Doctor not found!")
    else:
        print("Patient not found!")
    patient_menu()


# View Appointments
def view_appointments():
    patient_id = int(input("Enter your Patient ID: "))
    cur.execute(f"""
        SELECT a.appointment_id, d.name, d.specialization, a.date, a.time
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.id
        WHERE a.patient_id = {patient_id};
    """)
    appointments = cur.fetchall()
    if appointments:
        for app in appointments:
            print(f"""
                Appointment ID: {app[0]}
                Doctor: {app[1]} (Specialization: {app[2]})
                Date: {app[3]}, Time: {app[4]}
            """)
    else:
        print("No appointments found!")
    patient_menu()


# Doctor Menu
def doctor_menu():
    print("Doctor Menu:")
    print("1. View Scheduled Appointments")
    print("2. Back to Main Menu")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_doctor_appointments()
    else:
        login_menu()


# View Scheduled Appointments
def view_doctor_appointments():
    doctor_id = int(input("Enter your Doctor ID: "))
    cur.execute(f"""
        SELECT a.appointment_id, p.name, p.ailment, a.date, a.time
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        WHERE a.doctor_id = {doctor_id};
    """)
    appointments = cur.fetchall()
    if appointments:
        for app in appointments:
            print(f"""
                Appointment ID: {app[0]}
                Patient: {app[1]} (Ailment: {app[2]})
                Date: {app[3]}, Time: {app[4]}
            """)
    else:
        print("No scheduled appointments!")
    doctor_menu()


# Exit Prompt
def exit_prompt():
    choice = input("Are you sure you want to exit? (Y/N): ")
    if choice.upper() == "N":
        login_menu()
    else:
        print("Goodbye!")


# Starting the Program
if __name__ == "__main__":
    login_menu()
