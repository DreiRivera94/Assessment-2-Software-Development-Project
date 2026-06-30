counter = 10000 # This is a global counter variable outsside of the class used for the requisition ID.

class requisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self): # Constructor Method

    self.__requisitions = [] # The private list to store the requisition entries

    # The private variables for the approved, not approvved, and pending that have 0 as their value. This will have value later once it increments and decrements. 
    self.__approved_requisitions = 0
    self.__not_approved_requisitions = 0
    self.__pending_requisitions = 0

  def requisitionDetails(self): # Method used to store the item and price details that the user enters

    # The item and price lists used 
    item_list = []
    price_list = []

    print("Add items for the requisition.")

    add_confirm = "yes"

    while add_confirm == "yes":
      item_name = input("Enter item name: ")
      item_price = float(input("Enter item price: $"))

      item_list.append(item_name)
      price_list.append(item_price)

      add_confirm = input("Add another item? (yes/no): ")

    total = sum(price_list)

    details = [item_list, price_list, total]

    return details

  def approveRequisition(self, total, staff_id, requisition_id): # Method to check if the requisition entry is approved or not
    if total < 500:
      status = "Approved"
      approval_reference_number = staff_id + str(requisition_id)[-3:]

    # If the total is $500 or more, it is pending for manager response
    else:
      status = "Pending"
      approval_reference_number = "Not available"

    approval_details = [status, approval_reference_number]

    return approval_details

  def addRequistion(self): # Method to add a requisition entry

    global counter

    print("\n============ Add Requisition Entry ============")

    date = input("Enter the date (DD/MM/YEAR): ") # Asks user to enter date
    staff_id = input("Enter your 4 Digit Staff ID: ") # Asks user to enter 4 digit staff ID
    staff_name = input("Enter your name: ").title() # Asks user to enter full name, used title to capitalize the first letter of each section of the name

    counter += 1
    requisition_id = counter  # Value for the requisition ID starts at 

    details = self.requisitionDetails()

    item_list = details[0]
    price_list = details[1]
    total = details[2]

    approval_details = self.approveRequisition(total, staff_id, requisition_id)

    status = approval_details[0]
    approval_reference_number = approval_details[1]

    if status == "Approved":
      self.__approved_requisitions += 1

    elif status == "Pending":
      self.__pending_requisitions += 1

    requisition = {"Date": date,
                   "Staff_ID": staff_id,
                   "Staff_Name": staff_name,
                   "Requisition_ID": requisition_id,
                   "Total": total,
                   "Status": 'Pending',
                   "Approval_Reference_Number": 'Not available'}
  
    self.__requisitions.append(requisition)

    print("\n============ Requisition Entry has been added! ============")
    print(f"Date: {requisition["Date"]}")
    print(f"Staff ID: {requisition["Staff_ID"]}")
    print(f"Staff Name: {requisition["Staff_Name"]}")
    print(f"Requisition ID: {requisition["Requisition_ID"]}")
    print(f"Total: {requisition["Total"]}")
    print(f"Status: {requisition["Status"]}")
    print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

    return total

  def respondRequisition(self): # Method to respond to requisition entry by changing the status (pending to approved or not approved)
    if len(self.__requisitions) == 0:
      print("No requisition entries found. Please try again later.")

    else:
      print("\n============ Requisition Entries ============")

      for index, requisition in enumerate(self.__requisitions):
        print(index + 1, "| Requisition ID:", requisition["Requisition_ID"], requisition["Total"], "| Status:", requisition["Status"])

      requisition_choice = input("Enter the requisition number to respond to: ")

      if requisition_choice >= 1 and requisition_choice <= len(self.__requisitions):
        selected_requisition = self.__requisitions[requisition_choice - 1]

        if selected_requisition["Status"] == "Pending":
          status_response = input("Enter response (approved/not approved): ")

          if status_response == "approved":
            selected_requisition["Status"] = "Approved"
            selected_requisition["Approval_Reference_Number"] = selected_requisition["Staff_ID"] + str(selected_requisition["Requisition_ID"])[-3:]

            self.__pending_requisitions -= 1
            self.__approved_requisitions += 1

            print("Requisition has been approved.")

          elif status_response == "not approved":
            selected_requisition["Status"] = "Not approved"
            selected_requisition["Approval_Reference_Number"] = "Not available"

            self.__pending_requisitions -= 1
            self.__not_approved_requisitions += 1

            print("Requisition has not been approved.")

          else:
            print("Invalid response. Please type approved or not approved.")

        else:
          print("This requisition is not pending anymore.")

      else:
        print("Invalid requisition number.")

  def viewRequisition(self): # Method to view all requisitions 
    if len(self.__requisitions) == 0:
      print("No requisition entries found.")

    else:
      
      print("\n============ Requisition Requests ============")

      for requisition in self.__requisitions:

        print(f"Date: {requisition["Date"]}")
        print(f"Staff ID: {requisition["Staff_ID"]}")
        print(f"Staff Name: {requisition["Staff_Name"]}")
        print(f"Requisition ID: {requisition["Requisition_ID"]}")
        print(f"Total: {requisition["Total"]}")
        print(f"Status: {requisition["Status"]}")
        print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

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

    print("\n============ Requisition System Statistics ============")
    print(f"Total Requisition Entries: {len(self.__requisitions)}")
    print(f"Total of Approved Requisition Entries: {self.__approved_requisitions}")
    print(f"Total of Not Approved Requisition Entries: {self.__pending_requisitions}")
    print(f"Total of Pending Requisition Entries: {self.__not_approved_requisitions}")

  def requisitionSystemMenu(self):
    print("\n============ Requisition System Menu ============")
    print("0.) Exit Requisition")
    print("1.) Add Requisition Entry")
    print("2.) View Requisition Entries")
    print("3.) Respond to Requisition Status")
    print("4.) Display Requisition Entry")
    print("5.) View Requisition System Statistics")

  def runRequisitionSystem(self): # The method used to run the requisition system starting with the menu.
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