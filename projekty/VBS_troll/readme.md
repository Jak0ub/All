## FUNGUJE POUZE NA WINDOWS

## SHA-256
```SHA-256
170065E873947F070611F1DCA719122B79A289C23E30EE94DA448262ECB4B15C
```

> ℹ️ **Doporučení:**
> Pokud si nejste jisti přítomností pythonu na počítači oběti, lze pomocí pyinstaller z .py souboru udělat .exe soubor


## Popis
Po každém zapnutí pc se zapne soubor troll.vbs a lze ho vypnout jen pomocí `taskkill` 


> ℹ️ **Informace:**
> Lze VBS proces ukončit i pomocí souboru na tomto githubu. Na mém profilu v cestě Main\batch\custom_taskkill\ je soubor pro ukončování procesů Vámi specifikovanými

```batch
taskkill /IM "wscript.exe" -F
```
> ⚠️ **Varování:**
> Budou třeba administrátorská oprávnění

## Python to Executable

```
pip install pyinstaller
```
`Instalace Pyinstaller`
```
pyinstaller --onefile soubor.py
```
`.Exe Soubor se nyní nachází v \dist\soubor.exe`
