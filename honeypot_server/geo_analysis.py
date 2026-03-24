import json
import geoip2.database
import matplotlib.pyplot as plt
from collections import Counter

# Path to your GeoIP database
db_path = "/home/nihal/cowrie/GeoLite2-City.mmdb"

# Path to Cowrie logs
log_path = "/home/nihal/cowrie/var/log/cowrie/cowrie.json"

reader = geoip2.database.Reader(db_path)

ips = []

# Read log file
with open(log_path, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            if "src_ip" in data:
                ips.append(data["src_ip"])
        except:
            continue

# Count IP occurrences
ip_counts = Counter(ips)

countries = {}

# Map IPs to countries
for ip, count in ip_counts.items():
    try:
        response = reader.city(ip)
        country = response.country.name
        if country:
            countries[country] = countries.get(country, 0) + count
    except:
        continue

# Print results
print("\nTop Attacking Countries:\n")
for country, count in sorted(countries.items(), key=lambda x: x[1], reverse=True):
    print(f"{country}: {count}")

# Plot graph
plt.figure()
plt.bar(countries.keys(), countries.values())
plt.xticks(rotation=90)
plt.title("Attack Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Number of Attacks")
plt.tight_layout()
plt.show()
