# Program će iščitati zadatak iz datoteke koji je zadan riječima (osim brojeva koji s zadani znamenkama) te će ga prilagoditi uvjetima rješavanja
#(izbaciti će nepotrebne riječi: sve one riječi koje ne predstavljaju osnovne računske operacije ili brojeve), nakon čega će ga probati riješiti.
#Nakon toga će tražiti od osobe da upiše svoj odgovor koji predstavlja njezino rješenje zadanog zadatka
#Ukoliko se upiše krivo rješenje, program će ispisati poruku : „Rješenje nije točno.“, te će se tražiti da osoba proba ponudi drugi odgovor (točan odgovor).
#Program će brojati koliko je puta osoba ponudila netočan odgovor te će na kraju programa uz rješenje zadatka ispisati broj ponuđenih odgovora.
#Ukoliko osoba ponudi točan odgovor, program će ispisati poruku: „Čestitam, tvoj odgovor je točan.“ te će se program završiti.
#Cilj programa je ispisati rješenje zadatka te broj ponuđenih odgovora osobe koja je pokušala pogoditi rješenje.

file = open('ULAZ.txt', 'r')
r = file.readlines()
a = ''.join(r).replace('\n', '')
b = a.split()
l = []



zb_l = ['zbrajanje', 'zbrajanjem', 'zbraja', 'zbroj', 'zbrojeni', 'zbroji','pribroji']
od_l = ['oduzimanje', 'oduzimanjem', 'oduzima', 'razlika', 'oduzeti', 'oduzmi']
mn_l = ['množenje', 'množenjem', 'množi', 'umnožak', 'pomnoženi', 'pomnozi', 'umnozak', 'umnoskom']
dj_l = ['dijeljenje', 'dijeljenjem', 'dijeli', 'količnik', 'podijeljeni','podijeli']



l_c = []
l_c += [zb_l] + [od_l] + [mn_l] + [dj_l]

for i in b:
     if i in zb_l or i in od_l or i in mn_l or i in dj_l:
         l += [i]
     if i.isdigit():
         l += [i]

print(b)
print('Lista:', l)

def grupiraj_znamenke(lista):
    znamenke = []
    while (lista!=[] and lista[0].isdigit()):
        znamenke += [lista[0]]
        lista.pop(0)
    return [znamenke, lista]

def grupiraj(lista,rezultat):
    #print(lista)
    #print(rezultat)
    if lista==[]:
        #print('Vracam rezultat')
        # Ako nema vise elemenata za obradu onda vrati rezultat
        return rezultat 
        # Ako je prvi element znamenka, onda grupiraj znamenke,
        # vrati ostatak liste i ponovi grupiranje
    elif lista[0].isdigit():
        #print('Grupiram znamenke')
        grupirano=grupiraj_znamenke(lista)
        lista=grupirano[1]
        rezultat+=[grupirano[0]]
        return grupiraj(lista,rezultat)
        # Ako je racunska opreacija, dodaj u listu i nastavi grupiranje
    else:
        #print('Dodajem radnju')
        rezultat+=[lista[0]]
        return grupiraj(lista[1:],rezultat)


print(grupiraj(l,[]))
         

# ((3 * 10 * 2) + 2 ) / (3 * 6)


# #ja bi trebao nap npr index('zbraja') jer bi mi to znacilo da broj ispred rijeci zbraja treba zbrojit s brojem
# #iza te rijeci
# #a kada bi imao zbroj koji je pomnozen s nekim brojem to bi znacilo da ovo prije moram zbrojit i pomnozit s necim nadolazećim

# ##
# ##if 'zbroj' in l:
# ##    rj +=

# rj = 0
# for i in l_c:
#     for j in i:
#         if j in l:
#             if j in zb_l:
#                 zb = l.index(j)
#                 rj += int(l[zb-1]) + int(l[zb+1])
#             elif j in od_l:
#                 od = l.index(j)
#                 rj -= int(l[od+1])
#             elif j in mn_l:
#                 mn = l.index(j)
#                 rj *= int(l[mn+1])
#             elif j in dj_l:
#                 dj = l.index(j)
#                 rj /=int(l[dj+1])
#             else:
#                 rj += 0

# print('Riješenje je: {}'.format(rj))

# ##zb = l.index('zbrajanje') #for riječ in l, for i in lista_riječi_s_zbrajanjem, if riječ in lista_riječi_s_zbrajanjem, zb = l.index(lista_riječi_s_zbrajanjem[i])
# ####dj = l.index('dijeljenje')mkj
# ##od = l.index('oduzimanje')
# ####mn = l.index('množenje')
# ##rj = 0
# ##for i in l:
# ##    if i == 'zbrajanje':
# ##        rj = int(l[zb-1]) + int(l[zb+1])
# ##    if i == 'oduzimanje':
# ##        rj -= int(l[od+1])
# ##        print('Riješenje2:', rj)
# moje = int(input('Upiši svoje riješenje:'))
# s = 0
# if moje == rj:
#     s += 1
#     print('Čestitam, riješenje ti je točno.')
# if moje != rj:
#     s += 1
#     print('Riješenje ti je netočno.')
#     status = True
#     while status:
#         status = False
#         z = int(input('Upiši neko drugo riješenje:'))
#         if z != rj:
#             s += 1
#             print('Netočno ti je riješenje, probaj ponovno.')
#             if s > 2:
#                 print('Želiš li da se pokaže postupak?')
#                 odg = input('Odgovor:')
#                 if odg == 'da':
#                     print('pokazati postupak')
#                 elif odg == 'ne':
#                     print('U redu.')
#             status = True
#         else:
#             s += 1
#             print('Čestitam, riješenje ti je točno.')
#             status = False

# print('Broj pokušaja: {}'.format(s))



# #Meni ispisuje riješenje kad ide kroz program a ne izbacuje mi konačno riješenje - treba napravit funkciju za to 



# # Sada cemo napisati neki novi dio koda


