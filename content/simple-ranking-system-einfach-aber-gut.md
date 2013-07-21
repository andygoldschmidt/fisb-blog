Title: Simple Ranking System - einfach aber gut
Date: 2012-09-24 14:00
Author: footballissexbaby
Tags: Football, Margin of Victory, Ranking-Systeme, Simple Ranking System, Strength of schedule
Slug: simple-ranking-system-einfach-aber-gut

Ich habe in diesem Blog bereits ein Ranking-System vorgestellt, dass
[auf den Punktdifferenzen aller Spiele basiert][] und eines, dass
[lediglich Siege und Niederlagen in Betracht zieht][].

[![](|filename|/images/rodgers-brees-300x181.png)](|filename|/images/rodgers-brees.png)

Die beiden freuen sich über den geteilten 1. Platz im 2011er SRS.

Heute möchte ich noch ein drittes Ranking-System vorstellen: das
**Simple Ranking System**.

Wie der Name schon sagt, ist die Grundannahme dieses System sehr
einfach. Man nimmt die mittlere Differenz der Spielergebnisse eines
Teams (*margin of victory*) und korrigiert diesen Wert anhand der
Ratings der bereits gespielten Gegner.

Das sieht dann mathematisch einfach so aus:

$R_x = \text{MoV}_x + \frac{1}{N}\left(R_1 + R_2 + \dots +
R_N\right)$

Nimmt man also beispielsweise die Atlanta Falcons von 2012, dann würde
das also so aussehen:

$R(\text{ATL}) = \text{MoV}(\text{ATL}) +
\frac{1}{3}\left(R(\text{KC}) + R(\text{DEN}) +
R(\text{SD})\right)$

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

$\text{SRS} = \text{MoV} + \text{SOS}$

Eine simple Subtraktion von Rating und *margin of victory* liefert also
bereits die Stärke des Spielplans!

Schauen wir uns an, wie das Simple Ranking System nach dem Ende der
regulären Saison 2011 aussah (*Ergebnisse nach Woche 2 [finden sich
hier][], sind allerdings bisher nicht sehr aussagekräftig*):

<table class="table table-striped">
<thead>
<tr><th>Team</th><th>SRS</th><th>MoV</th><th>SOS</th></tr>
</thead>
<tbody>
<tr><td>Arizona Cardinals</td><td>-2.2</td><td>-2.2</td><td>0.0</td></tr>
<tr><td>Atlanta Falcons</td><td>3.5</td><td>3.2</td><td>0.3</td></tr>
<tr><td>Baltimore Ravens</td><td>6.1</td><td>7.0</td><td>-0.9</td></tr>
<tr><td>Buffalo Bills</td><td>-3.4</td><td>-3.9</td><td>0.5</td></tr>
<tr><td>Carolina Panthers</td><td>-1.3</td><td>-1.4</td><td>0.1</td></tr>
<tr><td>Chicago Bears</td><td>1.7</td><td>0.8</td><td>0.9</td></tr>
<tr><td>Cincinnati Bengals</td><td>0.5</td><td>1.3</td><td>-0.8</td></tr>
<tr><td>Cleveland Browns</td><td>-5.4</td><td>-5.6</td><td>0.2</td></tr>
<tr><td>Dallas Cowboys</td><td>1.6</td><td>1.4</td><td>0.2</td></tr>
<tr><td>Denver Broncos</td><td>-5.3</td><td>-5.1</td><td>-0.2</td></tr>
<tr><td>Detroit Lions</td><td>6.1</td><td>5.4</td><td>0.6</td></tr>
<tr><td>Green Bay Packers</td><td>11.4</td><td>12.6</td><td>-1.2</td></tr>
<tr><td>Houston Texans</td><td>4.5</td><td>6.4</td><td>-1.9</td></tr>
<tr><td>Indianapolis Colts</td><td>-11.3</td><td>-11.7</td><td>0.4</td></tr>
<tr><td>Jacksonville Jaguars</td><td>-5.6</td><td>-5.4</td><td>-0.3</td></tr>
<tr><td>Kansas City Chiefs</td><td>-8.1</td><td>-7.9</td><td>-0.2</td></tr>
<tr><td>Miami Dolphins</td><td>0.9</td><td>1.0</td><td>-0.1</td></tr>
<tr><td>Minnesota Vikings</td><td>-5.7</td><td>-6.8</td><td>1.1</td></tr>
<tr><td>New England Patriots</td><td>9.3</td><td>10.7</td><td>-1.4</td></tr>
<tr><td>New Orleans Saints</td><td>11.4</td><td>13.0</td><td>-1.6</td></tr>
<tr><td>New York Giants</td><td>1.6</td><td>-0.4</td><td>2.0</td></tr>
<tr><td>New York Jets</td><td>0.9</td><td>0.9</td><td>0.0</td></tr>
<tr><td>Oakland Raiders</td><td>-4.9</td><td>-4.6</td><td>-0.3</td></tr>
<tr><td>Philadelphia Eagles</td><td>4.7</td><td>4.2</td><td>0.5</td></tr>
<tr><td>Pittsburgh Steelers</td><td>5.3</td><td>6.1</td><td>-0.8</td></tr>
<tr><td>San Diego Chargers</td><td>0.9</td><td>1.8</td><td>-0.9</td></tr>
<tr><td>San Francisco 49ers</td><td>8.3</td><td>9.4</td><td>-1.1</td></tr>
<tr><td>Seattle Seahawks</td><td>0.8</td><td>0.4</td><td>0.4</td></tr>
<tr><td>St. Louis Rams</td><td>-10.5</td><td>-13.4</td><td>2.9</td></tr>
<tr><td>Tampa Bay Buccaneers</td><td>-10.6</td><td>-12.9</td><td>2.3</td></tr>
<tr><td>Tennessee Titans</td><td>-1.0</td><td>0.5</td><td>-1.5</td></tr>
<tr><td>Washington Redskins</td><td>-4.1</td><td>-4.9</td><td>0.8</td></tr>
</tbody>
</table>

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

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

  [auf den Punktdifferenzen aller Spiele basiert]: |filename|hausgemachte-sport-rankings-nach-sagarin-art-teil-1.md
  [lediglich Siege und Niederlagen in Betracht zieht]: |filename|yet-another-ranking-system.md
  [Strength of schedule]: |filename|strength-of-schedule-theorie-und-praxis.md
  [finden sich hier]: |filename|die-nfl-in-zahlen-woche-2.md
