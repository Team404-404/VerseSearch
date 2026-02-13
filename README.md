# Verskereső Flask alkalmazás

Ez egy egyszerű Flask-alapú webalkalmazás, amely verssorok alapján keres a megadott mappában található versek között. A keresés pontos egyezés helyett hasonlóság alapján történik (fuzzy search), így akkor is találhat verset, ha nem pontosan idézed a sort.

## Funkciók

- Versek betöltése `.txt` fájlokból
- Keresés egy megadott verssor alapján
- Ékezetmentesített összehasonlítás
- Hasonlósági küszöb: 69.9% feletti egyezés esetén találat
- JSON formátumú válasz

## Telepítés

1. **Függőségek telepítése**

```bash
pip install flask
