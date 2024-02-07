# Hospital Management System

This Python program is designed to manage patient admissions in a hospital environment. It allows the user to add new patients, view all patients, get the next patient based on priority, and remove patients from the system.

## Features

- **Add New Patient**: Users can add new patients to the system by providing the patient's name, condition, and specialization.
- **View All Patients**: The program displays all patients, sorted by priority (Super Urgent, Urgent, Normal).
- **Get Next Patient**: The system will determine the next patient to be attended to based on their condition's priority.
- **Remove Patient**: Allows the removal of a patient from the system once they are no longer required to be in the queue.

## Classes

- `Patient`: Represents a patient with attributes for name, condition, and specialization.
- `Hospital`: Manages a collection of `Patient` objects with methods to add, remove, and prioritize patients.

## Usage

Run the program in a Python environment. You will be prompted with a menu:

1. **Add New Patient**: Enter details for a new patient.
2. **Print All Patients**: View a list of all patients, sorted by priority.
3. **Get Next Patient**: The system will print the next patient's details.
4. **Remove Leaving Patient**: Remove a patient from the system by name.
5. **End the Program**: Exit the program.

Input your choice and follow the on-screen instructions to manage patient records.

## Important Notes

- Patient condition is input as a number: `0` for Normal, `1` for Urgent, and `2` for Super Urgent.
- Ensure all inputs are valid to avoid unexpected behavior.

## Disclaimer

This system is a simple demonstration and should not be used in real medical environments without proper validation and adaptation to meet specific healthcare standards and regulations.
