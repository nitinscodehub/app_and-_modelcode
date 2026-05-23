import os
import requests

# Data store karne ke liye ek folder banana
os.makedirs("gait_dataset", exist_ok=True)

# PhysioNet se kuch main subjects ki files download karna
# Co = Control (Healthy), Pt = Parkinson's Patient
files_to_download = [
    "GaCo01_01.txt", "GaCo02_01.txt", "GaCo03_01.txt", "GaCo04_01.txt",
    "GaPt01_01.txt", "GaPt02_01.txt", "GaPt03_01.txt", "GaPt04_01.txt"
]

base_url = "https://physionet.org/files/gaitpdb/1.0.0/"

print("--- Real PhysioNet dataset download ho raha hai ---")
for file_name in files_to_download:
    url = base_url + file_name
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"gait_dataset/{file_name}", "w") as f:
            f.write(response.text)
        print(f"Successfully download hua: {file_name}")
    else:
        print(f"Download fail hua: {file_name}")

print("Saare samples 'gait_dataset' folder me save ho gaye hain.")