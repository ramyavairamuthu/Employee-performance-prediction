import os

if os.path.exists("employees.db"):
    print("Database EXISTS in this folder.")
else:
    print("Database DOES NOT exist in this folder.")
