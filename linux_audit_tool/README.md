# 🔐 Linux Hardening Audit Tool

A Python-based Linux security auditing tool that evaluates system configuration against CIS-style hardening practices and generates a compliance score with risk classification.

---

## 📌 Project Overview

The Linux Hardening Audit Tool is designed to assess the security posture of a Linux system by analyzing critical configuration areas such as firewall status, SSH hardening, file permissions, rootkit detection, running services, and system updates.

This tool provides:

- Automated security checks
- Compliance scoring
- Risk level classification
- Practical hardening recommendations

---

## 🛠 Technologies Used

- Python 3
- os module
- subprocess module
- UFW (Firewall)
- OpenSSH
- chkrootkit
- systemctl

---

## 🔍 Security Checks Performed

### 1️⃣ Firewall Status
- Verifies whether UFW firewall is active

### 2️⃣ SSH Hardening
- Checks if root login is disabled
- Checks if password authentication is disabled

### 3️⃣ File Permission Verification
- Validates permissions of:
  - /etc/shadow
  - /etc/passwd

### 4️⃣ Service Inspection
- Detects insecure running services (e.g., Telnet)

### 5️⃣ Rootkit Detection
- Uses chkrootkit to scan for rootkit indicators

### 6️⃣ System Update Status
- Checks for pending package updates

---

## 📊 Scoring System

Each security check contributes to a total compliance score.

Final Score Formula:

(Checks Passed / Total Checks) × 100

### Risk Classification

| Score Range | Risk Level |
|-------------|------------|
| 80% – 100%  | LOW        |
| 50% – 79%   | MEDIUM     |
| Below 50%   | HIGH       |

---

## 🚀 Installation & Setup

### Step 1 – Install Required Packages

bash
sudo apt update
sudo apt install ufw openssh-server chkrootkit -y


### Step 2 – Clone the Repository

bash
git clone https://github.com/YOUR_USERNAME/linux-audit-tool.git
cd linux-audit-tool


### Step 3 – Run the Tool

bash
sudo python3 audit_tool.py


> ⚠ Must be run with sudo for accurate permission and service checks.

---

## 🧪 Sample Output


===== Linux Hardening Audit Report =====

[PASS] Firewall is active
[FAIL] Root login enabled
[WARN] Password authentication enabled
[PASS] /etc/shadow permissions secure
[PASS] No insecure services detected
[PASS] No rootkit detected
[WARN] Updates available

Security Score: 71.42%
Risk Level: MEDIUM


---

## 🛡 Hardening Recommendations

- Enable UFW firewall
- Disable SSH root login
- Disable SSH password authentication (use key-based login)
- Restrict file permissions for sensitive system files
- Regularly update packages
- Remove unnecessary services
- Perform periodic rootkit scans

---

## 🎯 Real-World Application

This tool can be used for:

- Security auditing in lab environments
- Internship cybersecurity projects
- Basic compliance validation
- System hardening practice
- Blue team defensive exercises

---

## 🏗 Future Improvements

- Export report as JSON/HTML
- Automated remediation suggestions
- CIS benchmark mapping
- Logging integration
- Port scanning checks
- Fail2Ban status auditing

---

## 👨‍💻 Author

Mohammed Nihal  
Cybersecurity Enthusiast | Linux Security | Ethical Hacking

---

## 📜 License

This project is for educational and research purposes only.
