from collections import defaultdict


def dictMaker():
    
    string = """Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
Sandshrew
Sandslash
Nidoran♀
Nidorina
Nidoqueen
Nidoran♂
Nidorino
Nidoking
Clefairy
Clefable
Vulpix
Ninetales
Jigglypuff
Wigglytuff
Zubat
Golbat
Oddish
Gloom
Vileplume
Paras
Parasect
Venonat
Venomoth
Diglett
Dugtrio
Meowth
Persian
Psyduck
Golduck
Mankey
Primeape
Growlithe
Arcanine
Poliwag
Poliwhirl
Poliwrath
Abra
Kadabra
Alakazam
Machop
Machoke
Machamp
Bellsprout
Weepinbell
Victreebel
Tentacool
Tentacruel
Geodude
Graveler
Golem
Ponyta
Rapidash
Slowpoke
Slowbro
Magnemite
Magneton
Farfetch’d
Doduo
Dodrio
Seel
Dewgong
Grimer
Muk
Shellder
Cloyster
Gastly
Haunter
Gengar
Onix
Drowzee
Hypno
Krabby
Kingler
Voltorb
Electrode
Exeggcute
Exeggutor
Cubone
Marowak
Hitmonlee
Hitmonchan
Lickitung
Koffing
Weezing
Rhyhorn
Rhydon
Chansey
Tangela
Kangaskhan
Horsea
Seadra
Goldeen
Seaking
Staryu
Starmie
Mr. Mime
Scyther
Jynx
Electabuzz
Magmar
Pinsir
Tauros
Magikarp
Gyarados
Lapras
Ditto
Eevee
Vaporeon
Jolteon
Flareon
Porygon
Omanyte
Omastar
Kabuto
Kabutops
Aerodactyl
Snorlax
Articuno
Zapdos
Moltres
Dratini
Dragonair
Dragonite
Mewtwo
Mew
Chikorita
Bayleef
Meganium
Cyndaquil
Quilava
Typhlosion
Totodile
Croconaw
Feraligatr
Sentret
Furret
Hoothoot
Noctowl
Ledyba
Ledian
Spinarak
Ariados
Crobat
Chinchou
Lanturn
Pichu
Cleffa
Igglybuff
Togepi
Togetic
Natu
Xatu
Mareep
Flaaffy
Ampharos
Bellossom
Marill
Azumarill
Sudowoodo
Politoed
Hoppip
Skiploom
Jumpluff
Aipom
Sunkern
Sunflora
Yanma
Wooper
Quagsire
Espeon
Umbreon
Murkrow
Slowking
Misdreavus
Unown
Wobbuffet
Girafarig
Pineco
Forretress
Dunsparce
Gligar
Steelix
Snubbull
Granbull
Qwilfish
Scizor
Shuckle
Heracross
Sneasel
Teddiursa
Ursaring
Slugma
Magcargo
Swinub
Piloswine
Corsola
Remoraid
Octillery
Delibird
Mantine
Skarmory
Houndour
Houndoom
Kingdra
Phanpy
Donphan
Porygon2
Stantler
Smeargle
Tyrogue
Hitmontop
Smoochum
Elekid
Magby
Miltank
Blissey
Raikou
Entei
Suicune
Larvitar
Pupitar
Tyranitar
Lugia
Ho-Oh
Celebi
Treecko
Grovyle
Sceptile
Torchic
Combusken
Blaziken
Mudkip
Marshtomp
Swampert
Poochyena
Mightyena
Zigzagoon
Linoone
Wurmple
Silcoon
Beautifly
Cascoon
Dustox
Lotad
Lombre
Ludicolo
Seedot
Nuzleaf
Shiftry
Taillow
Swellow
Wingull
Pelipper
Ralts
Kirlia
Gardevoir
Surskit
Masquerain
Shroomish
Breloom
Slakoth
Vigoroth
Slaking
Nincada
Ninjask
Shedinja
Whismur
Loudred
Exploud
Makuhita
Hariyama
Azurill
Nosepass
Skitty
Delcatty
Sableye
Mawile
Aron
Lairon
Aggron
Meditite
Medicham
Electrike
Manectric
Plusle
Minun
Volbeat
Illumise
Roselia
Gulpin
Swalot
Carvanha
Sharpedo
Wailmer
Wailord
Numel
Camerupt
Torkoal
Spoink
Grumpig
Spinda
Trapinch
Vibrava
Flygon
Cacnea
Cacturne
Swablu
Altaria
Zangoose
Seviper
Lunatone
Solrock
Barboach
Whiscash
Corphish
Crawdaunt
Baltoy
Claydol
Lileep
Cradily
Anorith
Armaldo
Feebas
Milotic
Castform
Kecleon
Shuppet
Banette
Duskull
Dusclops
Tropius
Chimecho
Absol
Wynaut
Snorunt
Glalie
Spheal
Sealeo
Walrein
Clamperl
Huntail
Gorebyss
Relicanth
Luvdisc
Bagon
Shelgon
Salamence
Beldum
Metang
Metagross
Regirock
Regice
Registeel
Latias
Latios
Kyogre
Groudon
Rayquaza
Jirachi
Deoxys
Turtwig
Grotle
Torterra
Chimchar
Monferno
Infernape
Piplup
Prinplup
Empoleon
Starly
Staravia
Staraptor
Bidoof
Bibarel
Kricketot
Kricketune
Shinx
Luxio
Luxray
Budew
Roserade
Cranidos
Rampardos
Shieldon
Bastiodon
Burmy
Wormadam
Mothim
Combee
Vespiquen
Pachirisu
Buizel
Floatzel
Cherubi
Cherrim
Shellos
Gastrodon
Ambipom
Drifloon
Drifblim
Buneary
Lopunny
Mismagius
Honchkrow
Glameow
Purugly
Chingling
Stunky
Skuntank
Bronzor
Bronzong
Bonsly
Mime Jr.
Happiny
Chatot
Spiritomb
Gible
Gabite
Garchomp
Munchlax
Riolu
Lucario
Hippopotas
Hippowdon
Skorupi
Drapion
Croagunk
Toxicroak
Carnivine
Finneon
Lumineon
Mantyke
Snover
Abomasnow
Weavile
Magnezone
Lickilicky
Rhyperior
Tangrowth
Electivire
Magmortar
Togekiss
Yanmega
Leafeon
Glaceon
Gliscor
Mamoswine
Porygon-Z
Gallade
Probopass
Dusknoir
Froslass
Rotom
Uxie
Mesprit
Azelf
Dialga
Palkia
Heatran
Regigigas
Giratina
Cresselia
Phione
Manaphy
Darkrai
Shaymin
Arceus
Victini
Snivy
Servine
Serperior
Tepig
Pignite
Emboar
Oshawott
Dewott
Samurott
Patrat
Watchog
Lillipup
Herdier
Stoutland
Purrloin
Liepard
Pansage
Simisage
Pansear
Simisear
Panpour
Simipour
Munna
Musharna
Pidove
Tranquill
Unfezant
Blitzle
Zebstrika
Roggenrola
Boldore
Gigalith
Woobat
Swoobat
Drilbur
Excadrill
Audino
Timburr
Gurdurr
Conkeldurr
Tympole
Palpitoad
Seismitoad
Throh
Sawk
Sewaddle
Swadloon
Leavanny
Venipede
Whirlipede
Scolipede
Cottonee
Whimsicott
Petilil
Lilligant
Basculin
Sandile
Krokorok
Krookodile
Darumaka
Darmanitan
Maractus
Dwebble
Crustle
Scraggy
Scrafty
Sigilyph
Yamask
Cofagrigus
Tirtouga
Carracosta
Archen
Archeops
Trubbish
Garbodor
Zorua
Zoroark
Minccino
Cinccino
Gothita
Gothorita
Gothitelle
Solosis
Duosion
Reuniclus
Ducklett
Swanna
Vanillite
Vanillish
Vanilluxe
Deerling
Sawsbuck
Emolga
Karrablast
Escavalier
Foongus
Amoonguss
Frillish
Jellicent
Alomomola
Joltik
Galvantula
Ferroseed
Ferrothorn
Klink
Klang
Klinklang
Tynamo
Eelektrik
Eelektross
Elgyem
Beheeyem
Litwick
Lampent
Chandelure
Axew
Fraxure
Haxorus
Cubchoo
Beartic
Cryogonal
Shelmet
Accelgor
Stunfisk
Mienfoo
Mienshao
Druddigon
Golett
Golurk
Pawniard
Bisharp
Bouffalant
Rufflet
Braviary
Vullaby
Mandibuzz
Heatmor
Durant
Deino
Zweilous
Hydreigon
Larvesta
Volcarona
Cobalion
Terrakion
Virizion
Tornadus
Thundurus
Reshiram
Zekrom
Landorus
Kyurem
Keldeo
Meloetta
Genesect
Chespin
Quilladin
Chesnaught
Fennekin
Braixen
Delphox
Froakie
Frogadier
Greninja
Bunnelby
Diggersby
Fletchling
Fletchinder
Talonflame
Scatterbug
Spewpa
Vivillon
Litleo
Pyroar
Flabébé
Floette
Florges
Skiddo
Gogoat
Pancham
Pangoro
Furfrou
Espurr
Meowstic
Honedge
Doublade
Aegislash
Spritzee
Aromatisse
Swirlix
Slurpuff
Inkay
Malamar
Binacle
Barbaracle
Skrelp
Dragalge
Clauncher
Clawitzer
Helioptile
Heliolisk
Tyrunt
Tyrantrum
Amaura
Aurorus
Sylveon
Hawlucha
Dedenne
Carbink
Goomy
Sliggoo
Goodra
Klefki
Phantump
Trevenant
Pumpkaboo
Gourgeist
Bergmite
Avalugg
Noibat
Noivern
Xerneas
Yveltal
Zygarde
Diancie
Hoopa
Volcanion
Rowlet
Dartrix
Decidueye
Litten
Torracat
Incineroar
Popplio
Brionne
Primarina
Pikipek
Trumbeak
Toucannon
Yungoos
Gumshoos
Grubbin
Charjabug
Vikavolt
Crabrawler
Crabominable
Oricorio
Cutiefly
Ribombee
Rockruff
Lycanroc
Wishiwashi
Mareanie
Toxapex
Mudbray
Mudsdale
Dewpider
Araquanid
Fomantis
Lurantis
Morelull
Shiinotic
Salandit
Salazzle
Stufful
Bewear
Bounsweet
Steenee
Tsareena
Comfey
Oranguru
Passimian
Wimpod
Golisopod
Sandygast
Palossand
Pyukumuku
Type: Null
Silvally
Minior
Komala
Turtonator
Togedemaru
Mimikyu
Bruxish
Drampa
Dhelmise
Jangmo-o
Hakamo-o
Kommo-o
Tapu Koko
Tapu Lele
Tapu Bulu
Tapu Fini
Cosmog
Cosmoem
Solgaleo
Lunala
Nihilego
Buzzwole
Pheromosa
Xurkitree
Celesteela
Kartana
Guzzlord
Necrozma
Magearna
Marshadow
Poipole
Naganadel
Stakataka
Blacephalon
Zeraora
Meltan
Melmetal
Alolan Raichu"""
    
    
    pokeDex = defaultdict(list)
    string = string.split("\n")
    string = string[:-1]
    
    for i in string:
        i = i.strip()
        pokeDex[len(i)].append(i)
    return pokeDex



def guesser(name):
    name = list(name)
    underscores = []
    
    for i in range(len(name)):
        if name[i] == "_":
            underscores.append(i)
    
    pokeDex = dictMaker()
    
    for i in pokeDex[len(name)]:
        a = list(i)
        for underscore in underscores:
            a[underscore] = "_"
        if name == a:
            return i
        
        
def guesserList(name):
    name = list(name)
    underscores = []
    results = []
    
    for i in range(len(name)):
        if name[i] == "_":
            underscores.append(i)
    
    pokeDex = dictMaker()
    
    for i in pokeDex[len(name)]:
        a = list(i)
        for underscore in underscores:
            a[underscore] = "_"
        if name == a:
            results.append( i )
    return results


#__________________________________________________________________________________________________________________________________
#___________IMAGE IDENTIFIER USING COLOR AVERAGES__________________________________________________________________________________
#__________________________________________________________________________________________________________________________________


from io import BytesIO

import requests, time, json
from PIL import Image
from PIL.ImageStat import Stat

data = {}

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint

def byColor(url):
    allPokemon = {8229509: 'Bulbasaur', 7372414: 'Ivysaur', 8948874: 'Venusaur', 9732213: 'Charmander', 9664626: 'Charmeleon', 9340798: 'Charizard', 7108730: 'Squirtle', 8094087: 'Wartortle', 8486785: 'Blastoise', 7436382: 'Caterpie', 7502948: 'Metapod', 9408403: 'Butterfree', 8813686: 'Weedle', 12893865: 'Kakuna', 8618365: 'Beedrill', 7695713: 'Pidgey', 8353903: 'Pidgeotto', 7300700: 'Pidgeot', 7827573: 'Rattata', 7497561: 'Raticate', 7232857: 'Spearow', 6971223: 'Fearow', 8087665: 'Ekans', 8287868: 'Arbok', 8484703: 'Pikachu', 7235677: 'Raichu', 9472374: 'Sandshrew', 7300695: 'Sandslash', 8752279: 'Nidoran♀', 7897991: 'Nidorina', 7305342: 'Nidoqueen', 8419205: 'Nidoran♂', 8418946: 'Nidorino', 9603731: 'Nidoking', 11574174: 'Clefairy', 10391950: 'Clefable', 9861998: 'Vulpix', 10591106: 'Ninetales', 9668748: 'Jigglypuff', 10459805: 'Wigglytuff', 5525850: 'Zubat', 6907503: 'Golbat', 6518377: 'Oddish', 8946049: 'Gloom', 9205373: 'Vileplume', 9798522: 'Paras', 8941673: 'Parasect', 7959424: 'Venonat', 10986922: 'Venomoth', 9142652: 'Diglett', 8287344: 'Dugtrio', 9209986: 'Meowth', 8091503: 'Persian', 11840152: 'Psyduck', 5397604: 'Golduck', 9802127: 'Mankey', 7827307: 'Primeape', 11774625: 'Growlithe', 9800062: 'Arcanine', 8949397: 'Poliwag', 8028297: 'Poliwhirl', 9804449: 'Poliwrath', 10328196: 'Abra', 8946542: 'Kadabra', 8222823: 'Alakazam', 8686478: 'Machop', 9276821: 'Machoke', 7435641: 'Machamp', 7501416: 'Bellsprout', 9738632: 'Weepinbell', 8753017: 'Victreebel', 7567227: 'Tentacool', 8422279: 'Tentacruel', 13092807: 'Geodude', 12040374: 'Graveler', 7697009: 'Golem', 11441546: 'Ponyta', 11178628: 'Rapidash', 10982810: 'Slowpoke', 10194834: 'Slowbro', 11514290: 'Magnemite', 7632504: 'Magneton', 8881020: 'Farfetch’d', 9868176: 'Doduo', 7367529: 'Dodrio', 9079951: 'Seel', 9146001: 'Dewgong', 10130845: 'Grimer', 11908023: 'Muk', 7630973: 'Shellder', 6907759: 'Cloyster', 10325146: 'Gastly', 6710121: 'Haunter', 6973044: 'Gengar', 6645097: 'Onix', 10985094: 'Drowzee', 8945762: 'Hypno', 11511200: 'Krabby', 10984857: 'Kingler', 11244437: 'Voltorb', 11117481: 'Electrode', 11708841: 'Exeggcute', 6252124: 'Exeggutor', 10197139: 'Cubone', 9144196: 'Marowak', 7433580: 'Hitmonlee', 8815234: 'Hitmonchan', 11442330: 'Lickitung', 10921378: 'Koffing', 8420480: 'Weezing', 8027778: 'Rhyhorn', 8553093: 'Rhydon', 11640999: 'Chansey', 8028554: 'Tangela', 8682358: 'Kangaskhan', 7768204: 'Horsea', 7372418: 'Seadra', 12302264: 'Goldeen', 9537928: 'Seaking', 7827040: 'Staryu', 8157307: 'Starmie', 7433072: 'Mr. Mime', 7107179: 'Scyther', 9996164: 'Jynx', 6249297: 'Electabuzz', 7298640: 'Magmar', 6578529: 'Pinsir', 6643289: 'Tauros', 8614250: 'Magikarp', 7370361: 'Gyarados', 5924717: 'Lapras', 10853805: 'Ditto', 9208182: 'Eevee', 7175552: 'Vaporeon', 8946029: 'Jolteon', 9403756: 'Flareon', 7566198: 'Porygon', 10133915: 'Omanyte', 8357508: 'Omastar', 11181717: 'Kabuto', 7235683: 'Kabutops', 9802646: 'Aerodactyl', 10396579: 'Snorlax', 6517371: 'Articuno', 9670275: 'Zapdos', 13549753: 'Moltres', 6447975: 'Dratini', 6712177: 'Dragonair', 9735809: 'Dragonite', 8354687: 'Mewtwo', 11511464: 'Mew', 9212805: 'Chikorita', 11184542: 'Bayleef', 12170413: 'Meganium', 11639950: 'Cyndaquil', 12957094: 'Quilava', 12299416: 'Typhlosion', 10068899: 'Totodile', 7238512: 'Croconaw', 7503488: 'Feraligatr', 12499639: 'Sentret', 9537408: 'Furret', 6906204: 'Hoothoot', 11117728: 'Noctowl', 9603712: 'Ledyba', 10459028: 'Ledian', 11054239: 'Spinarak', 7365730: 'Ariados', 9606038: 'Crobat', 8092797: 'Chinchou', 10790570: 'Lanturn', 8158062: 'Pichu', 10588813: 'Cleffa', 11642791: 'Igglybuff', 11249820: 'Togepi', 11448492: 'Togetic', 7105361: 'Natu', 10262929: 'Xatu', 11118235: 'Mareep', 9801360: 'Flaaffy', 9736066: 'Ampharos', 8814187: 'Bellossom', 8426911: 'Marill', 6188662: 'Azumarill', 7038816: 'Sudowoodo', 10265484: 'Politoed', 8419187: 'Hoppip', 10069890: 'Skiploom', 13158085: 'Jumpluff', 8156790: 'Aipom', 9605754: 'Sunkern', 8028008: 'Sunflora', 10986141: 'Yanma', 7766149: 'Wooper', 8951452: 'Quagsire', 6643297: 'Espeon', 6645092: 'Umbreon', 5659230: 'Murkrow', 12366256: 'Slowking', 6910585: 'Misdreavus', 6909552: 'Unown', 10202550: 'Wobbuffet', 10195848: 'Girafarig', 7042680: 'Pineco', 10589075: 'Forretress', 8553588: 'Dunsparce', 8153208: 'Gligar', 7040369: 'Steelix', 9864069: 'Snubbull', 9997972: 'Granbull', 6844774: 'Qwilfish', 8219755: 'Scizor', 7892574: 'Shuckle', 4673623: 'Heracross', 5198678: 'Sneasel', 11903892: 'Teddiursa', 10721424: 'Ursaring', 10517876: 'Slugma', 10649981: 'Magcargo', 11642271: 'Swinub', 9667193: 'Piloswine', 8940912: 'Corsola', 8685957: 'Remoraid', 9728105: 'Octillery', 10720402: 'Delibird', 11119019: 'Mantine', 9473167: 'Skarmory', 8288889: 'Houndour', 5459791: 'Houndoom', 6253421: 'Kingdra', 8295829: 'Phanpy', 11251377: 'Donphan', 7432819: 'Porygon2', 8683128: 'Stantler', 8552312: 'Smeargle', 6775137: 'Tyrogue', 6447456: 'Hitmontop', 12432811: 'Smoochum', 10197388: 'Elekid', 10456714: 'Magby', 9471618: 'Miltank', 11311518: 'Blissey', 9209723: 'Raikou', 7629410: 'Entei', 7172726: 'Suicune', 11053730: 'Larvitar', 9541279: 'Pupitar', 7633006: 'Tyranitar', 8948365: 'Lugia', 7496537: 'Ho-Oh', 8949381: 'Celebi', 6975065: 'Treecko', 6975335: 'Grovyle', 6187358: 'Sceptile', 11839636: 'Torchic', 6971734: 'Combusken', 9800064: 'Blaziken', 6779767: 'Mudkip', 7963009: 'Marshtomp', 9146773: 'Swampert', 7763574: 'Poochyena', 5395026: 'Mightyena', 11315622: 'Zigzagoon', 13026499: 'Linoone', 10128007: 'Wurmple', 8026748: 'Silcoon', 6644059: 'Beautifly', 8683908: 'Cascoon', 10855830: 'Dustox', 8164486: 'Lotad', 8095603: 'Lombre', 10132617: 'Ludicolo', 10394262: 'Seedot', 7696491: 'Nuzleaf', 7500653: 'Shiftry', 8683653: 'Noivern', 7762551: 'Swellow', 8750726: 'Wingull', 9276802: 'Pelipper', 11646383: 'Ralts', 11317161: 'Kirlia', 6514274: 'Gardevoir', 6514536: 'Surskit', 9341320: 'Masquerain', 10591896: 'Shroomish', 8421240: 'Breloom', 12565432: 'Slakoth', 11118504: 'Vigoroth', 11644071: 'Slaking', 12040375: 'Nincada', 10196886: 'Ninjask', 8880247: 'Shedinja', 10326156: 'Whismur', 7959418: 'Loudred', 8025468: 'Exploud', 11182992: 'Makuhita', 9667701: 'Hariyama', 7046550: 'Azurill', 7434113: 'Nosepass', 9734276: 'Skitty', 9669002: 'Delcatty', 5854305: 'Sableye', 8815486: 'Mawile', 9145999: 'Aron', 10066330: 'Lairon', 7171439: 'Aggron', 8160392: 'Meditite', 11642278: 'Medicham', 11186595: 'Electrike', 9606801: 'Manectric', 11246743: 'Plusle', 8949389: 'Minun', 12892856: 'Volbeat', 9869211: 'Illumise', 6581095: 'Roselia', 9082501: 'Gulpin', 8287883: 'Swalot', 8814972: 'Carvanha', 7041399: 'Sharpedo', 11712958: 'Wailmer', 11449527: 'Wailord', 10130040: 'Numel', 10851213: 'Camerupt', 9997442: 'Torkoal', 11249833: 'Spoink', 6972520: 'Grumpig', 9931142: 'Spinda', 11374466: 'Trapinch', 8357502: 'Vibrava', 8882304: 'Flygon', 9804944: 'Cacnea', 6450015: 'Cacturne', 13226971: 'Swablu', 9477542: 'Altaria', 8551550: 'Zangoose', 7237231: 'Seviper', 10064770: 'Lunatone', 6510666: 'Solrock', 11054512: 'Barboach', 8159624: 'Whiscash', 9598829: 'Corphish', 8284517: 'Crawdaunt', 6906457: 'Baltoy', 7695467: 'Claydol', 9274245: 'Lileep', 9014145: 'Cradily', 6512735: 'Anorith', 7632505: 'Armaldo', 9934482: 'Feebas', 8155759: 'Milotic', 12171707: 'Castform', 9342328: 'Kecleon', 7764099: 'Shuppet', 6710371: 'Banette', 9276810: 'Duskull', 7829109: 'Dusclops', 7042918: 'Tropius', 12171192: 'Chimecho', 10395554: 'Absol', 7964295: 'Wynaut', 9998469: 'Snorunt', 8422022: 'Glalie', 10922671: 'Spheal', 9476765: 'Sealeo', 7110536: 'Walrein', 7896968: 'Clamperl', 8882054: 'Gothitelle', 8880002: 'Gorebyss', 10262420: 'Relicanth', 13745085: 'Luvdisc', 10726060: 'Bagon', 10921382: 'Shelgon', 8947083: 'Salamence', 11647680: 'Beldum', 8226958: 'Metang', 9607838: 'Metagross', 8681589: 'Regirock', 7900051: 'Regice', 9342350: 'Registeel', 7367275: 'Latias', 8883345: 'Latios', 11515844: 'Kyogre', 11244175: 'Groudon', 5660504: 'Rayquaza', 10658712: 'Jirachi', 7169378: 'Deoxys', 10001803: 'Turtwig', 7107930: 'Grotle', 7502443: 'Torterra', 12102557: 'Chimchar', 9272946: 'Monferno', 9864055: 'Infernape', 10530483: 'Piplup', 6449513: 'Prinplup', 7303794: 'Empoleon', 8420217: 'Starly', 9473676: 'Staravia', 7894129: 'Staraptor', 9470063: 'Bidoof', 9273713: 'Bibarel', 12497322: 'Kricketot', 10062984: 'Kricketune', 6647405: 'Shinx', 6383203: 'Luxio', 5724760: 'Luxray', 11648418: 'Budew', 9936027: 'Roserade', 7699842: 'Cranidos', 8027776: 'Rampardos', 8025452: 'Shieldon', 8355194: 'Bastiodon', 10792351: 'Burmy', 7108203: 'Wormadam', 11709344: 'Mothim', 11775135: 'Combee', 8682090: 'Vespiquen', 9410972: 'Pachirisu', 11181973: 'Buizel', 9471864: 'Floatzel', 8943728: 'Cherubi', 8552578: 'Cherrim', 10720406: 'Shellos', 9798783: 'Gastrodon', 8353911: 'Ambipom', 10131608: 'Drifloon', 6840929: 'Drifblim', 12301742: 'Buneary', 9472122: 'Lopunny', 9735574: 'Mismagius', 8750986: 'Honchkrow', 6514023: 'Glameow', 8618373: 'Purugly', 8484710: 'Chingling', 7367534: 'Stunky', 9604495: 'Skuntank', 7900562: 'Bronzor', 10397349: 'Bronzong', 10330005: 'Bonsly', 9736339: 'Mime Jr.', 12103343: 'Happiny', 6580326: 'Chatot', 11968414: 'Spiritomb', 6976375: 'Gible', 5723484: 'Gabite', 5920860: 'Garchomp', 9278872: 'Munchlax', 5725791: 'Riolu', 9080206: 'Lucario', 10656392: 'Hippopotas', 10722707: 'Hippowdon', 7172216: 'Skorupi', 10722981: 'Drapion', 8290953: 'Croagunk', 6250853: 'Toxicroak', 7961967: 'Carnivine', 7961727: 'Finneon', 6844784: 'Lumineon', 8490647: 'Mantyke', 9672340: 'Snover', 8752010: 'Abomasnow', 6641243: 'Weavile', 9145742: 'Magnezone', 9073010: 'Lickilicky', 10326927: 'Rhyperior', 7436157: 'Tangrowth', 9012601: 'Electivire', 8743512: 'Magmortar', 11711925: 'Togekiss', 9341059: 'Yanmega', 8422775: 'Leafeon', 6910834: 'Glaceon', 7039855: 'Gliscor', 10459022: 'Mamoswine', 7763834: 'Porygon-Z', 7172461: 'Gallade', 7958643: 'Probopass', 8947586: 'Dusknoir', 13093063: 'Froslass', 9351882: 'Rotom', 8553083: 'Uxie', 9868183: 'Mesprit', 9278615: 'Azelf', 6251369: 'Dialga', 8289152: 'Palkia', 10657177: 'Heatran', 10526872: 'Regigigas', 7300191: 'Giratina', 10191745: 'Cresselia', 8556948: 'Phione', 9805986: 'Manaphy', 5723476: 'Darkrai', 9870217: 'Shaymin', 8487294: 'Arceus', 8814453: 'Victini', 8029040: 'Snivy', 6580830: 'Servine', 7438195: 'Serperior', 8614504: 'Tepig', 8876900: 'Pignite', 8349529: 'Emboar', 10397093: 'Oshawott', 9673372: 'Dewott', 6514794: 'Samurott', 8616044: 'Patrat', 12761779: 'Watchog', 11246734: 'Lillipup', 7498600: 'Herdier', 10131346: 'Stoutland', 8749188: 'Purrloin', 7235687: 'Liepard', 8622976: 'Pansage', 7833721: 'Simisage', 10585723: 'Pansear', 9072485: 'Simisear', 8293253: 'Panpour', 7308417: 'Simipour', 12033701: 'Munna', 11572131: 'Musharna', 7039079: 'Pidove', 6513249: 'Tranquill', 8158074: 'Unfezant', 10461085: 'Blitzle', 7566194: 'Zebstrika', 10066072: 'Roggenrola', 7235949: 'Boldore', 6444889: 'Gigalith', 9935258: 'Woobat', 6185314: 'Swoobat', 7170922: 'Drilbur', 8618111: 'Excadrill', 11312278: 'Audino', 9143165: 'Timburr', 7563111: 'Gurdurr', 9538697: 'Conkeldurr', 8948358: 'Tympole', 9213074: 'Palpitoad', 7044998: 'Seismitoad', 8485752: 'Throh', 7766404: 'Sawk', 10198142: 'Sewaddle', 8490095: 'Swadloon', 11383204: 'Leavanny', 9665920: 'Venipede', 9078666: 'Whirlipede', 5984338: 'Scolipede', 11975861: 'Cottonee', 11381916: 'Whimsicott', 11713195: 'Petilil', 10199693: 'Lilligant', 7239277: 'Basculin', 10130316: 'Sandile', 6972510: 'Krokorok', 7563885: 'Krookodile', 9400681: 'Darumaka', 8810603: 'Darmanitan', 8620415: 'Maractus', 8943985: 'Dwebble', 9077115: 'Crustle', 10458759: 'Scraggy', 11115665: 'Scrafty', 7762542: 'Sigilyph', 7565420: 'Yamask', 10593951: 'Cofagrigus', 10791342: 'Tirtouga', 8358292: 'Carracosta', 10328213: 'Archen', 8751754: 'Archeops', 6514787: 'Trubbish', 8618877: 'Garbodor', 8419966: 'Zorua', 6050131: 'Zoroark', 10065556: 'Minccino', 10329248: 'Cinccino', 10855078: 'Gothita', 9342606: 'Gothorita', 11323313: 'Solosis', 10929327: 'Duosion', 13031631: 'Reuniclus', 9674652: 'Ducklett', 8619652: 'Swanna', 10725548: 'Vanillite', 12109008: 'Vanillish', 10464700: 'Vanilluxe', 11248798: 'Deerling', 6182992: 'Sawsbuck', 10526358: 'Emolga', 10462111: 'Karrablast', 8747641: 'Escavalier', 10327954: 'Foongus', 8945791: 'Amoonguss', 6658474: 'Frillish', 10336973: 'Jellicent', 12563124: 'Alomomola', 10788228: 'Joltik', 9933189: 'Galvantula', 8291455: 'Ferroseed', 8554115: 'Ferrothorn', 8093055: 'Klink', 9212049: 'Klang', 10856360: 'Klinklang', 12108488: 'Tynamo', 8946817: 'Eelektrik', 11579824: 'Eelektross', 10793646: 'Elgyem', 10722456: 'Beheeyem', 12501198: 'Litwick', 7500917: 'Lampent', 6776940: 'Chandelure', 8553854: 'Axew', 6316636: 'Fraxure', 8223342: 'Haxorus', 11385538: 'Cubchoo', 8752011: 'Beartic', 7503503: 'Cryogonal', 9603463: 'Shelmet', 7038826: 'Accelgor', 11577245: 'Stunfisk', 8549481: 'Mienfoo', 6118492: 'Mienshao', 6516595: 'Druddigon', 6780273: 'Golett', 7306360: 'Golurk', 8157303: 'Pawniard', 11446696: 'Bisharp', 8222833: 'Bouffalant', 12368567: 'Rufflet', 6577501: 'Braviary', 6644318: 'Vullaby', 10854558: 'Mandibuzz', 10061438: 'Heatmor', 10921638: 'Durant', 8421505: 'Deino', 5526356: 'Zweilous', 5262672: 'Hydreigon', 8090480: 'Larvesta', 9337974: 'Volcarona', 9542555: 'Cobalion', 8420472: 'Terrakion', 9146501: 'Virizion', 10263452: 'Tornadus', 9080207: 'Thundurus', 8422280: 'Reshiram', 7303537: 'Zekrom', 9735049: 'Landorus', 7764347: 'Kyurem', 7367784: 'Keldeo', 11119269: 'Meloetta', 8221565: 'Genesect', 10328203: 'Chespin', 6578256: 'Quilladin', 8947583: 'Chesnaught', 11839124: 'Fennekin', 10656399: 'Braixen', 9271408: 'Delphox', 8228493: 'Froakie', 7831428: 'Frogadier', 9934232: 'Greninja', 10262677: 'Bunnelby', 9209471: 'Diggersby', 8221809: 'Fletchling', 6839640: 'Fletchinder', 8485494: 'Talonflame', 10657951: 'Scatterbug', 10394523: 'Spewpa', 8678516: 'Vivillon', 7957602: 'Litleo', 8283733: 'Pyroar', 8614761: 'Flabébé', 8485495: 'Floette', 8160128: 'Florges', 5989469: 'Skiddo', 7633776: 'Gogoat', 11184549: 'Pancham', 7960954: 'Pangoro', 11448235: 'Furfrou', 10000285: 'Espurr', 7568009: 'Meowstic', 10001309: 'Honedge', 10325651: 'Doublade', 8486265: 'Aegislash', 10060423: 'Spritzee', 11704996: 'Aromatisse', 12828609: 'Swirlix', 11049118: 'Slurpuff', 9276045: 'Inkay', 8091518: 'Malamar', 8485749: 'Binacle', 7104614: 'Barbaracle', 8748411: 'Skrelp', 6511707: 'Dragalge', 9673886: 'Clauncher', 10462633: 'Clawitzer', 9670530: 'Helioptile', 8157296: 'Heliolisk', 9867147: 'Tyrunt', 8615540: 'Tyrantrum', 10593696: 'Amaura', 10066839: 'Aurorus', 10722720: 'Sylveon', 9605516: 'Hawlucha', 9799534: 'Dedenne', 9672093: 'Carbink', 8354174: 'Goomy', 11117993: 'Sliggoo', 8683651: 'Goodra', 8947333: 'Klefki', 5920596: 'Phantump', 6579551: 'Trevenant', 7892324: 'Pumpkaboo', 8483947: 'Gourgeist', 11253703: 'Bergmite', 12109787: 'Avalugg', 7695734: 'Noibat', 8158073: 'Xerneas', 6575702: 'Yveltal', 5921358: 'Zygarde', 12626872: 'Diancie', 5590346: 'Hoopa', 8020833: 'Volcanion', 12828858: 'Rowlet', 11052959: 'Dartrix', 9934477: 'Decidueye', 10196628: 'Litten', 9733760: 'Torracat', 11839911: 'Incineroar', 9476003: 'Popplio', 11582400: 'Brionne', 8752788: 'Primarina', 9539213: 'Pikipek', 10000021: 'Trumbeak', 9472903: 'Toucannon', 12630709: 'Yungoos', 9670277: 'Gumshoos', 13880517: 'Grubbin', 11778992: 'Charjabug', 9277588: 'Vikavolt', 8490386: 'Crabrawler', 10527653: 'Crabominable', 9207166: 'Oricorio', 12368048: 'Cutiefly', 12499635: 'Ribombee', 11183523: 'Rockruff', 11644845: 'Lycanroc', 13422545: 'Wishiwashi', 10266540: 'Mareanie', 8487818: 'Toxapex', 10525336: 'Mudbray', 8813176: 'Mudsdale', 11976634: 'Dewpider', 10596532: 'Araquanid', 12042170: 'Fomantis', 12366001: 'Lurantis', 14079189: 'Morelull', 9999504: 'Shiinotic', 8355196: 'Salandit', 8881285: 'Salazzle', 10260881: 'Stufful', 8880514: 'Bewear', 10261646: 'Bounsweet', 10067090: 'Steenee', 10197903: 'Tsareena', 13285030: 'Comfey', 10329245: 'Oranguru', 8026999: 'Passimian', 10921126: 'Wimpod', 8356223: 'Golisopod', 11578277: 'Sandygast', 13086622: 'Palossand', 11116706: 'Pyukumuku', 9539727: 'Type: Null', 11053482: 'Silvally', 11183010: 'Minior', 10658980: 'Komala', 9667449: 'Turtonator', 12303030: 'Togedemaru', 10131603: 'Mimikyu', 11578028: 'Bruxish', 11449006: 'Drampa', 9343632: 'Dhelmise', 9276550: 'Jangmo-o', 9868171: 'Hakamo-o', 9209983: 'Kommo-o', 10262153: 'Tapu Koko', 12233646: 'Tapu Lele', 8287601: 'Tapu Bulu', 9737115: 'Tapu Fini', 9018294: 'Cosmog', 10986651: 'Cosmoem', 10197655: 'Solgaleo', 7894651: 'Lunala', 14279145: 'Nihilego', 9271670: 'Buzzwole', 13881034: 'Pheromosa', 8291458: 'Xurkitree', 7243907: 'Celesteela', 6512731: 'Kartana', 8488067: 'Guzzlord', 11513002: 'Necrozma', 11381673: 'Magearna', 8947850: 'Marshadow', 10064286: 'Poipole', 9341588: 'Naganadel', 3487284: 'Stakataka', 7434096: 'Blacephalon', 2762518: 'Zeraora', 2762269: 'Meltan', 309201: 'Melmetal'}


    
    image_url = url
    
    resp = requests.get(image_url)
    img = Image.open(BytesIO(resp.content)).convert('RGB')
    val = getIfromRGB([round(x) for x in Stat(img).mean])
    
    return allPokemon[val]
