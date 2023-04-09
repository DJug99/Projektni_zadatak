from datetime import date
# unos korisnikovih podataka
ime = input("Unesite ime korisnika: ").capitalize()
prezime = input("Unesite prezime korisnika: ").capitalize()
telefon = int(input("Unesite telefon korisnika: "))
email = input("Unesite email korisnika: ").strip()

# spremanje korisnikovih podataka u rječnik
korisnik = {
    "ime": ime,
    "prezime": prezime,
    "telefon": telefon,
    "email": email
}

# unos podataka o artiklu
naslov = input("Unesite naslov artikla: ")
opis = input("Unesite opis artikla: ")
cijena = float(input("Unesite cijenu artikla: "))

# spremanje podataka o artiklu u rječnik
artikl = {
    "naslov": naslov,
    "opis": opis,
    "cijena": cijena
}

# unos podataka o prodaji
dan = int(input("Unesite dan isteka prodaje: "))
mjesec = int(input("Unesite mjesec isteka prodaje: "))
godina = int(input("Unesite godinu isteka prodaje: "))

# spremanje podataka o prodaji u rječnik
prodaja = {
    "datum": date(godina, mjesec, dan),
    "artikl": artikl,
    "korisnik": korisnik
}

# ispis podataka o prodaji
print("Informacije o artiklu:")
print("Naslov:", prodaja["artikl"]["naslov"])
print("Opis:", prodaja["artikl"]["opis"])
print("Cijena:", prodaja["artikl"]["cijena"])
print("Datum isteka prodaje:")
print("Dan:", prodaja["datum"].day)
print("Mjesec:", prodaja["datum"].month)
print("Godina:", prodaja["datum"].year)
print("Informacije o korisniku:")
print(prodaja["korisnik"]["ime"], prodaja["korisnik"]["prezime"])
print("Telefon:", prodaja["korisnik"]["telefon"])
print("Email:", prodaja["korisnik"]["email"])




