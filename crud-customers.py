import mysql.connector

# --- Database Connection ---
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MyCo"
    )

# --- List Customers ---
def list_customers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, Fullname, Addressline FROM Customers")
    rows = cursor.fetchall()
    print("\n--- Customer List ---")
    for row in rows:
        print(f"{row[0]}. {row[1]} - {row[2]}")
    conn.close()


# --- Add Customer ---
def add_customer():
    fullname = input("Enter full name: ")
    address = input("Enter address: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (Fullname, Addressline) VALUES (%s, %s)", (fullname, address))
    conn.commit()
    print("Customer added.\n")
    conn.close()

# --- Edit Customer ---
def edit_customer():
    list_customers()
    try:
        customer_id = int(input("Enter customer ID to edit: "))
        new_name = input("Enter new full name: ")
        new_address = input("Enter new address: ")
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE Customers SET Fullname=%s, Addressline=%s WHERE id=%s", (new_name, new_address, customer_id))
        conn.commit()
        print("Customer updated.\n")
        conn.close()
    except ValueError:
        print("Invalid input.\n")


# --- View Customer ---
def view_customer():
    try:
        customer_id = input("Enter customer ID to view: ")
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT Fullname, Addressline FROM Customers WHERE id=%s", (customer_id,))
        row = cursor.fetchone()
        if row:
            print(f"\nFull Name: {row[0]}\nAddress: {row[1]}\n")
        else:
            print("Customer not found.\n")
        conn.close()
    except ValueError:
        print("Invalid input.\n")

# --- Delete Customer ---
def delete_customer():
    list_customers()
    try:
        customer_id = int(input("Enter customer ID to delete: "))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customers WHERE id=%s", (customer_id,))
        conn.commit()
        print("Customer deleted.\n")
        conn.close()
    except ValueError:
        print("Invalid input.\n")


# --- Main Menu ---
def main():
    while True:
        print("=== Customer Menu ===")
        print("1. List")
        print("2. Add")
        print("3. Edit")
        print("4. View")
        print("5. Delete")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            list_customers()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            edit_customer()
        elif choice == '4':
            view_customer()
        elif choice == '5':
            delete_customer()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()


