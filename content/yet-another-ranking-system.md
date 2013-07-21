Title: Yet Another Ranking System
Date: 2012-08-31 12:09
Author: footballissexbaby
Category: Footballmetrics
Tags: Football, Ranking-Systeme
Slug: yet-another-ranking-system

In diesem Beitrag soll es um ein Ranking-System gehen, dass im Gegensatz
zum Sagarin-Ranking-System nicht auf der Punktdifferenz (Point Spread)
aufbaut, sondern auf den Siegen bzw. Niederlagen eines Teams.

Diese Idee ist nicht neu, sondern [stammt von Doug Drinen][] von
[Pro-Football-Reference][], der wiederrum [von Peter Wolfe][] inspiriert
wurde.

Die Grundidee ist denkbar einfach. Die Siegwahrscheinlichkeit eines
Teams soll sich wie folgt aus den Ratings berechnen lassen:

$P(i) = \frac{R_i}{R_i + R_j}, P(j) = \frac{R_j}{R_i + R_j}$

Der Rest ist nur noch Mathematik! ([Hier geht es direkt zur Lösung][])
Um die Ratings zu berechnen muss man nun das Produkt der
Siegwahrscheinlichkeiten aller Spiele bilden:

$P = \prod P_{i,j} = P_{A,B} \cdot P_{C,D} \cdot P_{A,C} ... P_{m,n}$

beziehungsweise

$P = \frac{R_A}{R_A + R_B} \cdot \frac{R_C}{R_C + R_D}
\cdot \frac{R_A}{R_A + R_C} ... \frac{R_m}{R_m + R_n}$

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

$\ln(P) = \ln(R_A) - \ln(R_A + R_B) + \ln(R_C) -
\ln(R_C + R_D) +\ln(R_A) - \ln(R_A + R_C) + ...$

das lässt sich noch etwas zusammenfassen:

$\ln(P) = 2 \cdot \ln(R_A) - \ln(R_A + R_B) - \ln(R_A +
R_C) + \ln(R_C) - \ln(R_C + R_D) + ...$

Der nächste Schritt besteht darin die partielle Ableitung von ln(P) nach
jedem Rating zu bilden und sie gleich Null zu setzen:

$\frac{\partial\ln(P)}{\partial R_A} = \frac{2}{R_A}
- \left( \frac{1}{R_A + R_B} + \frac{1}{R_A + R_C}\right)
\stackrel{!}{=} 0$

Das Ganze kann man nun nach dem Rating für Team A auflösen:

$R_A = \frac{2}{\frac{1}{R_A + R_B} + \frac{1}{R_A +
R_C}}$

<a name="matheende"></a>

Betrachtet man mehr Spiele, so sieht man schnell, dass die Lösung sich
einfach interpretieren lässt als:

$R\_A = \\frac{\\text{Anzahl Siege Team
A}}{\\frac{\\text{Anz. Spiele gegen B}}{R\_A + R\_B} +
\\frac{\\text{Anz. Spiele gegen C}}{R\_A + R\_C}}$

Das sieht doch schon übersichtlicher aus! Man kann natürlich die Ratings
nicht einfach "ausrechnen", aber man kann leicht durch Iteration zur
Lösung gelangen.

Mithilfe eines Rechners lassen sich die Ratings sehr schnell bestimmen.
Schauen wir uns die Ergebnisse nach Woche 17 der letzten Saison an:

<table class="table">
<thead>
<tr>
<th>Team</th>
<th>Rating</th>
</tr>
</thead>
<tbody>
<tr><td>Arizona Cardinals</td><td>0.85</td></tr>
<tr><td>Atlanta Falcons</td><td>1.52</td></tr>
<tr><td>Baltimore Ravens</td><td>2.53</td></tr>
<tr><td>Buffalo Bills</td><td>0.64</td></tr>
<tr><td>Carolina Panthers</td><td>0.57</td></tr>
<tr><td>Chicago Bears</td><td>1.14</td></tr>
<tr><td>Cincinnati Bengals</td><td>1.19</td></tr>
<tr><td>Cleveland Browns</td><td>0.35</td></tr>
<tr><td>Dallas Cowboys</td><td>0.87</td></tr>
<tr><td>Denver Broncos</td><td>1.09</td></tr>
<tr><td>Detroit Lions</td><td>1.97</td></tr>
<tr><td>Green Bay Packers</td><td>8.33</td></tr>
<tr><td>Houston Texans</td><td>1.32</td></tr>
<tr><td>Indianapolis Colts</td><td>0.18</td></tr>
<tr><td>Jacksonville Jaguars</td><td>0.42</td></tr>
<tr><td>Kansas City Chiefs</td><td>0.84</td></tr>
<tr><td>Miami Dolphins</td><td>0.60</td></tr>
<tr><td>Minnesota Vikings</td><td>0.32</td></tr>
<tr><td>New England Patriots</td><td>3.06</td></tr>
<tr><td>New Orleans Saints</td><td>3.34</td></tr>
<tr><td>New York Giants</td><td>1.28</td></tr>
<tr><td>New York Jets</td><td>0.96</td></tr>
<tr><td>Oakland Raiders</td><td>1.04</td></tr>
<tr><td>Philadelphia Eagles</td><td>0.91</td></tr>
<tr><td>Pittsburgh Steelers</td><td>2.69</td></tr>
<tr><td>San Diego Chargers</td><td>1.08</td></tr>
<tr><td>San Francisco 49ers</td><td>3.18</td></tr>
<tr><td>Seattle Seahawks</td><td>0.77</td></tr>
<tr><td>St. Louis Rams</td><td>0.22</td></tr>
<tr><td>Tampa Bay Buccaneers</td><td>0.38</td></tr>
<tr><td>Tennessee Titans</td><td>1.05</td></tr>
<tr><td>Washington Redskins</td><td>0.41</td></tr>
</tbody>
</table>

Oder wenn wir es uns graphisch anschauen:

[![Maximum-likelihood Ranking](|filename|/images/ml_rating-300x215.png)](|filename|/images/ml_rating.png) 

*Die Stärken der einzelnen Teams im neuen Maximum-likelihood Ranking-System*

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

Im Gegensatz zum herkömmlichen Sagarin-Ranking, [bei dem es nicht ganz einfach ist eine Siegwahrscheinlichkeit zu berechnen][], kann man beim
ML-Ranking die Siegwahrscheinlichkeit direkt ablesen.

Nehmen wir als Beispiel den Season Opener New York Giants gegen Dallas
Cowboys. Die Giants haben ein Rating von 1.28, die Cowboys von 0.87.
Damit ergibt sich die Siegwahrscheinlichkeit als:

$P(\text{Giants}) = \frac{1.28}{1.28 + 0.87} = 0.59$

Das heißt zu 59% darf der Autor dieses Blogs nächsten Mittwoch jubeln,
das sind doch schöne Aussichten!

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

  [stammt von Doug Drinen]: http://www.pro-football-reference.com/blog/?p=171
  [Pro-Football-Reference]: http://www.pro-football-reference.com/
  [von Peter Wolfe]: http://prwolfe.bol.ucla.edu/cfootball/descrip.htm
  [Hier geht es direkt zur Lösung]: #matheende
  [hier genau nachlesen]: http://www.davemease.com/football/
  [bei dem es nicht ganz einfach ist eine Siegwahrscheinlichkeit zu berechnen]: |filename|herr-elo-und-der-rasenschach.md
    "Herr Elo und der Rasenschach"
