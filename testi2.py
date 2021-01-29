# Rakenteellisia tietotyyppejä

# Lista (list)
osallistujat = ['Hakala', 'Viljanen', 'Karilainen']
print('Listan toinen jäsen on', osallistujat[1])
osallistujat.append('Vainio')
osallistujat[3] = 'Öllönquist'
print(osallistujat)
print('listassa on', len(osallistujat), 'henkilöä')

tiimin_vetaja = 'Mikko Karilainen'
print('Nimen pituus on', len(tiimin_vetaja))
print(tiimin_vetaja.upper())

# Monikko (tuple)
kouluttajat = 'Hakala', 'Viljanen', 'Vainio'
# kouluttajat[3] = 'Öllönquist' ei toimi, koska jäsentä ei voi 
# Tuplen luomisen jälkeen enää muuttaa
print(kouluttajat)

# Joukko (set)
tutkinnon_osat = {'Perustehtävät', 'Ohjelmistojkehittäjä', 'IT-tukihenkilö'}
# Tutkitaan löytyykö joukosta jäsen (alkio) Hyvinvointiteknologia-asentaja
print('Raseko järjestää', 'Hyvinvointiteknologia-asentaja' in tutkinnon_osat)

# Avain- arvo parit (dictionary aka key value pair)
mini_sanakirja = { 'virtahepo' : 'flodhäst', 'karhu' : 'björn', 'kettu': 'räv'}
print('karhu on ruotsiksi', mini_sanakirja['karhu'])