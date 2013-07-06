Title: Yet Another Ranking System
Date: 2012-08-31 12:09
Author: footballissexbaby
Tags: Football, Modelle..., Ranking-Systeme, rankings, Sabermetrics, Sagarin, Stats, Taktik, Zahlen
Slug: yet-another-ranking-system

In diesem Beitrag soll es um ein Ranking-System gehen, dass im Gegensatz
zum Sagarin-Ranking-System nicht auf der Punktdifferenz (Point Spread)
aufbaut, sondern auf den Siegen bzw. Niederlagen eines Teams.

Diese Idee ist nicht neu, sondern[stammt von Doug Drinen][] von
[Pro-Football-Reference][], der wiederrum[von Peter Wolfe][] inspiriert
wurde.

Die Grundidee ist denkbar einfach. Die Siegwahrscheinlichkeit eines
Teams soll sich wie folgt aus den Ratings berechnen lassen:

[latex size=1]P(i) = \\frac{R\_i}{R\_i + R\_j}, P(j) = \\frac{R\_j}{R\_i
+ R\_j}[/latex]

Der Rest ist nur noch Mathematik! ([Hier geht es direkt zur Lösung][])
Um die Ratings zu berechnen muss man nun das Produkt der
Siegwahrscheinlichkeiten aller Spiele bilden:

[latex]P = \\prod P\_{i,j} = P\_{A,B} \\cdot P\_{C,D} \\cdot P\_{A,C}
... P\_{m,n}[/latex]

beziehungsweise

[latex]P = \\frac{R\_A}{R\_A + R\_B} \\cdot \\frac{R\_C}{R\_C + R\_D}
\\cdot \\frac{R\_A}{R\_A + R\_C} ... \\frac{R\_m}{R\_m + R\_n}[/latex]

Das entspricht also: (Wahrscheinlichkeit Sieg A gegen B) \*
(Wahrscheinlichkeit Sieg C gegen D) usw.

Das Ziel ist nun, das Rating für jedes Team so zu wählen, dass P maximal
wird, dass heißt die Wahrscheinlichkeit, das die Spiele so ausgehen, wie
sie wirklich ausgegangen sind, soll möglichst groß sein.

Man kann nun versuchen, die Ratings so lange zu raten bis man dass
Produkt aller Wahrscheinlichkeiten maximiert hat oder man geht einen
schnelleren und sichereren Weg: die Methode der maximalen
Wahrscheinlichkeit (*maximum-likelihood Methode*).

Dazu geht man wie folgt vor: zunächst logarithmiert man die Gleichung
für P (mit Logarithmen lässt sich leichter rechnen, da die Brüche und
Produkte zu Summen und Differenzen werden):

[latex size=-1]\\ln(P) = \\ln(R\_A) - \\ln(R\_A + R\_B) + \\ln(R\_C) -
\\ln(R\_C + R\_D) +\\ln(R\_A) - \\ln(R\_A + R\_C) + ...[/latex]

das lässt sich noch etwas zusammenfassen:

[latex]\\ln(P) = 2 \\cdot \\ln(R\_A) - \\ln(R\_A + R\_B) - \\ln(R\_A +
R\_C) + \\ln(R\_C) - \\ln(R\_C + R\_D) + ...[/latex]

Der nächste Schritt besteht darin die partielle Ableitung von ln(P) nach
jedem Rating zu bilden und sie gleich Null zu setzen:

[latex size=1]\\frac{\\partial\\ln(P)}{\\partial R\_A} = \\frac{2}{R\_A}
- \\left( \\frac{1}{R\_A + R\_B} + \\frac{1}{R\_A + R\_C}\\right)
\\stackrel{!}{=} 0[/latex]

Das Ganze kann man nun nach dem Rating für Team A auflösen:

[latex size=2]R\_A = \\frac{2}{\\frac{1}{R\_A + R\_B} + \\frac{1}{R\_A +
R\_C}}[/latex]

<a name="matheende"></a>Betrachtet man mehr Spiele, so sieht man
schnell, dass die Lösung sich einfach interpretieren lässt als:

[latex size=2]R\_A = \\frac{\\text{Anzahl Siege Team
A}}{\\frac{\\text{Anz. Spiele gegen B}}{R\_A + R\_B} +
\\frac{\\text{Anz. Spiele gegen C}}{R\_A + R\_C}}[/latex]

Das sieht doch schon übersichtlicher aus! Man kann natürlich die Ratings
nicht einfach "ausrechnen", aber man kann leicht durch Iteration zur
Lösung gelangen.

Mithilfe eines Rechners lassen sich die Ratings sehr schnell bestimmen.
Schauen wir uns die Ergebnisse nach Woche 17 der letzten Saison an:

  Team                   Rating
  ---------------------- --------
  Arizona Cardinals      0.85
  Atlanta Falcons        1.52
  Baltimore Ravens       2.53
  Buffalo Bills          0.64
  Carolina Panthers      0.57
  Chicago Bears          1.14
  Cincinnati Bengals     1.19
  Cleveland Browns       0.35
  Dallas Cowboys         0.87
  Denver Broncos         1.09
  Detroit Lions          1.97
  Green Bay Packers      8.33
  Houston Texans         1.32
  Indianapolis Colts     0.18
  Jacksonville Jaguars   0.42
  Kansas City Chiefs     0.84
  Miami Dolphins         0.60
  Minnesota Vikings      0.32
  New England Patriots   3.06
  New Orleans Saints     3.34
  New York Giants        1.28
  New York Jets          0.96
  Oakland Raiders        1.04
  Philadelphia Eagles    0.91
  Pittsburgh Steelers    2.69
  San Diego Chargers     1.08
  San Francisco 49ers    3.18
  Seattle Seahawks       0.77
  St. Louis Rams         0.22
  Tampa Bay Buccaneers   0.38
  Tennessee Titans       1.05
  Washington Redskins    0.41

Oder wenn wir es uns graphisch anschauen:

[caption id="attachment\_1177" align="aligncenter"
width="300"][![Maximum-likelihood Ranking][]][] Die Stärken der
einzelnen Teams im neuen Maximum-likelihood Ranking-System[/caption]

Man sieht, dass das Maximum-likelihood-Ranking (ML-Ranking) recht gut
zwischen starken und schwachen Teams unterscheidet. Wenig überraschend
sind die Colts und die Rams die schlechtesten Teams und die Packers das
beste.

Was jedoch auffällt ist die große Differenz zwischen bestem und
zweitbesten Rating. Das Rating der Packers weicht fast 5
Standardabweichungen vom Mittelwert ab, während 28 Teams innerhalb einer
Standardabweichung liegen und 31 Teams innerhalb von 2
Standardabweichungen.

Woher kommt das? Die Antwort ist recht einfach: Die Packers können ein
nahezu unendliches Rating haben, da sie nur einmal verloren haben!

Sieht man sich die Gleichung für die Berechnung für ein ungeschlagenes
Team an, so kann man für dieses Team den Ratingwert beliebig hoch wählen
ohne das die anderen Teams davon beeinflusst werden. Dieses Team spielt
dann also sprichwörtlich in einer anderen Liga!

Damit das vermieden wird und auch ungeschlagene Teams ein endliches
Rating bekommen, kann man einen einfachen Trick benutzen: jedes Team
spielt zweimal gegen ein fiktives Team mit dem Rating 1.0, gegen das
jedes Team einmal gewinnt und einmal verliert.

Dadurch ändert sich nominell nichts, aber man bekommt die
Unendlichkeiten in den Griff! (Skeptiker können das [hier genau
nachlesen][])

(*Obige Ratings wurden schon mit diesem Dummy-Team erstellt, wodurch
sich das Packers-Rating von 13.63 auf 8.33 reduziert hat.*)

Im Gegensatz zum herkömmlichen Sagarin-Ranking, [bei dem es nicht ganz
einfach ist eine Siegwahrscheinlichkeit zu berechnen][], kann man beim
ML-Ranking die Siegwahrscheinlichkeit direkt ablesen.

Nehmen wir als Beispiel den Season Opener New York Giants gegen Dallas
Cowboys. Die Giants haben ein Rating von 1.28, die Cowboys von 0.87.
Damit ergibt sich die Siegwahrscheinlichkeit als:

[latex size=1]P(\\text{Giants}) = \\frac{1.28}{1.28 + 0.87} =
0.59[/latex]

Das heißt zu 59% darf der Autor dieses Blogs nächsten Mittwoch jubeln,
das sind doch schöne Aussichten!

  [stammt von Doug Drinen]: http://www.pro-football-reference.com/blog/?p=171
  [Pro-Football-Reference]: http://www.pro-football-reference.com/
  [von Peter Wolfe]: http://prwolfe.bol.ucla.edu/cfootball/descrip.htm
  [Hier geht es direkt zur Lösung]: #matheende
  [Maximum-likelihood Ranking]: http://footballissexbaby.de/wp-content/uploads/2012/08/ml_rating-300x215.png
    "ml_rating"
  [![Maximum-likelihood Ranking][]]: http://footballissexbaby.de/wp-content/uploads/2012/08/ml_rating.png
  [hier genau nachlesen]: http://www.davemease.com/football/
  [bei dem es nicht ganz einfach ist eine Siegwahrscheinlichkeit zu
  berechnen]: http://footballissexbaby.de/2012/08/herr-elo-und-der-rasenschach/
    "Herr Elo und der Rasenschach"
