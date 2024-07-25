## Popis
Po každém zapnutí pc se zapne soubor troll.vbs a lze ho vypnout jen pomocí `taskkill` 


```batch
taskkill /IM "wscript.exe" -F
