# Hospital Management System (HMS)

## Overview
The Hospital Management System (HMS) is a menu-driven Python application that uses a MySQL database to manage hospital operations. It facilitates patient and doctor registration, appointment booking, and viewing schedules efficiently.

---

## Features
### **User Role Management**
- **Patients**:
  - Register with personal details.
  - Book appointments with doctors.
  - View their scheduled appointments.
- **Doctors**:
  - Register with professional details.
  - View their scheduled appointments.

### **Database Integration**
- Fully functional MySQL database for managing:
  - Patients.
  - Doctors.
  - Appointments.
- Relational schema ensures data integrity.

### **Menu-Driven System**
- Intuitive menus for navigating features based on roles (patient or doctor).

---

## Database Schema
### **Tables**
1. **`patients`**:
   - Stores patient details.
   - Columns:
     - `id` (Primary Key)
     - `name`
     - `age`
     - `sex`
     - `ailment`
     - `contact`

2. **`doctors`**:
   - Stores doctor details.
   - Columns:
     - `id` (Primary Key)
     - `name`
     - `specialization`
     - `availability`

3. **`appointments`**:
   - Tracks appointments between patients and doctors.
   - Columns:
     - `appointment_id` (Primary Key)
     - `patient_id` (Foreign Key to `patients.id`)
     - `doctor_id` (Foreign Key to `doctors.id`)
     - `date`
     - `time`

---

## Installation and Setup

### **1. Prerequisites**
- Python 3.x installed.
- MySQL Server installed and running.
- Python module `mysql-connector-python` installed:
  ```bash
  pip install mysql-connector-python
