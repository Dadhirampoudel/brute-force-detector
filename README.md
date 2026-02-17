Brute Force Login Detection Tool

Project Overview
This project simulates a real-world SOC (Security Operations Center) task: detecting brute-force login attempts by analyzing login log files.

Objective
Identify IP addresses that exceed a failed login attempt threshold, indicating possible brute-force attacks.

How It Works
- Reads a log file (`sample_log.txt`)
- Counts failed login attempts per IP address
- Flags IPs that exceed a defined threshold
- Displays suspicious IP addresses

Technologies Used
- Python 3

Project Files
- `log_analyzer.py` → Main detection script
- `sample_log.txt` → Sample login log data
- `README.md` → Project documentation

Example Output
Suspicious IPs (Possible Brute Force Attacks):
192.168.1.15 -> 4 failed attempts  
192.168.1.30 -> 4 failed attempts  

Skills Demonstrated
- Log parsing
- Basic threat detection logic
- Automation using Python
- Security analysis thinking

Future Improvements
- Export results to CSV
- Add timestamp analysis
- Integrate with SIEM-style logging
- Add IP blacklist feature

