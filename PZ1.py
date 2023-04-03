import datetime

# Inicijaliziramo prazne rječnike za korisnika, artikl i prodaju
korisnik = {}
artikl = {}
prodaja = {}

# Korisnik unosi podatke o sebi
ime = input("Unesite ime: ").title()
prezime = input("Unesite prezime: ").title()
telefon = int(input("Unesite telefon: "))
email = input("Unesite email: ").strip()

# Spremamo podatke o korisniku u rječnik
korisnik["ime"] = ime
korisnik["prezime"] = prezime
korisnik["telefon"] = telefon
korisnik["email"] = email

# Korisnik unosi podatke o artiklu
naslov = input("Unesite naslov artikla: ")
opis = input("Unesite opis artikla: ")
cijena = float(input("Unesite cijenu artikla: "))

# Spremamo podatke o artiklu u rječnik
artikl["naslov"] = naslov
artikl["opis"] = opis
artikl["cijena"] = cijena

# Inicijaliziramo datum prodaje kao današnji datum
datum = datetime.date.today()

# Spremamo podatke o prodaji u rječnik
prodaja["datum"] = datum
prodaja["artikl"] = artikl
prodaja["korisnik"] = korisnik

# Ispisujemo sve informacije o prodaji
print("Prodaja:")
print("Datum: ", prodaja["datum"])
print("Korisnik: ", prodaja["korisnik"]["ime"], prodaja["korisnik"]["prezime"])
print("Telefon: ", prodaja["korisnik"]["telefon"])
print("Email: ", prodaja["korisnik"]["email"])
print("Artikl: ", prodaja["artikl"]["naslov"])
print("Opis: ", prodaja["artikl"]["opis"])
print("Cijena: ", prodaja["artikl"]["cijena"])



