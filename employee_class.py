import mysql.connector as mysql

# Creating Connections
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hr"
)

# Creating the DB table
db_cursor = db.cursor()

# Employee as a class
class Employee:
    # Constructing the defaults of the "Employee" class
    def __init__(self):
        self.employee_id      = 0
        self.employee_name    = " "
        self.employee_surname = " "
        self.employee_mail    = " "
        self.employee_phone   = " "
        self.employee_address = " "
        self.employee_salary  = 0

# Adding an employee via list in DB
    def add_employee(self):
        add_status = True
        while add_status:
            employee_name = str(input("Παρακαλώ πληκτρολογήστε το όνομα του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                      "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε 'ΕΞΟΔΟΣ': "))
            if employee_name == 'ΕΞΟΔΟΣ':
                break
            employee_surname = str(input("Παρακαλώ πληκτρολογήστε το επώνυμο του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                  "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε 'ΕΞΟΔΟΣ': "))
            if employee_name == 'ΕΞΟΔΟΣ':
                break
            employee_mail = str(input("Παρακαλώ πληκτρολογήστε το email του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                      "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε 'ΕΞΟΔΟΣ': "))
            if employee_mail == 'ΕΞΟΔΟΣ':
                break
            employee_phone = int(input("Παρακαλώ πληκτρολογήστε το τηλέφωνο του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                       "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε '0': "))
            if employee_phone == 0:
                break
            employee_address = str(input("Παρακαλώ πληκτρολογήστε τη διεύθυνση του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                     "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε 'ΕΞΟΔΟΣ': "))
            if employee_address == 'ΕΞΟΔΟΣ':
                break
            employee_salary = float(input("Παρακαλώ πληκτρολογήστε το μισθό του υπαλλήλου που θέλετε να προσθέσετε.\n"
                                        "Αν δεν επιθυμούσατε πρόσθεση υπαλλήλου, πληκτρολογήστε '0': "))
            if employee_salary == 0:
                break

            # Place all inputs into list (ID is Auto-Incremented)
            employee_details = (employee_name, employee_surname, employee_mail, employee_phone, employee_address,
                                employee_salary)

            # Query to add a row in DB
            add_query = "INSERT INTO `employees`(`employee_name`, `employee_surname`, `employee_mail`, `employee_phone`, " \
                        "`employee_address`, `employee_salary`) VALUES (%s, %s, %s, %s, %s, %s)"
            db_cursor.execute(add_query, employee_details)
            db.commit()
            print(db_cursor.rowcount, " record added successfully in our employees table.")

            # Asking the user to continue viewing
            add_end = str(input("Θέλετε να συνεχίσετε την πρόσθεση υπαλλήλου; \n Πατήστε 'y' για να συνεχίσετε, "
                                 "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
            while add_end not in 'YyNn':
                add_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                     "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
            else:
                if add_end in 'Yy':
                    continue
                else:
                    add_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                         "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                    if add_end in 'Yy':
                        break
                    else:
                        continue


# Viewing an employee's details from DB
    def view_details(self):
        db_cursor = db.cursor()
        view_option = True
        while view_option:
            #Storing the name/surname inputs in tuple
            name_check = str(input("Eπιλέξτε το όνομα του υπαλλήλου που θα θέλατε να δείτε τα στοιχεία του.\n"
                                      "Αν δεν επιθυμείτε προβολή στοιχείων υπαλλήλου, πληκτρολογήστε 'Ε' για έξοδο: "))
            while name_check.isnumeric():
                name_check = str(input("Λάθος χαρακτήρας. Eπιλέξτε το όνομα του υπαλλήλου που θα θέλατε να δείτε τα "
                                       "στοιχεία του.\nΑν δεν επιθυμείτε προβολή στοιχείων υπαλλήλου, "
                                       "πληκτρολογήστε 'Ε' για έξοδο: "))
            if name_check == 'Ε':
                break
            surname_check = str(input("Eπιλέξτε το επώνυμο του υπαλλήλου που θα θέλατε να δείτε τα στοιχεία του.\n"
                                          "Αν δεν επιθυμείτε προβολή στοιχείων υπαλλήλου, πληκτρολογήστε 'Ε' για έξοδο: "))
            while surname_check.isnumeric():
                surname_check = str(input("Λάθος χαρακτήρας. Eπιλέξτε το επώνυμο του υπαλλήλου που θα θέλατε να δείτε τα "
                                       "στοιχεία του.\nΑν δεν επιθυμείτε προβολή στοιχείων υπαλλήλου, "
                                       "πληκτρολογήστε 'Ε' για έξοδο: "))
            if surname_check == '0':
                break
            employee_check = (name_check, surname_check)

            # View Query based on a name/surname combo + Printing the results fetched through a for loop and a dictionary
            view_all_query = "SELECT * FROM `employees` WHERE `employee_name` = (%s) AND `employee_surname` = (%s)"
            db_cursor.execute(view_all_query, employee_check)
            result = db_cursor.fetchall()
            dic = {}
            for i in result:
                dic[i[0]] = i[0:]
                print(dic[i[0]])

            # Asking the user to continue viewing
            view_end = str(input("Θέλετε να πραγματοποιήσετε άλλη αναζήτηση; \n Πατήστε 'y' "
                                 "για να συνεχίσετε, ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
            while view_end not in 'YyNn':
                view_end = str(input("Λάθος χαρακτήρας. Θέλετε να πραγματοποιήσετε άλλη αναζήτηση; \n Πατήστε 'y' "
                                     "για να συνεχίσετε, ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
            else:
                if view_end in 'Yy':
                    continue
                else:
                    view_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y'  για να βγείτε από "
                                         "το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε:"))
                    if view_end in 'Yy':
                        break
                    else:
                        continue


# Editing the details of an employee
    def edit_member(self):
        edit_status = True
        while edit_status:

            # Call the view function to print the entries that have the name/surname asked
            Employee.view_details(self)

            # If many users have the same name/surname combo, user gets to choose which one to edit
            id_to_change = str(input("Πληκτρολογήστε τον κωδικό που αντιστοιχεί στον υπάλληλο του οποίου "
                                     "τα στοιχεία που θα θέλατε να αλλάξετε: "))
            choice = str(input(" 1. Όνομα \n 2. Επώνυμο \n 3. Email \n 4. Τηλέφωνο \n 5. Διεύθυνση \n 6. Μισθός \n 7. Όλα \n"
                               "Πληκτρολογήστε τον αριθμό που αντιστοιχεί στο στοιχείο που θα θέλατε να αλλάξετε: "))

            # Input Security
            while choice not in '1234567':
                choice = str(input("Λάθος αριθμός/χαρακτήρας.\n"
                                   " 1. Όνομα \n 2. Επώνυμο \n 3. Email \n 4. Τηλέφωνο \n 5. Διεύθυνση \n 6. Μισθός \n 7. Όλα \n"
                                   "Πληκτρολογήστε τον αριθμό που αντιστοιχεί στο στοιχείο που θα θέλατε να αλλάξετε: "))
            else:
                # Choice 1 - Edit the Employee's name
                if choice == '1':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_name` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                                 "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 2 - Edit the Employee's surname
                elif choice == '2':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_surname` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(
                                input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 3 - Edit the Employee's email
                elif choice == '3':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_mail` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(
                                input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 4 - Edit the Employee's phone number
                elif choice == '4':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_phone` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(
                                input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 5 - Edit the Employee's address
                elif choice == '5':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_address` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(
                                input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 6 - Edit the Employee's salary (for those who have stayed in the same position for more than 3 years)
                elif choice == '6':
                    choice = str(input("\nΠαρακαλώ δώστε τα σωστά δεδομένα: "))
                    choice_tuple = (choice, id_to_change)  # Storing the values in a tuple
                    edit_query = "UPDATE `employees` SET `employee_salary` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue
                # Choice 7 - Edit the Employee's details
                elif choice == '7':
                    choice_1 = str(input("\nΠαρακαλώ δώστε τo σωστό όνομα: "))
                    choice_2 = str(input("\nΠαρακαλώ δώστε τo σωστό επώνυμο: "))
                    choice_3 = str(input("\nΠαρακαλώ δώστε τo σωστό e-mail: "))
                    choice_4 = int(input("\nΠαρακαλώ δώστε τo σωστό τηλέφωνο: "))
                    choice_5 = str(input("\nΠαρακαλώ δώστε τη σωστή διεύθυνση: "))
                    choice_6 = float(input("\nΠαρακαλώ δώστε τo σωστό μισθό: "))
                    # Storing the values and the id to be changed in a tuple
                    choice_tuple = (choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, id_to_change)
                    edit_query = "UPDATE `employees` SET `employee_name` = (%s), `employee_surname` = (%s), " \
                                 "`employee_mail` = (%s), `employee_phone` = (%s), `employee_address` = (%s), " \
                                 "`employee_salary` = (%s) WHERE `employee_id` = (%s)"
                    db_cursor.execute(edit_query, choice_tuple)
                    db.commit()

                    # Ensuring that our UPDATE query did the work
                    debug_update_query = "SELECT * FROM `employees` WHERE `employee_id` = %s"
                    db_cursor.execute(debug_update_query, (id_to_change,))
                    result = db_cursor.fetchall()
                    dic = {}
                    for i in result:
                        dic[i[0]] = i[0:]
                        print(dic[i[0]])

                    # Asking user to continue editing or abort
                    edit_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                         "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
                    while edit_end not in 'YyNn':
                        edit_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                             "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
                    else:
                        if edit_end in 'Yy':
                            continue
                        else:
                            edit_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                      "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                            if edit_end in 'Yy':
                                break
                            else:
                                continue

# Employee Promotion (user-defined salary)
    def promotion(self):
        db_cursor = db.cursor()
        # Call the view function to print the entries that have the name/surname asked
        Employee.view_details(self)

        # If many users have the same name/surname combo, user gets to choose which one to promote
        id_to_change = str(input("Πληκτρολογήστε τον κωδικό που αντιστοιχεί στον υπάλληλο του οποίου "
                                 "τα στοιχεία που θα θέλατε να αλλάξετε: "))
        edit_details = (id_to_change,)
        promo_query = "SELECT * FROM `employees` WHERE `employee_id` = (%s)"
        db_cursor.execute(promo_query, edit_details)
        result = db_cursor.fetchone()
        print(result)
        result = list(result)

        # Promoting the employee by input salary
        result[6] = float(input("Παρακαλώ εισάγετε το νέο μισθό του προαχθέντος υπαλλήλου: "))
        promo_query_2 = "UPDATE `employees` SET `employee_salary`= (%s)"
        result2 = (result[6],)
        db_cursor.execute(promo_query_2, result2)
        db.commit()
        print("Προαγωγή επιτυχής.")


# Delete Employee from Registry
    def delete_member(self):
        db_cursor = db.cursor()
        delete_status = True
        while delete_status:
            Employee.view_details(self)
            id_to_delete = str(input("Πληκτρολογήστε τον κωδικό που αντιστοιχεί στον υπάλληλο του οποίου "
                                 "τα στοιχεία που θα θέλατε να αλλάξετε: "))
            delete_details = (id_to_delete,)
            pre_delete = "SELECT * FROM `employees` WHERE `employee_id` = (%s)"
            db_cursor.execute(pre_delete, delete_details)
            result = db_cursor.fetchall()
            print(result)
            # Security against unwanted deletion
            choice = str(input("\nΕίστε σίγουρος/-η ότι επιθυμείτε να διαγραφεί ο συγκεκριμένος υπάλληλος από "
                               "το μητρώο; \nΠληκτρολογήστε 'y' για επιβεβαίωση, ή 'n' για απόρριψη."))
            while choice not in 'YyNn':
                choice = str(input("Παρακαλώ πληκτρολογήστε 'y' για επιβεβαίωση, ή 'n' για απόρριψη."))
            if choice in 'Yy':
                delete_query = "DELETE FROM employees WHERE `employee_id` = (%s)"
                db_cursor.execute(delete_query, delete_details)
                db.commit()
                print("Ο υπάλληλος διεγράφη επιτυχώς από το μητρώο!")
                db_cursor.close()
                break
            else:
                choice = str(input("Επιθυμείτε να επιστρέψετε στο αρχικό μενού;"
                                   "\nΠληκτρολογήστε 'y' για επιβεβαίωση, ή 'n' για απόρριψη."))
                while choice not in 'YyNn':
                    choice = str(input("Παρακαλώ πληκτρολογήστε 'y' για επιβεβαίωση, ή 'n' για απόρριψη."))
                if choice in 'Yy':
                    break
                else:
                    continue

# Search Employee by ID
    def browse_member(self):
        db_cursor = db.cursor()
        browse_status = True
        while browse_status:
            id_check = str(input("Eπιλέξτε τον κωδικό του υπαλλήλου που θα θέλατε να δείτε τα στοιχεία του.\n"
                                   "Αν δεν επιθυμείτε αναζήτηση στοιχείων υπαλλήλου, πληκτρολογήστε '0': "))
            # If input is alphabetic - Security Measure
            while id_check.isalpha():
                id_check = str(input("Eπιλέξτε τον αριθμητικό κωδικό του υπαλλήλου που θα θέλατε να δείτε τα στοιχεία του.\n"
                                     "Αν δεν επιθυμείτε αναζήτηση στοιχείων υπαλλήλου, πληκτρολογήστε '0': "))
            search_query = "SELECT * FROM `employees` WHERE `employee_id` = (%s)"
            db_cursor.execute(search_query, (id_check,))
            result = db_cursor.fetchall()
            dic = {}
            for i in result:
                dic[i[0]] = i[0:]
                print(dic[i[0]])
            # Continue Browsing or Return to Menu
            browse_end = str(input("Θέλετε να συνεχίσετε την επεξεργασία; \n Πατήστε 'y' για να συνεχίσετε, "
                                 "ή 'n' για να βγείτε από το μενού επεξεργασίας: "))
            while browse_end not in 'YyNn':
                browse_end = str(input("Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να παραμείνετε στο μενού "
                                     "επεξεργασίας ή το γράμμα 'n' για να βγείτε από το μενού επεξεργασίας:"))
            else:
                if browse_end in 'Yy':
                    continue
                else:
                    browse_end = str(input("Είστε σίγουρος; Παρακαλώ επιλέξτε ανάμεσα στο γράμμα 'y' για να βγείτε "
                                         "από το μενού επεξεργασίας και το γράμμα 'n' για να συνεχίσετε: "))
                    if browse_end in 'Yy':
                        break
                    else:
                        continue