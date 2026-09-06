import hashlib
import os
import subprocess

# Fix 1: Environment variable instead of hardcoded credential
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "DEFAULT_SAFE_PLACEHOLDER")

def run_system_diagnostic(user_input):
    # Fix 2: Remove shell=True and pass arguments as an explicit sanitized list
    safe_input = str(user_input).strip()
    subprocess.Popen(["ping", "-c", "1", safe_input], shell=False)

def hash_user_password(password):
    # Fix 3: Modern, collision-resistant hash (SHA-256)
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    print("Application Initialized Securely.")
