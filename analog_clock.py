import tkinter as tk
import time
import math

class Clock:
    def __init__(self, master):
        self.master = master
        master.title("Analog Clock")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.draw_clock_face()
        self.draw_clock_hands()

        self.update_clock()

    def draw_clock_face(self):
        center_x = 200
        center_y = 200
        radius = 180

        # Clock circle
        self.canvas.create_oval(center_x - radius, center_y - radius,
                                center_x + radius, center_y + radius,
                                width=2, outline="black")

        # Hour markers
        for i in range(12):
            angle = (i / 12) * 360
            x = center_x + radius * 0.8 * math.cos(math.radians(angle))
            y = center_y + radius * 0.8 * math.sin(math.radians(angle))
            self.canvas.create_line(center_x, center_y, x, y, width=2)

        # Minute markers
        for i in range(60):
            angle = (i / 60) * 360
            x = center_x + radius * 0.9 * math.cos(math.radians(angle))
            y = center_y + radius * 0.9 * math.sin(math.radians(angle))
            if i % 5 == 0:
                self.canvas.create_line(center_x, center_y, x, y, width=2)
            else:
                self.canvas.create_line(center_x, center_y, x, y, width=1)

    def draw_clock_hands(self):
        self.hour_hand = self.canvas.create_line(200, 200, 200, 150, width=4, fill="black")
        self.minute_hand = self.canvas.create_line(200, 200, 200, 100, width=3, fill="black")
        self.second_hand = self.canvas.create_line(200, 200, 200, 50, width=2, fill="red")

    def update_clock(self):
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        hour_angle = (hour + minute / 60) * 30
        minute_angle = (minute + second / 60) * 6
        second_angle = second * 6

        self.canvas.delete(self.hour_hand)
        self.canvas.delete(self.minute_hand)
        self.canvas.delete(self.second_hand)

        self.hour_hand = self.canvas.create_line(200, 200, 200 + 100 * math.cos(math.radians(hour_angle - 90)), 
                                                200 + 100 * math.sin(math.radians(hour_angle - 90)), 
                                                width=4, fill="black")
        self.minute_hand = self.canvas.create_line(200, 200, 200 + 140 * math.cos(math.radians(minute_angle - 90)), 
                                                200 + 140 * math.sin(math.radians(minute_angle - 90)), 
                                                width=3, fill="black")
        self.second_hand = self.canvas.create_line(200, 200, 200 + 160 * math.cos(math.radians(second_angle - 90)), 
                                                200 + 160 * math.sin(math.radians(second_angle - 90)), 
                                                width=2, fill="red")

        self.master.after(1000, self.update_clock)

root = tk.Tk()
clock = Clock(root)
root.mainloop()