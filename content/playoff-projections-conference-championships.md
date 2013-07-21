Title: Playoff Projections: Conference Championships
Date: 2013-01-17 15:00
Author: footballissexbaby
Tags: Conference Championship, Football, NFL, Playoff Projections, Playoffs
Slug: playoff-projections-conference-championships

Letzte Runde der Playoff Projections. Noch vier Teams sind im Rennen um
den Super Bowl. Nachfolgend gibt es die Wahrscheinlichkeiten jedes Teams
in den Playoffs zu gewinnen.

Im Vergleich zu den letzten beiden Woche veröffentliche ich diese Woche
sowohl die Wahrscheinlichkeiten aus dem Max-L Ranking (wie schon in den
letzten Wochen) und zusätzlich die Wahrscheinlichkeiten aus dem
FISB-Ranking.

Ich war in den letzten Wochen mit dem Max-L Ranking nicht sonderlich
zufrieden, die Berechnung auf Grundlage von Siegen ist nicht immer
optimal. Dagegen neigen die Wahrscheinlichkeiten im FISB-Ranking schnell
zu Extremen, so dass Siegwahrscheinlichkeiten \>90% keine Seltenheit
sind. Grund hierfür ist die logistische Regression, die dem ganzen zu
Grunde liegt und die ab einer gewissen Ranking-Differenz gegen 0
beziehungsweise 1 geht.

### Max-L

<table class="table">
  <thead>
    <tr>
      <th>Team</th>
      <th>Conf Win</th>
      <th>SB Win</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atlanta Falcons</td>
      <td>55.5%</td>
      <td>30.6%</td>
    </tr>
    <tr>
      <td>Baltimore Ravens</td>
      <td>34.6%</td>
      <td>12.5%</td>
    </tr>
    <tr>
      <td>New England Patriots</td>
      <td>65.4%</td>
      <td>34.7%</td>
    </tr>
    <tr>
      <td>San Francisco 49ers</td>
      <td>44.5%</td>
      <td>22.2%</td>
    </tr>
  </tbody>
</table>

### FISB

<table class="table">
  <thead>
    <tr>
      <th>Team</th>
      <th>Conf Win</th>
      <th>SB Win</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Atlanta Falcons</td>
      <td>47.2%</td>
      <td>20.0%</td>
    </tr>
    <tr>
      <td>Baltimore Ravens</td>
      <td>10.8%</td>
      <td>2.1%</td>
    </tr>
    <tr>
      <td>New England Patriots</td>
      <td>89.2%</td>
      <td>48.9%</td>
    </tr>
    <tr>
      <td>San Francisco 49ers</td>
      <td>52.8%</td>
      <td>29.1%</td>
    </tr>
  </tbody>
</table>

Als dringendes Todo für die Offseason ist auf jeden Fall eine bessere
und verlässlichere Berechnung von Siegwahrscheinlichkeiten vermerkt.
