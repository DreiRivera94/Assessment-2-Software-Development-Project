class requisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self): # Constructor Method
    self.__requisitions = []
    self.__item_list = []
    self.__price_list = []

  def addRequistion(self): # Method to add a requisition entry

    date = input("Enter the date (DD/MM/YEAR): ") # Asks user to enter date

    staff_id = input("Enter your 4 Digit Staff ID: ") # Asks user to enter 4 digit staff ID

    staff_name = input("Enter your name: ").title # Asks user to enter full name, used title to capitalize the first letter of each section of the name

    requisition_id = 10000 + counter # Value for the requisition ID starts at 

    for requisition in self.__requisitions: #Per new requisition, the counter will increment by 1 to allow each requisition ID to be unique
      counter =+ 1

    total = int(input("Enter your total amount the you would like to requisite: $"))
    
    approval_reference_number = staff_id + requisition_id[-3:]

    requisition = {"Date": date,
                   "Staff_ID": staff_id,
                   "Staff_Name": staff_name,
                   "Requisition_ID": requisition_id,
                   "Total": total,
                   "Status": 'Pending',
                   "Approval_Reference_Number": approval_reference_number}
  
    self.__requisitions.append(requisition)

    print(f"Requisition {requisition_id} has been added to the system.")

  def viewRequisition(self):
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
    pass

  def respondRequisition(self): # Method to respond to requisition entry by changing the status (pending to approved or not approved)
    pass

  def displayRequisition(self): # Method to display requistion information
    pass

  def requisition_statistics(self): # Method to display the statistics of the requistion system
    pass