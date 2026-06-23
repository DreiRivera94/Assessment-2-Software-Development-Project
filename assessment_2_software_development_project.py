class requisitionSystem: # Class to encapsulate methods and parameters for requistion system
  def __init__(self): # Constructor Method
    self.__requisitions = []

  def addRequistion(self): # Method to add a requisition entry

    date = input("Enter the date: (DD/MM/YEAR)")

    staff_id = input("Enter your 4 Digit Staff ID: ")

    staff_name = input("Enter your name: ")

    staff_name = staff_name.title

    requisition_id = 10000 + 1

    total = int(input("Enter your total amount the you would like to requisite: "))
    
    approval_reference_number = staff_id + requisition_id[2:]

    requisition = {"Date": date,
                   "Staff ID": staff_id,
                   "Staff Name": staff_name,
                   "Requisition ID": requisition_id,
                   "Total": total,
                   "Status": 'Pending',
                   "Approval Reference Number": approval_reference_number}
  
    self.__requisitions.append(requisition)

    print(f"Requisition {requisition_id} has been added to the system.")

  def approveRequisition(self): # Method to approve requisition entry
    pass

  def respondRequisition(self): # Method to respond to requisition entry 
    pass

  def displayRequisition(self): # Method to display requistion information
    pass

  def requisition_statistics(self): # Method to display the statistics of the requistion system
    pass