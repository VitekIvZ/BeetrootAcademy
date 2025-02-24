#! /bin/python


import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import socket
import time
import random
from concurrent.futures import ThreadPoolExecutor

class HoneypotSimulator:
    """
    A class to simulate different types of connections and attacks against our honeypot.
    This helps in testing the honeypot's logging and response capabilities.
    """

    def __init__(self, target_ip="127.0.0.1", intensity="medium"):
        # Configuration for the simulator
        self.target_ip = target_ip
        self.intensity = intensity

        # Common ports that attackers often probe
        self.target_ports = [21, 22, 23, 25, 80, 443, 3306, 5432]

        # Dictionary of common commands used by attackers for different services
        self.attack_patterns = {
            21: [  # FTP commands
                "USER admin\r\n",
                "PASS admin123\r\n",
                "LIST\r\n",
                "STOR malware.exe\r\n"
            ],
            22: [  # SSH attempts
                "SSH-2.0-OpenSSH_7.9\r\n",
                "admin:password123\n",
                "root:toor\n"
            ],
            80: [  # HTTP requests
                "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
                "POST /admin HTTP/1.1\r\nHost: localhost\r\nContent-Length: 0\r\n\r\n",
                "GET /wp-admin HTTP/1.1\r\nHost: localhost\r\n\r\n"
            ]
        }

        # Intensity settings affect the frequency and volume of simulated attacks
        self.intensity_settings = {
            "low": {"max_threads": 2, "delay_range": (1, 3)},
            "medium": {"max_threads": 5, "delay_range": (0.5, 1.5)},
            "high": {"max_threads": 10, "delay_range": (0.1, 0.5)}
        }

    def simulate_connection(self, port):
        """
        Simulates a connection attempt to a specific port with realistic attack patterns
        """
        try:
            # Create a new socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)

            print(f"[*] Attempting connection to {self.target_ip}:{port}")
            sock.connect((self.target_ip, port))

            # Get banner if any
            banner = sock.recv(1024)
            print(f"[+] Received banner from port {port}: {banner.decode('utf-8', 'ignore').strip()}")

            # Send attack patterns based on the port
            if port in self.attack_patterns:
                for command in self.attack_patterns[port]:
                    print(f"[*] Sending command to port {port}: {command.strip()}")
                    sock.send(command.encode())

                    # Wait for response
                    try:
                        response = sock.recv(1024)
                        print(f"[+] Received response: {response.decode('utf-8', 'ignore').strip()}")
                    except socket.timeout:
                        print(f"[-] No response received from port {port}")

                    # Add realistic delay between commands
                    time.sleep(random.uniform(*self.intensity_settings[self.intensity]["delay_range"]))

            sock.close()

        except ConnectionRefusedError:
            print(f"[-] Connection refused on port {port}")
        except socket.timeout:
            print(f"[-] Connection timeout on port {port}")
        except Exception as e:
            print(f"[-] Error connecting to port {port}: {e}")

    def simulate_port_scan(self):
        """
        Simulates a basic port scan across common ports
        """
        print(f"\n[*] Starting port scan simulation against {self.target_ip}")
        for port in self.target_ports:
            self.simulate_connection(port)
            time.sleep(random.uniform(0.1, 0.3))

    def simulate_brute_force(self, port):
        """
        Simulates a brute force attack against a specific service
        """
        common_usernames = ["admin", "root", "user", "test"]
        common_passwords = ["password123", "admin123", "123456", "root"]

        print(f"\n[*] Starting brute force simulation against port {port}")

        for username in common_usernames:
            for password in common_passwords:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((self.target_ip, port))

                    if port == 21:  # FTP
                        sock.send(f"USER {username}\r\n".encode())
                        sock.recv(1024)
                        sock.send(f"PASS {password}\r\n".encode())
                    elif port == 22:  # SSH
                        sock.send(f"{username}:{password}\n".encode())

                    sock.close()
                    time.sleep(random.uniform(0.1, 0.3))

                except Exception as e:
                    print(f"[-] Error in brute force attempt: {e}")

    def run_continuous_simulation(self, duration=300):
        """
        Runs a continuous simulation for a specified duration
        """
        print(f"\n[*] Starting continuous simulation for {duration} seconds")
        print(f"[*] Intensity level: {self.intensity}")

        end_time = time.time() + duration

        with ThreadPoolExecutor(
            max_workers=self.intensity_settings[self.intensity]["max_threads"]
        ) as executor:
            while time.time() < end_time:
                # Mix of different attack patterns
                simulation_choices = [
                    lambda: self.simulate_port_scan(),
                    lambda: self.simulate_brute_force(21),
                    lambda: self.simulate_brute_force(22),
                    lambda: self.simulate_connection(80)
                ]

                # Randomly choose and execute an attack pattern
                executor.submit(random.choice(simulation_choices))
                time.sleep(random.uniform(*self.intensity_settings[self.intensity]["delay_range"]))

class HoneypotSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Honeypot Simulator")

        # Input fields
        self.target_ip_label = tk.Label(root, text="Target IP:")
        self.target_ip_label.grid(row=0, column=0, padx=10, pady=10)
        self.target_ip_entry = tk.Entry(root)
        self.target_ip_entry.grid(row=0, column=1, padx=10, pady=10)
        self.target_ip_entry.insert(0, "127.0.0.1")

        self.intensity_label = tk.Label(root, text="Intensity:")
        self.intensity_label.grid(row=1, column=0, padx=10, pady=10)
        self.intensity_var = tk.StringVar(value="medium")
        self.intensity_menu = tk.OptionMenu(root, self.intensity_var, "low", "medium", "high")
        self.intensity_menu.grid(row=1, column=1, padx=10, pady=10)

        self.duration_label = tk.Label(root, text="Duration (seconds):")
        self.duration_label.grid(row=2, column=0, padx=10, pady=10)
        self.duration_entry = tk.Entry(root)
        self.duration_entry.grid(row=2, column=1, padx=10, pady=10)
        self.duration_entry.insert(0, "300")

        # Start button
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Output console
        self.output_console = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_console.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, width=20, height=2)
        self.exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        

    def start_simulation(self):
        """
        Starts the simulation in a separate thread
        """
        target_ip = self.target_ip_entry.get()
        intensity = self.intensity_var.get()
        duration = int(self.duration_entry.get())

        if not target_ip:
            messagebox.showerror("Error", "Please enter a target IP address.")
            return

        # Clear the console
        self.output_console.delete(1.0, tk.END)

        # Redirect print statements to the console
        import sys
        sys.stdout = TextRedirector(self.output_console, "stdout")

        # Run the simulation in a separate thread
        simulator = HoneypotSimulator(target_ip, intensity)
        simulation_thread = threading.Thread(target=simulator.run_continuous_simulation, args=(duration,))
        simulation_thread.start()

class TextRedirector:
    """
    A helper class to redirect print statements to a Tkinter ScrolledText widget
    """
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, text):
        self.widget.insert(tk.END, text, (self.tag,))
        self.widget.see(tk.END)

    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = HoneypotSimulatorApp(root)
    root.mainloop()
