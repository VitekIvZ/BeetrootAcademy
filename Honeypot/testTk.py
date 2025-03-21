import tkinter as tk
from tkinter import scrolledtext
import datetime
import json
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.log_file = "activity_log.txt"
        self.log_lock = threading.Lock()

        # Створення текстового поля для відображення логів
        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.log_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Кнопка для симуляції підозрілої активності
        self.test_button = tk.Button(root, text="Simulate Activity", command=self.simulate_activity)
        self.test_button.grid(row=1, column=0, pady=10, sticky="ew")

        # Налаштування розтягування рядків і стовпців
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def log_activity(self, port, remote_ip, data):
        """Log suspicious activity with timestamp and details"""
        try:
            data_str = data.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error decoding data: {e}")
            data_str = "[Binary data]"
        
        activity = {
            "timestamp": datetime.datetime.now().isoformat(),
            "remote_ip": remote_ip,
            "port": port,
            "data": data_str
        }
        
        with self.log_lock:
            # Запис у файл
            with open(self.log_file, 'a') as f:
                json.dump(activity, f)
                f.write('\n')
            
            # Додавання запису у текстове поле
            self.log_text.insert(tk.END, f"{activity['timestamp']} - {activity['remote_ip']}:{activity['port']} - {activity['data']}\n")
            self.log_text.see(tk.END)  # Прокрутка до останнього запису

    def simulate_activity(self):
        # Симуляція підозрілої активності
        self.log_activity(8080, "192.168.1.100", b"Suspicious data")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Activity Logger")
    app = App(root)
    root.mainloop()
