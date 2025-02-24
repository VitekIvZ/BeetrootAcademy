### README.md

# Honeypot Toolkit

Honeypot Toolkit is a Python-based application designed to simulate and analyze honeypot activities. It includes a Honeypot Simulator and a Log Analyzer, both of which provide valuable insights into potential attacks and vulnerabilities.

## Features

- **Honeypot Simulator**: Simulates various types of attacks and connections to test the honeypot's logging and response capabilities.
- **Log Analyzer**: Analyzes honeypot logs to identify patterns and potential threats.
- **Graphical User Interface (GUI)**: User-friendly interface for easy interaction with the toolkit.

## Requirements

- Python 3.6 or higher
- Tkinter (for GUI)
- `requests` library (for Log Analyzer)
- `multiprocessing` library (for Honeypot Simulator)

## Installation

1. **Clone the repository**:
   ```sh
   https://github.com/VitekIvZ/BeetrootAcademy/tree/main/Honeypot
   cd Honeypot
   ```

2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Honeypot Toolkit

1. **Activate the virtual environment**:
   ```sh
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Run the main GUI**:
   ```sh
   python honeypotGUI.py
   ```

### Honeypot Simulator

The Honeypot Simulator allows you to simulate different types of attacks and connections to test the honeypot's logging and response capabilities.

1. **Launch the Honeypot Simulator** from the main GUI.
2. **Configure the simulation**:
   - **Target IP**: The IP address of the target honeypot.
   - **Intensity**: The intensity of the simulation (`low`, `medium`, `high`).
   - **Duration**: The duration of the simulation in seconds.
3. **Start the simulation**: Click the "Start Simulation" button to begin the simulation.

### Log Analyzer

The Log Analyzer helps you analyze honeypot logs to identify patterns and potential threats.

1. **Launch the Log Analyzer** from the main GUI.
2. **Load log files**: Select the log files you want to analyze.
3. **Analyze logs**: Click the "Analyze Logs" button to start the analysis.

## File Structure

```
Honeypot/
├── honeypotGUI.py              # Main GUI for the Honeypot Toolkit
├── honeypotSimulatorGUI.py     # GUI for the Honeypot Simulator
├── analyzeLogGUI.py            # GUI for the Log Analyzer
├── honeypotSimulator.py        # Core logic for the Honeypot Simulator
├── analyzeLog.py               # Core logic for the Log Analyzer
├── requirements.txt            # List of dependencies
└── README.md                   # This README file
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [z-vi@i.ua](mailto:z-vi@i.ua).

---

This README provides an overview of the Honeypot Toolkit, including its features, installation instructions, usage guidelines, and file structure. It also includes information on contributing and licensing.