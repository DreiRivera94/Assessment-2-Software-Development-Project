counter = 10000 # This is a global counter variable outsside of the class used for the requisition ID.

class RequisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self): # Constructor Method

    self.__requisitions = [] # The private list to store the requisition entries

    # The private variables for the approved, not approvved, and pending that have 0 as their value. This will have value later once it increments and decrements. 
    self.__approved_requisitions = 0
    self.__not_approved_requisitions = 0
    self.__pending_requisitions = 0

  def requisitionDetails(self): # Method used to store the item and price details that the user enters.

    # The item and price lists used 
    item_list = []
    price_list = []

    print("Add items for the requisition.")

    # Used the same while loop from assessment 1 to loop through the user entering a item name and price.  
    add_confirm = "yes"

    while add_confirm == "yes":
      item_name = input("Enter item name: ")
      item_price = float(input("Enter item price: $")) # Typecasted to float for decimal points on price.

      #Used append to store the items and prices into the lists.
      item_list.append(item_name)
      price_list.append(item_price)

      add_confirm = input("Add another item? (yes/no): ")

    # Used sum method to get the total of all the price variables in the item_price list.
    total = sum(price_list)

    # Stored the lists and total into a new list called details.
    details = [item_list, price_list, total]

    # Allows me to call the value in the details list.
    return details

  def approveRequisition(self, total, staff_id, requisition_id): # Method to check if the requisition entry is approved or not. Embedded the parameters for total, staff ID, and requisition ID
    if total < 500:
      status = "Approved"
      approval_reference_number = staff_id + str(requisition_id)[-3:] #To get the reference number, I added the string values of the Staff ID and the last 3 digits of the requisition ID. Typecasted it as a string to get the index values from -3 to -1.

    # If the total is $500 or more, it is pending for manager response
    else:
      status = "Pending"
      approval_reference_number = "Not available"

    approval_details = [status, approval_reference_number] # 

    # Allows me to call the value in the approval_details list.
    return approval_details

  def addRequistion(self): # Method to add a requisition entry

    global counter # I called the counter outside the class by using global keyword. Now I can use it for this method.

    print("\n============ Add Requisition Entry ============")

    date = input("Enter the date (DD/MM/YEAR): ") # Asks user to enter date
    staff_id = input("Enter your 4 Digit Staff ID: ") # Asks user to enter 4 digit staff ID
    staff_name = input("Enter your name: ").title() # Asks user to enter full name, used title to capitalize the first letter of each section of the name

    counter += 1
    requisition_id = counter  # The value for the requisition ID will increment by 1 per new requisition entry.

    details = self.requisitionDetails() # Called the requisitionDetails method and assigned it as variable "details"

    total = details[2] # Assigned index 2 of details as the "total" variable

    approval_details = self.approveRequisition(total, staff_id, requisition_id)  # Called the approveRequisition and assigned it as variable "approval_details."

    status = approval_details[0]  # Assigned index 0 of approval_details as the "status" variable.
    approval_reference_number = approval_details[1] # Assigned index 1 of approval_details as the "approval_reference_number" variable.

    if status == "Approved":
      self.__approved_requisitions += 1

    elif status == "Pending":
      self.__pending_requisitions += 1

    else:
      status == "Not Approved"
      self.__not_approved_requisitions += 1

    # Dicitionary to store all information of a single requisition request.
    requisition = {"Date": date,
                   "Staff_ID": staff_id,
                   "Staff_Name": staff_name,
                   "Requisition_ID": requisition_id,
                   "Total": total,
                   "Status": status,
                   "Approval_Reference_Number": approval_reference_number}
  
    # Used append to store the requisition into the private list.
    self.__requisitions.append(requisition)

    # Print all information
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

      print("\n============================================")
      print("No requisition entries found. Please try again later.")

    else:
      print("\n============ Requisition Entries ============")

      # Loop to enumerate each requisition entry while displaying the ID, total, and status.
      for index, requisition in enumerate(self.__requisitions):
        print(index + 1, "| Requisition ID:", requisition["Requisition_ID"], "| Total:", requisition["Total"], "| Status:", requisition["Status"])

      print("\n============================================")
      requisition_choice = input("Enter the corresponding number of the requisition entry that you would like to respond to: ")

      # Typecasting the choice into integer for it to be viable for the if else conditions.
      if requisition_choice.isdigit():
        requisition_choice = int(requisition_choice)

        if requisition_choice >= 1 and requisition_choice <= len(self.__requisitions):
          selected_requisition = self.__requisitions[requisition_choice - 1]

          if selected_requisition["Status"] == "Pending":

            print("\n============================================")
            status_response = input("Enter response (approved/not approved): ").lower()

            # Status will be approved and approval reference number will be available.
            if status_response == "approved":
              selected_requisition["Status"] = "Approved"
              selected_requisition["Approval_Reference_Number"] = selected_requisition["Staff_ID"] + str(selected_requisition["Requisition_ID"])[-3:]

              # Decrement pending and increment approved
              self.__pending_requisitions -= 1
              self.__approved_requisitions += 1

              print("\n============================================")
              print("Requisition has been approved.")

            # Status will not be approved and reference number won't be available.
            elif status_response == "not approved":
              selected_requisition["Status"] = "Not Approved"
              selected_requisition["Approval_Reference_Number"] = "Not available"

              # Decrement pending and incement not approved
              self.__pending_requisitions -= 1
              self.__not_approved_requisitions += 1

              print("\n============================================")
              print("Requisition has not been approved.")

            else:
              print("\n============================================")
              print("Invalid response. Please type approved or not approved.")

          else:
            print("\n============================================")
            print("This requisition is not pending anymore.")

        else:
          print("\n============================================")
          print("Invalid requisition number.")

      else:
        print("\n============================================")
        print("Invalid requisition number.")

  def viewRequisitions(self): # Method to view all requisitions 
    if len(self.__requisitions) == 0:

      print("\n============================================")
      print("No requisition entries found. Please try again.")

    else:
      
      print("\n============ Requisition Requests ============")

      # Loop to display all requisitions inside the private list.
      for requisition in self.__requisitions:

        # Print all information
        print(f"Date: {requisition["Date"]}")
        print(f"Staff ID: {requisition["Staff_ID"]}")
        print(f"Staff Name: {requisition["Staff_Name"]}")
        print(f"Requisition ID: {requisition["Requisition_ID"]}")
        print(f"Total: {requisition["Total"]}")
        print(f"Status: {requisition["Status"]}")
        print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

        print("\n============================================")

  def displayRequisition(self): # Method to display a specific requistion information by entering the requesition ID
    if len(self.__requisitions) == 0:

      print("\n============================================")
      print("No requisition entries found.")

    else:
      print("\n============================================")
      selected_requisition = input("To display a requisition entry, please enter its corresponding requisition ID: ")

      # Loop to look through the private list and see if the selected requisition exists.
      for requisition in self.__requisitions:
        if selected_requisition == str(requisition["Requisition_ID"]):

          print("\n============ Requisition Entry has been found! ============")

          # Print all information
          print(f"Date: {requisition["Date"]}")
          print(f"Staff ID: {requisition["Staff_ID"]}")
          print(f"Staff Name: {requisition["Staff_Name"]}")
          print(f"Total: {requisition["Total"]}")
          print(f"Status: {requisition["Status"]}")
          print(f"Approval Reference Number: {requisition["Approval_Reference_Number"]}")

          return
      
      print("\n============================================")
      print(f"Sorry, requisition number {selected_requisition} has not been found. Please try again.")

  def requisitionStatistics(self): # Method to display the statistics of the requistion system

    print("\n============ Requisition System Statistics ============")
    print(f"Total Requisition Entries: {len(self.__requisitions)}")
    print(f"Total of Approved Requisition Entries: {self.__approved_requisitions}")
    print(f"Total of Not Approved Requisition Entries: {self.__pending_requisitions}")
    print(f"Total of Pending Requisition Entries: {self.__not_approved_requisitions}")

  def requisitionSystemMenu(self): # Method to display the menu selection.
    print("\n============ Requisition System Menu ============")

    print("Kia Ora! Welcome to the Home Menu of the Requisition System.")

    print("0.) Exit Requisition")
    print("1.) Add Requisition Entry")
    print("2.) View Requisition Entries")
    print("3.) Respond to Requisition Status")
    print("4.) Display Requisition Entry")
    print("5.) View Requisition System Statistics")

  def runRequisitionSystem(self): # The method used to run the requisition system starting with the menu.
    while True:
      self.requisitionSystemMenu() # Called the menu method.
      menu_choice = input("Enter your choice: ") # User will enter a number from 0 - 5 to navigate through the requisition system.

      if menu_choice == "0":
        print("\n============================================")
        print("Thank you for using the Requisition System. Now Exiting.")
        break

      # The user can use the methods by entering its corresponding number.
      elif menu_choice == "1":
        self.addRequistion()

      elif menu_choice == "2":
        self.viewRequisitions()

      elif menu_choice == "3":
        self.respondRequisition()

      elif menu_choice == "4":
        self.displayRequisition()

      elif menu_choice == "5":
        self.requisitionStatistics()

      else:
        print("\n============================================")
        print("Invalid choice. Please choose a number from 0 - 5.")

# Object to call the Class and to initialize the method to run the requisition system.
start_requisition_system = RequisitionSystem()
start_requisition_system.runRequisitionSystem()