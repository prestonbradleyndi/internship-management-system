# Internship Management System

## Overview

The **Internship Management System (IMS)** is a custom application developed using **Odoo 18** during my internship at **IWOMI Technologies**.

The system is designed to provide a centralized platform for managing internship activities within an organization. It helps manage interns, internship programmes, tasks, attendance, reports, evaluations, feedback, and user access.

The project consists of two custom Odoo modules:

- `internship_management` – Core internship management functionality.
- `internship_portal` – Portal interface for interns.

---

## Objectives

The main objectives of the system are to:

- Centralize internship-related information.
- Facilitate the management of interns and internship programmes.
- Allow supervisors to assign and monitor tasks.
- Record intern attendance.
- Manage internship reports, evaluations, and feedback.
- Provide role-based access to system functions and records.
- Provide interns with a dedicated portal interface.

---

## Technologies Used

- **Odoo 18**
- **Python**
- **PostgreSQL**
- **Odoo ORM**
- **XML**
- **HTML / QWeb**
- **Bootstrap**
- **Odoo Portal and Website**

---

## Main Features

### 1. Intern Management

The system allows authorized users to:

- Register interns.
- Store intern information such as name, email, phone, school, and programme.
- Define the internship period.
- Assign supervisors.
- Track the status of an internship.

### 2. Internship Management

Internship programmes can be created and monitored using information such as:

- Internship title
- Department
- Description
- Start date
- End date
- Status

### 3. Task Management

Supervisors can assign tasks to interns.

Each task can contain:

- Task title
- Description
- Assigned intern
- Supervisor
- Internship
- Assigned date
- Due date
- Subtasks
- Progress
- Status

Task progress is calculated automatically according to the completion of its subtasks.

### 4. Attendance Management

The system allows supervisors to record intern attendance, including:

- Date
- Check-in time
- Check-out time
- Attendance status
- Notes

### 5. Internship Reports

Internship reports can be recorded and tracked using:

- Report title
- Intern
- Internship
- Submission date
- File path
- Report status

### 6. Evaluation

Supervisors can evaluate interns by recording:

- Evaluation score
- Comments
- Evaluation date

### 7. Feedback

Supervisors can provide feedback to interns, including:

- Feedback comments
- Date
- Supervisor
- Intern

### 8. Role-Based Access Control

The system implements different user roles with different permissions:

- **Administrator**
- **HR Officer**
- **Internship Coordinator**
- **Senior Supervisor**
- **Internship Supervisor**
- **Intern**

Access rights and record rules are used to restrict users to the information and operations relevant to their roles.

For example, an assigned supervisor can access only the interns assigned to that supervisor.

---

## Intern Portal

The `internship_portal` module provides a dedicated portal interface for interns.

Through the portal, interns can access:

- Internship information
- Assigned supervisor
- Assigned tasks
- Task progress
- Internship reports
- Supervisor feedback

The portal provides interns with access to relevant information without requiring access to the Odoo back-office interface.

---

## Project Structure

```text
internship-management-system/
│
├── internship_management/
│   ├── models/
│   │   ├── __init__.py
│   │   └── intern.py
│   │
│   ├── views/
│   │   ├── intern_views.xml
│   │   ├── supervisor_views.xml
│   │   └── user_views.xml
│   │
│   ├── Security/
│   │   ├── security.xml
│   │   ├── ir.model.access.csv
│   │   └── ims_access_rules.xml
│   │
│   ├── static/
│   │   └── description/
│   │       └── icon.png
│   │
│   ├── __init__.py
│   └── __manifest__.py
│
├── internship_portal/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── portal.py
│   │
│   ├── views/
│   │   └── portal_templates.xml
│   │
│   ├── static/
│   │   └── description/
│   │       └── icon.png
│   │
│   ├── __init__.py
│   └── __manifest__.py
│
└── .gitignore
