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
        "LWZ (Lempel-Ziv-Welch)": False,
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
    Sequence("Állítsa sorrendbe a JPEG tömörítés lépéseit!", [
        "Blokkokra osztas", "DCT", "Kvantalas", "Cikk-cakk osszefuzes", "Entropia kodolas pl. Huffman"
    ]),
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
]