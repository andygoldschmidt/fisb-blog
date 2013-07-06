Title: Offenses und Defenses bewerten mit dem Simple Ranking System
Date: 2012-11-14 08:30
Author: footballissexbaby
Tags: Doug Drinen, DSRS, Football, NFL, OSRS, Pro-Football-Reference, Simple Ranking System, SRS
Slug: offenses-und-defenses-bewerten-mit-dem-simple-ranking-system

Das [Simple Ranking System][] wird in diesem Blog regelmäßig im
Zusammenhang mit der [Review auf den letzten NFL-Spieltag][] benutzt.

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

[latex]\\text{SRS(X)} = \\text{MoV(X)} + \\frac{1}{\\text{N}}\\left(
\\text{SRS(A)} + \\text{SRS(B)} + ...\\right)[/latex]

Dabei ist MoV die durchschnittliche Punktdifferenz, N die Anzahl
bisheriger Spiele und SRS(A), SRS(B), ... die Rankings der Gegner.  
Das Offense SRS (OSRS) bekommt man nun indem man die Formel leicht
anpasst:

[latex]\\text{OSRS(X)} = \\text{PF(X)} + \\frac{1}{\\text{N}}\\left(
\\text{PA(A)} + \\text{PA(B)} + ...\\right)[/latex]

Hier sind PF die erzielten Punkte und PA die zugelassenen Punkte. Das
DSRS bekommt man, indem man PF und PA in der Formel einfach vertauscht.

Diese Ratings haben eine nette Eigenschaft, denn es gilt:

[latex]\\text{SRS} = \\text{OSRS} + \\text{DSRS}[/latex]

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

  Team                   SRS     OSRS   DSRS
  ---------------------- ------- ------ -------
  Arizona Cardinals      -1.5    -8.6   7.2
  Atlanta Falcons        5.5     6.1    -0.6
  Baltimore Ravens       4.0     5.3    -1.3
  Buffalo Bills          -7.2    0.5    -7.7
  Carolina Panthers      -1.3    -0.9   -0.4
  Chicago Bears          11.4    1.6    9.9
  Cincinnati Bengals     -2.4    1.7    -4.1
  Cleveland Browns       -6.0    -3.1   -2.8
  Dallas Cowboys         1.8     -0.1   2.0
  Denver Broncos         10.2    10.5   -0.3
  Detroit Lions          -0.5    -2.3   1.8
  Green Bay Packers      7.9     0.9    7.0
  Houston Texans         11.7    4.5    7.3
  Indianapolis Colts     -4.6    -6.1   1.6
  Jacksonville Jaguars   -12.3   -9.8   -2.5
  Kansas City Chiefs     -13.3   -3.3   -10.0
  Miami Dolphins         -4.2    -6.6   2.4
  Minnesota Vikings      0.8     -1.7   2.5
  New England Patriots   9.9     9.3    0.6
  New Orleans Saints     -0.5    7.2    -7.6
  New York Giants        5.0     4.0    1.1
  New York Jets          -4.0    -4.7   0.8
  Oakland Raiders        -11.3   -0.4   -10.9
  Philadelphia Eagles    -6.4    -4.6   -1.7
  Pittsburgh Steelers    -0.1    0.7    -0.8
  San Diego Chargers     -1.7    2.5    -4.1
  San Francisco 49ers    10.1    -1.8   12.0
  Seattle Seahawks       5.9     -4.8   10.7
  St. Louis Rams         -1.3    -6.0   4.8
  Tampa Bay Buccaneers   3.2     7.2    -3.9
  Tennessee Titans       -7.7    -0.8   -6.8
  Washington Redskins    -1.5    4.1    -5.6

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

  [Simple Ranking System]: http://footballissexbaby.de/2012/09/simple-ranking-system-einfach-aber-gut/
    "Simple Ranking System – einfach aber gut"
  [Review auf den letzten NFL-Spieltag]: http://footballissexbaby.de/category/preview-review/
  [Pro-Football-Reference Blog]: http://www.pro-football-reference.com/blog/?p=37
  [Brian Burkes]: http://www.advancednflstats.com
  [Football Outsiders]: http://www.footballoutsiders.com
  [der Testdatensatz, den PFR im Blog zeigt]: http://www.pro-football-reference.com/blog/?p=539
