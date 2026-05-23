GaitWatch — Complete Usage Guide
1. Server Start (Laptop)
cd /home/kali/Documents/college\ project/gaitwatch/server
python3 server_production_ready.py
Output dikhega: ✓ Server running at http://0.0.0.0:8000

2. APK Install (Phone)
Purana APK uninstall kar
build/app/outputs/flutter-apk/gaitwatch.apk phone me copy karke install kar
Phone ko same WiFi pe connect kar (192.168.0.x network)
3. Test Run
App khol
"Start Test" dabayega → Permission popup aayega → Allow
Phone pocket me rakh, 30 sec walk kar
Data server pe jayega → LSTM model predict karega → Result dashboard pe dikhega
4. Check Result
App automatically result screen pe le jayega — risk score, status, confidence, step count sab dikhega.
