import os, time, subprocess

def trigger_alarm(filename):
    # STRENGER FILTER: Ignoriere alles, was das System selbst schreibt
    ignored_patterns = [".log", ".zip", "forensic", ".git", "system.log", "FETCH_HEAD"]
    if any(pattern in filename for pattern in ignored_patterns):
        return
    
    print(f"🚨 ECHTE MANIPULATION ERKANNT: {filename}")
    # Absolute Pfade nutzen
    core_path = "/sdcard/Download/INFINITY_SYSTEM/CORE/"
    subprocess.run(["bash", os.path.join(core_path, "issue_pusher.sh")])
    subprocess.run(["bash", os.path.join(core_path, "blackbox_snapshot.sh")])

def start_nexus():
    print("------------------------------------------------")
    print("INFINITY NEXUS ULTRA v2: FILTER AKTIV")
    print("------------------------------------------------")
    
    # Überwachung des Kernverzeichnisses
    cmd = ['inotifywait', '-m', '-e', 'modify', '/sdcard/Download/INFINITY_SYSTEM/CORE/']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    while True:
        line = proc.stdout.readline()
        if line:
            # Extrahiere den Dateinamen korrekt
            parts = line.decode().strip().split(" ")
            if len(parts) >= 3:
                trigger_alarm(parts[2])

if __name__ == "__main__":
    start_nexus()
