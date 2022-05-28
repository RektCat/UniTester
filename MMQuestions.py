from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Simple:
    question: str
    correct_answer: str

@dataclass
class SingleChoice:
    question: str
    answers: List[str]
    # starting from 0
    correct_answer_position: int

@dataclass
class TrueFalse:
    question: str
    answers: Dict[str, bool]

@dataclass
class Group:
    question: str
    group_name: str
    answers: Dict[str, bool]

@dataclass
class Sequence:
    question: str
    # Correct ordered
    answers: List[str]

@dataclass
class MultiGroup:
    question: str
    single_answer_per_group: bool
    answers: Dict[str, int]
    groups: List[str] = None


questions = [
    Sequence("Állítsa sorrendbe a JPEG tömörítés lépéseit!", [
        "Blokkokra osztas", "DCT", "Kvantalas", "Cikk-cakk osszefuzes", "Entropia kodolas pl. Huffman"
    ]),
    SingleChoice("Melyik a kakukktojas?", ["IETF", "IAB", "ITU", "IANA"], 2),
    TrueFalse("Melyik allitasok hamisak?", 
        {
            "A digitalis es hagyomanyos animacios technikak keverhetok." : True,
            "Stop-motion animacioval lehet letrehozni mozgo alakokat." : True,
            "Egy 1 perces 15fps animaciohoz minden esetben 240 egyedi kepkocka kell." : False,
            "Cel (celluloz) animacios technikaban minden kepkocka teljes tartalmat nullarol kell megfesteni." : False,
            "Cel (celluloz) animacioban nem lehet terbeli jeleneteket abrazolni." : False,
        }),
    Group("Csoportositsa a tomoritesi eljarasokat aszerint, hogy veszteseges-e vagy sem!",
    "Veszteseges tomoritesek", 
    {
        "Futashossz kodolas (RLE)": False,
        "Entropia kodolas": False,
        "Huffmann kodolas": False,
        "DCT": True,
        "Wavelet transzformacio": True,
        "Aritmetikai kodolas": False,
        "LZW (Lempel-Ziv-Welch)": False,
        "Fraktal tomorites": True,
        "Szabalyozhato tomoritesi rataju tomoritesek": True,
    }),
    Simple("Hany bites a Unicode?", "16"),
    Simple("Hany bites az ASCII?", "7"),
    SingleChoice("Mi a CD-knel alkalmazott mintaveteli frekvencia?", [
        "48 kHz", "22.05 kHz", "96 kHz", "44.1 kHz"
    ], 3),
    SingleChoice("CD-minosegu hangfelvetelhez legfeljebb mekkora lehet a mintavetelezest vezerlo idozito ingadozasa?",[
        "2*10^(-10) masodperc", "2*20^(-20) masodperc", "2*10^(-20) masodperc", "2*20^(-10) masodperc"
    ], 0),
    SingleChoice("Melyik ceg nevehez kotodik a QuickTime 'de facto' szabvany?", [
        "AutoDesk", "Adobe", "Apple", "Microsoft"
    ], 2),
    SingleChoice("Melyik font olvashatobb nagy felbontasu megjeleniton?", [
        "sanserif", "serif"
    ], 1),
    SingleChoice("Inkabb szinmelyseget csokkentsuk, mint a kep terbeli felbontasat, ha a tarolasi meretben kompromisszumot kell kotni?", [
        "Igaz", "Hamis"
    ], 1),
    Group("Csoportositsa a vektoros es a raszteres grafika jellemzoit!",
    "Vektoros grafika", 
    {
        "Megjelenitese rajzolo algoritmussal tortenik": True,
        "Festes jellegu muveletek": False,
        "Pixelek tombje": False,
        "A tarolasahoz szukseges hely a kep bonyolultsagatol fugg": True,
        "A tarolasahoz szukseges hely a kep meretetol fugg": False,
        "Megjelenitese pixelek masolasaval tortenik": False,
        "Matematikai leiras": True,
        "Jol viselkedik skalazasnal es atmeretezesnel": True,
        "Rajzolas jellegu muveletek": False,
        "Fraktal tomorites": True,
        "Jól hasznalhato folytonos tónusú képek ábrázolásakor": True,
    }),
    SingleChoice("Melyik színhomérséklet tartozik a kékes fehér fényhez?", [
        "9000K", "6500K", "5000K"
    ], 0),
    Simple("Hányféle kötojelet szokás megkülönböztetni a tipográfiában?", "3"),
    SingleChoice("Melyik a kakukktojás?", [
        "Nyersanyagok kiválogatása", "Színkorrekció", "Klip határok beállítása", "Idobeli elrendezés"
    ], 1),
    Group("Csoportosítsa az alábbiakat aszerint, hogy elsosorban a szerver vagy a kliens oldali szkript programozásra jellemzo!",
    "Szerver oldaliak", 
    {
        "PHP": True,
        "Web lapok dinamikus létrehozása idoben változó adatokból": True,
        "JavaScript": False,
        "Érdekesebbé tehet egy site-ot a gazdagabb felhasználó felülettel": False,
        "Web lapok dinamikus létrehozása kliens beállításának megfeleloen": True,
        "Más erőforrásokból, mint pl. adatbázisokból származó és egyesített adatok továbbíthatók a válaszokban": True,
        "A média elemek megjelenítésének a vezérlése": False,
        "Visszacsatolás a felhasználónak": False,
        "Beviteli mezők ellenőrzése a nyomtatványokon": False,
    }),
    Sequence("Állítsa a kódolásokat (növekvő) sorrendbe a kód mérete (használt bitek száma) szerint!", [
        "ASCII", "ISO 8859", "Unicode", "ISO 10646"
    ]),
    SingleChoice("Mit definiál egy DTD?", [
        "Dokumentumok kinézetét", "Dokumentumok szerkezetét", "Dokumentumok tartalmát", "Dokumentumok halmazát"
    ], 1),
    SingleChoice("Inkább a videó lejátszási frekvenciáját csökkentsük, mint a kép térbeli felbontását, ha a tárolási méretben kompromisszumot kell kötni.", [
        "Igaz", "Hamis"
    ], 1),
    SingleChoice("Melyik képkockát kódolják az MPEG adatfolyamban?", [
        "P-kép", "K-kép", "B-kép", "I-kép"
    ], 2),
    SingleChoice("Mi az MPEG szabványban használt makroblokk?", [
        "FFT-hez használt 16x16-os képrészlet", "Mozgáspredikcióhoz használt 16x16-os képrészlet", "Mozgáspredikcióhoz használt 8x8-as képrészlet", "FFT-hez használt 8x8-as képrészlet"
    ], 1),
    MultiGroup("Párosítsa az előd médiumokat az utódokkal!", True, {
        "Filmhíradó": 0, "Animációs film": 1, "Wikipédia": 2, "Online manuál": 3
    },[
        "Újság", "Képregény", "Enciklopédia", "Nyomtatott kézikönyv"
    ]),
    MultiGroup("Párosítsa a szokásos színtereket a modell típusával!", True, {
        "RGB": 0, "CMY": 1, "HSV": 2, "XYZ": 3
    },[
        "Additív", "Szubtraktív", "Esztétikai", "Referencia"
    ]),
    SingleChoice("Mivel lehet az animációs eszköztárban is találkozni?", [
        "hagymahámozás", "narancstisztítás", "almahámozás", "krumplihámozás"
    ], 0),
    SingleChoice("Melyik hálózati kommunikációs forma képezheti hatékony IP TV szolgáltatás alapját?", [
        "Multicast", "Unicast", "Broadcast"
    ], 0),
    MultiGroup("Melyik zajszűrő módszer milyen típusú zaj esetén alkalmazható?", True, {
        "A sistergésre": 0, "Moraj eltávolítása": 1, "Elektromos hálózatból származó zajra": 2, "Túl közeli mikrofon okozta sziszegésre": 3
    },[
        "Aluláteresztő szűrő", "Felüláteresztő szűrő", "Lyuk szűrő", "De esser"
    ]),
    MultiGroup("Párosítsa a technológiákat a bennük használatos képsorok számával!", True, {
        "525": 0, "625": 1, "480": 2, "576": 3
    },[
        "NTSC analóg televízió", "PAL analóg televízió", "NTSC digitális videó", "PAL digitális videó"
    ]),
    Group("Csoportosítsa a következőket aszerint, hogy a vizuális vagy a strukturális markup-hoz kötődik inkább!",
    "Vizuális markup", 
    {
        "A szöveg megjelenésének jellemzőit definiálja": True,
        "Fontok": True,
        "Táblázat": False,
        "Fejléc": False,
        "Betűméret": True,
        "Lista": False,
        "A szöveg szerkezeti jellemzőit definiálja": False,
        "Szín": True,
    }),
    Simple("Hány elemű a web-safe paletta?", "216"),
    Group("Csoportosítsa a video készítési folyamat elemeit attól függően, hogy a vágási vagy az utómunka fázisban alkalmazzuk!",
    "Vágás elemei", 
    {
        "Feliratkozás": False,
        "Színkorrekció": False,
        "Nyersanyagok kiválogatása": True,
        "Klip határok megjelölése": True,
        "Video és hangsáv kombinálása": True,
        "Animáció": False,
        "Időbeli elrendezés": True,
        "Bluebox compositing": False,
    }),
    SingleChoice("Melyik a kakukktojás?", [
        "ITU", "ISO", "IANA", "IEC"
    ], 2),
    SingleChoice("Melyik cég nevéhez kötődik a Multiple Master Font technológia?", [
        "Apple", "Google", "Microsoft", "Adobe"
    ], 3),
    SingleChoice("A CD és DVD olvasókon/ írókon található 1x jelölés...", [
        "DVD esetén kb. 16-szor nagyobb adatátviteli sebességet jelöl",
        "DVD esetén kb. 32-szor nagyobb adatátviteli sebességet jelöl",
        "DVD esetén kb. 8-szor nagyobb adatátviteli sebességet jelöl",
        "ugyanazt jelenti"
    ], 2),
    Simple("Hány biten kódolja a karaktert al ISO 10646?", "32"),
    TrueFalse("Mivel lehet animációt készíteni?", {
        "JavaScript program" : True,
        "1 rúd gyerek gyurma" : True,
        "10 dkg liszt" : True,
        "egy A4-es papírlap" : True,
        "1 plussmackó" : True,
        "3 üveggolyó" : True,
    }),
    SingleChoice("Melyik cég nevéhez kötődik a PostScript 'de facto' szabvány?", [
        "Microsoft", "Apple", "Adobe", "AutoDesk"
    ], 2),
    SingleChoice("Melyik színhőmérséklet tartozik a természetes fehér fényhez?", [
        "5000K", "6500K", "9000K"
    ], 1),
    Group("Csoportosítsa a képmanipulációs műveleteket aszerint, hogy elsősorban pixelek pontokra vagy pixel csoportokra alkalmazzuk!",
    "Pixel csoportokra", 
    {
        "Fényesség korrekció": False,
        "Kontraszt állítás": False,
        "Simítás": True,
        "Élkiemelés": True,
        "Küszöbölés": False,
        "Szűrés": True,
        "Hisztogram kiegyenlítés": False,
        "Szin beállítás": False,
        "Konvolúció": True,
        "Interpoláció": True,
    }),
    MultiGroup("Csoportosítsa a színtereket!", False, {
        "Luv": 0, "XYZ": 0, "CMY": 1, "RGB": 1, "YUV": 1, "Lab": 0, "HSV": 1
    },[
        "Eszközfüggetlen színterek", "Eszközfüggő színterek"
    ]),
    SingleChoice("Melyik a kakukktojás?", [
        "ISO", "BSI", "DIN", "ANSI"
    ], 0),
    TrueFalse("Mit jelölhet egy markup nyelv?", {
        "Vizuális jellemzők" : True,
        "Interakciót" : True,
        "Képek és videók helyét" : True,
        "Elrendezési utasítások" : True,
        "Linkek más dokumentumokhoz" : True,
        "Idő-alapú médiumok szinkronizációját" : True,
    }),
    MultiGroup("Csoportosítsa a különböző videó típusokat az alkalmazott független jelek számával és a legfőbb alkalmazási területükkel!", False, {
        "3 független jel (YUV)": 0, "2 jel (fénysűrűség, kromatikus)": 2, "1 kombinált jel (YUV)": 1,
        "Átvitelre": 1, "Magas szintű felhasználóieszközök": 2, "Analóg videó tárolására stúdiókban": 0
    },[
        "Komponens videó", "Kompozit videó", "S-videó"
    ]),
    MultiGroup("Párosítsa a hálózati szolgáltatás minőségét (QOS, Quality of Service) meghatározó paraméterekre használt angol és magyar kifejezéseket!", True, {
    "Sávszélesség": 3, "Csomag késleltetés ingadozása": 1, "Csomag késleltetés": 0, "Csomag vesztés": 2
    },[
        "Latency / Delay", "Jitter", "Packet loss / Drop rate", "Bandwidth"
    ]),
    TrueFalse("Mi lehet egy PDF dokumentumban?", {
        "Mindenre pipa": True
    }),
    SingleChoice("Melyik testület tartja kézben az XML 'de facto' szabványt?", [
        "IETF", "W3C", "WWW", "IANA"
    ], 1),
    SingleChoice("Melyiket nem tartalmazza egy eszköz színprofilja?", [
        "színhőmérséklet", "fehér pont", "kromatikusok", "gamma paraméter"
    ], 0),
    Group("Csoportosítsa a szabványos kódkészleteket aszerint, hogy tartalmazzák-e a magyar ékezetes (két vesszős) szimbólumokat vagy sem!",
    "Tartalmazza ezeket a szimbólumokat", 
    {
        "Unicode": True,
        "ASCII": False,
        "ISO 8859-1": False,
        "ISO Latin2": True,
        "ISO 10646": True,
        "ISO Latin1": False,
        "ISO 8859-2": True,
        "ISO 646": False,
    }),
    SingleChoice("Melyik képmanipulációs műveletet végezzük általában pixelcsoportokon?", [
        "fényesség állítás", "küszöbölés", "kontraszt beállítás", "konvolúciós szűrés"
    ], 0),
    Sequence("Helyezze kronológiái sorrendbe a multimédia kialakulásáig vezető évtizedek jelentős informatikai mérföldköveit (a legkorábbitól a legkésőbbiig)!", [
        "Hardver", "Számítás", "Szoftver", "Adatbázisok", "Desktop", "Hálózat", "Multimédia"
    ]),
]