# Kali Network Scanner
> A simple Python tool to find live computers in a lab network using Nmap.

## 🤔 What does this do? (For Beginners)
Think of a building with 256 rooms (IP addresses: 10.0.0.0 to 10.0.0.255).

This tool knocks on all doors and tells you which rooms have lights ON (computers that are ON).

- In our test: Found 12 hosts alive in 4.81 seconds
- Real-world: This is Step 1 of ethical hacking called Reconnaissance

## 🎯 Features
- Fast ping scan of 10.0.0.0/24 (LabNAT1 - college lab network)
- Saves live hosts to hosts.txt
- Built for Kali / Parrot OS
- Python + Nmap

## 🧪 How to Test It (2 minutes)
Anyone can use it in their own lab:

git clone https://github.com/AbyanH915/Kali-Network-Scanner.git
cd Kali-Network-Scanner
python3 scanner.py
cat hosts.txt

## 🔒 Is my IP exposed?
No. 10.0.0.x is a PRIVATE lab IP, not your home IP. It can't be tracked online.
We hide real results with .gitignore - only hosts.txt.example is public.

## 📁 Files
- scanner.py - main code
- hosts.txt.example - example results (safe)
- .gitignore - hides real scan data for privacy

## ⚠️ Disclaimer
For educational use only in your own lab. Do not scan networks without permission.

Built by AbyanH915
