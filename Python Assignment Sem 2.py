import os
from datetime import datetime
from collections import defaultdict


def login():
    usernames = ["Jimmy", "Visha", "Zoe", "SzyQi"]  # set username list and store the username data
    passwords = ["Jim01", "Vis02", "Zoe03", "SzyQi04"]  # set passwords list and store the passwords data
    num_attempts = 0  # set number of attempts to 0

    while num_attempts < 3:  # set number of attempts less than 3
        username = input("Enter username: ")  # read username input from user

        if username in usernames:  # if username input from user match with username data in username list
            password = input("Enter password: ")  # read password input from user

            if password == passwords[usernames.index(username)]:  # if password match with password list with the
                print("Login successfully.")  # same index of username list, login successful
                return True

            else:
                num_attempts += 1  # 3 times attempt
                print("Invalid password. Please try again. 3 times failure will lead to termination")

        else:
            num_attempts += 1
            print("Invalid username. Please try again. 3 times failure will lead to termination.")

    print("3 times failure. Program terminated.")
    return False


def inventory_creation():
    table1 = [
        ["Item Code", "Item Name", "Supplier Code", "Quantity in stock(boxes)"],
        ["HC", "Head Cover", "SE1", 100],
        ["FS", "Face Shield", "SE2", 100],
        ["MS", "Mask", "SE1", 100],
        ["GL", "Gloves", "SE3", 100],
        ["GW", "Gown", "SE3", 100],
        ["SC", "Shoe Covers", "SE4", 100]
    ]  # set nested list - table1 and insert all data of Item into sublist

    table_supplier = [
        ["Supplier Code", "Contact Number", "Email Address"],
        ["SE1", "0178853900", "sc1@yahoo.com"],
        ["SE2", "0127630749", "sc2@gmail.com"],
        ["SE3", "0138762946", "sc3@hotmail.com"],
        ["SE4", "0168374924", "sc4@outlook.com"]
    ]  # set nested list - table_supplier and insert all data of suppliers into sublist

    if not os.path.exists("ppe.txt"):
        with open("ppe.txt", "w") as f:
            for sublist in table1:
                line = ', '.join(map(str, sublist))
                # set line to join the sublist of table1 separated with comma after convert elements into string

                f.write(line + '\n')  # write the line into ppe.txt file with new line

    if not os.path.exists("suppliers.txt"):
        with open("suppliers.txt", "w") as f:
            for sublist in table_supplier:
                line = ', '.join(map(str, sublist))
                # set line to join the sublist of table_supplier separated with comma after convert into string

                f.write(line + '\n')  # write the line into suppliers.txt file with new line


def inventory_update():
    print("\n---Update Inventory---\n"  # print options for user to choose
          "1. Supplier details\n"
          "2. Hospital details\n"
          "3. Quantity of items\n"
          "4. Exit\n")

    update_choice = input("Enter the number of function: ")  # read the number input from user

    if update_choice not in ["1", "2", "3", "4"]:
        print("Invalid function. Please try again.")
        return inventory_update()

    elif update_choice == "1":
        try:
            with open("suppliers.txt", "r") as f:  # open suppliers.txt file with read function
                lines = f.readlines()  # set lines to read all the lines in suppliers.txt file
                for line in lines:
                    print(line.strip())
                    # print every line of text from suppliers.txt file, with leading and trailing whitespace removed

            supplier_edit = input("Enter the supplier code you wish to make changes: ").upper()
            # read the supplier code input from user, make the input become CAPITAL LETTER

            if supplier_edit in ["SE1", "SE2", "SE3", "SE4"]:
                found = False
                for i, line in enumerate(lines):
                    # Loops through each line in lines, where i is the index of the current line

                    if supplier_edit in line:  # check if the supplier code input from user is in the line
                        found = True
                        parts = line.strip().split(", ")
                        print("\nWhich part would you like to edit?\n"  # print options for user to choose
                              "1. Contact Number\n"
                              "2. Email Address\n"
                              )
                        details_choice = input("Enter the number of details need to be edit: ")
                        #  read the options from user

                        if details_choice == "1":
                            parts[1] = input("Enter the new contact number: ")
                            # change the data of contact number match with the supplier code given

                        elif details_choice == "2":
                            parts[2] = input("Enter the new email address: ")
                            # change the data of email address match with the supplier code given

                        else:
                            print("Invalid choice. Please try again.")
                            return

                        lines[i] = ", ".join(parts) + "\n"
                        # Joins the updated parts back into a single string, separated with comma and add new line
                        break

                if found:
                    with open("suppliers.txt", "w") as f:
                        f.writelines(lines)  # write the edited data into suppliers.txt file
                        print("The file has been updated.")

                else:
                    print(f"No matches found for {supplier_edit}")

            else:
                print("Invalid supplier code. Please try again.")
                return

        except FileNotFoundError:
            print(f"The file \"suppliers.txt\" does not exist.")

    elif update_choice == "2":
        table_hospital = [
            ["Hospital Code", "Contact Number", "Email Address"],
            ["HE1", "0184627394", "hc1@outlook.com"],
            ["HE2", "0199888392", "hc2@gmail.com"],
            ["HE3", "0159840945", "hc3@yahoo.com"],
            ["HE4", "0103425884", "hc4@hotmail.com"]
        ]  # set nested list - table_hospital and insert the data of hospitals into sublist

        if not os.path.exists("hospitals.txt"):
            with open("hospitals.txt", "w") as f:
                for sublist in table_hospital:
                    line = ', '.join(map(str, sublist))  # change the writing format for data into hospitals.txt file
                    f.write(line + '\n')  # write the data into hospitals.txt file
                    print("hospitals.txt file has been created. Please enter the number of function again.\n")

        else:
            try:
                with open("hospitals.txt", "r") as f:
                    lines = f.readlines()  # read lines in hospitals.txt file
                    for line in lines:
                        print(line.strip())

                hospital_edit = input("Enter the hospital code you wish to make changes: ").upper()
                # read hospital code from user

                if hospital_edit in ["HE1", "HE2", "HE3", "HE4"]:
                    found = False
                    for i, line in enumerate(lines):
                        if hospital_edit in line:
                            found = True
                            parts = line.strip().split(", ")
                            print("\nWhich part would you like to edit?\n"  # print options for user to choose
                                  "1. Contact Number\n"
                                  "2. Email Address\n"
                                  )
                            details_hospital_choice = input("Enter the number of details need to be edit: ")
                            #  read the number of options from user

                            if details_hospital_choice == "1":
                                parts[1] = input("Enter the new contact number: ")

                            elif details_hospital_choice == "2":
                                parts[2] = input("Enter the new email address: ")

                            else:
                                print("Invalid choice. Please try again.")
                                return

                            lines[i] = ", ".join(parts) + "\n"
                            break

                    if found:
                        with open("hospitals.txt", "w") as f:
                            f.writelines(lines)
                            print("The file has been updated.")
                            return

                    else:
                        print(f"No matches found for {hospital_edit}")
                        return

                else:
                    print("Invalid hospital code. Please try again")
                    return

            except FileNotFoundError:  # if the file doesn't exist
                print(f"The file \"hospitals.txt\" does not exist.")
                return

    elif update_choice == "3":
        print("\n1. Received Quantity\n"
              "2. Distributed Quantity\n")

        received_distributed = input("Enter the number of function you wish to perform: ")
        # read the number of options from user

        if received_distributed == "1":
            if not os.path.exists("report.txt"):
                with open("report.txt", "w") as f:
                    table_report = [
                        ["Item Code", "Item Name", "Supplier Code", "Quantity in stock(boxes)"],
                        ["HC", "Head Cover", "SE1", 0],
                        ["FS", "Face Shield", "SE2", 0],
                        ["MS", "Mask", "SE1", 0],
                        ["GL", "Gloves", "SE3", 0],
                        ["GW", "Gown", "SE3", 0],
                        ["SC", "Shoe Covers", "SE4", 0]
                    ]  # set nested list - table_report and insert the data of report into sublist

                    for sublist in table_report:
                        line = ', '.join(map(str, sublist))
                        f.write(line + '\n')
                    print("report.txt has been created. Please enter the number of function again.\n")

            else:
                try:
                    with open("ppe.txt", "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            print(line.strip())

                    item_code = input("Enter the item code that you wish to make changes: ").upper()
                    # read item code from user

                    found = False
                    for i, line in enumerate(lines):
                        if item_code in line:
                            found = True
                            parts = line.strip().split(", ")

                            received_quantity = input("Enter the quantity received in boxes: ")
                            # read the quantity received from user

                            parts[3] = str(int(parts[3]) + int(received_quantity))
                            # read the quantity of items in ppe.txt file and add the quantity received input from user

                            lines[i] = ", ".join(parts) + "\n"

                            if found:
                                with open("ppe.txt", "w") as f:
                                    f.writelines(lines)  # write the new quantity into ppe.txt file
                                    print("The ppe.txt file has been updated.")
                                    break

                    with open("report.txt", "r") as f:
                        lines_report = f.readlines()  # read lines from report.txt file

                    found_report = False
                    for x, line_report in enumerate(lines_report):
                        # Loops through each line in lines, where x is the index of the current line

                        if item_code in line_report:
                            found_report = True
                            parts_report = line.strip().split(", ")

                            parts_report[3] = str(int(parts[3]) + int(received_quantity))
                            # read the quantity of items in report.txt file and add the quantity received

                            lines_report[x] = ", ".join(parts) + "\n"

                            if found_report:
                                with open("report.txt", "w") as f_report:
                                    f_report.writelines(lines_report)
                                    # write the new quantity into report.txt file

                                    print("The report.txt file has been updated.")

                                current_date = datetime.now().strftime("%d/%m/%Y")
                                # set current_date to read the current date

                                with open("report_supplies.txt", "a") as f:
                                    f.write(f"\nItem Code: {item_code}, Supplier Code: {parts[2]},"
                                            f" Quantity Received: {received_quantity},"
                                            f" Date: {current_date}")
                                    # write the data into report_supplies.txt file

                                    print("The report_supplies.txt file has been updated.")
                                    return

                    else:
                        print(f"No matches found for {item_code}.")
                        return

                except FileNotFoundError:
                    print(f"The file \"report.txt\" / \"ppe.txt\" not found.")
                    return

        elif received_distributed == "2":
            try:
                with open("ppe.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        print(line.strip())

                item_code = input("Enter the item code that you wish to make changes: ").upper()
                # read the item code from user

                found = False
                for i, line in enumerate(lines):
                    if item_code in line:
                        found = True
                        parts = line.strip().split(", ")

                        if item_code in ["HC", "FS", "MS", "GL", "GW", "SC"]:
                            distributed_quantity = int(input("Enter the quantity distributed in boxes: "))
                            # read the distributed quantity from user

                            if int(parts[3]) < distributed_quantity:
                                # if the quantity store in the ppe.txt file is lower than distributed quantity

                                print(f"Insufficient quantity for {item_code}. Stock left {int(parts[3])}")
                                return

                            else:
                                hos_distributed = input("Enter the hospital code that need to distribute the item "
                                                        "(HE1, HE2, HE3, HE4): ").upper()
                                # read the hospital code that need to distribute the item from user

                                if hos_distributed not in ["HE1", "HE2", "HE3", "HE4"]:
                                    print("Invalid hospital code. Please try again.")
                                    return

                                else:
                                    parts[3] = str(int(parts[3]) - int(distributed_quantity))
                                    # deduct the distributed quantity from the quantity of item in ppe.txt file

                        else:
                            print("Invalid item code. Please try again.")
                            return

                        lines[i] = ", ".join(parts) + "\n"
                        break

                if found:
                    with open("ppe.txt", "w") as f:
                        f.writelines(lines)

                        current_date = datetime.now().strftime("%d/%m/%Y")
                        # set current_date to read the current date

                    with open("distribution.txt", "a") as f:
                        f.write(f"\nItem Code: {item_code}, Hospital Code: {hos_distributed},"
                                f" Quantity Distributed: {distributed_quantity},"
                                f" Date: {current_date}")
                        # write the data into distribution.txt file

                    print("The file has been updated.")
                    return

                else:
                    print(f"No matches found for {item_code}.")
                    return

            except FileNotFoundError:
                print("The file \"ppe.txt\" not found.")
                return

    elif update_choice == "4":
        print("Returning back...")
        return

    else:
        print("Invalid function. Returning back.")
        return


def inventory_tracker():
    try:
        with open("ppe.txt", "r") as f:
            lines = f.readlines()

        print("\n---Track Inventory---\n"  # print options for tracking the inventory
              "1. Total available quantity of items in ascending order\n"
              "2. Records of all items that has stock quantity less than 25 boxes\n"
              "3. Search distribution list\n"
              "4. Exit")

        tracker_choice = input("Enter the number of function: ")
        # read the number of options from user

        if tracker_choice == "1":
            items = []  # set items to empty list
            for line in lines[1:]:  # Skipping header if there is any
                parts = line.strip().split(", ")
                items.append(parts)

            items.sort(key=lambda x: int(x[3]))  # sort the item by quantity of item

            for item in items:
                print(", ".join(item))

        elif tracker_choice == "2":
            for line in lines[1:]:  # Skipping header if there is any
                parts = line.strip().split(", ")
                if int(parts[3]) < 25:  # if the quantity of items in ppe.txt file lower than 25
                    print(", ".join(parts))

        elif tracker_choice == "3":
            try:
                with open("distribution.txt", "r") as f:
                    lines = f.readlines()

                found = False  # Flag to check if the item is found

                search_item = input("Enter the item code: ").upper()
                # read the item code from user that want to search

                distribution_dict = defaultdict(lambda: defaultdict(int))
                # Initialize the nested default_dict

                for line in lines:
                    if search_item in line:
                        item_code, hos_distributed, distributed_quantity, current_date = line.strip().split(", ")
                        # Split the line into its components

                        quantity = int(distributed_quantity.split(":")[1].strip())
                        # Convert the quantity to an integer

                        distribution_dict[hos_distributed][item_code] += quantity
                        # Sum up the quantity of same Item Code in the nested default_dict

                        found = True

                if found:
                    for hos_distributed, items in distribution_dict.items():
                        for item_code, total_quantity in items.items():
                            print(f"{item_code}, Total quantity: {total_quantity}, {hos_distributed}")
                            # Print the results if the item is found

                else:
                    print(f"No matches found for {search_item}.")

            except FileNotFoundError:
                print(f"The file \"distribution.txt\" does not exist.")

        elif tracker_choice == "4":
            print("Returning back...")
            return

        else:
            print("Invalid function. Please try again.")
            return

    except FileNotFoundError:
        print(f"The file \"distribution.txt\" does not exist.")


def report_function():
    print("\n---Report---\n"  # print options for printing the report
          "1. List of suppliers with their PPE equipments supplied.\n"
          "2. List of hospitals with quantity of distribution items\n"
          "3. Overall transaction report for a selected month\n")

    report_choice = input("Enter the number of function: ")
    # read the options from user

    if report_choice == "1":
        with open("report.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())

    elif report_choice == "2":
        with open("distribution.txt", "r") as f:
            lines = f.readlines()
            items = []
            for line in lines:
                parts = line.strip().split(", ")
                if len(parts) >= 2:  # Check there are at least 2 parts
                    items.append(parts)

            # Sorting by hospital code which locates at index 1
            items.sort(key=lambda x: x[1])

            for item in items:
                print(", ".join(item))

    elif report_choice == "3":
        month_year = input("Enter the month and year of report needed (mm/yyyy): ")
        # read the date from user

        try:
            with open("report_supplies.txt", "r") as f:
                supplies_lines = f.readlines()

            with open("distribution.txt", "r") as f:
                distribution_lines = f.readlines()

            print(f"---Report for {month_year}---")
            for line in supplies_lines:
                if month_year in line:
                    print(line.strip())
                    # print data from report_supplies.txt file

            for line in distribution_lines:
                parts = line.strip().split(", ")
                if month_year in parts[-1]:
                    print(line.strip())
                    # print data from distribution.txt file

        except FileNotFoundError:
            print(f"File not found.")

    else:
        print("Invalid choice. Please try again.")
        return


def main_menu():
    if not login():  # Check if the user is logged in
        return  # Exit the function if the login fails

    if not os.path.exists("ppe.txt"):
        inventory_creation()
        print("Initial inventory creation completed.\n")
        print("Please log in again after creating the inventory.\n")
        return main_menu()

    else:
        while True:  # Start an infinite loop for the main menu
            print("\n---Inventory Management System---\n",  # print options for inventory management system
                  "1. Update Inventory\n",
                  "2. Track Inventory / Search distribution list\n",
                  "3. Generate Report\n",
                  "4. Log Out\n")

            choice = input("Enter the number of function: ")
            # read number of option from user

            if choice == "1":
                inventory_update()  # call the function to update inventory
                continue  # Continue the loop to show the menu again

            elif choice == "2":
                inventory_tracker()  # Call the function to track and search inventory
                continue  # Continue the loop to show the menu again

            elif choice == "3":
                report_function()  # call the function to print the report
                continue  # Continue the loop to show the menu again

            elif choice == "4":
                print("Logging out...")
                return  # Exit the loop function to log out

            else:
                print("Invalid choice. Please try again")
                continue  # Continue the loop to show the menu again


if __name__ == '__main__':
    main_menu()  # call the function to start the inventory management system
