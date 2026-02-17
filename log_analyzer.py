def detect_brute_force(log_file, threshold=3):
  failed_attempts = {}

  with open(log_file, "r") as file:
    for line in fil:
      parts = line.strip().split(" - ")
      ip = parts[0]
      status = parts[1]

if status == "FAILED"
  if ip in failed_attempts:
    failed_attempts[ip] += 1
  else:
    failed_attempts[ip] = 1

print("Suspicious IPs (Possible Brute Force Attacks):")
for ip, count in failed_attempts.items():
  if count >= threshold:
    print(f"{ip} -> {count} failed attempts")

if __name__ == " __main__":
  detect_brute_force("sample_log.txt")
