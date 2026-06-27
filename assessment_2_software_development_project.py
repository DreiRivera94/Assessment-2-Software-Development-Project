class requisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self, date, staff_id, staff_name, requisition_id, total, approval_reference_number): # Constructor Method
    self.__requisitions = []
    self.__approved_requisitions = []
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
    if self.total < 500:
     self.status = "Approved"

    else:
      self.total = "Not Approved"

  def respondRequisition(self): # Method to respond to requisition entry by changing the status (pending to approved or not approved)
    pass

  def displayRequisition(self): # Method to display requistion information
    pass

  def requisition_statistics(self): # Method to display the statistics of the requistion system
    pass