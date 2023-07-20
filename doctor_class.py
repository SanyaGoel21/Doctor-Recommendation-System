import tkinter as tk
import sqlite3

class DoctorManagementSystem:
    def __init__(self):
        # Create a connection to the database
        self.conn = sqlite3.connect('doctors.db')
        # Create a cursor object
        self.c = self.conn.cursor()

        # Create the "doctors" table if it does not exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS doctors
                         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         NAME           TEXT    NOT NULL,
                         PHONE_NO       TEXT    NOT NULL,
                         LOCATION       TEXT    NOT NULL,
                         SPECIALITY     TEXT    NOT NULL,
                         PINCODE        INT     NOT NULL,
                         FEE            INT     NOT NULL,
                         TIMING         TEXT    NOT NULL)''')

        self.root = tk.Tk()
        self.root.title("Doctor Management System")

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.location_label = tk.Label(self.root, text="Location:")
        self.location_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.location_entry = tk.Entry(self.root)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5)

        self.speciality_label = tk.Label(self.root, text="Speciality:")
        self.speciality_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.speciality_entry = tk.Entry(self.root)
        self.speciality_entry.grid(row=3, column=1, padx=5, pady=5)

        self.pincode_label = tk.Label(self.root, text="Pincode:")
        self.pincode_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.pincode_entry = tk.Entry(self.root)
        self.pincode_entry.grid(row=4, column=1, padx=5, pady=5)

        self.fee_label = tk.Label(self.root, text="Fee:")
        self.fee_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.fee_entry = tk.Entry(self.root)
        self.fee_entry.grid(row=5, column=1, padx=5, pady=5)

        self.timing_label = tk.Label(self.root, text="Timing:")
        self.timing_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.timing_entry = tk.Entry(self.root)
        self.timing_entry.grid(row=6, column=1, padx=5, pady=5)

        self.doctor_listbox = tk.Listbox(self.root, width=50)
        
        self.doctor_listbox.grid(row=0, column=2, rowspan=7, padx=5, pady=5)
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=0, column=3, rowspan=7, padx=0, pady=5, sticky="ns")
        self.doctor_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.doctor_listbox.yview)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=7, column=2, padx=5, pady=5)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_doctor)
        self.search_button.grid(row=7, column=3, padx=5, pady=5)
        self.add_button = tk.Button(self.root, text="Add", command=self.add_doctor)
        self.add_button.grid(row=8, column=0, padx=5, pady=5)

        self.edit_button = tk.Button(self.root, text="Edit", command=self.edit_doctor)
        self.edit_button.grid(row=8, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_doctor)
        self.delete_button.grid(row=8, column=2, padx=5, pady=5)

    def add_doctor(self):
        # Get the values from the input fields
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        location = self.location_entry.get()
        speciality = self.speciality_entry.get()
        pincode = int(self.pincode_entry.get())
        fee = int(self.fee_entry.get())
        timing = self.timing_entry.get()

        # Insert the values into the "doctors" table
        self.c.execute("INSERT INTO doctors (NAME, PHONE_NO, LOCATION, SPECIALITY, PINCODE, FEE, TIMING) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, phone, location, speciality, pincode, fee, timing))
        self.conn.commit()

        # Clear the input fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.speciality_entry.delete(0, tk.END)
        self.pincode_entry.delete(0, tk.END)
        self.fee_entry.delete(0, tk.END)
        self.timing_entry.delete(0, tk.END)

    def edit_doctor(self):
        # Get the values from the input fields
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        location = self.location_entry.get()
        speciality = self.speciality_entry.get()
        pincode = int(self.pincode_entry.get())
        fee = int(self.fee_entry.get())
        timing = self.timing_entry.get()

        # Get the ID of the selected doctor from the listbox
        selected_id = int(self.doctor_listbox.get(self.doctor_listbox.curselection())[0])

        # Update the values in the "doctors" table
        self.c.execute("UPDATE doctors SET NAME=?, PHONE_NO=?, LOCATION=?, SPECIALITY=?, PINCODE=?, FEE=?, TIMING=? WHERE ID=?",
                       (name, phone, location, speciality, pincode, fee, timing, selected_id))
        self.conn.commit()

        # Clear the input fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
                # ...continued from previous code snippet
        self.phone_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.speciality_entry.delete(0, tk.END)
        self.pincode_entry.delete(0, tk.END)
        self.fee_entry.delete(0, tk.END)
        self.timing_entry.delete(0, tk.END)

    def delete_doctor(self):
        # Get the ID of the selected doctor from the listbox
        selected_id = int(self.doctor_listbox.get(self.doctor_listbox.curselection())[0])

        # Delete the selected doctor from the "doctors" table
        self.c.execute("DELETE FROM doctors WHERE ID=?", (selected_id,))
        self.conn.commit()

    def load_data(self):
        # Clear the listbox
        self.doctor_listbox.delete(0, tk.END)
        # Get the data from the "doctors" table
        self.c.execute("SELECT * FROM doctors")
        data = self.c.fetchall()

        # Add the data to the listbox
        for doctor in data:
            self.doctor_listbox.insert(tk.END, doctor)

    def search_doctor(self):
        # Get the search query from the input field
        query = self.search_entry.get()
        # Clear the listbox
        self.doctor_listbox.delete(0, tk.END)

        # Search for doctors in the "doctors" table
        self.c.execute("SELECT * FROM doctors WHERE NAME LIKE ? OR SPECIALITY LIKE ? OR LOCATION LIKE ? OR TIMING LIKE ?",
                       ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))
        data = self.c.fetchall()

        # Add the search results to the listbox
        for doctor in data:
            self.doctor_listbox.insert(tk.END, doctor)

def show_ui(self):
        # Define your GUI elements and logic here
        
        # Start the Tkinter event loop
        self.root.mainloop()

def show_doctor_info():
    # Create an instance of the DoctorManagementSystem class
    dms = DoctorManagementSystem() 
    # Call the show_ui() method to display the UI
    dms.show_ui()