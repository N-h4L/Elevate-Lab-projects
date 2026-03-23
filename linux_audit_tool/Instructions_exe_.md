# 🔐 Linux Hardening Audit Report

**Author:** Mohammed Nihal  
**Platform:** Kali Linux (VirtualBox – Oracle VM)  
**Kernel Version:** 6.18.9-kali  
**Audit Date:** 21 Feb 2026  

---

## 📌 1️⃣ Objective

The objective of this project was to design and implement a **Linux Hardening Audit Tool** to evaluate system security configuration against CIS-style best practices.

The tool audits:

- Firewall status  
- SSH hardening  
- File permissions  
- Rootkit presence  
- Running services  
- System updates  

It generates a **compliance score** and **risk classification**.

---

## 🖥 2️⃣ Environment Setup

The audit was performed on a **Kali Linux Virtual Machine** configured in **Oracle VirtualBox**.

### 🔧 Installed & Configured Tools

- UFW (Firewall)
- OpenSSH Server
- chkrootkit
- rkhunter
- Lynis
- auditd
- fail2ban
- net-tools

All packages were successfully installed and updated using:

```bash
sudo apt update
sudo apt upgrade -y
```

SSH service was enabled and verified:

```bash
sudo systemctl status ssh
```

---

## 🔥 3️⃣ Firewall Configuration

The UFW firewall was enabled and configured.

### Commands Executed

```bash
sudo ufw enable
sudo ufw status
```

### Findings

- ✅ Firewall status: **Active**
- ✅ Port 22 (SSH) allowed
- ❌ Port 80 denied
- 🚫 Custom deny rule applied for external IP

Firewall protection is active and enforced.

---

## 🔐 4️⃣ SSH Security Assessment

**Configuration File:**

```
/etc/ssh/sshd_config
```

### Current Settings Identified

```
PermitRootLogin yes
PasswordAuthentication yes
```

### ⚠ Security Impact

- Root login enabled → High security risk  
- Password authentication enabled → Brute-force risk  

SSH service confirmed running and listening on port 22:

```bash
netstat -tulnp
```

---

## 🛡 5️⃣ Rootkit & Malware Scan

### 🔎 chkrootkit Scan

- Initially executed without root privileges
- Re-executed properly with sudo

**Results:**
- No rootkits detected
- All binaries reported *"not infected"*

---

### 🔎 rkhunter

- Successfully installed
- Version: 1.4.6 configured
- No malicious indicators detected

---

## 📊 6️⃣ Lynis System Audit

Lynis Version: **3.1.6**

```bash
sudo lynis audit system
```

### System Identified

- OS: Kali Linux (Rolling)
- Architecture: x86_64
- Kernel: 6.18.9-kali

Lynis completed successfully and provided hardening recommendations focused on SSH and authentication security.

---

## 🤖 7️⃣ Custom Python Audit Tool Results

The developed audit tool performed automated checks on:

- Firewall status
- SSH root login
- SSH password authentication
- File permissions (`/etc/shadow`)
- Insecure services
- Rootkit detection
- Pending updates

### 📄 Output

```
[PASS] Firewall is active
[FAIL] Root login enabled
[WARN] Password authentication enabled
[PASS] /etc/shadow permissions secure
[PASS] No insecure services detected
[PASS] No rootkit detected
[WARN] Updates available
```

---

## 📈 Security Score

**57.14%**

### 🚨 Risk Level: MEDIUM

---

## ⚠ 8️⃣ Identified Security Gaps

| Issue | Risk Level | Recommendation |
|--------|------------|----------------|
| Root SSH login enabled | High | Set `PermitRootLogin no` |
| Password authentication enabled | Medium | Disable & use key-based authentication |
| Pending updates | Medium | Run full system upgrade |
| SSH open to all networks | Medium | Restrict allowed IPs |

---

## 🛠 9️⃣ Hardening Recommendations

### Disable SSH Root Login

```
PermitRootLogin no
```

### Disable Password Authentication

```
PasswordAuthentication no
```

### Restart SSH

```bash
sudo systemctl restart ssh
```

### Apply Pending Updates

```bash
sudo apt upgrade -y
```

### Additional Recommendations

- Configure **Fail2Ban** to prevent brute-force attacks  
- Restrict SSH access to trusted IP addresses  
- Perform periodic rootkit scans  
- Conduct regular system audits  

---

## 🔟 Conclusion

The Linux Hardening Audit Tool successfully evaluated system security posture and generated a quantifiable compliance score.

The system currently falls under **Medium Risk (57.14%)**, primarily due to:

- Insecure SSH configuration  
- Pending system updates  

Firewall configuration and rootkit integrity checks passed successfully, indicating:

- Active network protection  
- No malware presence  

After implementing the recommended hardening measures, the expected security score would exceed **80%**, placing the system in the **Low Risk category**.

---

## 🚀 Project Outcome

- Custom automated Linux audit tool developed  
- Real-time security validation performed  
- Practical hardening measures identified  
- Version-controlled via GitHub  

---

**Author:** Mohammed Nihal  
Cybersecurity Enthusiast | Linux Security | Ethical Hacking
