Nyiss egy új projektet Pycharmban(Fontos, hogy kigenerálódjon egy venv mappa, anélkül nem működik)
Az importoknál kattints a flask-re, villanykörte: install package (1-2 percet várj utána, amíg eltűnik a piros aláhúzás).
Kattints Terminal: pip install flask_cors (1-2 percet várj utána, amíg eltűnik a piros aláhúzás)
Ha a flask_cors így is aláhúzva marad, akkor keresd meg a venv mappán belül Lib\site-packages és ezen belülre másold be a következő linken található mappákat és a six.py file-t:
https://drive.google.com/drive/folders/1z018yyCrZ52zyBsgffSuuDriaAXI4naZ?usp=sharing

Miután ezek megvannak:
A python employeeDB.py fájlban hozod létre az adatbázis, ezt személyre szabhatod, hogy egyedi táblád legyen.
Terminál: python employeeDB.py Így létrejön a db fájl.
Ezt követően elindítható a webapp és ha sikerült elindítani, utána nyisd meg az add.html fájlt, adj pár adatot hozzá az adatbázishoz.
Ha már van rekord az adatbázisban, akkor megnyitható az index.html fájl és ki kell írnia az adatokat a nyomógombokkal együtt.
