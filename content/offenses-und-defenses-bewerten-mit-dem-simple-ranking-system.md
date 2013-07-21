Title: Offenses und Defenses bewerten mit dem Simple Ranking System
Date: 2012-11-14 08:30
Author: footballissexbaby
Tags: Doug Drinen, DSRS, Football, NFL, OSRS, Pro-Football-Reference, Simple Ranking System, SRS
Slug: offenses-und-defenses-bewerten-mit-dem-simple-ranking-system

Das [Simple Ranking System][] wird in diesem Blog regelmäßig im
Zusammenhang mit der Review auf den letzten NFL-Spieltag benutzt.

Populär wurde es in dieser Form und unter diesem Namen hauptsächlich
durch Doug Drinen, der es im [Pro-Football-Reference Blog][] vorgestellt
hat und auf den Team-Seiten von PFR standardmäßig eingeführt hat.

Wer jedoch öfter auf den Seiten von PFR unterwegs ist, wird bereits
bemerkt haben, dass es dort neben SRS auch ein OSRS und ein DSRS gibt -
ein Offense und ein Defense Simple Rating System.

Die Idee ist einfach, aber sehr clever: Wenn man statt der
durchschnittlichen Punktdifferenz die durchschnittliche Anzahl an
Punkten nimmt und mit den durchschnittlich zugelassenen Punkten der
bisher gespielten Defenses korrigiert, bekommt man einen Wert dafür, wie
gut die Offense wirklich ist.

Genauso gut lässt sich das natürlich auch mit der Anzahl zugelassener
Punkte und durch die Gegner erzielten Punkte machen, um ein Maß für die
Stärke der Defense zu finden.

Das normale SRS berechnet sich wie folgt:

$\text{SRS(X)} = \text{MoV(X)} + \frac{1}{\text{N}}\left(
\text{SRS(A)} + \text{SRS(B)} + ...\right)$

Dabei ist MoV die durchschnittliche Punktdifferenz, N die Anzahl
bisheriger Spiele und SRS(A), SRS(B), ... die Rankings der Gegner.  
Das Offense SRS (OSRS) bekommt man nun indem man die Formel leicht
anpasst:

$\text{OSRS(X)} = \text{PF(X)} + \frac{1}{\text{N}}\left(
\text{PA(A)} + \text{PA(B)} + ...\right)$

Hier sind PF die erzielten Punkte und PA die zugelassenen Punkte. Das
DSRS bekommt man, indem man PF und PA in der Formel einfach vertauscht.

Diese Ratings haben eine nette Eigenschaft, denn es gilt:

$\text{SRS} = \text{OSRS} + \text{DSRS}$

Es handelt sich also lediglich in eine Zerlegung des SRS in zwei
Summanden.

OSRS und DSRS sind sicher nicht weltbewegend, denn auch sie bauen
lediglich auf der Anzahl an Punkten auf und sind daher Metriken wie
[Brian Burkes][] EPA (expected points added) oder [Football Outsiders][]
DVOA (Defense-adjusted value oder average) unterlegen.

Aber wie auch im herkömmlichen SRS vermitteln diese beiden Werte einen
guten Eindruck davon, warum ein Team gut oder schlecht ist. Oder auch,
ob ein Team auf einer Seite des Balls deutlich stärker ist als auf der
anderen.

Im folgenden sind die alle Simple Ranking System-Größen (SRS, MoV, SOS,
OSRS und DSRS) für die NFL-Saison 2012 nach Woche 10 aufgelistet:

<table class="table table-striped">
<thead>
<tr><th>Team</th><th>SRS</th><th>OSRS</th><th>DSRS</th></tr>
</thead>
<tbody>
<tr><td>Arizona Cardinals</td><td>-1.5</td><td>-8.6</td><td>7.2</td></tr>
<tr><td>Atlanta Falcons</td><td>5.5</td><td>6.1</td><td>-0.6</td></tr>
<tr><td>Baltimore Ravens</td><td>4.0</td><td>5.3</td><td>-1.3</td></tr>
<tr><td>Buffalo Bills</td><td>-7.2</td><td>0.5</td><td>-7.7</td></tr>
<tr><td>Carolina Panthers</td><td>-1.3</td><td>-0.9</td><td>-0.4</td></tr>
<tr><td>Chicago Bears</td><td>11.4</td><td>1.6</td><td>9.9</td></tr>
<tr><td>Cincinnati Bengals</td><td>-2.4</td><td>1.7</td><td>-4.1</td></tr>
<tr><td>Cleveland Browns</td><td>-6.0</td><td>-3.1</td><td>-2.8</td></tr>
<tr><td>Dallas Cowboys</td><td>1.8</td><td>-0.1</td><td>2.0</td></tr>
<tr><td>Denver Broncos</td><td>10.2</td><td>10.5</td><td>-0.3</td></tr>
<tr><td>Detroit Lions</td><td>-0.5</td><td>-2.3</td><td>1.8</td></tr>
<tr><td>Green Bay Packers</td><td>7.9</td><td>0.9</td><td>7.0</td></tr>
<tr><td>Houston Texans</td><td>11.7</td><td>4.5</td><td>7.3</td></tr>
<tr><td>Indianapolis Colts</td><td>-4.6</td><td>-6.1</td><td>1.6</td></tr>
<tr><td>Jacksonville Jaguars</td><td>-12.3</td><td>-9.8</td><td>-2.5</td></tr>
<tr><td>Kansas City Chiefs</td><td>-13.3</td><td>-3.3</td><td>-10.0</td></tr>
<tr><td>Miami Dolphins</td><td>-4.2</td><td>-6.6</td><td>2.4</td></tr>
<tr><td>Minnesota Vikings</td><td>0.8</td><td>-1.7</td><td>2.5</td></tr>
<tr><td>New England Patriots</td><td>9.9</td><td>9.3</td><td>0.6</td></tr>
<tr><td>New Orleans Saints</td><td>-0.5</td><td>7.2</td><td>-7.6</td></tr>
<tr><td>New York Giants</td><td>5.0</td><td>4.0</td><td>1.1</td></tr>
<tr><td>New York Jets</td><td>-4.0</td><td>-4.7</td><td>0.8</td></tr>
<tr><td>Oakland Raiders</td><td>-11.3</td><td>-0.4</td><td>-10.9</td></tr>
<tr><td>Philadelphia Eagles</td><td>-6.4</td><td>-4.6</td><td>-1.7</td></tr>
<tr><td>Pittsburgh Steelers</td><td>-0.1</td><td>0.7</td><td>-0.8</td></tr>
<tr><td>San Diego Chargers</td><td>-1.7</td><td>2.5</td><td>-4.1</td></tr>
<tr><td>San Francisco 49ers</td><td>10.1</td><td>-1.8</td><td>12.0</td></tr>
<tr><td>Seattle Seahawks</td><td>5.9</td><td>-4.8</td><td>10.7</td></tr>
<tr><td>St. Louis Rams</td><td>-1.3</td><td>-6.0</td><td>4.8</td></tr>
<tr><td>Tampa Bay Buccaneers</td><td>3.2</td><td>7.2</td><td>-3.9</td></tr>
<tr><td>Tennessee Titans</td><td>-7.7</td><td>-0.8</td><td>-6.8</td></tr>
<tr><td>Washington Redskins</td><td>-1.5</td><td>4.1</td><td>-5.6</td></tr>
</tbody>
</table>

Vergleicht man die Werte mit denen von Pro-Football-Reference, so
erkennt man teilweise gravierende Unterschiede. Das kommt daher, dass
mein SRS nicht "gedeckelt" ist. Das heißt, wenn ein Team mit 40 Punkten
Vorsprung gewinnt, so fließt das auch so in den Algorithmus ein. Andere
Implementationen deckeln die Punktdifferenz, typischerweise ab etwa 21
Punkten.

Das führt schon im herkömmlichen SRS zu größeren Differenzen, aber bei
der Aufspaltung in Offense- und Defense-Komponenten verstärkt sich
dieser "Shootout-Effekt" deutlich. Das Verwenden einer künstlichen
Grenze macht in dem Zusammenhang sicher Sinn und ich werde das auch
demnächst implementieren.

Desweiteren scheint PFR sein SRS allerdings auch anderweitig verändert
zu haben. Denn [der Testdatensatz, den PFR im Blog zeigt][], passt
ziemlich gut mit meiner Implementierung überein. Aktuelle Werte hingegen
zeigen die beschriebenen teils dramatischen Abweichungen.

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

  [Simple Ranking System]: |filename|simple-ranking-system-einfach-aber-gut.md
    "Simple Ranking System – einfach aber gut"
  [Pro-Football-Reference Blog]: http://www.pro-football-reference.com/blog/?p=37
  [Brian Burkes]: http://www.advancednflstats.com
  [Football Outsiders]: http://www.footballoutsiders.com
  [der Testdatensatz, den PFR im Blog zeigt]: http://www.pro-football-reference.com/blog/?p=539
