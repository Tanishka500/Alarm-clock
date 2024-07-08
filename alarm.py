import tkinter as tk
from tkinter import messagebox
import datetime
import winsound

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.configure(background='black')  # Set background color of the window
        
        # Clock label
        self.clock_label = tk.Label(master, font=("ds-digital", 80), background="black", foreground="cyan")
        self.clock_label.pack(anchor='center', pady=50)
        
        # Alarm entry
        self.alarm_time = tk.StringVar()
        entry_frame = tk.Frame(master, background='black')
        entry_frame.pack()
        
        tk.Label(entry_frame, text="Enter alarm time (HH:MM):", font=("ds-digital", 18), background='black', foreground='cyan').pack(side=tk.LEFT, padx=10)
        self.entry = tk.Entry(entry_frame, textvariable=self.alarm_time, font=("ds-digital", 18), background="cyan", foreground="black", justify='center')
        self.entry.pack(side=tk.LEFT)
        
        # Set Alarm button
        tk.Button(master, text="Set Alarm", font=("ds-digital", 18), background="black", foreground="cyan", command=self.set_alarm).pack(pady=20)
        
        # Quit button
        tk.Button(master, text="Quit", font=("ds-digital", 18), background="black", foreground="cyan", command=self.master.destroy).pack()

        # Update clock
        self.update_clock()

    def update_clock(self):
        current_time = datetime.datetime.now().strftime('%H:%M:%S %p')
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    def set_alarm(self):
        alarm_time_str = self.alarm_time.get()
        
        try:
            alarm_time_obj = datetime.datetime.strptime(alarm_time_str, "%H:%M")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format! Use HH:MM")
            return
        
        current_time = datetime.datetime.now()
        alarm_time_today = alarm_time_obj.replace(year=current_time.year, month=current_time.month, day=current_time.day)
        
        if alarm_time_today < current_time:
            alarm_time_today += datetime.timedelta(days=1)
        
        time_diff = (alarm_time_today - current_time).total_seconds()
        
        self.master.withdraw()  # Hide the main window
        
        # Wait until it's time for the alarm
        self.master.after(int(time_diff * 1000), self.trigger_alarm)
    
    def trigger_alarm(self):
        # Show a message box when it's time for the alarm
        tk.messagebox.showinfo("Alarm", f"It's time to wake up!")
        
        # Play sound (Windows-specific)
        winsound.Beep(440, 1000)  # Beep at 440 Hz for 1 second
        
        self.master.deiconify()  # Show the main window again

def main():
    root = tk.Tk()
    root.geometry("600x400")  # Set initial size of the window
    alarm_clock = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
