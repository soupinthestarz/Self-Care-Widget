import tkinter as tk
import random
import datetime

# Self-care messages and daily affirmations
reminder_messages = [
    "Time to drink some water 💧",
    "Stretch your arms, lovely 🌸",
    "Take 3 deep breaths 💕",
    "Give your eyes a rest 👁️👁️",
    "You’re doing amazing, sweetie 💖",
    "Write one thing you're grateful for ✍️"
]

daily_affirmations = [
    "You are enough just as you are.",
    "You radiate calm and peace.",
    "You are allowed to rest.",
    "You are doing your best — and that’s enough."
]

# Pick affirmation of the day
seed = datetime.date.today().toordinal()
random.seed(seed)
affirmation = random.choice(daily_affirmations)

# Create invisible window at first
root = tk.Tk()
root.withdraw()  # hide window initially

# Function to show popup window
def show_reminder():
    reminder = random.choice(reminder_messages)

    # Create popup
    popup = tk.Toplevel()
    popup.title("Self-Care Reminder <3")
    popup.geometry("400x230")
    popup.configure(bg="#fff0f5")  # light floral pink
    popup.attributes('-topmost', True)

    # Labels
    tk.Label(popup, text=affirmation, font=("Comic Sans MS", 11, "italic"),
             bg="#fff0f5", fg="#cc6699", wraplength=280, justify="center").pack(pady=(10, 5))

    tk.Label(popup, text=reminder, font=("Comic Sans MS", 13, "bold"),
             bg="#fff0f5", fg="#663366", wraplength=280, justify="center").pack(pady=10)

    tk.Button(popup, text="Close", command=popup.destroy, bg="#ffb6c1", fg="white").pack(pady=5)

    # Schedule next reminder
    root.after(1800000, show_reminder)  # 30 minutes

# First reminder
root.after(1000, show_reminder)

# Keep running silently
root.mainloop()
