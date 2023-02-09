# Importing the Employee class file (for code readability)
from employee_class import Employee as employee

# Main Program // Menu as a dictionary - Generated through a for loop function
menu_dict = {
    1: 'Προσθήκη Υπαλλήλου',
    2: 'Προβολή Στοιχείων Υπαλλήλου',
    3: 'Επεξεργασία Υπαλλήλου',
    4: 'Προαγωγή Υπαλλήλου (ΣΧΟΛΙΟ: Αφορά αύξηση μισθού)',
    5: 'Διαγραφή Υπαλλήλου',
    6: 'Αναζήτηση Υπαλλήλου',
    7: 'Έξοδος από το πρόγραμμα'
}


def print_menu():
    for key in menu_dict.keys():
        print(key, ': ', menu_dict[key])


program_status = True
while program_status:
    employee_obj = employee()
    # Printing the menu
    print(f"Καλώς ήρθατε στο πρόγραμμα διαχείρισης υπαλλήλων 'HR-G6'.\n")
    print_menu()
    menu_input = str(input("\nΠαρακαλείστε να γράψετε τον αριθμό που επιθυμείτε,"
                           " για να προχωρήσετε στην αντίστοιχη επιλογή: "))
    # Defensive measure against invalid menu inputs
    while menu_input not in '1234567':
        menu_input = str(input("Λάθος κωδικός καταχώρησης. Παρακολώ πληκτρολογήστε τον αριθμό "
                               "που αντιστοιχεί στην επιθυμητή ρύθμιση: "))
    # Menu Options - Add Member
    if menu_input == '1':
        employee_obj.add_employee()
    # Menu Options - View Member Details
    if menu_input == '2':
        employee_obj.view_details()
    # Menu Options - Edit Employee
    if menu_input == '3':
        employee_obj.edit_member()
    # Menu Options - Promote Employee
    if menu_input == '4':
        employee_obj.promotion()
    # Menu Options - Delete Member from Registry
    if menu_input == '5':
        employee_obj.delete_member()
    # Menu Options - Browse Details
    if menu_input == '6':
        employee_obj.browse_member()
    # Exit Program Option
    if menu_input == '7':
        exit()
