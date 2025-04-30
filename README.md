# DATABASE SYSTEMS
## Overview 
The Dentist Clinic Database is designed to manage information related to employees, patients, appointments, treatments, medicines, and operations. The database ensures efficient
storage, manipulation, and retrieval of data to support clinical operations and management decision-making. It includes at least 8 tables to organize data about staff (dentists,
nurses, employees), patients, appointments, treatments (medical and operational), medicines, and payments. The system supports data analysis through statistical queries to
provide insights for management, such as identifying high-performing doctors, popular medicines, and patient payment trends. The design adheres to normalization principles (up
to 3NF) to ensure data integrity and scalability.

### Why Use SQLite3 for the Dental Clinic Database?
SQLite3 is ideal for the dental clinic’s 3NF-normalized database due to:
Simplicity: Serverless, single-file database with minimal setup, perfect for small clinics.
Efficiency: Handles moderate data (e.g., Patient , Appointment ) and supports foreign keys for relationships (e.g., DentistID in Appointment ).
Reliability: ACID-compliant, ensuring data integrity for critical records like Payment or Prescription .
Cost-Effective: Free and low-resource, reducing costs for hardware and licensing.
Portability: Cross-platform, embedded, and easy to back up or transfer.
Scalability: Suitable for small to medium workloads, with the 3NF design optimizing performance.
