import platform
import datetime
import socket
import json
import os
import subprocess

score = 0
max_score = 15
total_checks = 10
report = []

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
END = "\033[0m"

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return output.decode()
    except:
        return ""

def system_info():
    info = {
        "Hostname": socket.gethostname(),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Kernel": platform.release(),
        "Audit Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

def check_firewall():
    global score
    result = run_command("ufw status")
    if "Status: active" in result:
        report.append(GREEN + "[PASS] Firewall is active" + END)
        score += 2
    else:
        report.append(RED + "[FAIL] Firewall is not active" + END)
        report.append(YELLOW + "  → Recommendation: Enable firewall using 'sudo ufw enable'" + END)

def check_ssh_root():
    global score
    with open("/etc/ssh/sshd_config", "r") as f:
        data = f.read()
        if "PermitRootLogin no" in data:
            report.append(GREEN + "[PASS] Root login disabled" + END)
            score += 3
        else:
            report.append(RED + "[FAIL] Root login enabled" + END)
            report.append(YELLOW + "  → Recommendation: Set 'PermitRootLogin no' in /etc/ssh/sshd_config" + END)

def check_ssh_password():
    global score
    with open("/etc/ssh/sshd_config", "r") as f:
        data = f.read()
        if "PasswordAuthentication no" in data:
            report.append(GREEN + "[PASS] Password authentication disabled" + END)
            score += 2
        else:
            report.append(YELLOW + "[WARN] Password authentication enabled" + END)
            report.append(YELLOW + "  → Recommendation: Set 'PasswordAuthentication no' and use SSH keys" + END)

def check_shadow_permissions():
    global score
    perm = oct(os.stat("/etc/shadow").st_mode)[-3:]
    if perm in ["600", "640"]:
        report.append(GREEN + "[PASS] /etc/shadow permissions secure" + END)
        score += 1
    else:
        report.append(RED + "[FAIL] /etc/shadow permissions insecure" + END)

def check_services():
    global score
    services = run_command("systemctl list-units --type=service --state=running")
    if "telnet" in services:
        report.append(RED + "[FAIL] Telnet service running" + END)
    else:
        report.append(GREEN + "[PASS] No insecure services detected" + END)
        score += 1

def check_password_policy():
    global score
    try:
        with open("/etc/login.defs", "r") as f:
            data = f.read()

        if "PASS_MIN_LEN" in data:
            report.append(GREEN + "[PASS] Password policy defined" + END)
            score += 1
        else:
            report.append(YELLOW + "[WARN] Weak password policy" + END)
            report.append(YELLOW + "  → Recommendation: Configure PASS_MIN_LEN in /etc/login.defs" + END)

    except:
        report.append(RED + "[FAIL] Could not read password policy file" + END)

def check_fail2ban():
    global score
    result = run_command("systemctl is-active fail2ban")

    if "active" in result:
        report.append(GREEN + "[PASS] Fail2Ban is active" + END)
        score += 1
    else:
        report.append(YELLOW + "[WARN] Fail2Ban not active" + END)
        report.append(YELLOW + "  → Recommendation: Enable using 'sudo systemctl enable fail2ban'" + END)

def check_rootkit():
    global score
    result = run_command("chkrootkit")
    if "INFECTED" in result:
        report.append(RED + "[FAIL] Rootkit detected" + END)
    else:
        report.append(GREEN + "[PASS] No rootkit detected" + END)
        score += 1

def check_open_ports():
    global score
    result = run_command("ss -tuln")

    risky_ports = ["21", "23", "25", "3306"]  # FTP, Telnet, SMTP, MySQL

    found_risky = False

    for port in risky_ports:
        if f":{port}" in result:
            found_risky = True

    if found_risky:
        report.append(YELLOW + "[WARN] Potentially risky ports open" + END)
        report.append(YELLOW + "  → Recommendation: Review open ports using 'ss -tulnp'" + END)
    else:
        report.append(GREEN + "[PASS] No risky ports detected" + END)
        score += 1

def check_updates():
    global score
    result = run_command("apt list --upgradable 2>/dev/null")
    if "upgradable" not in result:
        report.append(GREEN + "[PASS] System up to date" + END)
        score += 1
    else:
        report.append(YELLOW + "[WARN] Updates available" + END)
        report.append(YELLOW + "  → Recommendation: Run 'sudo apt upgrade -y'" + END)

check_firewall()
check_ssh_root()
check_ssh_password()
check_shadow_permissions()
check_services()
check_rootkit()
check_updates()

final_score = (score / total_checks) * 100

print("\n===== Linux Hardening Audit Report =====\n")

info = system_info()
for key, value in info.items():
    print(f"{key}: {value}")

print("\n----------------------------------------\n")

for item in report:
    print(item)

print("\nSecurity Score: {:.2f}%".format(final_score))

audit_data = {
    "system_info": system_info(),
    "results": report,
    "score": final_score
}

with open("audit_report.json", "w") as f:
    json.dump(audit_data, f, indent=4)

# ---------------- HTML EXPORT ----------------

html_content = f"""
<html>
<head>
    <title>Linux Hardening Audit Report</title>
    <style>
        body {{ font-family: Arial; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
        .warn {{ color: orange; }}
    </style>
</head>
<body>
    <h1>Linux Hardening Audit Report</h1>
    <h2>System Information</h2>
    <ul>
"""

for key, value in system_info().items():
    html_content += f"<li><b>{key}:</b> {value}</li>"

html_content += "</ul><h2>Audit Results</h2><ul>"

for item in report:
    html_content += f"<li>{item}</li>"

html_content += f"""
    </ul>
    <h2>Final Score: {final_score:.2f}%</h2>
</body>
</html>
"""

with open("audit_report.html", "w") as f:
    f.write(html_content)

print("\nHTML report generated: audit_report.html")

if final_score >= 80:
    print(GREEN + "Risk Level: LOW" + END)
elif final_score >= 50:
    print(YELLOW + "Risk Level: MEDIUM" + END)
else:
    print(RED + "Risk Level: HIGH" + END)

#N-h4L
