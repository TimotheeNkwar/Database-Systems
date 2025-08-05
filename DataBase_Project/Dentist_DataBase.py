import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the database
try:
    conn = sqlite3.connect("Dentist_Clinic_DataBase.db")
    cursor = conn.cursor()

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")
    # DATA DEFINITION LANGUAGE (DDL)
    # Create tables
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Staff (
        StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT,
        Role TEXT CHECK(Role IN ('Dentist', 'Nurse', 'Employee')),
        Phone TEXT,
        Email TEXT,
        HireDate DATE
    );

    CREATE TABLE IF NOT EXISTS Dentist (
        DentistID INTEGER PRIMARY KEY,
        Specialty TEXT,
        FOREIGN KEY (DentistID) REFERENCES Staff(StaffID)
    );

    CREATE TABLE IF NOT EXISTS Patient (
        PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT,
        DOB DATE,
        Gender TEXT CHECK(Gender IN ('M', 'F', 'Other')),
        Phone TEXT,
        Email TEXT,
        Address TEXT
    );

    CREATE TABLE IF NOT EXISTS Appointment (
        AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        PatientID INTEGER,
        DentistID INTEGER,
        AppointmentDate DATE,
        AppointmentTime TIME,
        Status TEXT CHECK(Status IN ('Scheduled', 'Completed', 'Cancelled')),
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
        FOREIGN KEY (DentistID) REFERENCES Dentist(DentistID)
    );

    CREATE TABLE IF NOT EXISTS Treatment (
        TreatmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        AppointmentID INTEGER,
        TreatmentType TEXT CHECK(TreatmentType IN ('Medical', 'Operational')),
        Description TEXT,
        Cost REAL,
        FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID)
    );

    CREATE TABLE IF NOT EXISTS Medicine (
        MedicineID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Description TEXT,
        StockQuantity INTEGER
    );

    CREATE TABLE IF NOT EXISTS Prescription (
        PrescriptionID INTEGER PRIMARY KEY AUTOINCREMENT,
        TreatmentID INTEGER,
        MedicineID INTEGER,
        Dosage TEXT,
        Duration TEXT,
        FOREIGN KEY (TreatmentID) REFERENCES Treatment(TreatmentID),
        FOREIGN KEY (MedicineID) REFERENCES Medicine(MedicineID)
    );

    CREATE TABLE IF NOT EXISTS Payment (
        PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
        TreatmentID INTEGER,
        PatientID INTEGER,
        Amount REAL,
        PaymentDate DATE,
        FOREIGN KEY (TreatmentID) REFERENCES Treatment(TreatmentID),
        FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
    );
    """)
                        ##5. Data Manipulation Language (DML)
    # Helper functions for random data generation
    def random_date(start_year, end_year):
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

    def random_time():
        hour = random.randint(8, 17)  # Clinic hours: 8 AM to 5 PM
        minute = random.choice([0, 15, 30, 45])
        return f"{hour:02d}:{minute:02d}:00"

    def random_phone():
        return f"555-{random.randint(1000, 9999)}"

    # Sample data pools
    first_names = ['John', 'Mary', 'Alice', 'Bob', 'Emma', 'James', 'Sarah', 'David', 'Lisa', 'Michael',
                   'Anna', 'Chris', 'Laura', 'Tom', 'Emily', 'Mark', 'Susan', 'Paul', 'Karen', 'Steven']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Wilson', 'Davis', 'Clark', 'Lewis', 'Walker', 'Hall',
                  'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green', 'Adams', 'Baker', 'Nelson', 'Carter']
    roles = ['Dentist', 'Nurse', 'Employee']
    specialties = ['Orthodontics', 'Endodontics', 'Periodontics', 'Prosthodontics', 'General Dentistry']
    genders = ['M', 'F', 'Other']
    addresses = ['123 Main St', '456 Oak Ave', '789 Pine Rd', '101 Maple Dr', '202 Birch Ln']
    treatment_types = ['Medical', 'Operational']
    treatment_descs = ['Root Canal', 'Teeth Cleaning', 'Filling', 'Extraction', 'Braces Adjustment']
    medicine_names = ['Ibuprofen', 'Amoxicillin', 'Paracetamol', 'Lidocaine', 'Fluoride Gel']
    statuses = ['Scheduled', 'Completed', 'Cancelled']

    # Insert 50 Staff (30 Dentists, 10 Nurses, 10 Employees)
    staff_data = []
    dentist_staff_ids = []
    for i in range(50):
        role = 'Dentist' if i < 30 else 'Nurse' if i < 40 else 'Employee'
        staff_data.append((
            random.choice(first_names),
            random.choice(last_names),
            role,
            random_phone(),
            f"{first_names[i % len(first_names)]}.{last_names[i % len(last_names)]}@clinic.com".lower(),
            random_date(2015, 2024)
        ))
        if role == 'Dentist':
            dentist_staff_ids.append(i + 1)  # StaffID is AUTOINCREMENT, so 1-based

    cursor.executemany("""
    INSERT INTO Staff (FirstName, LastName, Role, Phone, Email, HireDate)
    VALUES (?, ?, ?, ?, ?, ?)
    """, staff_data)

    # Insert 30 Dentists (StaffID 1–30, all with role 'Dentist')
    dentist_data = [(staff_id, random.choice(specialties)) for staff_id in dentist_staff_ids]
    cursor.executemany("""
    INSERT INTO Dentist (DentistID, Specialty)
    VALUES (?, ?)
    """, dentist_data)

    # Insert 50 Patients
    patient_data = []
    for i in range(50):
        patient_data.append((
            random.choice(first_names),
            random.choice(last_names),
            random_date(1960, 2010),
            random.choice(genders),
            random_phone(),
            f"{first_names[i % len(first_names)]}.{last_names[i % len(last_names)]}@patient.com".lower(),
            random.choice(addresses)
        ))
    cursor.executemany("""
    INSERT INTO Patient (FirstName, LastName, DOB, Gender, Phone, Email, Address)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, patient_data)

    # Get all PatientIDs and DentistIDs for realistic foreign key assignment
    cursor.execute("SELECT PatientID FROM Patient")
    patient_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT DentistID FROM Dentist")
    dentist_ids = [row[0] for row in cursor.fetchall()]

    # Insert 50 Appointments (linking real PatientIDs and DentistIDs)
    appointment_data = []
    for i in range(50):
        appointment_data.append((
            random.choice(patient_ids),
            random.choice(dentist_ids),
            random_date(2024, 2025),
            random_time(),
            random.choice(statuses)
        ))
    cursor.executemany("""
    INSERT INTO Appointment (PatientID, DentistID, AppointmentDate, AppointmentTime, Status)
    VALUES (?, ?, ?, ?, ?)
    """, appointment_data)

    # Get all AppointmentIDs for Treatments
    cursor.execute("SELECT AppointmentID, PatientID FROM Appointment")
    appointment_rows = cursor.fetchall()
    appointment_ids = [row[0] for row in appointment_rows]
    appointment_patient_map = {row[0]: row[1] for row in appointment_rows}

    # Insert 50 Treatments (each linked to a real Appointment)
    treatment_data = []
    for i in range(50):
        appointment_id = appointment_ids[i % len(appointment_ids)]
        treatment_data.append((
            appointment_id,
            random.choice(treatment_types),
            random.choice(treatment_descs),
            round(random.uniform(100.00, 1000.00), 2)
        ))
    cursor.executemany("""
    INSERT INTO Treatment (AppointmentID, TreatmentType, Description, Cost)
    VALUES (?, ?, ?, ?)
    """, treatment_data)

    # Get all TreatmentIDs for Prescriptions and Payments
    cursor.execute("SELECT TreatmentID, AppointmentID FROM Treatment")
    treatment_rows = cursor.fetchall()
    treatment_ids = [row[0] for row in treatment_rows]
    treatment_appointment_map = {row[0]: row[1] for row in treatment_rows}

    # Insert 50 Medicines
    medicine_data = []
    for i in range(50):
        medicine_data.append((
            random.choice(medicine_names) + f" {i + 1}",
            f"{random.choice(medicine_names)} for dental use",
            random.randint(10, 200)
        ))
    cursor.executemany("""
    INSERT INTO Medicine (Name, Description, StockQuantity)
    VALUES (?, ?, ?)
    """, medicine_data)

    # Get all MedicineIDs for Prescriptions
    cursor.execute("SELECT MedicineID FROM Medicine")
    medicine_ids = [row[0] for row in cursor.fetchall()]

    # Insert 50 Prescriptions (linking real TreatmentIDs and MedicineIDs)
    prescription_data = []
    for i in range(50):
        prescription_data.append((
            random.choice(treatment_ids),
            random.choice(medicine_ids),
            f"{random.randint(100, 500)}mg {random.choice(['once', 'twice', 'thrice'])} daily",
            f"{random.randint(3, 14)} days"
        ))
    cursor.executemany("""
    INSERT INTO Prescription (TreatmentID, MedicineID, Dosage, Duration)
    VALUES (?, ?, ?, ?)
    """, prescription_data)

    # Insert 50 Payments (PatientID matches Appointment's PatientID for Treatment)
    payment_data = []
    for treatment_id in treatment_ids:
        appointment_id = treatment_appointment_map[treatment_id]
        patient_id = appointment_patient_map[appointment_id]
        payment_data.append((
            treatment_id,
            patient_id,
            round(random.uniform(100.00, 1000.00), 2),
            random_date(2024, 2025)
        ))
    cursor.executemany("""
    INSERT INTO Payment (TreatmentID, PatientID, Amount, PaymentDate)
    VALUES (?, ?, ?, ?)
    """, payment_data)

    # Commit changes
    conn.commit()

    # Verify row counts
    for table in ['Staff', 'Dentist', 'Patient', 'Appointment', 'Treatment', 'Medicine', 'Prescription', 'Payment']:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table}: {count} rows")

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close connection
    conn.close()