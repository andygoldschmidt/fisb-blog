Title: Strength of schedule - Theorie und Praxis
Date: 2012-07-27 18:12
Author: footballissexbaby
Category: Footballmetrics
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
Ungeduldigen können direkt ans Ende des Artikels zu den Ergebnissen scrollen.)

**1. Die BCS-Methode:**

Diese Methode wurde verwendet, um im College Football festzulegen, wer
in den BCS Bowls spielt.

Diese Methode beruht auf der Anzahl von Siegen und Niederlagen. Für die
Berechnung der SOS eines Teams werden die Siege und Niederlagen der
Gegner (*opponents' record, OR*) sowie die Siege und Niederlagen der
Gegner der Gegner (opponents' opponents record, OOR) benutzt.

Die Strength of schedule berechnet sich dann zu zwei Dritteln aus OR und
einem Drittel OOR:

$\text{SOS} = \frac{2 \cdot \text{OR} +\text{OOR}}{3}$

**2. Die Average-Methode:**

Die Average-Methode benutzt im Gegensatz zur BCS-Methode nicht Siege und
Niederlagen, sondern die Punkte, die erzielt und erlaubt wurden. Aus
diesen Punktverhältnissen lassen sich nun [Ratings erstellen][].

Die Strength of schedule berechnet sich nun einfach als Durchschnitt der
gegnerischen Ratings:

$\text{SOS} = \frac{1}{N}\sum\limits_{i=0}\^N R(i)$

**3. Die "weighted average"-Methode:**

Diese Methode beruht ebenfalls auf den Ratings der gegnerischen
Mannschaften. Jedoch wird hier nicht direkt mit den Ratings gerechnet,
sondern mit den Quadratwurzeln der Ratings.

$\text{SOS} = \frac{1}{N}\sum\limits_{i=0}\^{N}
\sqrt{\frac{R(i)}{100}} \cdot 100$ 

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

[Die Ergebnisse:](#myTable)

Zum Abschluss noch eine Tabelle mit beiden SOS-Werten für die 2012er
Saison:

<table class="table table-striped">
<thead>
<tr>
<th>Team</th>
<th>BCS</th>
<th>Average</th>
</tr>
</thead>
<tbody>
<tr>
<td>Arizona Cardinals</td>
<td>0.511834</td>
<td>2.155008</td>
</tr>
<tr>
<td>Atlanta Falcons</td>
<td>0.497535</td>
<td>-0.792174</td>
</tr>
<tr>
<td>Baltimore Ravens</td>
<td>0.518738</td>
<td>0.041039</td>
</tr>
<tr>
<td>Buffalo Bills</td>
<td>0.467949</td>
<td>-1.484856</td>
</tr>
<tr>
<td>Carolina Panthers</td>
<td>0.5</td>
<td>-0.528739</td>
</tr>
<tr>
<td>Chicago Bears</td>
<td>0.481509</td>
<td>-0.377778</td>
</tr>
<tr>
<td>Cincinnati Bengals</td>
<td>0.491741</td>
<td>-0.948918</td>
</tr>
<tr>
<td>Cleveland Browns</td>
<td>0.496795</td>
<td>-1.265077</td>
</tr>
<tr>
<td>Dallas Cowboys</td>
<td>0.510108</td>
<td>1.085323</td>
</tr>
<tr>
<td>Denver Broncos</td>
<td>0.536982</td>
<td>0.855769</td>
</tr>
<tr>
<td>Detroit Lions</td>
<td>0.487919</td>
<td>-0.107826</td>
</tr>
<tr>
<td>Green Bay Packers</td>
<td>0.48681</td>
<td>-0.150614</td>
</tr>
<tr>
<td>Houston Texans</td>
<td>0.500247</td>
<td>0.306344</td>
</tr>
<tr>
<td>Indianapolis Colts</td>
<td>0.494576</td>
<td>0.424426</td>
</tr>
<tr>
<td>Jacksonville Jaguars</td>
<td>0.503821</td>
<td>0.684495</td>
</tr>
<tr>
<td>Kansas City Chiefs</td>
<td>0.493466</td>
<td>-1.118269</td>
</tr>
<tr>
<td>Miami Dolphins</td>
<td>0.48644</td>
<td>-1.122569</td>
</tr>
<tr>
<td>Minnesota Vikings</td>
<td>0.47966</td>
<td>-0.96899</td>
</tr>
<tr>
<td>New England Patriots</td>
<td>0.476701</td>
<td>-1.358013</td>
</tr>
<tr>
<td>New Orleans Saints</td>
<td>0.518861</td>
<td>-0.180823</td>
</tr>
<tr>
<td>New York Giants</td>
<td>0.547461</td>
<td>2.41262</td>
</tr>
<tr>
<td>New York Jets</td>
<td>0.490631</td>
<td>-0.302751</td>
</tr>
<tr>
<td>Oakland Raiders</td>
<td>0.50074</td>
<td>-0.596287</td>
</tr>
<tr>
<td>Philadelphia Eagles</td>
<td>0.51997</td>
<td>0.954901</td>
</tr>
<tr>
<td>Pittsburgh Steelers</td>
<td>0.500986</td>
<td>-0.965905</td>
</tr>
<tr>
<td>San Diego Chargers</td>
<td>0.519231</td>
<td>-0.687927</td>
</tr>
<tr>
<td>San Francisco 49ers</td>
<td>0.510725</td>
<td>1.709335</td>
</tr>
<tr>
<td>Seattle Seahawks</td>
<td>0.502342</td>
<td>1.314009</td>
</tr>
<tr>
<td>St. Louis Rams</td>
<td>0.500493</td>
<td>1.020126</td>
</tr>
<tr>
<td>Tampa Bay Buccaneers</td>
<td>0.475345</td>
<td>-1.244818</td>
</tr>
<tr>
<td>Tennessee Titans</td>
<td>0.501849</td>
<td>1.144271</td>
</tr>
<tr>
<td>Washington Redskins</td>
<td>0.488536</td>
<td>0.094671</td>
</tr>
</tbody>
</table>

  [Ratings erstellen]: |filename|hausgemachte-sport-rankings-nach-sagarin-art-teil-1.md
  [pythagoräischen Erwartung]: |filename|sag-mir-deine-punkte-und-ich-sag-dir-wie-oft-du-gewinnst.md
