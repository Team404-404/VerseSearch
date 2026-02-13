# Biztonsági irányelvek – Verskereső Flask alkalmazás

## Támogatott verziók

Mivel ez egy egyszerű oktatási célú Flask alkalmazás, jelenleg csak a legfrissebb verzió támogatott:

| Verzió   | Támogatott            |
|----------|----------------------|
| 1.0.x    | :white_check_mark: Igen |
| < 1.0    | :x: Nem              |

## Biztonsági rés bejelentése

Ez az alkalmazás **helyi fejlesztési környezetben** való futtatásra készült, és nem rendelkezik beépített biztonsági funkciókkal (pl. hitelesítés, HTTPS, bemenet szigorú validálása).

### Ismert biztonsági korlátok
- Nincs felhasználói hitelesítés
- Nincs rate limiting
- Nincs HTTPS beállítás
- A keresés minden fájlt beolvas a `vers_tar` mappából
- Nincs szűrés a fájlnevekre (bármilyen `.txt` fájlt betölt)

### Bejelentés módja
Ha biztonsági rést találsz, kérjük, nyiss egy **GitHub Issue**-t, vagy írj a [biztonsag@pelda.hu](mailto:biztonsag@pelda.hu) címre.

### Javasolt biztonsági intézkedések éles használat előtt
- Bemeneti adatok szigorúbb validálása
- HTTPS beállítása (pl. Let's Encrypt)
- Hitelesítés hozzáadása ha szükséges
- Rate limiting bevezetése
- Környezeti változók használata érzékeny adatokhoz

### Felelősség kizárása
Ez az alkalmazás **oktatási célra** készült. Éles környezetben történő használat előtt **alapos biztonsági felülvizsgálat szükséges**.
