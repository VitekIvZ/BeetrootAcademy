#! /bin/python


import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import socket
import datetime
import json
import time
from pathlib import Path

# Configure logging directory
LOG_DIR = Path("honeypot_logs")
LOG_DIR.mkdir(exist_ok=True)
if not LOG_DIR.exists():
    print(f"Error: Directory {LOG_DIR} could not be created.")

class Honeypot:
    def __init__(self, bind_ip="0.0.0.0", ports=None, log_text=None):
        self.bind_ip = bind_ip
        self.ports = ports or [21, 22, 80, 443]  # Default ports to monitor
        self.active_connections = {}
        self.log_file = LOG_DIR / f"honeypot_{datetime.datetime.now().strftime('%Y%m%d')}.json"
        self.log_lock = threading.Lock()
        self.log_text = log_text  # Додаємо текстове поле для логів
    
    def log_activity(self, port, remote_ip, data):
        """Log suspicious activity with timestamp and details"""
        try:
            data_str = data.decode('utf-8', errors='ignore')
            if not data_str.strip():  # Перевірка на порожній рядок
                data_str = "[Empty or non-decodable data]"
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
            with open(self.log_file, 'a') as f:
                json.dump(activity, f)
                f.write('\n')
            # Додавання запису у текстове поле
            if self.log_text:  # Перевіряємо, чи передано текстове поле
                self.log_text.insert(tk.END, f"{activity['timestamp']} - {activity['remote_ip']}:{activity['port']} - {activity['data']}\n")
                self.log_text.see(tk.END)  # Прокрутка до останнього запису
	

    def handle_connection(self, client_socket, remote_ip, port):
        """Handle individual connections and emulate services"""
        service_banners = {
            21: "220 FTP server ready\r\n",
            22: "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n",
            80: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n",
            443: "HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\n\r\n"
        }

        try:
            # Send appropriate banner for the service
            if port in service_banners:
                client_socket.send(service_banners[port].encode())
                print(f"Sent banner to {remote_ip}:{port}")

            # Receive data from attacker
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        print(f"No data received from {remote_ip}:{port}. Closing connection.")
                        break
                
                    print(f"Received data from {remote_ip}:{port} - {data}")
                    self.log_activity(port, remote_ip, data)

                    # Send fake response
                    client_socket.send(b"Command not recognized.\r\n")
                except BrokenPipeError:
                    print(f"[-] Broken pipe error on port {port}. Connection might be closed by {remote_ip}.")
                    break
                except ConnectionResetError:
                    print(f"[-] Connection reset by peer {remote_ip}:{port}.")
                    break
                except socket.timeout:
                    print(f"[-] Timeout while receiving data from {remote_ip}:{port}.")
                    break
                except socket.error as e:
                    print(f"[-] Socket error while communicating with {remote_ip}:{port}: {e}")
                    break

        except Exception as e:
            print(f"Error handling connection from {remote_ip}:{port}: {e}")
        finally:
            client_socket.close()
            print(f"Connection with {remote_ip}:{port} closed.")

    def start_listener(self, port):
        """Start a listener on specified port"""
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.bind_ip, port))
            server.listen(5)

            print(f"[*] Listening on {self.bind_ip}:{port}")

            while True:
                client, addr = server.accept()
                print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

                # Handle connection in separate thread
                client_handler = threading.Thread(
                    target=self.handle_connection,
                    args=(client, addr[0], port)
                )
                client_handler.start()

        except Exception as e:
            print(f"Error starting listener on port {port}: {e}")

class HoneypotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Honeypot GUI")

        # Input fields
        self.bind_ip_label = tk.Label(root, text="Bind IP:")
        self.bind_ip_label.grid(row=0, column=0, padx=10, pady=10)
        self.bind_ip_entry = tk.Entry(root)
        self.bind_ip_entry.grid(row=0, column=1, padx=10, pady=10)
        self.bind_ip_entry.insert(0, "0.0.0.0")

        self.ports_label = tk.Label(root, text="Ports (comma-separated):")
        self.ports_label.grid(row=1, column=0, padx=10, pady=10)
        self.ports_entry = tk.Entry(root)
        self.ports_entry.grid(row=1, column=1, padx=10, pady=10)
        self.ports_entry.insert(0, "21,22,80,443")

        # Start button
        self.start_button = tk.Button(root, text="Start Honeypot", command=self.start_honeypot)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Output console label
        self.output_console_label = tk.Label(root, text="Output Console:")
        self.output_console_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Output console
        self.output_console = scrolledtext.ScrolledText(root, width=50, height=10)
        self.output_console.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Log text label
        self.log_text_label = tk.Label(root, text="Log Activity:")
        self.log_text_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Log text
        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.log_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Налаштування розтягування рядків і стовпців
        root.grid_rowconfigure(4, weight=1)
        root.grid_rowconfigure(6, weight=1)
        root.grid_columnconfigure(1, weight=1)
        
        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, width=20, height=2)
        self.exit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
                

    def start_honeypot(self):
        """
        Starts the honeypot in a separate thread
        """
        bind_ip = self.bind_ip_entry.get()
        ports = self.ports_entry.get().strip()

        if not bind_ip:
            messagebox.showerror("Error", "Please enter a bind IP address.")
            return

        if not ports:
            messagebox.showerror("Error", "Please enter at least one port.")
            return

    # Convert ports to a list of integers
        try:
            ports = [int(port.strip()) for port in ports.split(",")]
        except ValueError:
            messagebox.showerror("Error", "Invalid port format. Please use comma-separated integers.")
            return

    # Clear the console
        self.output_console.delete(1.0, tk.END)

    # Redirect print statements to the console
        import sys
        sys.stdout = TextRedirector(self.output_console, "stdout")

    # Start the honeypot in a separate thread
        self.honeypot = Honeypot(bind_ip, ports, log_text=self.log_text)  # Передаємо log_text
        honeypot_thread = threading.Thread(target=self.run_honeypot)
        honeypot_thread.daemon = True
        honeypot_thread.start()

    def run_honeypot(self):
        """
        Runs the honeypot and keeps it alive
        """
        # Start listeners for each port in separate threads
        for port in self.honeypot.ports:
            listener_thread = threading.Thread(
                target=self.honeypot.start_listener,
                args=(port,)
            )
            listener_thread.daemon = True
            listener_thread.start()

        try:
            # Keep main thread alive
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[*] Shutting down honeypot...")

class TextRedirector:
    """
    A helper class to redirect print statements to a Tkinter ScrolledText widget
    """
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
        self.buffer = ""

    # def write(self, text):
    #     self.widget.insert(tk.END, text, (self.tag,))
    #     self.widget.see(tk.END)
    
    def write(self, text):
        self.buffer += text
        if len(self.buffer) > 100:  # Оновлюємо GUI тільки після накопичення 100 символів
            self.widget.insert(tk.END, self.buffer)
            self.widget.see(tk.END)
            self.buffer = ""

    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = HoneypotApp(root)
    root.mainloop()
