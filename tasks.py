# -*- coding: utf-8 -*-
"""
tasks.py – 1. pilot feladatsor: EGYENLETEK (középszintű érettségi típusfeladatok)

Szerkezet feladatonként:
    id              – a QR-kód ?task= paramétere (pl. "P1-01")
    cim, tema       – megjelenítéshez
    nehezseg        – 1 (könnyű) … 3 (nehezebb)
    szoveg          – a feladat szövege (Streamlit-markdown, $...$ LaTeX-szel)
    vegeredmeny     – CSAK a mentor belső ellenőrzéséhez! Soha nem jeleníthető meg.
    lepesek         – szigorú sorrendű lépések:
                        cel            – mit kell a diáknak ebben a lépésben elérnie
                        vezeto_kerdes  – a mentor szókratészi kérdése ehhez a lépéshez
                        elvart         – az elvárt köztes eredmény (belső ellenőrzéshez,
                                         a mentor nem mondhatja ki előbb, mint a diák)
    tipikus_hibak   – hiba leírása + a mentor visszakérdezése, ha ezt észleli

Fontos: a 'vegeredmeny' és az 'elvart' mezők a system promptba kerülnek belső
referenciaként. A system promptnak kifejezetten tiltania kell ezek kimondását.
"""

TASKS = {
    # ------------------------------------------------------------------ 01
    "P1-01": {
        "id": "P1-01",
        "cim": "Elsőfokú egyenlet törtes együtthatókkal",
        "tema": "Elsőfokú egyenletek",
        "nehezseg": 1,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! "
                  r"$$\frac{x+3}{4}-\frac{x-1}{6}=2$$",
        "vegeredmeny": "x = 13",
        "lepesek": [
            {"cel": "A közös nevező meghatározása.",
             "vezeto_kerdes": "Melyik az a legkisebb pozitív szám, amely a 4-gyel és a 6-tal is osztható?",
             "elvart": "12"},
            {"cel": "Az egyenlet mindkét oldalának szorzása a közös nevezővel (a jobb oldalt is!).",
             "vezeto_kerdes": "Ha az egyenlet minden tagját megszorzod 12-vel, mi lesz az egyes törtekből, és mi lesz a jobb oldalon álló 2-ből?",
             "elvart": "3(x+3) − 2(x−1) = 24"},
            {"cel": "A zárójelek felbontása az előjelekre figyelve.",
             "vezeto_kerdes": "Mit kapsz, ha a −2-t beszorzod a (x−1) zárójelbe? Figyelj a két negatív szám szorzatára!",
             "elvart": "3x + 9 − 2x + 2 = 24"},
            {"cel": "Az egynemű tagok összevonása.",
             "vezeto_kerdes": "Vond össze külön az x-es tagokat és külön a számokat! Mit kapsz a bal oldalon?",
             "elvart": "x + 11 = 24"},
            {"cel": "Az ismeretlen kifejezése.",
             "vezeto_kerdes": "Milyen műveletet kell mindkét oldalon elvégezned, hogy x egyedül maradjon?",
             "elvart": "x = 13"},
            {"cel": "Ellenőrzés behelyettesítéssel az eredeti egyenletbe.",
             "vezeto_kerdes": "Helyettesítsd vissza az eredményedet az EREDETI egyenletbe! Mennyi lesz a bal oldal?",
             "elvart": "16/4 − 12/6 = 4 − 2 = 2, tehát igaz"},
        ],
        "tipikus_hibak": [
            {"hiba": "A jobb oldali 2-t nem szorozza meg 12-vel (3(x+3) − 2(x−1) = 2).",
             "visszakerdezes": "Az egyenlet MINDEN tagját megszoroztad 12-vel? Nézd meg még egyszer a jobb oldalt!"},
            {"hiba": "Előjelhiba a zárójelbontásnál: −2(x−1) = −2x − 2.",
             "visszakerdezes": "Mennyi (−2)·(−1)? Ellenőrizd a második zárójel felbontását!"},
            {"hiba": "Rossz bővítő szorzó: pl. a 4-es nevezőjű törtet 4-gyel szorozza 3 helyett.",
             "visszakerdezes": "Hányszor van meg a 4 a 12-ben? Ennyiszeresére kell bővítened a számlálót."},
            {"hiba": "Csak a számlálót írja le, a zárójelet elhagyja: 3·x + 3 − 2·x − 1.",
             "visszakerdezes": "A 3-mal a teljes (x+3) számlálót kell szorozni. Hova kell ehhez zárójel?"},
        ],
    },

    # ------------------------------------------------------------------ 02
    "P1-02": {
        "id": "P1-02",
        "cim": "Kétismeretlenes elsőfokú egyenletrendszer",
        "tema": "Egyenletrendszerek",
        "nehezseg": 1,
        "szoveg": r"Oldja meg a valós számpárok halmazán az alábbi egyenletrendszert! "
                  r"$$\begin{aligned} x+y&=11\\ 2x-y&=4 \end{aligned}$$",
        "vegeredmeny": "x = 5, y = 6, azaz (5; 6)",
        "lepesek": [
            {"cel": "A megoldási módszer kiválasztása (egyenlő együtthatók módszere).",
             "vezeto_kerdes": "Nézd meg a két egyenletben az y együtthatóit! Mit veszel észre, és mi történne, ha a két egyenletet összeadnád?",
             "elvart": "Az y együtthatói ellentettek (+1 és −1), összeadáskor y kiesik."},
            {"cel": "A két egyenlet összeadása.",
             "vezeto_kerdes": "Add össze a két egyenlet bal oldalát és jobb oldalát! Milyen egyenletet kapsz?",
             "elvart": "3x = 15"},
            {"cel": "Az első ismeretlen kiszámítása.",
             "vezeto_kerdes": "Mennyi ebből x?",
             "elvart": "x = 5"},
            {"cel": "Visszahelyettesítés a második ismeretlenért.",
             "vezeto_kerdes": "Helyettesítsd be x értékét az első egyenletbe! Mennyi y?",
             "elvart": "5 + y = 11, y = 6"},
            {"cel": "Ellenőrzés a MÁSIK egyenletben.",
             "vezeto_kerdes": "Teljesül-e a második egyenlet is a kapott értékekkel?",
             "elvart": "2·5 − 6 = 4, igaz"},
            {"cel": "A válasz megadása számpárként.",
             "vezeto_kerdes": "Hogyan írod fel a megoldást számpárként?",
             "elvart": "(5; 6)"},
        ],
        "tipikus_hibak": [
            {"hiba": "Kivonja a két egyenletet összeadás helyett, és y nem esik ki (−y − (−y) hibás kezelése).",
             "visszakerdezes": "Melyik művelettel tűnik el az y: összeadással vagy kivonással? Próbáld ki mindkettőt az y-os tagokon!"},
            {"hiba": "Csak x értékét adja meg válaszként.",
             "visszakerdezes": "Az egyenletrendszernek hány ismeretlenje van? Mindegyiket megadtad?"},
            {"hiba": "Abban az egyenletben ellenőriz, amelybe visszahelyettesített.",
             "visszakerdezes": "Abba az egyenletbe helyettesítettél vissza, amelyből y-t számoltad. Melyik egyenlet ellenőrzése mond többet?"},
        ],
    },

    # ------------------------------------------------------------------ 03
    "P1-03": {
        "id": "P1-03",
        "cim": "Szöveges feladat: százalékos árcsökkentés",
        "tema": "Szöveges egyenletek, százalékszámítás",
        "nehezseg": 1,
        "szoveg": r"Egy kabát árát 20%-kal csökkentették, így az új ára 25 600 Ft lett. "
                  r"Mennyi volt a kabát eredeti ára? Válaszát egyenlet felírásával indokolja!",
        "vegeredmeny": "Az eredeti ár 32 000 Ft.",
        "lepesek": [
            {"cel": "Az ismeretlen megválasztása és jelölése.",
             "vezeto_kerdes": "Mit nem ismerünk a feladatban? Jelöld egy betűvel, és írd le, mit jelent!",
             "elvart": "x = a kabát eredeti ára (Ft)"},
            {"cel": "A csökkentett ár kifejezése az ismeretlennel.",
             "vezeto_kerdes": "Ha egy ár 20%-kal csökken, az eredeti ár hány százaléka marad meg? Hogyan írod ezt fel x-szel, tizedes törttel?",
             "elvart": "Az eredeti ár 80%-a marad: 0,8x"},
            {"cel": "Az egyenlet felírása.",
             "vezeto_kerdes": "Minek egyenlő a csökkentett ár a szöveg szerint? Írd fel az egyenletet!",
             "elvart": "0,8x = 25 600"},
            {"cel": "Az egyenlet megoldása.",
             "vezeto_kerdes": "Milyen művelettel kapod meg x-et?",
             "elvart": "x = 32 000"},
            {"cel": "Ellenőrzés a szöveg alapján.",
             "vezeto_kerdes": "Mennyi az eredményed 20%-a, és mennyi marad, ha ezt levonod belőle?",
             "elvart": "32 000 · 0,2 = 6 400; 32 000 − 6 400 = 25 600, egyezik"},
            {"cel": "Szöveges válasz.",
             "vezeto_kerdes": "Fogalmazd meg egy mondatban a választ a feladat kérdésére!",
             "elvart": "A kabát eredeti ára 32 000 Ft volt."},
        ],
        "tipikus_hibak": [
            {"hiba": "A 25 600 Ft-hoz adja hozzá annak 20%-át (30 720 Ft).",
             "visszakerdezes": "A 20% melyik árnak a 20%-a: az eredetinek vagy az újnak? Mihez viszonyítottak a csökkentésnél?"},
            {"hiba": "1,2-vel szorozza a 25 600-at.",
             "visszakerdezes": "Ha az eredményedet 20%-kal csökkented, tényleg 25 600-at kapsz? Ellenőrizd!"},
            {"hiba": "A 0,2x = 25 600 egyenletet írja fel.",
             "visszakerdezes": "A 0,2x a csökkentés mértéke vagy a csökkentett ár? Melyiket ismerjük a szövegből?"},
        ],
    },

    # ------------------------------------------------------------------ 04
    "P1-04": {
        "id": "P1-04",
        "cim": "Abszolútértékes egyenlet",
        "tema": "Abszolútérték",
        "nehezseg": 2,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! $$|2x-3|=7$$",
        "vegeredmeny": "x = 5 vagy x = −2",
        "lepesek": [
            {"cel": "Az abszolútérték jelentésének értelmezése.",
             "vezeto_kerdes": "Mely számok abszolútértéke 7? Mit jelent ez a 2x − 3 kifejezés lehetséges értékeire?",
             "elvart": "2x − 3 = 7 vagy 2x − 3 = −7"},
            {"cel": "Az első eset megoldása.",
             "vezeto_kerdes": "Oldd meg a 2x − 3 = 7 egyenletet!",
             "elvart": "2x = 10, x = 5"},
            {"cel": "A második eset megoldása.",
             "vezeto_kerdes": "Most oldd meg a 2x − 3 = −7 egyenletet is!",
             "elvart": "2x = −4, x = −2"},
            {"cel": "Ellenőrzés mindkét megoldásra.",
             "vezeto_kerdes": "Helyettesítsd vissza mindkét értéket! Mennyi lesz |2x − 3| az egyes esetekben?",
             "elvart": "x = 5: |7| = 7; x = −2: |−7| = 7, mindkettő igaz"},
        ],
        "tipikus_hibak": [
            {"hiba": "Csak a pozitív esetet vizsgálja, egy megoldást ad.",
             "visszakerdezes": "Csak egyetlen szám abszolútértéke lehet 7? Melyik másik számé még?"},
            {"hiba": "Úgy kezeli, mintha az abszolútérték 'eltüntetné a mínuszt': 2x + 3 = 7.",
             "visszakerdezes": "Az abszolútérték a teljes kifejezés értékére vonatkozik, vagy az egyes tagjaira? Mennyi |2·1 − 3|?"},
            {"hiba": "A második esetben −2x − 3 = 7 vagy hasonló előjelhibás felírás.",
             "visszakerdezes": "Írd fel úgy a második esetet, hogy a bal oldal változatlan maradjon, és csak a jobb oldal előjele változzon!"},
        ],
    },

    # ------------------------------------------------------------------ 05
    "P1-05": {
        "id": "P1-05",
        "cim": "Másodfokú egyenlet megoldóképlettel",
        "tema": "Másodfokú egyenletek",
        "nehezseg": 2,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! $$2x^2-5x-3=0$$",
        "vegeredmeny": "x₁ = 3, x₂ = −1/2",
        "lepesek": [
            {"cel": "Az együtthatók azonosítása előjellel együtt.",
             "vezeto_kerdes": "Az ax² + bx + c = 0 alakhoz viszonyítva mennyi itt a, b és c? Figyelj az előjelekre!",
             "elvart": "a = 2, b = −5, c = −3"},
            {"cel": "A diszkrimináns kiszámítása.",
             "vezeto_kerdes": "Számold ki a D = b² − 4ac értékét! Mennyi (−5)², és mennyi −4·2·(−3)?",
             "elvart": "D = 25 + 24 = 49"},
            {"cel": "A megoldások számának megállapítása.",
             "vezeto_kerdes": "A diszkrimináns előjeléből mire következtetsz: hány valós megoldás van? Mennyi √D?",
             "elvart": "D > 0, két valós megoldás; √D = 7"},
            {"cel": "A megoldóképlet felírása behelyettesítve.",
             "vezeto_kerdes": "Írd fel a megoldóképletet a konkrét számokkal! Mennyi −b, és mennyi a nevező (2a)?",
             "elvart": "x = (5 ± 7) / 4"},
            {"cel": "A két gyök kiszámítása.",
             "vezeto_kerdes": "Számold ki külön a + és külön a − esetet!",
             "elvart": "x₁ = 12/4 = 3, x₂ = −2/4 = −1/2"},
            {"cel": "Ellenőrzés (behelyettesítés vagy Viète-formulák).",
             "vezeto_kerdes": "Ellenőrizd: mennyi a két gyök összege és szorzata, és ez egyezik-e −b/a, illetve c/a értékével?",
             "elvart": "x₁ + x₂ = 5/2 = −b/a; x₁·x₂ = −3/2 = c/a"},
        ],
        "tipikus_hibak": [
            {"hiba": "−b helyett −5-öt ír a képletbe (b előjelének elrontása).",
             "visszakerdezes": "Mennyi b értéke? És mennyi akkor −b, vagyis a b ellentettje?"},
            {"hiba": "b²-et −25-nek számolja (−5² = −25 hiba).",
             "visszakerdezes": "A (−5)²-ben a mínusz is négyzetre emelődik? Mennyi (−5)·(−5)?"},
            {"hiba": "A −4ac tagnál előjelhiba: D = 25 − 24 = 1.",
             "visszakerdezes": "c negatív. Mennyi −4·2·(−3)? Hány negatív tényező szerepel a szorzatban?"},
            {"hiba": "A nevezőben 2a helyett 2 szerepel, vagy csak a √D-t osztja el.",
             "visszakerdezes": "A képletben mennyi a nevező, és a számláló melyik részét kell elosztani vele?"},
        ],
    },

    # ------------------------------------------------------------------ 06
    "P1-06": {
        "id": "P1-06",
        "cim": "Törtes egyenlet értelmezési tartománnyal",
        "tema": "Törtes egyenletek",
        "nehezseg": 2,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! "
                  r"$$\frac{x^2+x}{x-3}=\frac{12}{x-3}$$",
        "vegeredmeny": "x = −4 (az x = 3 nem eleme az értelmezési tartománynak)",
        "lepesek": [
            {"cel": "Az értelmezési tartomány megállapítása.",
             "vezeto_kerdes": "Milyen x értékre nem értelmezhetők a törtek? Mit kell kikötnöd?",
             "elvart": "x ≠ 3"},
            {"cel": "A nevezők eltávolítása.",
             "vezeto_kerdes": "Mivel a két tört nevezője ugyanaz és nem nulla, mit mondhatsz a számlálókról? (Vagy: mivel szoroznád meg mindkét oldalt?)",
             "elvart": "x² + x = 12"},
            {"cel": "Nullára rendezés.",
             "vezeto_kerdes": "Rendezd az egyenletet úgy, hogy a jobb oldalon 0 legyen!",
             "elvart": "x² + x − 12 = 0"},
            {"cel": "A másodfokú egyenlet megoldása.",
             "vezeto_kerdes": "Oldd meg ezt a másodfokú egyenletet (megoldóképlettel vagy szorzattá alakítással)!",
             "elvart": "x₁ = 3, x₂ = −4"},
            {"cel": "A gyökök összevetése az értelmezési tartománnyal.",
             "vezeto_kerdes": "Nézd meg az első lépésben tett kikötésedet! Mindkét kapott szám megoldása az eredeti egyenletnek?",
             "elvart": "x = 3 nem megoldás (kizártuk); csak x = −4 marad"},
            {"cel": "Ellenőrzés behelyettesítéssel.",
             "vezeto_kerdes": "Helyettesítsd be a megmaradt értéket az eredeti egyenlet mindkét oldalába!",
             "elvart": "(16 − 4)/(−7) = 12/(−7), igaz"},
        ],
        "tipikus_hibak": [
            {"hiba": "Elhagyja az értelmezési tartományt, és x = 3-at is megoldásnak tekinti.",
             "visszakerdezes": "Próbáld behelyettesíteni az x = 3-at az EREDETI egyenletbe! Mi történik a nevezővel?"},
            {"hiba": "Nullára rendezés nélkül 'szorzattá alakít': x(x + 1) = 12, ezért x = 12 vagy x + 1 = 12.",
             "visszakerdezes": "Egy szorzatról mikor következtethetünk a tényezőire? Csak akkor, ha a szorzat értéke mennyi?"},
            {"hiba": "x-szel egyszerűsít (osztja az egyenletet x-szel), és gyököt veszít.",
             "visszakerdezes": "Szabad-e az egyenletet x-szel osztani, ha nem tudjuk, hogy x nem nulla? Mit veszíthetünk el így?"},
        ],
    },

    # ------------------------------------------------------------------ 07
    "P1-07": {
        "id": "P1-07",
        "cim": "Négyzetgyökös egyenlet hamis gyökkel",
        "tema": "Gyökös egyenletek",
        "nehezseg": 3,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! $$\sqrt{x+7}=x-5$$",
        "vegeredmeny": "x = 9 (az x = 2 hamis gyök)",
        "lepesek": [
            {"cel": "A feltételek megállapítása.",
             "vezeto_kerdes": "Mikor értelmezhető a bal oldali gyök? És milyen előjelű lehet egy négyzetgyök értéke, mit jelent ez a jobb oldalra?",
             "elvart": "x + 7 ≥ 0 és x − 5 ≥ 0, összesen x ≥ 5"},
            {"cel": "Négyzetre emelés.",
             "vezeto_kerdes": "Hogyan tudod eltüntetni a gyököt? Mit kapsz, ha mindkét oldalt négyzetre emeled?",
             "elvart": "x + 7 = (x − 5)²"},
            {"cel": "A jobb oldal kifejtése nevezetes azonossággal.",
             "vezeto_kerdes": "Melyik nevezetes azonosság vonatkozik (a − b)²-re? Bontsd fel!",
             "elvart": "(x − 5)² = x² − 10x + 25"},
            {"cel": "Nullára rendezés.",
             "vezeto_kerdes": "Rendezd az egyenletet ax² + bx + c = 0 alakra!",
             "elvart": "x² − 11x + 18 = 0"},
            {"cel": "A másodfokú egyenlet megoldása.",
             "vezeto_kerdes": "Melyik két szám ezek? (Megoldóképlettel vagy szorzattá alakítással.)",
             "elvart": "x₁ = 9, x₂ = 2"},
            {"cel": "A gyökök vizsgálata a feltétellel és ellenőrzés.",
             "vezeto_kerdes": "Mindkét szám megfelel az első lépésben kapott feltételnek? Ellenőrizd behelyettesítéssel az eredeti egyenletbe!",
             "elvart": "x = 9: √16 = 4 = 9 − 5, igaz; x = 2: √9 = 3 ≠ −3, hamis gyök"},
        ],
        "tipikus_hibak": [
            {"hiba": "(x − 5)²-et x² − 25-nek vagy x² + 25-nek bontja.",
             "visszakerdezes": "Számold ki (x − 5)·(x − 5)-öt tagonként! Hány tag lesz a szorzatban?"},
            {"hiba": "Nem ellenőriz, és mindkét gyököt megoldásnak adja meg.",
             "visszakerdezes": "A négyzetre emelés ekvivalens átalakítás? Mi történik, ha x = 2-t beírod az eredeti egyenletbe?"},
            {"hiba": "Csak a bal oldalt emeli négyzetre: x + 7 = x − 5.",
             "visszakerdezes": "Ha egy egyenlet egyik oldalával elvégzel egy műveletet, mit kell tenned a másik oldallal?"},
        ],
    },

    # ------------------------------------------------------------------ 08
    "P1-08": {
        "id": "P1-08",
        "cim": "Exponenciális egyenlet kiemeléssel",
        "tema": "Exponenciális egyenletek",
        "nehezseg": 3,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! $$3^{x+1}+3^{x}=108$$",
        "vegeredmeny": "x = 3",
        "lepesek": [
            {"cel": "Hatványazonosság alkalmazása.",
             "vezeto_kerdes": "Hogyan írható fel 3^(x+1) két hatvány szorzataként, a hatványozás azonosságai szerint?",
             "elvart": "3^(x+1) = 3 · 3^x"},
            {"cel": "A közös tényező kiemelése.",
             "vezeto_kerdes": "Melyik közös tényezőt tudod kiemelni a bal oldalon? Mi marad a zárójelben?",
             "elvart": "3^x · (3 + 1) = 108, azaz 4 · 3^x = 108"},
            {"cel": "A hatvány kifejezése.",
             "vezeto_kerdes": "Mennyi ebből 3^x?",
             "elvart": "3^x = 27"},
            {"cel": "Azonos alapú hatvány felírása.",
             "vezeto_kerdes": "A 27 a 3-nak hányadik hatványa?",
             "elvart": "27 = 3³"},
            {"cel": "Következtetés a kitevőre indoklással.",
             "vezeto_kerdes": "Ha 3^x = 3³, miért következik ebből, hogy a kitevők egyenlők? Melyik függvénytulajdonság garantálja ezt?",
             "elvart": "Az exponenciális függvény szigorú monotonitása (kölcsönös egyértelműsége) miatt x = 3"},
            {"cel": "Ellenőrzés.",
             "vezeto_kerdes": "Helyettesítsd vissza: mennyi 3⁴ + 3³?",
             "elvart": "81 + 27 = 108, igaz"},
        ],
        "tipikus_hibak": [
            {"hiba": "Összeg esetén összeadja a kitevőket: 3^(x+1) + 3^x = 3^(2x+1).",
             "visszakerdezes": "Melyik műveletnél adódnak össze a kitevők: hatványok szorzásánál vagy összeadásánál? Próbáld ki: 3² + 3¹ egyenlő 3³-nal?"},
            {"hiba": "3^(x+1)-et 3^x + 3-nak vagy 3^x + 1-nek írja.",
             "visszakerdezes": "Nézd meg egy konkrét értékkel: x = 1 esetén mennyi 3^(x+1), és mennyi 3^x + 3?"},
            {"hiba": "A 108-at közvetlenül próbálja 3 hatványaként felírni.",
             "visszakerdezes": "A 108 a 3-nak egész kitevős hatványa? Mit tehetnél előbb a bal oldallal, hogy egyetlen hatvány maradjon?"},
        ],
    },

    # ------------------------------------------------------------------ 09
    "P1-09": {
        "id": "P1-09",
        "cim": "Logaritmusos egyenlet",
        "tema": "Logaritmikus egyenletek",
        "nehezseg": 3,
        "szoveg": r"Oldja meg a valós számok halmazán az alábbi egyenletet! "
                  r"$$\log_2(x+3)+\log_2(x-3)=4$$",
        "vegeredmeny": "x = 5 (az x = −5 nem eleme az értelmezési tartománynak)",
        "lepesek": [
            {"cel": "Az értelmezési tartomány megállapítása.",
             "vezeto_kerdes": "Milyen feltételnek kell teljesülnie egy logaritmus argumentumára? Mit jelent ez a két logaritmusra együtt?",
             "elvart": "x + 3 > 0 és x − 3 > 0, összesen x > 3"},
            {"cel": "A logaritmus azonosságának alkalmazása.",
             "vezeto_kerdes": "Melyik azonosság szerint vonható össze két azonos alapú logaritmus összege egyetlen logaritmussá?",
             "elvart": "log₂((x + 3)(x − 3)) = 4"},
            {"cel": "A logaritmus definíciójának alkalmazása.",
             "vezeto_kerdes": "Mit jelent a logaritmus definíciója szerint, hogy log₂(valami) = 4? Mennyi akkor a 'valami'?",
             "elvart": "(x + 3)(x − 3) = 2⁴ = 16"},
            {"cel": "Az egyenlet rendezése.",
             "vezeto_kerdes": "Melyik nevezetes azonossággal egyszerűsíthető a bal oldal? Mit kapsz x²-re?",
             "elvart": "x² − 9 = 16, x² = 25"},
            {"cel": "A gyökök meghatározása.",
             "vezeto_kerdes": "Mely számok négyzete 25?",
             "elvart": "x = 5 vagy x = −5"},
            {"cel": "Összevetés az értelmezési tartománnyal és ellenőrzés.",
             "vezeto_kerdes": "Mindkét szám benne van az első lépésben meghatározott tartományban? Ellenőrizd a megmaradót behelyettesítéssel!",
             "elvart": "−5 nem megoldás; x = 5: log₂8 + log₂2 = 3 + 1 = 4, igaz"},
        ],
        "tipikus_hibak": [
            {"hiba": "Az argumentumokat összeadja szorzás helyett: log₂(2x) = 4.",
             "visszakerdezes": "Az azonosság szerint logaritmusok összege melyik szám logaritmusa: az argumentumok összegéé vagy szorzatáé?"},
            {"hiba": "A definíciót rosszul alkalmazza: (x + 3)(x − 3) = 4 vagy = 8.",
             "visszakerdezes": "log₂(y) = 4 azt jelenti, hogy a 2-t hányadik hatványra kell emelni? Mennyi tehát y?"},
            {"hiba": "Az értelmezési tartomány nélkül x = −5-öt is megtartja.",
             "visszakerdezes": "Írd be az x = −5-öt az eredeti egyenletbe! Értelmezhető log₂(−2)?"},
        ],
    },

    # ------------------------------------------------------------------ 10
    "P1-10": {
        "id": "P1-10",
        "cim": "Trigonometrikus egyenlet adott alaphalmazon",
        "tema": "Trigonometrikus egyenletek",
        "nehezseg": 2,
        "szoveg": r"Oldja meg az alábbi egyenletet a $[0^\circ;\,360^\circ]$ intervallumon! "
                  r"$$2\sin x-1=0$$",
        "vegeredmeny": "x = 30° vagy x = 150°",
        "lepesek": [
            {"cel": "Rendezés sin x-re.",
             "vezeto_kerdes": "Fejezd ki az egyenletből sin x értékét!",
             "elvart": "sin x = 1/2"},
            {"cel": "Nevezetes szög megkeresése.",
             "vezeto_kerdes": "Melyik nevezetes hegyesszög szinusza 1/2?",
             "elvart": "x₁ = 30°"},
            {"cel": "A második megoldás megkeresése az egységkörön.",
             "vezeto_kerdes": "Az egységkörön melyik síknegyedekben pozitív a szinusz? A 30°-on kívül melyik szögnek ugyanennyi a szinusza 0° és 360° között?",
             "elvart": "Az I. és II. negyedben; x₂ = 180° − 30° = 150°"},
            {"cel": "Az alaphalmaz ellenőrzése.",
             "vezeto_kerdes": "Van-e további megoldás a [0°; 360°] intervallumban? Mi a helyzet 30° + 360°-kal?",
             "elvart": "Nincs több; 390° már kívül esik az intervallumon"},
            {"cel": "Ellenőrzés és válasz.",
             "vezeto_kerdes": "Ellenőrizd mindkét szögre, hogy 2 sin x − 1 = 0! Mi a végső válasz?",
             "elvart": "2·(1/2) − 1 = 0 mindkettőre; x = 30° vagy x = 150°"},
        ],
        "tipikus_hibak": [
            {"hiba": "Csak egy megoldást ad meg (30°).",
             "visszakerdezes": "Rajzold fel az egységkört! Hány pontjában lesz az y koordináta 1/2?"},
            {"hiba": "A második megoldást 360° − 30° = 330°-nak számolja.",
             "visszakerdezes": "Mennyi sin 330°? Pozitív vagy negatív a szinusz a IV. negyedben?"},
            {"hiba": "Radiánban adja meg a választ (π/6, 5π/6), holott fokban van az alaphalmaz.",
             "visszakerdezes": "Milyen mértékegységben adták meg az alaphalmazt? Abban add meg a választ is!"},
        ],
    },
}


# ---------------------------------------------------------------- segédfüggvények
def get_task(task_id: str):
    """Visszaadja a feladatot az ID alapján (kis-/nagybetűtől függetlenül), vagy None-t."""
    if not task_id:
        return None
    return TASKS.get(task_id.strip().upper())


def validate_tasks():
    """Egyszerű integritás-ellenőrzés: kötelező mezők, ID-egyezés, lépésszerkezet."""
    kotelezo = {"id", "cim", "tema", "nehezseg", "szoveg", "vegeredmeny", "lepesek", "tipikus_hibak"}
    for kulcs, t in TASKS.items():
        hianyzo = kotelezo - t.keys()
        assert not hianyzo, f"{kulcs}: hiányzó mezők: {hianyzo}"
        assert t["id"] == kulcs, f"{kulcs}: az 'id' mező nem egyezik a kulccsal"
        assert len(t["lepesek"]) >= 3, f"{kulcs}: túl kevés lépés"
        for i, l in enumerate(t["lepesek"], 1):
            assert {"cel", "vezeto_kerdes", "elvart"} <= l.keys(), f"{kulcs} {i}. lépés hiányos"
        for h in t["tipikus_hibak"]:
            assert {"hiba", "visszakerdezes"} <= h.keys(), f"{kulcs}: hiányos tipikus hiba"
    return True


if __name__ == "__main__":
    validate_tasks()
    print(f"OK – {len(TASKS)} feladat betöltve: {', '.join(TASKS)}")
