import re
import hashlib
from collections import Counter
import matplotlib.pyplot as plt
import csv
import os

data_folder = 'data'
password_file = os.path.join(data_folder, 'passwords.txt')

passwords = []

try:
    with open(password_file, 'r', encoding='utf-8') as f:
        for line in f:
            pwd = line.strip()
            if pwd:
                passwords.append(pwd)
except FileNotFoundError:
    print(f"File {password_file} not found. Using sample passwords.")
    passwords = [
        "123456", "password", "qwerty", "letmein", "sunshine",
        "football", "iloveyou", "admin", "welcome", "monkey",
        "StrongPass1!", "My$ecureP@ss", "hello123", "abc123"
    ]

print(f"Loaded {len(passwords)} passwords.")

def check_password_strength(password):
    if len(password) < 8:
        return 'Weak'
    if re.fullmatch(r'[a-zA-Z]+', password):
        return 'Weak'
    if re.fullmatch(r'[a-zA-Z0-9]+', password):
        return 'Medium'
    if re.search(r'[^a-zA-Z0-9]', password):
        return 'Strong'
    return 'Medium'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

strengths = []
hashed_passwords = []

for pwd in passwords:
    strength = check_password_strength(pwd)
    hashed = hash_password(pwd)
    strengths.append(strength)
    hashed_passwords.append(hashed)

strength_count = Counter(strengths)

results_folder = 'results'
os.makedirs(results_folder, exist_ok=True)
output_file = os.path.join(results_folder, 'password_analysis_results.csv')

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Password', 'Strength', 'SHA-256 Hash'])
    for pwd, strg, hsh in zip(passwords, strengths, hashed_passwords):
        writer.writerow([pwd, strg, hsh])

print(f"Analysis exported to {output_file}")

labels = strength_count.keys()
counts = strength_count.values()

plt.figure(figsize=(6,4))
plt.bar(labels, counts, color=['red', 'orange', 'green'])
plt.title("Password Strength Distribution")
plt.xlabel("Strength")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

