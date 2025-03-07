import psutil
import os
import time
import logging
import csv
import keyboard  # ✅ Replaced pynput.keyboard with correct keyboard module
import pygetwindow as gw

# Logging setup
logging.basicConfig(
    filename="keylogger_detector.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Suspicious process names (expand this list)
SUSPICIOUS_PROCESSES = ["keylogger.exe", "unknown_process.exe", "logger.py"]


# Function to check running processes
def check_running_processes():
    logging.info("Checking for suspicious processes...")
    found_suspicious = False

    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            process_name = proc.info["name"].lower()
            if any(sp in process_name for sp in SUSPICIOUS_PROCESSES):
                logging.warning(
                    f"🚨 Suspicious process detected: {process_name} (PID: {proc.info['pid']})"
                )
                log_to_csv("SUSPICIOUS_PROCESS", process_name)
                found_suspicious = True

                # 🔴 OPTIONAL: Kill the suspicious process
                try:
                    os.kill(proc.info["pid"], 9)  # Force terminate process
                    logging.info(f"🛑 Terminated suspicious process: {process_name}")
                    log_to_csv("TERMINATED_PROCESS", process_name)
                except Exception as e:
                    logging.error(f"❌ Failed to terminate {process_name}: {e}")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return found_suspicious


# Function to detect active keyboard hooks
def detect_keyboard_hooks():
    logging.info("Checking for active keyboard hooks...")
    try:
        active_window = gw.getActiveWindow()
        active_window_title = active_window.title if active_window else "Unknown Window"

        if keyboard.is_pressed("ctrl") or keyboard.is_pressed("shift"):
            logging.warning(
                f"🚨 Suspicious keyboard activity detected in '{active_window_title}'!"
            )
            log_to_csv("KEYBOARD_HOOK", f"Triggered in window: {active_window_title}")
            return True
    except Exception as e:
        logging.error(f"Error detecting keyboard hooks: {e}")
    return False


# Function to log suspicious activities to CSV
def log_to_csv(event_type, description):
    with open("keylogger_detected.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), event_type, description])


# Main function
def keylogger_detector():
    while True:
        suspicious_process = check_running_processes()
        keylogger_hooks = detect_keyboard_hooks()

        if suspicious_process or keylogger_hooks:
            logging.warning("⚠️ Potential Keylogger Detected! Check logs for details.")

        time.sleep(10)  # Scan every 10 seconds


# Run the detector
if __name__ == "__main__":
    logging.info("🚀 Starting Keylogger Detector...")
    keylogger_detector()
