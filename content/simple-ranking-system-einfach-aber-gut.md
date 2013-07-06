Title: Simple Ranking System - einfach aber gut
Date: 2012-09-24 14:00
Author: footballissexbaby
Tags: Football, Margin of Victory, Ranking-Systeme, Simple Ranking System, Strength of schedule
Slug: simple-ranking-system-einfach-aber-gut

Ich habe in diesem Blog bereits ein Ranking-System vorgestellt, dass
[auf den Punktdifferenzen aller Spiele basiert][] und eines, dass
[lediglich Siege und Niederlagen in Betracht zieht][].

<div>
[caption id="attachment\_1380" align="alignright" width="300"][![][]][]
Die beiden freuen sich über den geteilten 1. Platz im 2011er
SRS.[/caption]

</div>
Heute möchte ich noch ein drittes Ranking-System vorstellen: das
**Simple Ranking System**.

Wie der Name schon sagt, ist die Grundannahme dieses System sehr
einfach. Man nimmt die mittlere Differenz der Spielergebnisse eines
Teams (*margin of victory*) und korrigiert diesen Wert anhand der
Ratings der bereits gespielten Gegner.

Das sieht dann mathematisch einfach so aus:

[latex]R\_x = \\text{MoV}\_x + \\frac{1}{N}\\left(R\_1 + R\_2 + \\dots +
R\_N\\right)[/latex]

Nimmt man also beispielsweise die Atlanta Falcons von 2012, dann würde
das also so aussehen:

[latex]R(\\text{ATL}) = \\text{MoV}(\\text{ATL}) +
\\frac{1}{3}\\left(R(\\text{KC}) + R(\\text{DEN}) +
R(\\text{SD})\\right)[/latex]

Das einzige Problem das man nun hat: man kennt die einzelnen *R*
(Ratings) nicht. Das heißt also, man hat 32 Gleichungen mit 32
Unbekannten.

Um dieses Problem zu lösen hat man nun zwei Möglichkeiten:

1.  durch Lösen des Gleichungssystem als Matrix
2.  durch Iteration

Wählt man Möglichkeit 1, so nimmt man einfach eine der zahllosen
Möglichkeiten ein Gleichungssystem mittels eines PCs zu lösen. Die 32
Lösungen sind dann die Ratings für jedes der 32 Teams.

Bei Möglichkeit 2, dem Iterieren, fängt man sinnvollerweise damit an,
jedem Team als Anfangsrating einfach den MoV zuzuweisen und dann zu
aktualisieren, bis sich die Werte nicht mehr ändern.

Welche Variante man wählt ist wohl absolut Geschmackssache, mathematisch
eleganter ist sicher die 1. Variante, schnell sind aber auf modernen
Rechnern beide.

Doch das Simple Ranking System ist hier noch nicht am Ende. Denn über
die Ratings hinaus ist es auch noch möglich eine [Strength of
schedule][] (SOS) zu berechnen, eigentlich eher abzulesen.

Denn wenn man sich die Formel noch einmal anschaut, steht da eigentlich
nichts anderes als:

[latex]\\text{SRS} = \\text{MoV} + \\text{SOS}[/latex]

Eine simple Subtraktion von Rating und *margin of victory* liefert also
bereits die Stärke des Spielplans!

Schauen wir uns an, wie das Simple Ranking System nach dem Ende der
regulären Saison 2011 aussah (*Ergebnisse nach Woche 2 [finden sich
hier][], sind allerdings bisher nicht sehr aussagekräftig*):

  Team                   SRS     MoV     SOS
  ---------------------- ------- ------- ------
  Arizona Cardinals      -2.2    -2.2    0.0
  Atlanta Falcons        3.5     3.2     0.3
  Baltimore Ravens       6.1     7.0     -0.9
  Buffalo Bills          -3.4    -3.9    0.5
  Carolina Panthers      -1.3    -1.4    0.1
  Chicago Bears          1.7     0.8     0.9
  Cincinnati Bengals     0.5     1.3     -0.8
  Cleveland Browns       -5.4    -5.6    0.2
  Dallas Cowboys         1.6     1.4     0.2
  Denver Broncos         -5.3    -5.1    -0.2
  Detroit Lions          6.1     5.4     0.6
  Green Bay Packers      11.4    12.6    -1.2
  Houston Texans         4.5     6.4     -1.9
  Indianapolis Colts     -11.3   -11.7   0.4
  Jacksonville Jaguars   -5.6    -5.4    -0.3
  Kansas City Chiefs     -8.1    -7.9    -0.2
  Miami Dolphins         0.9     1.0     -0.1
  Minnesota Vikings      -5.7    -6.8    1.1
  New England Patriots   9.3     10.7    -1.4
  New Orleans Saints     11.4    13.0    -1.6
  New York Giants        1.6     -0.4    2.0
  New York Jets          0.9     0.9     0.0
  Oakland Raiders        -4.9    -4.6    -0.3
  Philadelphia Eagles    4.7     4.2     0.5
  Pittsburgh Steelers    5.3     6.1     -0.8
  San Diego Chargers     0.9     1.8     -0.9
  San Francisco 49ers    8.3     9.4     -1.1
  Seattle Seahawks       0.8     0.4     0.4
  St. Louis Rams         -10.5   -13.4   2.9
  Tampa Bay Buccaneers   -10.6   -12.9   2.3
  Tennessee Titans       -1.0    0.5     -1.5
  Washington Redskins    -4.1    -4.9    0.8

Ohne viele Annahmen kann man sich also ein Rating und die Strength of
schedule eines Teams berechnen. Und im Vergleich zu anderen
Ranking-Systemen (wie z.B. dem Maximum-Likelihood-Modell) kann man die
Zahlen sehr einfach interpretieren:

Hat Team A ein 3 Punkte größeres Rating als Team B, so kann man davon
ausgehen, dass Team A mit 3 Punkten Vorsprung gewinnen wird.

Genauso mit der Strength of schedule: hat ein Team einen SOS-Wert von
1.5, dann waren seine Gegner 1.5 Punkte besser als der Durchschnitt.
Analog bedeutet ein negativer SOS-Wert, dass das Team gegen schwache
Gegner gespielt hat - also eine leichte Schedule hatte.

Man hat mit dem Simple Ranking System also ein sehr einfaches aber
aussagekräftiges System, an dem man sehr schnell ablesen kann, wie gut
ein Team ist und ob es nur so gut ist, weil es gegen schwache Gegner
gespielt hat.

  [auf den Punktdifferenzen aller Spiele basiert]: http://footballissexbaby.de/2011/05/hausgemachte-sport-rankings-nach-sagarin-art-teil-1/
    "Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 1"
  [lediglich Siege und Niederlagen in Betracht zieht]: http://footballissexbaby.de/2012/08/yet-another-ranking-system/
    "Yet Another Ranking System"
  []: http://footballissexbaby.de/wp-content/uploads/2012/09/rodgers-brees-300x181.png
    "rodgers-brees"
  [![][]]: http://footballissexbaby.de/wp-content/uploads/2012/09/rodgers-brees.png
  [Strength of schedule]: http://footballissexbaby.de/2012/07/strength-of-schedule-theorie-und-praxis/
    "Strength of schedule – Theorie und Praxis"
  [finden sich hier]: http://footballissexbaby.de/2012/09/die-nfl-in-zahlen-woche-2/
    "Die NFL in Zahlen: Woche 2"
