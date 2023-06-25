import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ImageUpdater:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
        self.ax.set_xlim([0, width])
        self.ax.set_ylim([0, height])
        self.canvas = None
        self.animation = None
        self.current_polyline = []
        self.polylines = []
        self.pointer_coords = ""
        self.snap_mode = False
        self.ortho_mode = False
        self.preview_line = None
        self.prev_x = 0
        self.prev_y = 0

    def start_animation(self):
        self.animation = FuncAnimation(self.fig, self.update_image, interval=100)
        self.canvas.draw()

    def stop_animation(self):
        self.animation.event_source.stop()

    def update_image(self, frame):
        self.ax.clear()
        self.ax.plot([0, self.width], [0, self.height], 'w-')
        for polyline in self.polylines:
            self.ax.plot(*zip(*polyline), 'r-')
        if self.current_polyline:
            self.ax.plot(*zip(*self.current_polyline), 'r-')
        if self.preview_line:
            self.ax.plot(*zip(*self.preview_line), 'b--')
        self.canvas.draw()

    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            if event.button == 1:
                x, y = event.xdata, event.ydata
                if self.snap_mode:
                    x, y = self.snap_to_existing_points(x, y)
                if self.ortho_mode and self.current_polyline:
                    dx = x - self.prev_x
                    dy = y - self.prev_y
                    if abs(dx) > abs(dy):
                        y = self.prev_y
                    else:
                        x = self.prev_x
                self.current_polyline.append((x, y))
                self.update_preview_line()  # Update the preview line
                self.update_image(None)  # Update the image immediately after adding a point
                self.prev_x = x
                self.prev_y = y
            elif event.button == 3:
                if self.current_polyline:
                    self.polylines.append(self.current_polyline)
                    self.current_polyline = []
                    self.update_preview_line()  # Clear the preview line
                    self.update_polyline_listbox()  # Update the polyline listbox
                    self.update_image(None)  # Update the image after finishing the current polyline

    def on_motion(self, event):
        if event.xdata is not None and event.ydata is not None:
            self.pointer_coords = f"X: {event.xdata:.2f}, Y: {event.ydata:.2f}"
        else:
            self.pointer_coords = ""
        self.pointer_label.config(text=self.pointer_coords)
        if event.button == 1 and self.ortho_mode and self.current_polyline:
            x, y = event.xdata, event.ydata
            dx = x - self.prev_x
            dy = y - self.prev_y
            if abs(dx) > abs(dy):
                y = self.prev_y
            else:
                x = self.prev_x
            self.preview_line = [self.current_polyline[-1], (x, y)]
            self.update_image(None)  # Update the image to show the preview line

    def on_key_press(self, event):
        if event.key == 'Shift':
            self.snap_mode = True
        elif event.key == 'Alt':
            self.ortho_mode = True

    def on_key_release(self, event):
        if event.key == 'Shift':
            self.snap_mode = False
        elif event.key == 'Alt':
            self.ortho_mode = False

    def snap_to_existing_points(self, x, y):
        threshold = self.width / 10
        closest_dist = float('inf')
        closest_point = None
        for polyline in self.polylines:
            for point in polyline:
                dist = np.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2)
                if dist < closest_dist and dist < threshold:
                    closest_dist = dist
                    closest_point = point
        if closest_point is not None:
            return closest_point[0], closest_point[1]
        return x, y

    def update_preview_line(self):
        if self.preview_line:
            self.preview_line = None

    def update_polyline_listbox(self):
        self.polyline_listbox.delete(0, tk.END)
        for i, polyline in enumerate(self.polylines):
            name = f"Polyline {i + 1}"
            length = self.calculate_length(polyline)
            area = self.calculate_area(polyline)
            self.polyline_listbox.insert(tk.END, f"{name}: Length={length:.2f}, Area={area:.2f}")

    def calculate_length(self, polyline):
        length = 0
        for i in range(1, len(polyline)):
            x1, y1 = polyline[i - 1]
            x2, y2 = polyline[i]
            length += np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return length

    def calculate_area(self, polyline):
        area = 0
        n = len(polyline)
        for i in range(n):
            x1, y1 = polyline[i]
            x2, y2 = polyline[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2

    def change_polyline_name(self):
        selection = self.polyline_listbox.curselection()
        if selection:
            index = selection[0]
            name = self.polyline_listbox.get(index).split(":")[0]
            new_name = tk.simpledialog.askstring("Rename Polyline", "Enter new name:", initialvalue=name)
            if new_name:
                self.polyline_listbox.delete(index)
                self.polyline_listbox.insert(index, f"{new_name}: Length=..., Area=...")

root = tk.Tk()
root.title("Image Updater")

image_width = 800
image_height = 800

image_updater = ImageUpdater(image_width, image_height)

image_updater.canvas = FigureCanvasTkAgg(image_updater.fig, master=root)
image_updater.canvas.get_tk_widget().pack(side=tk.LEFT)

image_updater.fig.canvas.mpl_connect('button_press_event', image_updater.onclick)
image_updater.fig.canvas.mpl_connect('motion_notify_event', image_updater.on_motion)

root.bind('<KeyPress>', image_updater.on_key_press)
root.bind('<KeyRelease>', image_updater.on_key_release)

# Snap checkbutton
snap_var = tk.BooleanVar()
snap_checkbutton = tk.Checkbutton(root, text="Snap Mode", variable=snap_var)
snap_checkbutton.pack(side=tk.TOP)

# Ortho checkbutton
ortho_var = tk.BooleanVar()
ortho_checkbutton = tk.Checkbutton(root, text="Ortho Mode", variable=ortho_var)
ortho_checkbutton.pack(side=tk.TOP)

# Pointer coordinates label
image_updater.pointer_label = tk.Label(root, text="")
image_updater.pointer_label.pack(side=tk.BOTTOM)

# Polyline listbox
image_updater.polyline_listbox = tk.Listbox(root, width=30)
image_updater.polyline_listbox.pack(side=tk.RIGHT, fill=tk.Y)
image_updater.update_polyline_listbox()

# Rename button
rename_button = tk.Button(root, text="Rename", command=image_updater.change_polyline_name)
rename_button.pack(side=tk.RIGHT)

image_updater.start_animation()

tk.mainloop()
