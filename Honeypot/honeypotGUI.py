import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Honeypot Toolkit")
        self.root.geometry("400x400")

        # Title
        self.title_label = tk.Label(root, text="Honeypot Toolkit", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Buttons to launch different GUIs
        self.launch_simulator_button = tk.Button(
            root, text="Launch Honeypot Simulator", command=self.launch_simulator, width=20, height=2
        )
        self.launch_simulator_button.pack(pady=10)

        self.launch_analyzer_button = tk.Button(
            root, text="Launch Log Analyzer", command=self.launch_analyzer, width=20, height=2
        )
        self.launch_analyzer_button.pack(pady=10)

        self.launch_honeypot_button = tk.Button(
            root, text="Launch Honeypot", command=self.launch_honeypot, width=20, height=2
        )
        self.launch_honeypot_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, width=20, height=2)
        self.exit_button.pack(pady=10)

    def launch_simulator(self):
        """Launches the Honeypot Simulator GUI"""
        try:
            # Run the Honeypot Simulator script
            subprocess.Popen([sys.executable, "honeypotSimulatorGUI.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Honeypot Simulator: {e}")

    def launch_analyzer(self):
        """Launches the Honeypot Log Analyzer GUI"""
        try:
            # Run the Log Analyzer script
            subprocess.Popen([sys.executable, "analyzeLogGUI.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Log Analyzer: {e}")

    def launch_honeypot(self):
        """Launches the Honeypot GUI"""
        try:
            # Run the Honeypot script
            subprocess.Popen([sys.executable, "honeypotRunGUI.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Honeypot: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()