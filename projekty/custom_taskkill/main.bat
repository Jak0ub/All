@echo off
goto main
:fail
cls
echo zadany proces nebyl nalezen!
del asdasdas.txt
:main
set /p ok=Jaky proces hledate? 
tasklist > asdasdas.txt
cls
findstr /i "%ok%" asdasdas.txt
if %errorlevel% equ 0 (goto kill)else (goto fail)
:kill
set /p main=zadejte proces na ukonceni(Pokud nic tak ENTER): 
taskkill /IM "%main%.exe" -F
del asdasdas.txt
