# 🛡️ Keylogger Detector

🚀 **Keylogger Detector** is a Python-based security tool designed to detect and prevent unauthorized keystroke logging activities. It continuously monitors system processes and keyboard hooks to identify potential keyloggers and logs any suspicious activity.

---

## 📌 Features

✅ **Process Scanning** - Identifies running processes that match known keylogger signatures.  
✅ **Keyboard Hook Detection** - Detects suspicious keyboard monitoring activities.  
✅ **Automated Logging** - Saves all detections to both a log file (`keylogger_detector.log`) and a CSV file (`keylogger_detected.csv`).  
✅ **Process Termination (Optional)** - Automatically terminates detected keylogger processes.  
✅ **Real-Time Monitoring** - Runs continuously in the background, scanning every 10 seconds.

---

## 🛠️ How It Works

1. **Detects Suspicious Processes:**
   - Scans all running processes.
   - Compares process names against a predefined list of known keyloggers.
   - Logs any matches and optionally terminates the process.

2. **Monitors Keyboard Hooks:**
   - Detects applications that may be recording keystrokes.
   - Logs the detection along with the active window title.

3. **Logs Suspicious Activity:**
   - Suspicious activities are recorded in:
     - `keylogger_detector.log` - Human-readable log file.
     - `keylogger_detected.csv` - Structured log file for further analysis.

4. **Runs Automatically:**
   - The script continuously scans the system every 10 seconds.
   - If a keylogger is detected, a warning is logged and optionally removed.

---

## 🚀 Installation & Usage

### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install psutil keyboard pygetwindow
```

### 2️⃣ Run the Detector
Execute the script:
```bash
python keylogger_detector.py
```

### 3️⃣ Check the Logs
- **Log File:** `keylogger_detector.log`
- **CSV Report:** `keylogger_detected.csv`

---

## 🔮 To-Do List (Future Enhancements)

🟢 **Email Alerts** - Notify the user via email when a keylogger is detected.  
🟢 **GUI Dashboard** - Implement a user-friendly interface using Tkinter or Flask.  
🟢 **Network Monitoring** - Detect keyloggers sending logs to remote servers.  
🟢 **Behavior Analysis** - Monitor CPU, RAM, and Disk I/O to identify unusual activity.  
🟢 **AI-Powered Detection** - Use machine learning to detect unknown keyloggers dynamically.  
🟢 **Whitelist System** - Allow users to mark safe applications to reduce false positives.

---

### 🔥 Work in Progress!
This project is continuously improving! Feel free to contribute, test, and suggest enhancements! 🚀

