Title: Time of Possession: irrelevant oder nützlich?
Date: 2013-09-14 20:00
Author: footballissexbaby
Category: Analyse
Tags: time of possession
Slug: time-of-possession-irrelevant-oder-nuetzlich


Jeder wird schonmal die farblichen Einblendungen bei Fox oder NBC gesehen haben, in denen drastische Unterschiede beim Ballbesitz, der *Time of Possession*, angezeigt werden. Jüngst so geschehen beim Spiel Dallas Cowboys gegen New York Giants im Sunday Night Football, in dem die Giants zur Halbzeit nicht mal 9 Minuten Ballbesitz hatten, die Cowboys logischerweise aber über 21 Minuten. Dennoch war das Spiel mit 13-10 noch recht eng. Am Spielende hatten die Cowboys über 37 Minuten den Ball und gewannen mit 5 Punkten Vorsprung.

Doch ist es wirklich so, dass ein Team viel Ballbesitz braucht, um ein Spiel zu gewinnen oder ist es wieder einmal nur eine dieser Pundit-Weisheiten?

## Time of Possession und Punktdifferenz

Um zu sehen, wie groß der Einfluss der Time of Possession auf das Spielergebnis ist, ist es am einfachsten eine Korrelation zwischen Ballbesitz des Heimteams und Punktedifferenz aus Sicht des Heimteams zu bilden. Dafür habe ich ein wundervolles Python-Modul namens [**nflgame**](https://github.com/BurntSushi/nflgame) bemüht, dass alle möglichen Team- und Spielerstatistiken sowie Play-by-Play-Daten einfach abrufbar macht.

Betrachtet man den Zeitraum von 2009 bis 2012, also insgesamt 1024 *Regular Season Games*, dann ergibt sich ein **Korrelationskoeffizient von 0.46**. Das ist kein sensationell guter Wert, aber immerhin besteht ein gewisser Zusammenhang zwischen Time of Possession und Punktdifferenz am Spielende. Dies zeigt auch eine Unterteilung in einzelne Saisons:

<table class="table table-striped">
<thead>
    <tr>
        <th>Jahr</th>
        <th>Korrelation</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>2009</td>
        <td>0.48</td>
    </tr>
    <tr>
        <td>2010</td>
        <td>0.51</td>
    </tr>
    <tr>
        <td>2011</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>2012</td>
        <td>0.43</td>
    </tr>
</tbody>
</table>

Der Zusammenhang zwischen Ballbesitz und Punktdifferenz ist relativ stabil auf einem nicht allzu hohem Level.
Schaut man sich das ganze graphisch an, wird es ebenfalls klar, dass es einen gewissen Zusammenhang zwischen Ballbesitz und Punktdifferenz gibt:

![](|filename|/images/top_vs_pt_diff.png)

Man sieht deutlich, dass ein Team mit größerem Ballbesitz am Ende in der Regel auch mit einem größeren Vorsprung gewinnen wird. Aber man erkennt eben auch, dass es eine ziemliche Streuung gibt: ein Team mit 35 Minuten Ballbesitz (2100 Sekunden) kann sowohl mit 25 Punkten Rückstand verlieren als auch mit 60 Punkten Vorsprung gewinnen.

## Punkte pro Drive zu Länge des Drives

Eine andere Möglichkeit, um die Wichtigkeit der Time of Possession einschätzen zu können, ist es die Länge eines Drives mit den Punkten pro Drive zu vergleichen. Das ist insofern verschieden von der vorherigen Betrachtung als das sich die erstere Analyse auf das Endergebnis des Spiels bezogen hat, diese Auswertung allerdings lediglich die Effizienz pro Drive bewertet. Die dazu benötigten Daten gibt es beispielsweise auf [Football Outsiders](http://www.footballoutsiders.com/stats/drivestats).

### Offense

Für die Offense ist der **Korrelationskoeffizient zwischen Points per Drive und Time of Possession per Drive 0.54**. (Ich habe hier nur die Saison 2012 betrachtet, daher sollte man diesen Wert mit Vorsicht genießen, siehe auch unten.) Auch hier gilt also wieder: *je länger ein Team den Ball hat, umso mehr Punkte macht es auch*.

Auch hier hilft eine Graphik, um den Zusammenhang deutlicher zu machen:

![](|filename|/images/top_vs_pts_per_drive_off.png)

Wie schon bei der ersten Graphik gilt auch hier: **viel Rauschen**. Lässt man die extremsten Werte auf der linken und rechten Seite weg, so hat man eine schöne "Wolke", also das Gegenteil einer Linie, die man bei hoher Korrelation erwarten würde. Das heißt konkret: egal, wie lange ein Drive dauert, die Punktausbeute ist fast unabhängig davon. Lediglich die niedrigen und höchsten Werte sorgen für eine gewisse Korrelation.

### Defense

Für die Defense ergibt sich eine etwas geringere Korrelation als für die Offense, **der Korrelationskoeffizient ist hier 0.49**. Zwar gilt auch hier der erwartete Zusammenhang *kürzerer Drive gleich weniger Punkte*, aber auch hier ist es so, dass mit größerer Time of Possession die Aussagekraft gänzlich verschwindet. Die folgende Graphik macht das besonders deutlich:

![](|filename|/images/top_vs_pts_per_drive_def.png)

## Fazit

Man kann nicht abstreiten, dass es einen gewissen Zusammenhang zwischen Ballbesitz und Erfolg gibt; der gesunde Menschenverstand lässt das auch schon vermuten.

Allerdings ist es wie gesehen bei weitem nicht zwingend, viel Ballbesitz zu haben, um zu gewinnen. Auch das ist bei etwas genauerem Überlegen nicht sonderlich verwunderlich. Teams wie die New Orleans Saints finden sich mit der Länge ihrer Drives im hinteren Mittelfeld, sind aber dennoch durch ihre explosive (Pass-)Offense extrem gefährlich. Es gibt viele Teams in der NFL, die nicht lange brauchen, um Punkte aufs Scoreboard zu bringen. Genauso gibt es natürlich auch viele Teams, die das Feld schnell wieder räumen müssen, ohne zu punkten.

Diese Ähnlichkeit in der Dauer der Drives bei einer komplett unterschiedlichen Punktausbeute ist der Grund dafür, warum man der Time of Possession keinen allzu großen Wert zumessen sollte. Es scheint eher so zu sein, dass erfolgreiche Teams größeren Ballbesitz haben, als das Teams mit großem Ballbesitz mehr Erfolg haben. Korrelation und Kausalität sind zwei Dinge, die man dringend auseinanderhalten muss. Doch da es sehr schwer ist Kausalitäten nachzuweisen, begnüge ich mich hier mit der Erkenntnis, das die Time of Possession nicht sonderlich aussagekräftig ist.
