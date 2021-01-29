# Esimerkkejä muuttujista (variable)

etunimi = 'Mika' # Merkkijono (string)
sukunimi = "Hakala" # Toinen tapa tehdä merkkojono
kengan_koko = 44 # kaksiosainen nimi: snake case suositeltu tapa
kenganKoko = 42.5 # kaksiosainen nimi: dromedar case, ei suositella
KenganKoko = 52 # kaksiosainen nimi: camel case, ei suositella
opettaja = True

# Esimerkkejä rakenteista ja komennoista

# Ruudulle tulostaminen
print('Opettajana on tänään', etunimi, sukunimi) 

print(sukunimi, 'on isokenkäinen, kengän koko on',kengan_koko, '\n')

# Kysytään käyttäjältä tietoja (koko nimi)
koko_nimi = input('Kirjoita nimesi ')

# Tekstien yhdistäminen (katenointi, concatenation)
tervehdys = 'Morjensta ' + koko_nimi + ', tervetuloa Tampereelle'

print(tervehdys, '\n')

# Luetaan numeerista tietoa näppäimistöstä
markat = input('kuinka monta markkaa sait kakarana viikkorahaa? ')
eurot = float(markat) / 6 
print('se olisi nykyään', eurot, 'euroa')

# Funktiot pythonissa, esim funktio, joka muuttaa markat euroiksi
def euroa(markkaa):
    
    """Funktio palautta markkoina annetun arvon euroina

    Args:
        markkaa (float): rahamäärä markkoina

    Returns:
        float: rahan määrä euroina
    """

    return markkaa / 6

viikkoraha = euroa(100)

print('Se on nykyisin euroina', viikkoraha )

