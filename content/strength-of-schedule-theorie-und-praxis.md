Title: Strength of schedule - Theorie und Praxis
Date: 2012-07-27 18:12
Author: footballissexbaby
Tags: BCS, Football, Modelle..., NFL, Stats, Strength of schedule, Taktik, Zahlen
Slug: strength-of-schedule-theorie-und-praxis

Um in der NFL am Jahresende eine Siegbilanz einordnen zu können, ist es
unerlässlich ein Maß für die Stärke der  in dieser Saison gespielten
Gegner zu haben. Dieses Maß nennt man gemeinhin *Strength of
schedule*(SOS). Je stärker die Gegner waren, umso größer sollte der Wert
der SOS ein.

Mit der Strength of schedule ist es möglich, am Ende der Saison zu
sagen, wie schwer eine Spielplan für ein Team war, man kann aber genauso
gut herausfinden, wie schwer die Schedule für die nächste Saison sein
wird.

Für die Berechnung der SOS benutzt man üblicherweise eine der folgenden
drei Methoden:

1.  Bowl Championship Series Methode (**BCS**)
2.  Durchschnitt der gegnerischen Power Rankings (**average**)
3.  Durchschnitt der gewichteten gegnerischen Power Rankings (**weighted
    average**)

Im Folgenden möchte ich die drei Methoden kurz vorstellen. (Die
Ungeduldigen können [direkt zu den Ergebnissen für die Saison 2012
springen][].)

<span style="text-decoration: underline;">**1. Die BCS-Methode:**</span>

Diese Methode wurde verwendet, um im College Football festzulegen, wer
in den BCS Bowls spielt.

Diese Methode beruht auf der Anzahl von Siegen und Niederlagen. Für die
Berechnung der SOS eines Teams werden die Siege und Niederlagen der
Gegner (*opponents' record, OR*) sowie die Siege und Niederlagen der
Gegner der Gegner (opponents' opponents record, OOR) benutzt.

Die Strength of schedule berechnet sich dann zu zwei Dritteln aus OR und
einem Drittel OOR:

[latex]\\text{SOS} = \\frac{2 \\cdot \\text{OR} +\\text{OOR}}{3}[/latex]

**<span style="text-decoration: underline;">2. Die
Average-Methode:</span>**

Die Average-Methode benutzt im Gegensatz zur BCS-Methode nicht Siege und
Niederlagen, sondern die Punkte, die erzielt und erlaubt wurden. Aus
diesen Punktverhältnissen lassen sich nun [Ratings erstellen][].

Die Strength of schedule berechnet sich nun einfach als Durchschnitt der
gegnerischen Ratings:

[latex]\\text{SOS} = \\frac{1}{N}\\sum\\limits\_{i=0}\^N R(i)[/latex]

<span style="text-decoration: underline;">**3. Die "weighted
average"-Methode:**</span>

Diese Methode beruht ebenfalls auf den Ratings der gegnerischen
Mannschaften. Jedoch wird hier nicht direkt mit den Ratings gerechnet,
sondern mit den Quadratwurzeln der Ratings.

[latex]\\text{SOS} = \\frac{1}{N}\\sum\\limits\_{i=0}\^{N}
\\sqrt{\\frac{R(i)}{100}} \\cdot 100[/latex]

 

Es gibt also zwei grundlegende Methoden: siegbasiert und punktbasiert.

Der Vorteil der BCS-Methode ist, dass man theoretisch die SOS per Hand
berechnen kann, man addiert jeweils nur die Siege der Gegner und teilt
durch die Anzahl der Spiele und wiederholt das für jeden Gegner dieses
Gegners.

Hingegen ist man bei der Average-Methode von computergenerierten Ratings
abhängig. Dabei stellt sich dann die Frage, wie sehr man dieser
Berechnung vertraut. Die eigentliche Ermittlung der SOS dagegen ist
bestechend einfach.

Am Ende ist es wohl Geschmackssache, welche der beiden Methoden man
verwendet, BCS scheint mir verbreiteter zu sein. Jedoch sollte man immer
darauf achten, dass beide teils deutlich abweichende Werte liefern.

Und wie auch bei der [pythagoräischen Erwartung][] gilt: Eine Metrik
allein kann ein komplexes Spiel wie Football nie ausreichend
beschreiben.

Das nächste Update meines Footballmetrics-Moduls wird sowohl die
BCS-Methode als auch die Average-Methode beherrschen.

Zum Abschluss noch eine Tabelle mit beiden SOS-Werten für die 2012er
Saison:

  Team                   BCS        Average
  ---------------------- ---------- -----------
  Arizona Cardinals      0.511834   2.155008
  Atlanta Falcons        0.497535   -0.792174
  Baltimore Ravens       0.518738   0.041039
  Buffalo Bills          0.467949   -1.484856
  Carolina Panthers      0.5        -0.528739
  Chicago Bears          0.481509   -0.377778
  Cincinnati Bengals     0.491741   -0.948918
  Cleveland Browns       0.496795   -1.265077
  Dallas Cowboys         0.510108   1.085323
  Denver Broncos         0.536982   0.855769
  Detroit Lions          0.487919   -0.107826
  Green Bay Packers      0.48681    -0.150614
  Houston Texans         0.500247   0.306344
  Indianapolis Colts     0.494576   0.424426
  Jacksonville Jaguars   0.503821   0.684495
  Kansas City Chiefs     0.493466   -1.118269
  Miami Dolphins         0.48644    -1.122569
  Minnesota Vikings      0.47966    -0.96899
  New England Patriots   0.476701   -1.358013
  New Orleans Saints     0.518861   -0.180823
  New York Giants        0.547461   2.41262
  New York Jets          0.490631   -0.302751
  Oakland Raiders        0.50074    -0.596287
  Philadelphia Eagles    0.51997    0.954901
  Pittsburgh Steelers    0.500986   -0.965905
  San Diego Chargers     0.519231   -0.687927
  San Francisco 49ers    0.510725   1.709335
  Seattle Seahawks       0.502342   1.314009
  St. Louis Rams         0.500493   1.020126
  Tampa Bay Buccaneers   0.475345   -1.244818
  Tennessee Titans       0.501849   1.144271
  Washington Redskins    0.488536   0.094671

  [direkt zu den Ergebnissen für die Saison 2012 springen]: #myTable
  [Ratings erstellen]: http://footballissexbaby.de/wordpress/2011/05/hausgemachte-sport-rankings-nach-sagarin-art-teil-1/
    "Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 1"
  [pythagoräischen Erwartung]: http://footballissexbaby.de/wordpress/2011/10/sag-mir-deine-punkte-und-ich-sag-dir-wie-oft-du-gewinnst/
    "Sag’ mir deine Punkte und ich sag’ dir wie oft du gewinnst!"
