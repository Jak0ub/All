# Překladač Pro Náročnější

## SHA-256
```SHA-256
0FA51FDCAF5FE25A62FA67BFC3B9D62C6162ABCAAC6AB1287E3B92509F911CEE
```
## K úvodu

`1.`
Pro uživatekské výsledky budete potřebovat `Vysledky.txt` soubor. Soubor je zahashovaný! V programu samotném jsou data ovšem čitelná

`2.`
Pro všechna uživatelská jména a hesla budete potřebovat `credentials.file` soubor, který je také zahashovaný!

`3.`
Pro všechna slovíška a jejich překlad budete potřebovat `words_configFile.txt` soubor. Není hashovaný!
> ❕ **Důležité:**
> Pokud chcete zamezit modifikaci ostatními uživateli,(pokud plánujete soubor distribuovat. Například na školní síti) upravte oprávnění souborů na Read-only pro koncové uživatele. Ovšem soubor výsledky NIKDY nedávejte jako Read-only, jinak se výsledky uživatelů nezapíšou


### ⚠️ Všechny tyto soubory jsou automaticky vytvořeny pokud chybí, takže pokud Vám záleží na obsahu některého ze souborů, budete muset soubor sdílet mezi zařízeními, na kterých tento obsah chcete mít⚠️


## O projektu

Projekt zaměřený pro ty, kteří si chtějí procvičit cizí jazyk. Soubor je na všechny OS. Doufám, že Vám v učení pomůže. Jedná se o CLI!
> ⚠️ **Upozornění:**
> Soubor může mít chyby, při nalezení některé z nich mě prosím kontaktujte


## Popis

Bude dobré si něco zjistit, například defaultní uživatel je `admin` a heslo je `Password`. Tento model je náročnější, proto doporučuji nejprve odzkoušet, až poté užívat v praxi.

## Stáhnutí
Jednoduše klikněte na projekt `main.py`  a stáhněte tzv."raw file". Samotný program Vám poté popíše co a jak

> ℹ️ **Informace:**
> Je snad jasné, že pro spuštění bude potřeba `Python`

## Python to Executable

```
pip install pyinstaller
```
`Instalace Pyinstaller`
```
pyinstaller --onefile soubor.py
```
`.Exe Soubor se nyní nachází v \dist\soubor.exe`

