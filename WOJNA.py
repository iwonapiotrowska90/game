import random

czlowiek = 'czlowiek: '
komputer = 'komputer: '
talia1 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jopek': 11, 'Dama': 12, 'Krol': 13,
          'As': 14}
talia2 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jopek': 11, 'Dama': 12, 'Krol': 13,
          'As': 14}
talia = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jopek', 'Dama', 'Krol', 'As']

punkty_czlowieka = []
punkty_komputera = []

karty_odrzucone = []

for x in range(1, 11):

    for karta_z_talii in talia1:
        talja = [karta_z_talii for karta_z_talii in talia1]
    print(f'Twoje karty w talii: {talja}')

    print('Rozgrywka nr ', x)
    while True:
        try:

            karta = input('Podaj karte z talii: ')
            karta1 = talia1[karta]
            break

        except KeyError:
            print('Podales bledna wartosc.')

    karta0 = random.choice(talia)
    karta2 = talia2[karta0]
    talia.remove(karta0)

    print(czlowiek, karta)
    print(komputer, karta0)

    if karta1 > karta2:
        print('czlowiek wygral runde')
        punkty_czlowieka.append(1)
    elif karta1 == karta2:
        print('Remis w rundzie')
        punkty_czlowieka.append(1)
        punkty_komputera.append(1)
    else:
        print('komputer wygral runde')
        punkty_komputera.append(1)

    karty_odrzucone.append(karta1)

    talia1.pop(karta)
    talia2.pop(karta0)

    # print('Zostalo ', len(talia1), ' kart w talii1')
    # print('Zostalo ', len(talia2), ' kart w talii2')
    # print('Punkty czlowieka: ', punkty_czlowieka)
    # print('Punkty komputera: ', punkty_komputera)
    print()

if len(punkty_czlowieka) > len(punkty_komputera):
    print('czlowiek wygral gre')
elif len(punkty_czlowieka) == len(punkty_komputera):
    print('REMIS, nikt nie wygral gry')
else:
    print('komputer wygral gre')
