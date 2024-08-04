import tkinter as tk

# import database
def add_pg():
    pass
def view_pgs():
    pass
def search_pgs():
    pass
def show_statistics():
    pass
def show_settings():
    pass

root = tk.Tk()
root.title("User Pannel")
root.geometry("800x600")


header = tk.Label(root, text="PG NEST", font=("Arial", 24))
header.pack(pady=10)


nav_frame = tk.Frame(root)
nav_frame.pack(side=tk.LEFT, fill=tk.Y)

buttons = {
    "Home": tk.Button(nav_frame, text="Home", command=lambda: print("Home")),
    "Add PG": tk.Button(nav_frame, text="Add PG", command=lambda:print("Add Pg")),
    "View PGs": tk.Button(nav_frame, text="View PGs", command=lambda:print("View Pg")),
    "Search PGs": tk.Button(nav_frame, text="Search PGs", command=lambda:print("Search Pg")),
    "Statistics": tk.Button(nav_frame, text="Statistics", command=lambda:print("Statistics")),
    "Settings": tk.Button(nav_frame, text="Settings", command=lambda:print("Settings"))
}

for name, button in buttons.items():
    button.pack(pady=5, fill=tk.X)


main_content = tk.Frame(root)
main_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

footer = tk.Label(root, text=" For any help Contact: support@pgnest.com", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
