import tkinter as tk
from tkinter import ttk
# import database

class PGNEST :
    def __init__(self, root):
        self.root = root
        self.root.title("PG NEST ")

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        self.menu.add_command(label="New", command=self.new_file)
        self.menu.add_command(label="Save", command=self.save_file)
        self.menu.add_command(label="Exit", command=root.quit)

        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        
        self.create_home_frame()
        self.create_student_entry_frame()
        self.create_pg_entry_frame()
        self.create_allocation_frame()
        self.create_management_frame()

    def create_home_frame(self):
        self.home_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.home_frame, text='Home')
        ttk.Label(self.home_frame, text="WELOCOME TO PG NEST ").pack(pady=10)

    def create_student_entry_frame(self):
        self.student_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.student_frame, text='Student Entry')
        ttk.Label(self.student_frame, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
        self.student_name = tk.Entry(self.student_frame)
        self.student_name.grid(row=0, column=1, padx=10, pady=5)
        

    def create_pg_entry_frame(self):
        self.pg_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.pg_frame, text='PG Entry')
        ttk.Label(self.pg_frame, text="PG ID:").grid(row=0, column=0, padx=10, pady=5)
        self.pg_id = tk.Entry(self.pg_frame)
        self.pg_id.grid(row=0, column=1, padx=10, pady=5)
        

    def create_allocation_frame(self):
        self.allocation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.allocation_frame, text='Allocation')
        

    def create_management_frame(self):
        self.management_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.management_frame, text='Management')
        

    def new_file(self):
        pass  

    def save_file(self):
        pass  

if __name__ == "__main__":
    root = tk.Tk()
    app = PGNEST(root)
    root.mainloop()


