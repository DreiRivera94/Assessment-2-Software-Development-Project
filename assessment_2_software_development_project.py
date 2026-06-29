class requisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self, date, staff_id, staff_name, requisition_id, total, approval_reference_number): # Constructor Method

    self.__requisitions = []

    self.__approved_requisitions = []
    self.__not_approved_requisitions = []
    self.__pending_requisitions = []
    self.__item_list = []
    self.__price_list = []

    self.date = date
    self.staff_id = staff_id
    self.staff_name = staff_name
    self.requisition_id = requisition_id
    self.total = total
    self.approval_reference_number = approval_reference_number

  def addRequistion(self): # Method to add a requisition entry

    self.date = input("Enter the date (DD/MM/YEAR): ") # Asks user to enter date

    self.staff_id = input("Enter your 4 Digit Staff ID: ") # Asks user to enter 4 digit staff ID

    self.staff_name = input("Enter your name: ").title # Asks user to enter full name, used title to capitalize the first letter of each section of the name

    self.requisition_id = 10000 + counter # Value for the requisition ID starts at 

    for requisition in self.__requisitions: #Per new requisition, the counter will increment by 1 to allow each requisition ID to be unique
      counter =+ 1

    self.total = int(input("Enter your total amount the you would like to requisite: $"))
    
    self.approval_reference_number = self.staff_id + self.requisition_id[-3:]

    requisition = {"Date": self.date,
                   "Staff_ID": self.staff_id,
                   "Staff_Name": self.staff_name,
                   "Requisition_ID": self.requisition_id,
                   "Total": self.total,
                   "Status": 'Pending',
                   "Approval_Reference_Number": 'Not available'}
  
    self.__requisitions.append(requisition)

    print(f"Requisition {self.requisition_id} has been added to the system.")

  def viewRequisition(self): # Method to view all requisitions 
    if len(self.__requisitions) == 0:
      print("No requisition entries found.")

    else:
      
      print("-------------------")

      print("Requisition Requests")

      print("-------------------")

      for requisition in self.__requisitions:

        print(f"Date: {requisition["Date"]}")
        print(f"Staff ID: {requisition["Staff_ID"]}")
        print(f"Staff Name: {requisition["Staff_Name"]}")
        print(f"Requisition ID: {requisition["Requisition_ID"]}")
        print(f"Total: {requisition["Total"]}")
        print(f"Status: {requisition["Status"]}")
        print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

        print("-------------------")

  def approveRequisition(self): # Method to check if the requisition entry is approved or not
    if self.total < 500:
     self.status = "Approved"

    else:
      self.total = "Not Approved"

  def respondRequisition(self): # Method to respond to requisition entry by changing the status (pending to approved or not approved)
    if len(self.__requisitions) == 0:
      print("No requisition entries found. Please try again later.")

    else:
      for requisition in self.__requisitions:
        print(f"{requisition + 1} | {requisition["Requisition_ID"]} | Status: {requisition["Status"]}")

      requisition_choice = input("Enter your selected requisition ID: ")

      if requisition_choice >= 1 and requisition_choice <= len(requisition):
        selected_requisition = self.__requisition[requisition_choice - 1]

        if selected_requisition["Status"] == "Pending":
          print("This requisition entry is pending")

        else:
          selected_requisition["Status"] = "Approved"
          self.__approved_requisitions += 1
          print(f"{selected_requisition["Requisition_ID"]} has been changed to approved.")

      else:
        print("Invalid requisition ID, please try again.")
  
  def displayRequisition(self): # Method to display a specific requistion information by entering the requesition ID
    if len(self.__requisitions) == 0:
      print("No requisition entries found.")

    else:
      selected_requisition = input("To display a requisition entry, please enter its corresponding requisition ID: ")

      for requisition in self.__requisitions:
        if selected_requisition == str(requisition["Requisition_ID"]):

          print("-------------------")
          print(f"Requisition ID: {selected_requisition} has been found.")
          print("-------------------")

          print(f"Date: {requisition["Date"]}")
          print(f"Staff ID: {requisition["Staff_ID"]}")
          print(f"Staff Name: {requisition["Staff_Name"]}")
          print(f"Total: {requisition["Total"]}")
          print(f"Status: {requisition["Status"]}")
          print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

          return
      
      print(f"Sorry, requisition number {selected_requisition} has not been found. Please try again.")
      print("-------------------")

  def requisitionStatistics(self): # Method to display the statistics of the requistion system
    total_number_requisitions = len(self.__requisitions)
    total_number_approved = len(self.__approved_requisitions)
    total_number_not_approved = len(self.__not_approved_requisitions)
    total_number_pending = len(self.__pending_requisitions)

    print("----------- Requisition System Statistics -----------")
    print(f"Total Requisition Entries: {total_number_requisitions}")
    print(f"Total of Approved Requisition Entries: {total_number_approved}")
    print(f"Total of Not Approved Requisition Entries: {total_number_not_approved}")
    print(f"Total of Pending Requisition Entries: {total_number_pending}")

  def requisitionSystemMenu(self):
    print("----------- Requisition System Menu -----------")
    print("0.) Exit Requisition")
    print("1.) Add Requisition Entry")
    print("2.) View Requisition Entries")
    print("3.) Respond to Requisition Status")
    print("4.) Display Requisition Entry")
    print("5.) View Requisition System Statistics")

  def runRequisitionSystem(self):
    while True:
      self.requisitionSystemMenu()
      menu_choice = input("Enter your choice: ")

      if menu_choice == "0":
        print("Thank you for using the Requisition System. Now Exiting.")
        break

      elif menu_choice == "1":
        self.addRequistion()

      elif menu_choice == "2":
        self.viewRequisition()

      elif menu_choice == "3":
        self.respondRequisition()

      elif menu_choice == "4":
        self.displayRequisition()

      elif menu_choice == "5":
        self.requisitionStatistics()

      else:
        print("Invalid choice. Please choose a number from 0 - 5.")

requisition_system = requisitionSystem()
requisition_system.runRequisitionSystem()