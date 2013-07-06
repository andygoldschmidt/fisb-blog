Title: GFL-Playoffs: Wer wird am Ende in Berlin jubeln?
Date: 2012-09-18 14:00
Author: footballissexbaby
Tags: Football, German Bowl, GFL, Modelle..., Playoffs, Ranking-Systeme, Siegwahrscheinlichkeit, Taktik, win probability, Zahlen
Slug: gfl-playoffs-wer-wird-am-ende-in-berlin-jubeln

In der German Football League stehen die Playoffs vor der Tür. Damit
wird es höchste Zeit, einen genaueren Blick darauf zu werfen, wer am 13.
Oktober in Berlin jubeln darf.

Dazu verlassen wir uns natürlich nicht auf irgendwelche Prognosen von
Experten, sondern auf knallharte Statistik! Vor einigen Wochen habe ich
ein [Maximum-Likelihood Ranking-System vorgestellt][], dass es sehr
einfach macht, Siegwahrscheinlichkeiten zu berechnen.

<div>
[caption id="attachment\_1259" align="alignright" width="300"][![][]][]
GFL-Playoff-Szenario. Quelle: [Facebook][][/caption]

</div>
Auf der nebenstehenden Graphik sieht man sehr übersichtlich, welche
Teams sich im Viertelfinale gegenüberstehen, wer im Halbfinale lauern
würde und auf welchen Gegner man erst im German Bowl treffen kann.

Mit diesem Wissen und den Ratings kann man nun die
Siegwahrscheinlichkeiten für jedes Team im Viertelfinale berechnen, dann
die Wahrscheinlichkeit, gegen jeden möglichen Gegner im Halbfinale zu
gewinnen etc.

Die Wahrscheinlichkeit den German Bowl zu gewinnen ist dann einfach das
Produkt aus der Siegwahrscheinlichkeit im Viertelfinale, der
Siegwahrscheinlichkeit im Halbfinale und der Siegwahrscheinlichkeit im
Finale.

(Wer neugierig ist und direkt zu den German
Bowl-Siegwahrscheinlichkeiten will, der [klickt hier][]. Und diejenigen,
die alle Wahrscheinlichkeiten sehen wollen, aber bloß keine Formeln, die
[klicken hier][].)

**Die Theorie**

Die Theorie ist wie oben erwähnt sehr einfach: man berechnet für jeden
möglichen Gegner die Siegwahrscheinlichkeit und gewichtet sie mit der
Wahrscheinlichkeit, mit der diese Partie stattfindet. Wir haben es also
mit [bedingten Wahrscheinlichkeiten][] zu tun. Klingt schlimmer als es
tatsächlich ist. Schauen wir uns zur Demonstration das Szenario der Kiel
Baltic Hurricanes an:

Im Viertelfinale empfangen die Hurricanes die Stuttgart Scorpions. Die
Wahrscheinlichkeit für das Auftreten dieses Ereignisses ist 100%. Die
Siegwahrscheinlichkeit lässt sich nach folgender Formel leicht
berechnen:

[latex size=1]P\_\\text{HF}(\\text{Hurricanes}) =
\\frac{R(\\text{Hurricanes})}{R(\\text{Hurricanes}) +
R(\\text{Scorpions})} = 0.84[/latex]

Das heißt, Kiel wird zu 84% ins Halbfinale einziehen. Mögliche Gegner
dort sind die Rhein-Neckar-Bandits oder die Dresden Monarchs. Dieses
Spiel geht laut Ranking-System zu 50.4% für die Rhein-Neckar-Bandits aus
und damit zu 49.6% für die Dresden Monarchs. Für Kiel bedeutet das also,
dass sie im Halbfinale zu 50.4% auf die Bandits und zu 49.6% auf die
Monarchs treffen. Demzufolge ergibt sich Kiels Wahrscheinlichkeit in den
German Bowl einzuziehen als:

[latex size=1]P\_\\text{F}(\\text{Hurricanes}) = 0.504 \\cdot
\\frac{R(\\text{Hurricanes})}{R(\\text{Hurricanes}) +
R(\\text{Bandits})} + 0.496 \\cdot
\\frac{R(\\text{Hurricanes})}{R(\\text{Hurricanes}) +
R(\\text{Monarchs})} [/latex]

Die Wahrscheinlichkeit eines Kieler Sieges ist in diesem Fall 75.1%.

Das heißt zu 84% Prozent ziehen die Canes ins Halbfinale ein, dass sie
wiederum zu 75.1% gewinnen. Die Wahrscheinlichkeit des German
Bowl-Einzugs ist also:

[latex]0.84 \\cdot 0.751 = 0.631 = 63.1\\%[/latex]

Das gleiche lässt sich für die vier möglichen Finalgegner genauso
weiterführen, aus Übersichtlichkeitsgründen verzichte ich aber darauf.

<a name="halbfinale">**Halbfinal-Einzug**</a>

Die Wahrscheinlichkeit eines Sieges für jedes Team im Viertelfinale
zeigt die folgende Tabelle:

  Team 1                     Team 2                Sieg Team 1   Sieg Team 2
  -------------------------- --------------------- ------------- -------------
  Kiel Baltic Hurricanes     Stuttgart Scorpions   84.0%         16.0%
  Rhein-Neckar Bandits       Dresden Monarchs      50.4%         49.6%
  Schwäbisch Hall Unicorns   Düsseldorf Panther    83.4%         16.6%
  Berlin Adler               Marburg Mercenaries   64.8%         35.2%

**Final-Einzug**

Jedes Team trifft auf eines von zwei möglichen Teams.
Einzelwahrscheinlichkeit bezieht sich hier auf die gewichtete
Siegwahrscheinlichkeit gegen beide Teams, die Gesamtwahrscheinlichkeit
ist das Produkt aus Siegwahrscheinlichkeit im Viertelfinale und
Halbfinale, also die Wahrscheinlichkeit den German Bowl zu erreichen.

<table>
<thead>
<tr>
<th>
Team

</th>
<th>
mögliche Gegner

</th>
<th>
Einzel-Wkt

</th>
<th>
Gesamt-Wkt

</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Kiel Baltic Hurricanes

</td>
<td>
-   Rhein-Neckar Bandits
-   Dresden Monarchs

</td>
<td>
75.1%

</td>
<td>
63.1%

</td>
</tr>
<tr>
<td>
Stuttgart Scorpions

</td>
<td>
-   Rhein-Neckar Bandits
-   Dresden Monarchs

</td>
<td>
36.5%

</td>
<td>
5.8%

</td>
</tr>
<tr>
<td>
Rhein-Neckar Bandits

</td>
<td>
-   Kiel Baltic Hurricanes
-   Stuttgart Scorpions

</td>
<td>
31.2%

</td>
<td>
15.7%

</td>
</tr>
<tr>
<td>
Dresden Monarchs

</td>
<td>
-   Kiel Baltic Hurricanes
-   Stuttgart Scorpions

</td>
<td>
30.9%

</td>
<td>
15.3%

</td>
</tr>
<tr>
<td>
Schwäbisch Hall Unicorns

</td>
<td>
-   Berlin Adler
-   Marburg Mercenaries

</td>
<td>
62.9%

</td>
<td>
52.5%

</td>
</tr>
<tr>
<td>
Düsseldorf Panther

</td>
<td>
-   Berlin Adler
-   Marburg Mercenaries

</td>
<td>
25.9%

</td>
<td>
4.3%

</td>
</tr>
<tr>
<td>
Berlin Adler

</td>
<td>
-   Schwäbisch Hall Unicorns
-   Düsseldorf Panther

</td>
<td>
48.0%

</td>
<td>
31.1%

</td>
</tr>
<tr>
<td>
Marburg Mercenaries

</td>
<td>
-   Schwäbisch Hall Unicorns
-   Düsseldorf Panther

</td>
<td>
34.6%

</td>
<td>
12.2%

</td>
</tr>
</tbody>
</table>
<a name="german-bowl">**German Bowl-Sieg**</a>

Kommen wir also zur entscheidenden Frage: **Wer ist der
wahrscheinlichste German Bowl-Sieger?**

  Team                       Einzel-Wkt.   Gesamt-Wkt.
  -------------------------- ------------- -------------
  Kiel Baltic Hurricanes     66.9%         **42.2%**
  Stuttgart Scorpions        29.0%         **1.7%**
  Rhein-Neckar Bandits       41.2%         **6.5%**
  Dresden Monarchs           40.9%         **6.3%**
  Schwäbisch Hall Unicorns   49.4%         **25.9%**
  Düsseldorf Panther         18.1%         **0.8%**
  Berlin Adler               42.1%         **13.1%**
  Marburg Mercenaries        29.3%         **3.6%**

Am Samstag gehen die Playoffs endlich los und werden sicher die ein oder
andere Überraschung bereithalten.

Auch wenn sich der Autor dieses Blogs eine *etwas* höhere
Wahrscheinlichkeit für ein gewisses Team aus der sächsischen
Landeshauptstadt gewünscht hätte, fiebere ich den Spielen entgegen und
freue mich auf die tollen Rückblicke, die uns [GFL TV][] sicher wieder
ermöglicht.

  [Maximum-Likelihood Ranking-System vorgestellt]: http://footballissexbaby.de/2012/08/yet-another-ranking-system/
    "Yet Another Ranking System"
  []: http://footballissexbaby.de/wp-content/uploads/2012/09/560405_10151166313622460_1376931964_n-300x300.jpg
    "GFL-Playoff-Szenario"
  [![][]]: http://footballissexbaby.de/wp-content/uploads/2012/09/560405_10151166313622460_1376931964_n.jpg
  [Facebook]: http://www.facebook.com/photo.php?fbid=10151166313622460&set=a.290885202459.147524.288799632459&type=1
  [klickt hier]: #german-bowl
  [klicken hier]: #halbfinale
  [bedingten Wahrscheinlichkeiten]: http://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit
  [GFL TV]: http://www.gfl-tv.de/
