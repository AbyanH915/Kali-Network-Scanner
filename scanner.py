#!/usr/bin/env python3
import subprocess

print("🔍 Scanning LabNAT1 10.0.0.0/24 ...")
result = subprocess.run(["nmap", "-sn", "10.0.0.0/24"], capture_output=True, text=True)
print(result.stdout)

with open("hosts.txt","w") as f:
    f.write(result.stdout)

print("Saved to hosts.txt")
