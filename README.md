# BACT7501 Assessment 2 - Software Development Project: Requisition System
## Ethan Andrei Rivera | ID: 20251303

---

## Project Description and Features:
This software development project will be an improved version of the Requisition System from my Assessment 1.
This system allows users to:
- Enter a list of information for their requisition entries such as the Date, Staff ID, Staff Name, Items, Price, and Total that they’ll request for requisition.
- Automatically be assigned to a unique Requisition ID (global counter starts at 10000, then increment by 1 per new requisition entry) once they’ve entered their information.
- Automatically be assigned to a unique Reference Number (ID number +  last 3 digits of Requisition ID, e.g. ER94001) if their requisition request doesn’t exceed $500.
- Create multiple instances of requisition entries.
- Change the status of the requisition (Approved, Not Approved.)
- Display the requisition information of all entries.
- Display the requisition system’s statistics such as the total number of requisition entries, number of approved, pending, and approved entries respectively.
- Use an option menu to select which method would they like to use (add requisition, display requisitions, display data, etc.)

---
## Technologies and Tools Used
- Python
- Git
- GitHub
- Visual Studio Code
- Notepad
- readme.so
---

## Object-Oriented Programming Concepts Used

### Class
`RequisitionSystem`

---

### Attributes
The attributes used in this project are:

- `__requisitions`  

- `__approved_requisitions`  

- `__not_approved_requisitions`  

- `__pending_requisitions`  

- `counter`  

Each requisition entry also stores the following information using dictionary:

- `Date`
- `Staff_ID`
- `Staff_Name`
- `Requisition_ID`
- `Total`
- `Status`
- `Approval_Reference_Number`

---

### Methods
The methods used in this project are:

- `__init__()`

- `requisitionDetails()`

- `approveRequisition(total, staff_id, requisition_id)`

- `addRequistion()`  

- `respondRequisition()`  

- `viewRequisitions()`  

- `displayRequisition()`  

- `requisitionStatistics()`  

- `requisitionSystemMenu()`  

- `runRequisitionSystem()`  

---

## Sample Output

```text
============ Requisition System Menu ============
0.) Exit Requisition
1.) Add Requisition Entry
2.) View Requisition Entries
3.) Respond to Requisition Status
4.) Display Requisition Entry
5.) View Requisition System Statistics

Enter your choice: 1

============ Add Requisition Entry ============
Enter the date (DD/MM/YEAR): 30/06/2026
Enter your 4 Digit Staff ID: 1234
Enter your name: ethan rivera

Add items for the requisition.
Enter item name: Keyboard
Enter item price: $120
Add another item? (yes/no): yes
Enter item name: Mouse
Enter item price: $80
Add another item? (yes/no): no

============ Requisition Entry has been added! ============
Date: 30/06/2026
Staff ID: 1234
Staff Name: Ethan Rivera
Requisition ID: 10001
Total: 200.0
Status: Approved
Approval Reference Number: 1234001

============ Requisition System Menu ============
0.) Exit Requisition
1.) Add Requisition Entry
2.) View Requisition Entries
3.) Respond to Requisition Status
4.) Display Requisition Entry
5.) View Requisition System Statistics

Enter your choice: 5

============ Requisition System Statistics ============
Total Requisition Entries: 1
Total of Approved Requisition Entries: 1
Total of Not Approved Requisition Entries: 0
Total of Pending Requisition Entries: 0
