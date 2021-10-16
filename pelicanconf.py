#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tech WG'
AUTHORS = {"Tech WG": {
        "url": "https://th.pycon.org/",
        "blurb": "Website author.",
        "avatar": "",
    },}
SITENAME = 'PyCon APAC 2021'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Bangkok'

DEFAULT_LANG = 'en'

LANGUAGE_CODES = {
        'en': 'English',
        'th': 'ไทย',
        }

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),
        )

# Social widget
SOCIAL = (('email', 'contact@pyconthailand.org'),
          ('facebook', 'https://www.facebook.com/Pyconthailand'),
          ('twitter', 'https://twitter.com/pyconthailand'),
          ('instagram','https://www.instagram.com/pyconthailand/'),
          ('youtube','https://www.youtube.com/pyconthailand'),
         )

DEFAULT_PAGINATION = False

JINJA_GLOBALS = {
    "speakers": [
        {
            "img": "/theme/img/speakers/andygoldberg.png",
            "name": "Andy Goldberg",
            "pronoun": "He/Him",
            "country": "USA",
            "github": "https://github.com/2x2xplz",
            "twitter": "https://twitter.com/cfnine",
            "linkedin": "https://www.linkedin.com/in/andygoldberg/",
            "link": "/pages/speakers#Andy-Goldberg",
        },
        {
            "img": "/theme/img/speakers/abdurrahmaanjanhangeer.jpg",
            "name": "Abdur-Rahmaan J",
            "pronoun": "He/Him",
            "country": "Mauritius",
            "github": "https://github.com/Abdur-RahmaanJ",
            "twitter": "https://twitter.com/osdotsystem",
            "linkedin": "https://www.linkedin.com/in/appinv/",
            "link": "/pages/speakers#abudur-rahmaan",
        },
        {
            "img": "/theme/img/speakers/kanouivirach.jpg",
            "name": "Kan Ouivirach",
            "pronoun": "He/Him",
            "country": "Thailand",
            "github": "https://github.com/zkan",
            "twitter": "https://twitter.com/zkancs",
            "linkedin": "https://www.linkedin.com/in/kanouivirach/",
            "instagram": "https://instagram.com/zkancs",
            "link": "/pages/speakers#Kan-Ouivirach",
        },
        {
            "img": "/theme/img/speakers/susanshuchang.jpg",
            "name": "Susan Shu Chang",
            "pronoun": "She/Her",
            "country": "Canada",
            "twitter": "https://twitter.com/susan_shuc",
            "linkedin": "https://www.linkedin.com/in/susan-shu-chang/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/TonyaSims.jpg",
            "name": "Tonya Sims",
            "pronoun": "She/Her",
            "country": "USA",
            "github": "https://github.com/geekchick",
            "twitter": "https://twitter.com/tonyasims",
            "linkedin": "https://www.linkedin.com/in/tonyasims/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/AnthonyShaw.jpg",
            "name": "Anthony Shaw",
            "pronoun": "He/Him",
            "country": "Australia",
            "github": "https://github.com/tonybaloney",
            "twitter": "https://twitter.com/anthonypjshaw",
            "linkedin": "https://www.linkedin.com/in/anthonypshaw/",
            "link": "/pages/speakers#Anthony-Shaw",
        },
        {
            "img": "/theme/img/speakers/pratibhajagnere.jpg",
            "name": "Pratibha",
            "pronoun": "She/Her",
            "country": "India",
            "github": "https://github.com/pratibhajagnere",
            "twitter": "https://twitter.com/Pratibhajagnere",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/MattLebrun.jpg",
            "name": "Matt Lebrun",
            "pronoun": "He/Him",
            "country": "Philippines",
            "github": "https://github.com/cr8ivecodesmith",
            "twitter": "https://twitter.com/cr8ivecodesmith",
            "linkedin": "https://www.linkedin.com/in/cr8ivecodesmith/",
            "instagram": "https://instagram.com/cr8ivecodesmith",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/TusharBansal.jpg",
            "name": "Tushar Bansal",
            "pronoun": "He/Him",
            "country": "India",
            "twitter": "https://twitter.com/tusharb104?s=09",
            "instagram": "https://instagram.com/bansal__tushar",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/novialistiyani.jpg",
            "name": "Novia L Wirhaspati",
            "pronoun": "She/Her",
            "country": "Indonesia",
            "github": "https://github.com/novialistiyani",
            "linkedin": "https://www.linkedin.com/in/novia-listiyani-wirhaspati",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/NaomiCeder.jpg",
            "name": "Naomi Ceder",
            "pronoun": "She/Her",
            "country": "USA",
            "github": "https://github.com/nceder",
            "twitter": "https://twitter.com/NaomiCeder",
            "linkedin": "https://www.linkedin.com/in/naomiceder",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/YothinMuangsommuk.jpg",
            "name": "Yothin Muangsommuk ",
            "pronoun": "He/Him",
            "country": "Thailand",
            "github": "https://github.com/yothinix",
            "twitter": "https://twitter.com/yothinix",
            "linkedin": "https://www.linkedin.com/in/yothinx",
            "instagram": "https://instagram.com/yothinix",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/kirchou.jpg",
            "name": "Kir Chou ",
            "pronoun": "-",
            "country": "Taiwan",
            "github": "https://github.com/note35",
            "twitter": "https://twitter.com/k1rch0u",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/IsabelaMoreira.JPG",
            "name": "Isabela Moreira",
            "pronoun": "She/Her",
            "country": "USA",
            "github": "https://github.com/isabelacmor",
            "twitter": "https://twitter.com/isabelacmor",
            "linkedin": "https://www.linkedin.com/in/isabela-moreira/",
            "link": "/pages/speakers#Isabela-Moreira",
        },
        {
            "img": "/theme/img/speakers/ScottyKwok.jpg",
            "name": "Scotty Kwok",
            "pronoun": "He/Him",
            "country": "Hong Kong",
            "github": "https://github.com/scottykwok",
            "twitter": "https://twitter.com/scottykwok",
            "linkedin": "https://www.linkedin.com/in/scottykwok/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/DrCherHanLau.jpg",
            "name": "Dr. Lau Cher Han",
            "pronoun": "He/Him",
            "country": "Malaysia",
            "github": "https://github.com/drhanlau",
            "twitter": "https://twitter.com/cherhan",
            "linkedin": "https://www.linkedin.com/in/drhanlau/",
            "instagram": "https://instagram.com/drhanlau",
            "link": "/pages/speakers#Dr-Lau-Cher-Han",
        },
        {
            "img": "/theme/img/speakers/NeerajPandey.jpg",
            "name": "Neeraj Pandey",
            "pronoun": "He/Him",
            "country": "India",
            "github": "https://github.com/neerajp99",
            "twitter": "https://twitter.com/neerajp99",
            "instagram": "https://instagram.com/gen0art",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/GrimmerKang.jpg",
            "name": "Grimmer Kang",
            "name2": "康登傑",
            "pronoun": "He/Him",
            "country": "Taiwan",
            "github": "https://github.com/grimmer0125",
            "linkedin": "https://www.linkedin.com/in/tckang/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/DimaDinama.JPG",
            "name": "Dima Maharika Dinama",
            "pronoun": "He/Him",
            "country": "Indonesia",
            "github": "https://github.com/dmaharika",
            "twitter": "https://twitter.com/dmaharika",
            "linkedin": "https://www.linkedin.com/in/dmaharika/",
            "instagram": "https://instagram.com/dmaharika",
            "link": "/pages/speakers#Dima-M-Dinama",
        },
        {
            "img": "/theme/img/speakers/KatieMcLaughlin.jpg",
            "name": "Katie McLaughlin",
            "pronoun": "She/Her",
            "country": "Australia",
            "github": "https://github.com/glasnt",
            "twitter": "https://twitter.com/glasnt",
            "linkedin": "https://www.linkedin.com/in/glasnt/",
            "instagram": "https://instagram.com/glasnt",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/DiogPascua.jpg",
            "name": "Diogenes Armando Pascua",
            "pronoun": "He/Him",
            "country": "Philippines",
            "linkedin": "https://www.linkedin.com/in/diogenes-pascua-132185118?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BOL597v%2FCQqa57v9Ecte4AA%3D%3D/",
            "link": "/pages/speakers#Diogenes-Armando-Pascua",
        },
        {
            "img": "/theme/img/speakers/IvyFung.jpg",
            "name": "Ivy Fung",
            "pronoun": "She/Her",
            "country": "Malaysia",
            "github": "https://github.com/ivyfung1",
            "twitter": "https://twitter.com/ivyfung81",
            "linkedin": "https://www.linkedin.com/in/ivyfung/",
            "instagram": "https://instagram.com/ivyfung1",
            "link": "/pages/speakers#Ivy-Fung",
        },
        {
            "img": "/theme/img/speakers/gajendra.jpg",
            "name": "Gajendra Deshpande",
            "pronoun": "He/Him",
            "country": "India",
            "github": "https://github.com/gcdeshpande",
            "twitter": "https://twitter.com/gcdeshpande",
            "linkedin": "https://www.linkedin.com/in/gajendradeshpande/",
            "link": "/pages/speakers#Gajendra-Deshpande",
        },
        {
            "img": "/theme/img/speakers/wujingjing.jpg",
            "name": "Wu Jing Jing",
            "name2": "吴京京",
            "pronoun": "He/Him",
            "country": "China",
            "github": "https://github.com/wj-Mcat",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/KanisornSutham.jpg",
            "name": "Kanisorn Sutham",
            "pronoun": "He/Him",
            "country": "Thailand",
            "github": "https://github.com/heyfirst",
            "twitter": "https://twitter.com/heyfirst",
            "linkedin": "https://www.linkedin.com/in/kanisorn-sutham/",
            "link": "/pages/speakers#Kanisorn-Sutham",
        },
        {
            "img": "/theme/img/speakers/ArvsLat.jpg",
            "name": "Joshua Arvin Lat",
            "pronoun": "He/Him",
            "country": "Philippines",
            "github": "https://github.com/joshualat",
            "twitter": "https://twitter.com/mrjoshualat",
            "linkedin": "https://www.linkedin.com/in/joshualat/",
            "link": "/pages/speakers#Joshua-Arvin-Lat",
        },
        {
            "img": "/theme/img/speakers/JiwonKim.jpg",
            "name": "Jiwon Kim",
            "pronoun": "She/Her",
            "country": "Korea",
            "github": "https://github.com/jiwon5315",
            "instagram": "https://instagram.com/jiwon5315",
            "link": "/pages/speakers#Kim-JiWon",
        },
        {
            "img": "/theme/img/speakers/peacock.jpg",
            "name": "Peacock",
            "pronoun": "He/Him",
            "country": "Japan",
            "github": "https://github.com/peacock0803sz",
            "twitter": "https://twitter.com/peacock0803sz",
            "linkedin": "https://www.linkedin.com/in/peacock0803sz/",
            "instagram": "https://instagram.com/peacock0803sz",
            "link": "",
        },
        
        {
            "img": "/theme/img/speakers/Ming-YangHo.jpg",
            "name": "Ming-Yang Ho",
            "pronoun": "He/Him",
            "country": "Taiwan",
            "github": "https://github.com/Kaminyou",
            "linkedin": "https://www.linkedin.com/in/kaminyou/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/HARSH.jpg",
            "name": "Harsh",
            "pronoun": "He/Him",
            "country": "India",
            "github": "https://github.com/harshcasper",
            "twitter": "https://twitter.com/harsh_casper",
            "linkedin": "https://www.linkedin.com/in/harshcasper/",
            "instagram": "https://instagram.com/harshcasper",
            "link": "/pages/speakers#Harsh",
        },
        {
            "img": "/theme/img/speakers/Albert-Yumol.jpg",
            "name": "Albert Yumol",
            "pronoun": "-",
            "country": "Philippines",
            "github": "https://github.com/albertyumol",
            "twitter": "https://twitter.com/albert1177",
            "linkedin": "https://www.linkedin.com/in/albertyumol/",
            "link": "/pages/speakers#Albert-Yumol",
        },
        {
            "img": "/theme/img/speakers/ZorexSalvo.JPG",
            "name": "Zorex",
            "pronoun": "He/Him",
            "country": "Philippines",
            "github": "https://github.com/zorexsalvo",
            "twitter": "https://twitter.com/zorexsalvo",
            "linkedin": "https://www.linkedin.com/in/zorexsalvo/",
            "instagram": "https://instagram.com/zorexsalvo",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/JaeyoonKim.jpg",
            "name": "Jaeyoon Kim",
            "pronoun": "He/Him",
            "country": "South Korea",
            "linkedin": "https://www.linkedin.com/in/jaeyoon-kim-99533113a/",
            "link": "/pages/speakers#Kim-Jaeyoon",
        },
        {
            "img": "/theme/img/speakers/AnjLapastora.jpg",
            "name": "Anj Lapastora",
            "pronoun": "She/Her",
            "country": "Philippines",
            "github": "https://github.com/anjlapastora",
            "linkedin": "https://www.linkedin.com/in/angelica-lapastora-6585b2139/",
            "link": "/pages/speakers#Anj-Lapastora",
        },
        {
            "img": "/theme/img/speakers/OngChinHwee.jpg",
            "name": "Chin Hwee Ong",
            "pronoun": "She/Her",
            "country": "Singapore",
            "github": "https://github.com/hweecat",
            "twitter": "https://twitter.com/ongchinhwee",
            "linkedin": "https://www.linkedin.com/in/ongchinhwee/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/YevonnaelAndrew.jpg",
            "name": "Yevonnael Andrew",
            "pronoun": "He/Him",
            "country": "Indonesia",
            "github": "https://github.com/glasnt",
            "twitter": "https://twitter.com/glasnt",
            "linkedin": "https://www.linkedin.com/in/yevonnael-andrew-3351b9a7/",
            "instagram": "https://instagram.com/yevonnael_aw",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/AravindPutrevu.jpg",
            "name": "Aravind Putrevu",
            "pronoun": "He/Him",
            "country": "India",
            "github": "https://github.com/aravindputrevu",
            "twitter": "https://twitter.com/aravindputrevu",
            "linkedin": "https://www.linkedin.com/in/aravindputrevu",
            "link": "/pages/speakers#Aravind-Putrevu",
        },
        {
            "img": "/theme/img/speakers/MasashiShibata.jpg",
            "name": "Masashi Shibata",
            "pronoun": "He/Him",
            "country": "Japan",
            "github": "https://github.com/c-bata",
            "twitter": "https://twitter.com/c-bata",
            "linkedin": "https://www.linkedin.com/in/c-bata/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/KalyanPrasad.jpg",
            "name": "Kalyan Prasad",
            "pronoun": "He/Him",
            "country": "India",
            "twitter": "https://twitter.com/itskpflow",
            "linkedin": "https://www.linkedin.com/in/kalyan-prasad-3a647b22/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/IvanTorroledo.jpg",
            "name": "Iván Torroledo",
            "pronoun": "He/Him",
            "country": "Columbia",
            "github": "https://github.com/torroledo",
            "twitter": "https://twitter.com/IvanTorroledo",
            "linkedin": "https://www.linkedin.com/in/Ivantorroledopena/",
            "instagram": "https://instagram.com/ivantorroledo",
            "link": "/pages/speakers#Ivan-Torroledos",
        },
        {
            "img": "/theme/img/speakers/RamonPerez.JPG",
            "name": "Ramon Perez",
            "pronoun": "He/Him",
            "country": "Dominica",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/KarishmaBabbar.jpg",
            "name": "Karishma Babbar",
            "pronoun": "She/Her",
            "country": "India",
            "linkedin": "https://linkedin.com/in/karishma-babbar",
            "instagram": "https://instagram.com/karishma.babbar",
            "link": "/pages/speakers#Karishma-Babbar",
        },
        {
            "img": "/theme/img/speakers/BenThompson.jpg",
            "name": "Ben Thompson",
            "pronoun": "He/Him",
            "country": "Thailand",
            "instagram": "https://instagram.com/chiangmaiosteopathy",
            "link": "/pages/speakers#Ben-Thompson",
        },
        {
            "img": "/theme/img/speakers/DrewMallory.jpg",
            "name": "Dr. Drew B. Mallory",
            "pronoun": "He/Him",
            "country": "USA",
            "linkedin": "https://www.linkedin.com/in/drewbmallory/",
            "link": "/pages/speakers#Dr-Drew-Mallory",
        },
        {
            "img": "/theme/img/speakers/TakanoriSuzuki.jpg",
            "name": "Takanori Suzuki",
            "pronoun": "He/Him",
            "country": "Japan",
            "github": "https://github.com/takanory",
            "twitter": "https://twitter.com/takanory",
            "linkedin": "https://www.linkedin.com/in/takanory/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/JesseHirata.jpg",
            "name": "Tetsuya Jesse Hirata",
            "pronoun": "He/Him",
            "country": "Columbia",
            "twitter": "https://twitter.com/JesseTetsuya",
            "linkedin": "https://www.linkedin.com/in/tetsuya-hirata/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/CheukTingHo.JPG",
            "name": "Cheuk Ting Ho",
            "pronoun": "She/Her",
            "country": "United Kingdom",
            "github": "https://github.com/Cheukting",
            "twitter": "https://twitter.com/cheukting_ho",
            "linkedin": "https://www.linkedin.com/in/cheukting-ho/",
            "link": "/pages/speakers#Cheuk-Ting-Ho",
        },
        {
            "img": "/theme/img/speakers/RosalindandSteve.jpg",
            "name": "Rosalind Yunibandhu & Steve Doucakis",
            "pronoun": "-",
            "country": "Thailand & USA",
            "twitter": "https://twitter.com/ryunibandhu",
            "linkedin": "https://www.linkedin.com/in/ryunibandhu/",
            "instagram": "https://instagram.com/arcadiafinefoods",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/StevenKolawole.jpg",
            "name": "Steven Kolawole",
            "pronoun": "He/Him",
            "country": "Nigeria",
            "github": "https://github.com/stevekola",
            "twitter": "https://twitter.com/steveddev",
            "linkedin": "https://www.linkedin.com/in/steven-kolawole-80/",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/lokinfey.jpg",
            "name": "Kinfey Lo",
            "pronoun": "He/Him",
            "country": "China",
            "github": "https://github.com/kinfey",
            "link": "",
        },
        {
            "img": "/theme/img/speakers/JintaoZhang.jpg",
            "name": "Jintao Zhang",
            "pronoun": "He/Him",
            "country": "China",
            "github": "https://github.com/tao12345666333",
            "twitter": "https://twitter.com/zhangjintao9020",
            "link": "/pages/speakers#Jintao-Zhang",
        },
        {
            "img": "/theme/img/speakers/bookee.jpg",
            "name": "Bookee Suksa",
            "pronoun": "She/Her",
            "country": "Thailand",
            "instagram": "https://instagram.com/Book_books",
            "link": "",
        },
        {
            "img": "theme/img/speakers/JoongiKim.jpg",
            "name": "Kim Joonki",
            "pronoun": "He/Him",
            "country": "South Korea",
            "github": "https://github.com/achimnol",
            "twitter": "https://twitter.com/achimnol",
            "linkedin": "https://www.linkedin.com/in/joongikim",
            "link": "/pages/speakers#Kim-Joonki",
        },
    ]
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
