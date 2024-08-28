## JEDNÁ SE O BATCH NIKOLI BASH, PROTO FUNGUJE POUZE NA WINDOWS

## SHA-256
```SHA-256
A3F62D55A57A466344C57A79C4DC837A2341EF3583C14538C8D664FA598764CD
```

> ℹ️ **Doporučení:**
> Jedná se o taskkill s parametrem -F, proto budou i systémové procesy ukončeny. Berte na vědomí rizika ukončování systémových procesů


## Popis
Po zapnutí souboru se spustí CLI, ve kterém lze vyhledat dostupnost procesu. Pokud byl proces nalezen, bude uživatel dotázán jestli chce proces ukončit. V případě inputu 1 pro ANO, bude proces ukončen. V případě chyby je uživatel informován


```batch
main.bat
```
> ⚠️ **Varování:**
> Lze pomocí tohoto souboru ukončit i systémové soubory
