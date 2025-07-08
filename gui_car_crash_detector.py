import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import subprocess

print("🚀 GUI script is starting...")

# Function to run YOLOv5 detection
def detect_car_crash(image_path):
    try:
        print(f"🔍 Detecting: {image_path}")
        subprocess.run([
            "python", "yolov5/detect.py",
            "--weights", "yolov5s.pt",
            "--source", image_path,
            "--project", "yolov5/runs/detect",
            "--name", "gui_output",
            "--exist-ok"
        ])
        return True
    except Exception as e:
        print(f"❌ Detection failed: {e}")
        return False

# GUI class
class CarCrashDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Car Crash Detection - YOLOv5")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")

        self.image_path = None

        self.title_label = tk.Label(master, text="Car Crash Detection using YOLOv5",
                                    font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.browse_button = tk.Button(master, text="📁 Browse Image or Video",
                                       command=self.browse_file, font=("Helvetica", 12))
        self.browse_button.pack(pady=10)

        self.detect_button = tk.Button(master, text="▶️ Run Detection",
                                       command=self.run_detection, font=("Helvetica", 12), state=tk.DISABLED)
        self.detect_button.pack(pady=10)

        self.image_label = tk.Label(master, bg="#f0f0f0")
        self.image_label.pack(pady=10)

    def browse_file(self):
        filetypes = [("Image/Video Files", "*.jpg *.jpeg *.png *.mp4 *.avi")]
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.image_path = filepath
            self.display_image(filepath)
            self.detect_button.config(state=tk.NORMAL)

    def display_image(self, path):
        if path.lower().endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(path)
            img.thumbnail((600, 400))
            img = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img)
            self.image_label.image = img
        else:
            self.image_label.configure(text="📹 Video selected (no preview)", font=("Helvetica", 14))

    def run_detection(self):
        if not self.image_path:
            messagebox.showerror("Error", "No file selected")
            return

        success = detect_car_crash(self.image_path)
        if success:
            messagebox.showinfo("Done", "Detection completed!\nCheck: yolov5/runs/detect/gui_output/")
        else:
            messagebox.showerror("Error", "Detection failed")

# ✅ Start GUI
if __name__ == "__main__":
    print("🟢 Launching GUI...")
    root = tk.Tk()
    app = CarCrashDetectorApp(root)
    root.mainloop()
