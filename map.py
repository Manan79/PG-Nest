from tkinter import *
import tkintermapview

root = Tk()
root.title("Manan Sood")

root.geometry("900x700")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=0)
map_widget.pack(fill=BOTH , expand=True)
# Set Coordinates
map_widget.set_position(31.345543911576634, 75.55886715330807 , marker=True) # Vegas Baby!
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=e...{x}&y={y}&z={z}&s=Ga", max_zoom=22)

# Set Address

# map_widget.set_address("India" ,marker=True)

# Set A Zoom Level
# map_widget.set_zoom(0)


map_widget.pack()



root.mainloop()