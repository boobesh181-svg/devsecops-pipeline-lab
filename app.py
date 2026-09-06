import hashlib
import os
import subprocess

# Vulnerability 1: Hardcoded secret/API key
AWS_SECRET_KEY = "AKIAIMOCKSECRETKEYDOESNOTEXIST123"

def run_system_diagnostic(user_input):
    # Vulnerability 2: Command injection risk (shell=True)
    command = "ping -c 1 " + user_input
    subprocess.Popen(command, shell=True)

def hash_user_password(password):
    # Vulnerability 3: Weak cryptographic algorithm
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Application Initialized.")
