## Popis
Po každém zapnutí pc se zapne soubor troll.vbs a lze ho vypnout jen pomocí taskkill 


## Ukončení procesu souboru troll.vbs

Chcete-li ukončit proces souboru troll.vbs neboli proces jménem `wscript.exe`, můžete použít následující příkaz v batch souboru:

```batch
taskkill /IM "wscript.exe" /F

