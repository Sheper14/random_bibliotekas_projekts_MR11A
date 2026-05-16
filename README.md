# Python [Random](https://docs.python.org/3/library/index.html) bibliotēkas izpēte



## Bibliotēkas izvēles pamatojums

### 

### Autors - Markuss Rozentāls 11.A



#### RANDOM





"Random" ir viens no Python standarta bibliotēkām, kura ir iekļauta Python bez papildu instalācijas. Tā nodrošina vairākas metodes nejaušu skaitļu un izvēļu uzģenerēšanai. Šī bibiotēka tiek plaši izmantota visur, taču īpaši tiek pielietota spēļu izstrādē vai simulācijās. Es izvēlējos šo bibliotēku, jo tā piedāvā daudz un dažādas funkcijas, kuras nav grūti saprotamas un demonstrējamas. Izvēloties šo bibliotēku, vienlaikus iemācījos, ko jaunu, kā arī, iespējams, varu nodot šo informācijas apkopojumu citiem.





#### Kāpēc random?



Izvēlējos random bibliotēku, jo tā jau ir iekļauta Python. Tai ir daudz dažādu funkciju, kuras var uzskatāmi parādīt ar vienkāršiem piemēriem.



#### Funkciju apraksti



1. random.random() - ģenerē nejaušu decimālskaitli no 0 līdz 1
2. random.randint(a, b) - ģenerē nejaušu veselu skaitli norādītajā diapazonā
3. random.choice(seq) - izvēlas vienu nejaušu elementu no saraksta
4. random.choices(pop, k) - izvēlas vairākus elementus, var atkārtoties, var norādīt svērtās vērtības
5. random.shuffle(lst) - veido sarakstu nejaušā kārtībā
6. random.sample(pop, k) - izvēlas k unikālus elementus, neatkārtojas
7. random.uniform(a, b) - ģenerē nejaušu decimālskaitli norādītajā diapazonā
8. random.seed(a) - nosaka ģeneratora sākumpunktu, ar vienu seed vienmēr vienāds rezultāts
9. random.randrange(s, e, st) - nejauša skaitļa izvēle no diapazona ar soli, stop netiek iekļauts
10. random.gauss(mu, sigma) - ģenerē skaitļus pēc zvana formas sadalījuma, lielākā daļa tuvu vidējam
11. random.getrandbits(k) - ģenerē nejaušu skaitli ar norādītu bitu skaitu
12. random.triangular(l, h, m) - ģenerē skaitļus kur mode vērtība sanāk visbiežāk
13. random.expovariate(lambd) - ģenerē skaitļus ar eksponenciālo sadalījumu, noderīgs gaidīšanas laiku simulācijai
14. random.getstate() un setstate() - saglabā ģeneratora stāvokli un ļauj atgriezties pie tā vēlāk
15. random.betavariate(a, b) - ģenerē skaitļus no 0 līdz 1, alpha un beta nosaka kur tie biežāk krīt



#### Secinājumi



###### Ieguvumi:

* nav jāinstalē, nāk kopā ar Python
* ir gan vienkāršas funkcijas kā randint un choice, gan sarežģītākas kā gauss un betavariate
* ar seed, getstate un setstate var pilnībā kontrolēt ģeneratoru un atkārtot rezultātus
* lieto daudzās jomās, spēlēs, simulācijās, testēšanā, statistikā



###### Ierobežojumi:

* nav droša kriptogrāfijai, šim nolūkam jālieto secrets bibliotēka
* skaitļi izskatās nejauši, bet patiesībā ģenerēti ar algoritmu
* var rasties problēmas, ja programma izmanto vairākus pavedienus vienlaikus



#### Avoti



https://docs.python.org/3/library/random.html

https://www.geeksforgeeks.org/blogs/python-libraries-to-know/

