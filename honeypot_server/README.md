# 🍯 Honeypot Server for Attack Detection

## 📌 Overview

This project implements a **low-interaction SSH honeypot** using Cowrie to simulate a vulnerable system and capture real-world attack patterns. It logs attacker behavior, analyzes intrusion attempts, and visualizes attack origins.

---

## 🎯 Objectives

* Deploy a honeypot to attract malicious traffic
* Log attacker IPs, login attempts, and commands
* Analyze attack patterns from logs
* Block repeated attackers using Fail2Ban
* Visualize attacker geolocation

---

## 🛠️ Tools & Technologies

* **Cowrie** – SSH honeypot emulator
* **Fail2Ban** – Intrusion prevention system
* **Python** – Log analysis & visualization
* **GeoLite2** – IP geolocation database
* **Kali Linux (Oracle VM)** – Deployment environment

---

## ⚙️ Setup & Installation

### 1️⃣ Install Dependencies

```bash
sudo apt update && sudo apt install git python3 python3-venv python3-pip jq fail2ban -y
```

### 2️⃣ Clone and Setup Cowrie

```bash
git clone https://github.com/cowrie/cowrie.git
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```

### 3️⃣ Start Honeypot

```bash
bin/cowrie start
```

Default port: **2222**

---

## 📊 Logging & Monitoring

Log files location:

```
var/log/cowrie/
├── cowrie.log
├── cowrie.json
```

---

## 🧪 Simulating Attacks

Example brute-force attack using Hydra:

```bash
hydra -l root -p 123456 ssh://127.0.0.1 -s 2222
```

---

## 🛡️ Fail2Ban Configuration

### Jail Configuration

```
/etc/fail2ban/jail.local
```

```ini
[cowrie]
enabled = true
port = 2222
filter = cowrie
logpath = /home/<user>/linux_audit_project/honeypot_server/var/log/cowrie/cowrie.log
maxretry = 3
bantime = 3600
findtime = 600
ignoreip =
```

---

## 📈 Log Analysis

### Top Attacking IPs

```bash
cat cowrie.json | jq -r '.src_ip' | sort | uniq -c | sort -nr | head
```

### Most Used Passwords

```bash
cat cowrie.json | jq -r '.password' | sort | uniq -c | sort -nr | head
```

### Common Commands

```bash
cat cowrie.json | jq -r '.input' | sort | uniq -c | sort -nr | head
```

---

## 🌍 Geolocation Visualization

### Requirements

Download GeoLite2 database:
https://dev.maxmind.com/geoip/geolite2-free-geolocation-data/

### Run Script

```bash
python3 geo_analysis.py
```

---

## 📸 Screenshots

*Add screenshots of logs, attacks, and graphs here*

---

## 🔍 Observations

* Majority of attacks are automated bots
* Common usernames: `root`, `admin`
* Frequent passwords: `123456`, `password`
* Attackers attempt to download malicious scripts

---

## ⚠️ Security Notes

* Run in isolated VM environment
* Do not expose sensitive data
* Honeypot is for monitoring, not full protection

---

## 📦 Project Structure

```
honeypot_server/
├── bin/
├── etc/
├── var/
├── geo_analysis.py
├── README.md
```

---

## 🚀 Future Improvements

* Add ELK Stack dashboard
* Real-time alerting system
* Multi-service honeypot (FTP, HTTP)
* Cloud deployment for real attack capture

---

## 👨‍💻 Author

**Mohammed Nihal**

---

## 📜 License

This project is for educational and research purposes only.
