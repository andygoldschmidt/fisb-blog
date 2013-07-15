Title: DVOA gegen Koko, den Affen
Date: 2012-07-26 14:00
Author: footballissexbaby
Tags: Aaron Schatz, Football, Football Outsiders, NFL, Pythagorean expectation, Ranking-Systeme
Slug: dvoa-gegen-koko-den-affen

In meinem [letzten Artikel][] habe ich mich ein wenig mit der
Vorhersagekraft der pythagoräischen Erwartung beschäftigt und gezeigt,
dass man zwar keine Vorhersagen ableiten kann, aber es dennoch eine
gewisse Korrelation zwischen Siegbilanz und pythagoräischer Erwartung am
Ende der letzten Saison gibt.

In den Kommentaren zu dem Artikel hat [korsakoff][] auf einen sehr
interessanten Artikel von Brian Burke verwiesen, der hier zu finden ist:

<http://www.advancednflstats.com/2010/07/pre-season-predictions-are-still.html>

Darin vergleicht er die Vorhersagegenauigkeit von [Football
Outsiders][]' Defense-adjusted value over average ([DVOA][]) mit 2
simplen Vergleichsmetriken:

1.  **CoMA** (Constant Median Approximation): Alle Teams haben exakt 8
    Siege. Das entspricht der Annahme, dass man gar nichts über die NFL
    weiß, außer das eine Saison 16 Spiele umfasst.
2.  **Koko the monkey**: Die Anzahl der Siege ist einfach festgelegt als 6 +
    (Anzahl der Siege im Vorjahr) / 4.

Ich habe überdies noch die pythagoräische Erwartung am Ende der
Vorjahres-Saison als weiteren Prediktor herangezogen.

Als Vergleichsgröße benutzt Burke den *root mean squared error* (RMS)
und den *mean absolute error* (MAE), die Berechnung wird in Brian's
Artikel beschrieben.

Hier noch einmal die Ergebnisse für die 2009er Saison zusammengefasst:

<table class="table">
<thead>
<tr>
<th>
Metrik

</th>
<th>
MAE

</th>
<th>
RMS

</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Football Outsiders

</td>
<td>
2.6

</td>
<td>
3.0

</td>
</tr>
<tr>
<td>
CoMA

</td>
<td>
2.5

</td>
<td>
3.1

</td>
</tr>
<tr>
<td>
Koko

</td>
<td>
2.2

</td>
<td>
2.8

</td>
</tr>
<tr>
<td>
Pythagorean

</td>
<td>
2.2

</td>
<td>
2.7

</td>
</tr>
</tbody>
<caption align="bottom">
2009 Season

</caption>
</table>
Die Projektionen von Football Outsiders sind also schlechter als die
"Vorhersage", die man ohne jegliches Wissen getroffen hat (CoMA); wie
Brian Burke darlegt, ist man dadurch also nicht klüger, sondern sogar
dümmer als zuvor. Doch laut [FO-Chef Aaron Schatz][] war die 2009er
Saison ein schwieriges Jahr für Voraussagen. Schauen wir uns also an,
wie Football Outsiders in den Saisons 2010 und 2011 abgeschnitten hat:

<table class="table">
<thead>
<tr>
<th>
Metrik

</th>
<th>
MAE

</th>
<th>
RMS

</th>
</tr>
</thead>
<tbody>
<tr>
<td>
[Football Outsiders][1]

</td>
<td>
1.9

</td>
<td>
2.2

</td>
</tr>
<tr>
<td>
CoMA

</td>
<td>
2.6

</td>
<td>
2.9

</td>
</tr>
<tr>
<td>
Koko

</td>
<td>
2.4

</td>
<td>
2.9

</td>
</tr>
<tr>
<td>
Pythagorean

</td>
<td>
2.8

</td>
<td>
3.4

</td>
</tr>
</tbody>
<caption align="bottom">
2010 Season

</caption>
</table>
<table class="table">
<thead>
<tr>
<th>
Metrik

</th>
<th>
MAE

</th>
<th>
RMS

</th>
</tr>
</thead>
<tbody>
<tr>
<td>
[Football Outsiders][2]

</td>
<td>
2.5

</td>
<td>
3.0

</td>
</tr>
<tr>
<td>
CoMA

</td>
<td>
2.4

</td>
<td>
3.2

</td>
</tr>
<tr>
<td>
Koko

</td>
<td>
2.4

</td>
<td>
3.0

</td>
</tr>
<tr>
<td>
Pythagorean

</td>
<td>
2.3

</td>
<td>
2.9

</td>
</tr>
</tbody>
<caption align="bottom">
2011 Season

</caption>
</table>
2010 hat Football Outsiders den Nagel also voll auf den Kopf getroffen
und deutlich besser abgeschnitten als jede der drei anderen Metriken,
die pythagoräische Erwartung schneidet sogar deutlich schlechter ab als
CoMA und Koko.

2011 zeigt sich jedoch wieder ein ähnliches Bild wie bereits 2009. Auch
ohne etwas über Football zu wissen, kann man die Standings am Ende der
Saison genauso gut vorhersagen, wie FO mit ihrer umworbenen DVOA-Metrik.

Man sieht also schnell, was auch intuitiv recht schnell klar ist: man
kann eine Football-Saison einfach nicht zuverlässig vorhersagen. Zuviel
hängt von Veränderungen in der Offseason (Free Agency-Zugänge, Draft,
Trainerwechsel), von Verletzungen und nicht zuletzt auch von Glück ab.

Jedoch sieht man auch, dass man sich zweimal überlegen sollte, ob man
für Statistiken wie DVOA wirklich Geld ausgeben möchte oder man sich
doch mit den vielen großartigen Statheads, wie z.B. [Brian Burke][],
[David Myers][] oder [Keith Goldner][] zufrieden geben möchte, die seit
Jahren grandiose Arbeit leisten, sie kostenfrei und oftmals auch offen
zur Verfügung stellen.

  [letzten Artikel]: |filename|die-vorhersagekraft-der-pythagoraischen-erwartung.md
    "Die Vorhersagekraft der pythagoräischen Erwartung"
  [korsakoff]: http://sidelinereporter.wordpress.com
  [Football Outsiders]: http://www.footballoutsiders.com
  [DVOA]: http://en.wikipedia.org/wiki/Football_Outsiders#Key_Metrics
  [FO-Chef Aaron Schatz]: http://www.footballoutsiders.com/stat-analysis/2010/oddities-2009
  [1]: http://www.footballoutsiders.com/dvoa-ratings/2010/2010-dvoa-projections
  [2]: http://www.footballoutsiders.com/dvoa-ratings/2011/2011-dvoa-projections
  [Brian Burke]: http://www.advancednflstats.com
  [David Myers]: http://codeandfootball.wordpress.com
  [Keith Goldner]: http://www.drivebyfootball.com/
