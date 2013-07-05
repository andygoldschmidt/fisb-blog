Title: Die Erfolgsquote der Running Backs
Date: 2013-05-10 07:19
Author: footballissexbaby
Tags: Brian Burke, Football, Football Outsiders, NFL, Success Rate
Slug: die-erfolgsquote-der-running-backs

<div>
[caption id="attachment\_2174" align="alignright" width="300"]![Der
derzeit zweifellos beste Running Back der NFL.][] Der derzeit zweifellos
beste Running Back der NFL.[/caption]

</div>
Geht es darum, wer der beste Running Back in der NFL ist, hört man
schnell: der Spieler mit den meisten Laufyards. Nur wenig
aussagekräftiger ist es, die Yards pro Versuch oder Touchdowns
anzuführen.

Ein Running Back mit 6.0 Yards pro Versuch mag ja gut sein, aber wenn
dieser Wert in 5 Versuchen zustande gekommen ist, ist das weder ein Maß
für die Qualität des Spielers noch sehr aussagekräftig.

Was kann man also tun, um besser einzuschätzen, welche Running Backs
besonders erfolgreich waren? Ein Konzept ist die sogenannte *Success
Rate*, die situationsabhängig entscheidet, ob ein Lauf erfolgreich war
oder nicht und schließlich die Zahl der erfolgreichen Runs durch die
Gesamtzahl teilt.

Die Idee dahinter ist einfach: beispielsweise ist ein Lauf über 3 Yards
nicht in jeder Situation gleich wertvoll. Bei einem 1st & 20, ist einem
damit nicht besonders viel geholfen. Bei einem 4th & 1 hingegen ist
dieser Lauf dafür verantwortlich, dass der Drive am Leben bleibt. Der
exakt gleiche Lauf war also einmal ein Erfolg und das andere Mal nicht.

Und hierbei wird auch schon die große Herausforderung mit der Success
Rate deutlich: was definiert einen Lauf als Erfolg oder Misserfolg?

Einigkeit herrscht hierbei überhaupt nicht.

Die "klassische" Definition, die auch von vielen Coaches (z.B. Cam
Cameron) so benutzt wird, ist die folgende:

-   **1st Down:** \>= 4 Yards
-   **2nd Down:** \> Hälfte der *Yards to go*
-   **3rd Down:** neues First Down
-   **4th Down:** neues First Down

Hierbei ist zu erwähnen, dass oftmals Läufe im 4th down aus der
Betrachtung ausgenommen werden; warum ist mir nicht ganz klar, daher
behandele ich ein 4th down wie ein 3rd down.

Die Football Outsiders haben eine ganz eigene Definition, die FO-typisch
etwas willkürlich wirkt.

> -   In general, a play counts as a "hit" if it gains 40% of yards on
>     first down, 60% of yards on second down, and 100% of yards on
>     third down.
> -   If the team is behind by more than a touchdown in the fourth
>     quarter, the benchmarks switch to 50%/65%/100%.
> -   If the team is ahead by any amount in the fourth quarter, the
>     benchmarks switch to 30%/50%/100%.

(Quelle: [Football Outsiders][])

Die eleganteste Version liefert - wie so oft, wenn es um Advanced
Statistics geht - Brian Burke: ein Lauf ist dann erfolgreich, wenn er
die *Expected Points* erhöht. Doch Expected Points ist ein sehr
umfangreiches System und daher nicht für den Hausgebrauch zu übernehmen.

Daher habe ich mich in meinem Versuch eine Success Rate zu
implementieren auf die klassische Definition beschränkt. Doch die
Definition ist in der Implementierung erst der letzte Schritt. Die
meiste Zeit muss man darauf verwenden, die Play-by-Play-Daten ordentlich
zu durchforsten und auf die vielen Sonderfälle Rücksicht zu nehmen.

Gleich vorweg: ich habe sicher einige "spezielle" Plays in den Daten
kaltblütig ignoriert, aber die öffentlichen Datensätze sind nicht
besonders sauber und daher werde ich sicher dem ein oder anderen Running
Back immer wieder mal Unrecht getan haben.

Die Success Rate für 2012 sieht für die 25 erfolgreichsten Running Backs
wie folgt aus:

<table>
<thead>
<tr>
<th>
Name

</th>
<th>
Att

</th>
<th>
Yds

</th>
<th>
TD

</th>
<th>
SR

</th>
<tr>
</thead>
<tbody>
<tr>
<td>
W.McGahee

</td>
<td>
167

</td>
<td>
731

</td>
<td>
4

</td>
<td>
0.57

</td>
</tr>
<tr>
<td>
D.Murray

</td>
<td>
161

</td>
<td>
663

</td>
<td>
4

</td>
<td>
0.55

</td>
</tr>
<tr>
<td>
B.Brown

</td>
<td>
115

</td>
<td>
564

</td>
<td>
4

</td>
<td>
0.55

</td>
</tr>
<tr>
<td>
C.Spiller

</td>
<td>
207

</td>
<td>
1244

</td>
<td>
6

</td>
<td>
0.55

</td>
</tr>
<tr>
<td>
A.Bradshaw

</td>
<td>
221

</td>
<td>
1015

</td>
<td>
6

</td>
<td>
0.51

</td>
</tr>
<tr>
<td>
L.McCoy

</td>
<td>
200

</td>
<td>
840

</td>
<td>
2

</td>
<td>
0.50

</td>
</tr>
<tr>
<td>
S.Greene

</td>
<td>
276

</td>
<td>
1063

</td>
<td>
8

</td>
<td>
0.50

</td>
</tr>
<tr>
<td>
B.Pierce

</td>
<td>
108

</td>
<td>
532

</td>
<td>
1

</td>
<td>
0.50

</td>
</tr>
<tr>
<td>
A.Morris

</td>
<td>
335

</td>
<td>
1606

</td>
<td>
13

</td>
<td>
0.50

</td>
</tr>
<tr>
<td>
M.Lynch

</td>
<td>
315

</td>
<td>
1590

</td>
<td>
11

</td>
<td>
0.49

</td>
</tr>
<tr>
<td>
F.Gore

</td>
<td>
259

</td>
<td>
1212

</td>
<td>
8

</td>
<td>
0.49

</td>
</tr>
<tr>
<td>
P.Thomas

</td>
<td>
105

</td>
<td>
473

</td>
<td>
1

</td>
<td>
0.49

</td>
</tr>
<tr>
<td>
S.Jackson

</td>
<td>
257

</td>
<td>
1042

</td>
<td>
4

</td>
<td>
0.48

</td>
</tr>
<tr>
<td>
M.Bush

</td>
<td>
114

</td>
<td>
411

</td>
<td>
5

</td>
<td>
0.47

</td>
</tr>
<tr>
<td>
R.Bush

</td>
<td>
227

</td>
<td>
986

</td>
<td>
6

</td>
<td>
0.47

</td>
</tr>
<tr>
<td>
S.Ridley

</td>
<td>
290

</td>
<td>
1263

</td>
<td>
12

</td>
<td>
0.46

</td>
</tr>
<tr>
<td>
F.Jones

</td>
<td>
111

</td>
<td>
402

</td>
<td>
3

</td>
<td>
0.46

</td>
</tr>
<tr>
<td>
M.Ingram

</td>
<td>
156

</td>
<td>
602

</td>
<td>
5

</td>
<td>
0.46

</td>
</tr>
<tr>
<td>
I.Redman

</td>
<td>
110

</td>
<td>
410

</td>
<td>
2

</td>
<td>
0.46

</td>
</tr>
<tr>
<td>
A.Peterson

</td>
<td>
348

</td>
<td>
2097

</td>
<td>
12

</td>
<td>
0.46

</td>
</tr>
<tr>
<td>
B.Green-Ellis

</td>
<td>
278

</td>
<td>
1094

</td>
<td>
6

</td>
<td>
0.45

</td>
</tr>
<tr>
<td>
A.Green

</td>
<td>
134

</td>
<td>
456

</td>
<td>
0

</td>
<td>
0.45

</td>
</tr>
<tr>
<td>
K.Moreno

</td>
<td>
139

</td>
<td>
528

</td>
<td>
4

</td>
<td>
0.44

</td>
</tr>
<tr>
<td>
J.Charles

</td>
<td>
284

</td>
<td>
1513

</td>
<td>
5

</td>
<td>
0.44

</td>
</tr>
<tr>
<td>
F.Jackson

</td>
<td>
115

</td>
<td>
437

</td>
<td>
3

</td>
<td>
0.44

</td>
</tr>
</tbody>
</table>
Die Frage "Wo ist Adrian Peterson???" wird sich sicher fast jedem
stellen. Doch sein Spiel besteht eben aus vielen 1-Yard-Läufen, die
immer wieder von überragenden 20 oder 30 Yard-Runs vergessen gemacht
werden. Insgesamt ist diese Spielweise aber nicht so erfolgreich wie von
anderen RBs.

Das heißt natürlich nicht, dass Willis McGahee der beste NFL-RB ist oder
besser als Adrian Peterson ist, vielmehr besagt die Success Rate
lediglich, dass man sich auf McGahee mehr verlassen kann, wenn es darum
geht kritische Yards zu bekommen.

Betrachtet man nicht nur Running Backs, sondern alle Spieler, wird die
Liste übrigens von Robert Griffin III mit einer Erfolgsquote von 61%
angeführt.

Der aufmerksame Leser wird bemerkt haben, dass die Zahlen teilweise
deutlich von denen bei Football Outsiders abweichen. Zum einen liegt das
daran, dass sie wie bereits erwähnt eine andere Berechnungsgrundlage
haben. Gerade bei erfolgreichen Teams, die das Laufspiel zum Zeit
verbrauchen nutzen, dürfte der Effekt einer leistungsabhängigen
Berechnung (Führung/Rückstand) deutlich zutage treten.

Zum anderen liegt es aber auch an den Daten. Wie bereits erwähnt, gibt
es in den öffentlichen Play-by-play-Daten immer wieder mysteriöse
Einträge, die kaum vernünftig auswertbar sind. Football Outsiders hat
den Riesenvorteil, genug Manpower zu haben, um ihre eigenen
Play-by-Play-Daten erstellen zu können und so eine wesentlich bessere
Datengrundlage zu haben.

Mein Algorithmus ist sicher noch nicht ganz perfekt und ich werde in den
kommenden Wochen weiter daran feilen, die Daten noch besser auswerten zu
können und Spezialfälle berücksichtigen zu können. Doch die Success Rate
war eher ein Nebenprodukt eines größeren Projekts, für das ich diese
Metrik benötige.

Wie bei allen Statistiken, muss man vorsichtig sein nicht zu viel
hineinzuinterpretieren, jedoch gibt die Success Rate einen deutlich
besseren Eindruck über die Effizienz eines RBs als nur die Total Yards
oder nur die Yards pro Versuch.

Doch auch wenn Adrian Peterson in der Success Rate nur Mittelmaß ist,
besteht wohl kein Zweifel daran, dass er zurecht als derzeit bester
Running Back in der NFL gesehen wird.

  [Der derzeit zweifellos beste Running Back der NFL.]: http://footballissexbaby.de/wordpress/wp-content/uploads/2013/05/ap-300x200.jpg
  [Football Outsiders]: http://www.footballoutsiders.com/stat-analysis/2004/introducing-running-back-success-rate
