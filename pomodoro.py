import tkinter as tk
from tkinter import ttk

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.configure(bg='#181818')  # Dark background (YouTube-inspired)

        # Apply YouTube-inspired styles
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use a theme that supports custom styling
        self.style.configure("Red.TButton",
                             font=("Helvetica", 12),
                             foreground="white",
                             background="#FF0000",  # YouTube red
                             borderwidth=1,
                             relief="flat")
        self.style.map("Red.TButton",
                       background=[("active", "#CC0000")],  # Darker red on hover
                       foreground=[("active", "white")])

        self.style.configure("TLabel", font=("Helvetica", 40), background="#181818", foreground="white")

        # Timer label
        self.timer_label = ttk.Label(self.root, text="25:00", style="TLabel")
        self.timer_label.pack(pady=20)

        self.playlist = [
            "https://www.youtube.com/watch?v=jfKfPfyJRdk",
            "https://www.youtube.com/watch?v=sF80I-TQiW0",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        
        ]
        self.current_video_index = 0
        
        # Play music button
        self.play_button = ttk.Button(self.root, text="Play Music", style="Red.TButton", command=self.play_music)
        self.play_button.pack(pady=10)

        # Start and reset buttons
        self.start_button = ttk.Button(self.root, text="Start", style="Red.TButton", command=self.start_timer)
        self.start_button.pack(side="left", padx=20)

        self.reset_button = ttk.Button(self.root, text="Reset", style="Red.TButton", command=self.reset_timer)
        self.reset_button.pack(side="right", padx=20)
        
        self.time_left = 1500  # 25 minutes in seconds
        self.running = False

    def play_music(self):
        import webbrowser
        if self.current_video_index < len(self.playlist):
            webbrowser.open(self.playlist[self.current_video_index])
            self.current_video_index += 1
        else:
            self.current_video_index = 0
            webbrowser.open(self.playlist[self.current_video_index])
            self.current_video_index += 1

    def start_timer(self):
        if not self.running:
            self.running = True
            self.countdown()

    def reset_timer(self):
        self.running = False
        self.time_left = 1500
        self.timer_label.config(text="25:00")

    def countdown(self):
        if self.running:
            if self.time_left > 0:
                minutes, seconds = divmod(self.time_left, 60)
                self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.time_left -= 1
                self.root.after(1000, self.countdown)
            else:
                self.running = False
                self.timer_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop() 