import subprocess

# After Effects 실행 파일 경로
after_effects_path = "C:\\Program Files\\Adobe\\Adobe After Effects CC 2022\\Support Files\\AfterFX.exe"

# After Effects 스크립트 파일 경로
script_path = "script.jsx"

# After Effects를 백그라운드에서 실행
subprocess.Popen([after_effects_path, "-r", script_path], shell=True)
