import tkinter as tk

print("✅ Starting Tkinter")

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x150")

label = tk.Label(root, text="Tkinter is working!", font=("Arial", 14))
label.pack(pady=40)

root.mainloop()
