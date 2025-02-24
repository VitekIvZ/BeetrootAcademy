#! /bin/python


import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import datetime
import json

def analyze_logs(log_file):
    """Enhanced honeypot log analysis with temporal and behavioral patterns"""
    ip_analysis = {}
    port_analysis = {}
    hourly_attacks = {}
    data_patterns = {}

    # Track session patterns
    ip_sessions = {}
    attack_timeline = []

    with open(log_file, 'r') as f:
        for line in f:
            try:
                activity = json.loads(line)
                timestamp = datetime.datetime.fromisoformat(activity['timestamp'])
                ip = activity['remote_ip']
                port = activity['port']
                data = activity['data']

                # Initialize IP tracking if new
                if ip not in ip_analysis:
                    ip_analysis[ip] = {
                        'total_attempts': 0,
                        'first_seen': timestamp,
                        'last_seen': timestamp,
                        'targeted_ports': set(),
                        'unique_payloads': set(),
                        'session_count': 0
                    }

                # Update IP statistics
                ip_analysis[ip]['total_attempts'] += 1
                ip_analysis[ip]['last_seen'] = timestamp
                ip_analysis[ip]['targeted_ports'].add(port)
                ip_analysis[ip]['unique_payloads'].add(data.strip())

                # Track hourly patterns
                hour = timestamp.hour
                hourly_attacks[hour] = hourly_attacks.get(hour, 0) + 1

                # Analyze port targeting patterns
                if port not in port_analysis:
                    port_analysis[port] = {
                        'total_attempts': 0,
                        'unique_ips': set(),
                        'unique_payloads': set()
                    }
                port_analysis[port]['total_attempts'] += 1
                port_analysis[port]['unique_ips'].add(ip)
                port_analysis[port]['unique_payloads'].add(data.strip())

                # Track payload patterns
                if data.strip():
                    data_patterns[data.strip()] = data_patterns.get(data.strip(), 0) + 1

                # Track attack timeline
                attack_timeline.append({
                    'timestamp': timestamp,
                    'ip': ip,
                    'port': port
                })

            except (json.JSONDecodeError, KeyError) as e:
                continue

    # Analysis Report Generation
    report = "\n=== Honeypot Analysis Report ===\n"

    # 1. IP-based Analysis
    report += "\nTop 10 Most Active IPs:\n"
    sorted_ips = sorted(ip_analysis.items(), key=lambda x: x[1]['total_attempts'], reverse=True)[:10]
    for ip, stats in sorted_ips:
        duration = stats['last_seen'] - stats['first_seen']
        report += f"\nIP: {ip}\n"
        report += f"Total Attempts: {stats['total_attempts']}\n"
        report += f"Active Duration: {duration}\n"
        report += f"Unique Ports Targeted: {len(stats['targeted_ports'])}\n"
        report += f"Unique Payloads: {len(stats['unique_payloads'])}\n"

    # 2. Port Analysis
    report += "\nPort Targeting Analysis:\n"
    sorted_ports = sorted(port_analysis.items(), key=lambda x: x[1]['total_attempts'], reverse=True)
    for port, stats in sorted_ports:
        report += f"\nPort {port}:\n"
        report += f"Total Attempts: {stats['total_attempts']}\n"
        report += f"Unique Attackers: {len(stats['unique_ips'])}\n"
        report += f"Unique Payloads: {len(stats['unique_payloads'])}\n"

    # 3. Temporal Analysis
    report += "\nHourly Attack Distribution:\n"
    for hour in sorted(hourly_attacks.keys()):
        report += f"Hour {hour:02d}: {hourly_attacks[hour]} attempts\n"

    # 4. Attack Sophistication Analysis
    report += "\nAttacker Sophistication Analysis:\n"
    for ip, stats in sorted_ips:
        sophistication_score = (
            len(stats['targeted_ports']) * 0.4 +  # Port diversity
            len(stats['unique_payloads']) * 0.6   # Payload diversity
        )
        report += f"IP {ip}: Sophistication Score {sophistication_score:.2f}\n"

    # 5. Common Payload Patterns
    report += "\nTop 10 Most Common Payloads:\n"
    sorted_payloads = sorted(data_patterns.items(), key=lambda x: x[1], reverse=True)[:10]
    for payload, count in sorted_payloads:
        if len(payload) > 50:  # Truncate long payloads
            payload = payload[:50] + "..."
        report += f"Count {count}: {payload}\n"

    return report

class HoneypotAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Honeypot Log Analyzer")

        self.label = tk.Label(root, text="Select a log file to analyze:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Log File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.analyze_button = tk.Button(root, text="Analyze", command=self.analyze_logs, state=tk.DISABLED)
        self.analyze_button.pack(pady=10)

        self.report_text = scrolledtext.ScrolledText(root, width=80, height=20)
        self.report_text.pack(pady=10)
        
        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, width=20, height=2)
        self.exit_button.pack(pady=10)

        self.file_path = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if self.file_path:
            self.analyze_button.config(state=tk.NORMAL)
            self.label.config(text=f"Selected file: {self.file_path}")

    def analyze_logs(self):
        if self.file_path:
            report = analyze_logs(self.file_path)
            self.report_text.delete(1.0, tk.END)
            self.report_text.insert(tk.END, report)
        else:
            messagebox.showerror("Error", "No file selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HoneypotAnalyzerApp(root)
    root.mainloop()