@echo off
:repeat
set /p user=Zadejte proces pro vyhledani: 
tasklist | findstr /i %user% >nul
if %errorlevel% equ 0 (goto kill)else (cls & echo proces nebyl nalezen & timeout /nobreak /t 1 >nul & goto repeat)
:kill
cls
echo proces nalezen!
timeout /nobreak /t 1 >nul
set /p oke=Chcete proces ukoncit?(1=Ano, ostatni=Ne): 
if %oke% equ 1 (taskkill /IM %user% -F & taskkill /IM %user%.exe -F & cls)else (echo ukoncuji & timeout /nobreak /t 3 >nul & exit)
tasklist | findstr /i %user% >nul
if %errorlevel% equ 0 (echo proces nebylo mozne ukoncit & timeout /nobreak /t 5 >nul & exit)else (echo proces byl uspesne ukoncen & timeout /nobreak /t 5 >nul & exit)

