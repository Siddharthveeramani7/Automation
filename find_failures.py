import subprocess

result = subprocess.run(
    ['sudo','grep','Failed','/var/log/auth.log'],
    capture_output = True,
    text = True
)

# print(result.stdout)

def failed_logins(log_path):
    failed_lines=[]
    try:
        with open(log_path, 'r') as log_file:
            for line in log_file:
                if 'Failed' in line:
                    failed_lines.append(line.strip())
    except FileNotFoundError:
        print(f"Log file {log_path} not found.")
    except PermissionError:
        print(f"Permission denied when trying to read {log_path}. Try running via sudo")
    return failed_lines

failures = failed_logins("/var/log/auth.log")
for line in failures:
    print(line)


