Title: Herr Elo und der Rasenschach
Date: 2012-08-21 07:30
Author: footballissexbaby
Tags: Arpad Elo, Elo rating, Football, logistic curve, logistische funktion, NFL, Ranking-Systeme, Sagarin, Stats
Slug: herr-elo-und-der-rasenschach

Auf diesem Blog ging es ja schon oft um Ranking-Systeme, z. B. [hier][]
und [hier][1]. Jedoch war das Rating eines Teams bisher bloß eine
abstrakte Zahl. Hat ein Team ein Rating von Null, so heißt das, es ist
ein durchschnittliches Team und je höher ein Rating umso besser.

<div>
[caption id="attachment\_1096" align="alignright" width="250"]![][]
Arpad Elo, der Erfinder der Elo-Zahl. Copyright:
[chessbase.com][][/caption]

</div>
Trifft nun Heimteam A auf Gastteam B, so berechnet sich die Vorhersage
für den Sieger recht leicht:

[latex]W(A, B) = R(A) - R(B) + H[/latex]

Hierbei sind R(A) und R(B) die Ratings des jeweiligen Teams und H ist
der Heimvorteil.

Nehmen wir also an, dass Team A ein Rating von 9.8 hat, Team B ein
Rating von 1.4 und der Heimvorteil 3 Punkte beträgt, so würde man
erwarten:

[latex]W(A, B) = 9.8 - 1.4 + 3.0 = 11.4[/latex]

Team A würde in diesem Szenario also laut Ranking-System als Sieger den
heimischen Platz verlassen, da die Differenz der Ratings positiv ist.

Wie jedoch oben erwähnt ist diese Zahl 11.4 abstrakt. Sie hat keinen
echten Zusammenhang mit dem zu erwartenden Punktabstand (*point spread*)
und sie gibt auch keine Siegwahrscheinlichkeit an. Man kann aus ihr
einzig die Aussage treffen: Ist W(A, B) positiv, so gewinnt das
Heimteam, ist sie negativ das Auswärtsteam.

Diese Aussage ist natürlich nicht zufriedenstellend, was benötigt wird,
ist ein Maß, was eine gewisse Ratingdifferenz für die
Siegwahrscheinlichkeit bedeutet.

Und genau da kommt der nette Mann auf dem Foto ins Spiel: Sein Name ist
Arpad Elo, ein ungarischer Physikprofessor. Unter Footballfans wohl
gänzlich unbekannt, dürfte ihn aber der ein oder andere Schachspieler
durchaus kennen.

Arpad Elo ist der Erfinder des sogenannten [Elo-Systems][]: Ein System,
dass jedem Schachspieler einen Stärkewert zuweist. Das Elo-System ist in
der Lage für zwei Spieler anhand einer Formel eine Vorhersage zu
treffen, wieviele Siege welcher Spieler zu erwarten hat (sprich: wie
hoch die Siegwahrscheinlichkeit ist).

Dieser Erwartungswert ergibt sich für Spieler A wie folgt:

[latex size="2"]E(A) = \\frac{1}{1 + 10\^{(R(A) - R(B))/400}}[/latex]

Und analog für Spieler B:

[latex size="2"]E(B) = \\frac{1}{1 + 10\^{(R(B) - R(A))/400}}[/latex]

Nun ist es aber so, dass Schach und Football nicht viel miteinander zu
tun haben, auch wenn man letzteres gern mal als Rasenschach bezeichnet.
Die Elo-Zahl ist also (wie zu erwarten) nicht 1:1 auf Football
übertragbar.  
Jedoch ist die Form des Erwartungswerts genau das, was wir suchen.
Schauen wir uns das Ganze mal etwas genauer an:

Der Erwartungswert des Elo-Ratings ist mathematisch gesehen eine
sogenannte [logistische Funktion][]. Diese hat folgende generelle Form:

[latex size="2"]P(t) = \\frac{1}{1 + e\^{-t}}[/latex]

Die logisitische Funktion ist in Natur, Physik, Sozialwissenschaften und
eben Logistik gleichermaßen wichtig. Sie beschreibt beispielsweise das
Wachstum einer Bakterienpopulation, das Wachstum eines Tumors, das
Verhalten von Quantengasen (Fermi-Dirac-Statistik) oder auch die
Veränderung der Sprache.

Darüber hinaus besitzt sie einige für Ranking-Systeme sehr interessante
Eigenschaften:

-   für x \>\> 0 nähert sie sich 1
-   für x \<\< 0 nähert sie sich 0
-   für x = 0 ist sie 0.5

Das heißt also besonders hohe Ratingdifferenzen führen zu einem fast
sicheren Sieg (positive x), bzw. einer fast sicheren Niederlage
(negative x). Sind zwei Teams laut Rating gleich stark, so erwartet man
einen halben Sieg für beide Teams, sprich ein Unentschieden. Das klingt
doch schon sehr vernünftig!

Wie in der letzten Formel zu sehen, hängt die logistische Funktion von
dem Parameter t ab, dieser ergibt sich in unserem Fall als
Ratingdifferenz geteilt durch einen zu bestimmenden Wert a (im
Elo-Rating ist a = 400).

Ich habe alle Regular Season Spiele der letzten 10 Jahre betrachtet und
jeweils für die ganzzahlig gerundeten Ratingdifferenz die
Siegwahrscheinlichkeit berechnet. Anschließend habe ich die Daten mit
einer logistischen Funktion gefittet. Schauen wir uns das Ergebnis an:

[caption id="attachment\_1125" align="aligncenter"
width="300"][![][2]][] Wie im Elo-Rating folgt auch die auf
Ranking-Systemen basierende Siegwahrscheinlichkeit einer logistischen
Funktion.[/caption]

Die Siegwahrscheinlichkeit, die sich aus der Ratingdifferenz ergibt,
folgt also nicht nur im Schach, sondern auch im Football einer
logistischen Funktion.

Der Parameter a ist in unserem Fall 6.042, bei einem angenommenen
statischen Heimvorteil von 3 Punkten.

Der Zusammenhang zwischen Ranking und Siegen ergibt sich im Football
also wie folgt:

[latex size="2"]W(A) = \\frac{1}{1 + e\^{(R(A) - R(B) + 3) /
6.012}}[/latex]

Beziehungsweise für das Auswärtsteam:

[latex size="2"]W(B) = \\frac{1}{1 + e\^{(R(B) - R(A) - 3) /
6.012}}[/latex]

Greifen wir also auf unser erfundenes Beispiel von vorhin zurück, so
würde Team A eine Siegchance von etwa 87% haben, Team B hingegen nur
13%.

Mit Hilfe dieses "modifizierten" Elo-Erwartungswert ist es nun also
leicht möglich, für beliebige Begegnungen die Siegwahrscheinlichkeit zu
berechnen.

 

***Dank gebürt an dieser Stelle meinem Leser [JohnJohn][], der mich in
einem [Kommentar][] auf die Elo-Ratings aufmerksam gemacht hat! Vielen
Dank nochmal an dieser Stelle!***

  [hier]: http://footballissexbaby.de/2011/05/hausgemachte-sport-rankings-nach-sagarin-art-teil-1/
    "Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 1"
  [1]: http://footballissexbaby.de/2011/06/hausgemachte-sport-rankings-nach-sagarin-art-teil-2/
    "Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 2"
  []: http://footballissexbaby.de/wp-content/uploads/2012/08/elo09.jpg
    "elo09"
  [chessbase.com]: http://www.chessbase.com/newsprint.asp?newsid=4326
  [Elo-Systems]: http://de.wikipedia.org/wiki/Elo-Zahl
  [logistische Funktion]: http://de.wikipedia.org/wiki/Logistische_Funktion
  [2]: http://footballissexbaby.de/wp-content/uploads/2012/08/rating_wins_elo-300x225.png
    "rating_wins_elo"
  [![][2]]: http://footballissexbaby.de/wp-content/uploads/2012/08/rating_wins_elo.png
  [JohnJohn]: http://twitter.com/JohnyChamp
  [Kommentar]: http://footballissexbaby.de/2012/08/gfl-ratings-4-8-5-8-2012/#comment-164
