Title: PPA: Wie gut ist eine Offense?
Date: 2013-01-15 16:02
Author: footballissexbaby
Category: Footballmetrics
Tags: DVOA, EPA, Football, NFL, PPA
Slug: ppa-wie-gut-ist-eine-offense

Es gibt sehr fortgeschrittene Metriken, die in der Lage sind jedem
einzelnen Play einen Wert für zu erwartende Punkte und
Siegwahrscheinlichkeit zuzuweisen, beispielsweise EPA oder DVOA.  
Summiert man hierbei alle einzelnen Plays auf, so bekommt man einen
Wert dafür, wie viele Punkte ein bestimmter Spieler oder eine ganze
Offense "hinzugefügt" haben.

Allerdings kann man diese Metriken nicht mal eben so selbst berechnen,
da es notwendig ist, zur Berechnung Play-by-Play-Daten zu analysieren
und ein sehr ausgereiftes Modell zu haben, dass in der Lage ist aus
diesen Daten EPA, WPA oder DVOA zu berechnen.

Interessiert man sich nicht so sehr für einzelne Spieler, sondern Teams
und nicht so sehr für einzelne Plays, sondern ganze Spiele, dann ist es
möglich mit wesentlich einfacheren Indikatoren Vorhersagen darüber zu
machen, [wer ein Spiel gewinnen sollte][].

Um abzuschätzen, wie effektiv aber eine Offense oder eine Defense ist,
ist es nicht immer sinnvoll in Siegen zu denken, sondern vielmehr in
Punkten.

Die Idee ist simpel: man nimmt die Punkte, die ein Team pro Spiel
gemacht hat und versucht die Parameter zu finden, die diese Punktzahl am
besten nachbilden. Man führt also eine lineare Regression durch.

Das schwierigste an dieser Aufgabe ist es, Parameter zu finden, die
signifikant sind und alle unabhängig voneinander sind. Hat man die
entsprechenden Prediktoren gefunden, kann man ganz einfach sagen,
wieviele Punkte ein Team hätte erreichen *sollen*.

Und da jede Metrik auch einen Namen haben sollte, habe ich diese **PPA**
getauft: **P**rojected **P**oints over **A**verage.

Wie der Name schon sagt, bezieht sich diese Metrik auf den Durchschnitt
aller Teams, das heißt der Mittelwert von PPA ist 0.

Die folgende Tabelle zeigt, welche Parameter in PPA einfließen:

<table class="table">
<thead>
<tr><th>Statistik</th><th>Koeffizient</th><th>Z score</th></tr>
</thead>
<tbody>
<tr><td>Net Yards per Pass Attempt</td><td>4.10</td><td>15.97</td></tr>
<tr><td>Interception rate</td><td>-52.61</td><td>-2.28</td></tr>
<tr><td>Rush Yards per Attempt</td><td>1.48</td><td>3.13</td></tr>
<tr><td>Fumble Rate</td><td>-143.49</td><td>-2.67</td></tr>
</tbody>
</table>

Die Signifikanz für alle Prediktoren ist größer als 95%.

Man sieht sehr schnell, dass der wichtigste Parameter einer Offense die
Net Yards per Pass Attempt sind. Also die Differenz von Pass-Yards und
Sack-Yards geteilt durch die Summe aus Passversuchen und Sacks. Wenig
überraschend ist auch, dass ein Fumble in etwa eine genauso große
negative Auswirkung hat, wie eine Interception (bei gleich vielen Lauf-
und Passversuchen).

Die folgende Tabelle zeigt das PPA für jedes Team in der regulären
Saison 2012.

<table class="table table-striped">
<thead>
<tr><th>Team</th><th>PPA</th></tr>
</thead>
<tbody>
<tr><td>Arizona Cardinals</td><td>-9.2</td></tr>
<tr><td>Atlanta Falcons</td><td>3.4</td></tr>
<tr><td>Baltimore Ravens</td><td>1.4</td></tr>
<tr><td>Buffalo Bills</td><td>-1.3</td></tr>
<tr><td>Carolina Panthers</td><td>3.6</td></tr>
<tr><td>Chicago Bears</td><td>-2.3</td></tr>
<tr><td>Cincinnati Bengals</td><td>-1.0</td></tr>
<tr><td>Cleveland Browns</td><td>-2.5</td></tr>
<tr><td>Dallas Cowboys</td><td>1.2</td></tr>
<tr><td>Denver Broncos</td><td>4.1</td></tr>
<tr><td>Detroit Lions</td><td>0.1</td></tr>
<tr><td>Green Bay Packers</td><td>2.0</td></tr>
<tr><td>Houston Texans</td><td>2.5</td></tr>
<tr><td>Indianapolis Colts</td><td>-0.7</td></tr>
<tr><td>Jacksonville Jaguars</td><td>-4.1</td></tr>
<tr><td>Kansas City Chiefs</td><td>-4.9</td></tr>
<tr><td>Miami Dolphins</td><td>-2.1</td></tr>
<tr><td>Minnesota Vikings</td><td>-2.2</td></tr>
<tr><td>New England Patriots</td><td>4.3</td></tr>
<tr><td>New Orleans Saints</td><td>4.7</td></tr>
<tr><td>New York Giants</td><td>3.3</td></tr>
<tr><td>New York Jets</td><td>-5.8</td></tr>
<tr><td>Oakland Raiders</td><td>-0.7</td></tr>
<tr><td>Philadelphia Eagles</td><td>-3.2</td></tr>
<tr><td>Pittsburgh Steelers</td><td>-1.6</td></tr>
<tr><td>San Diego Chargers</td><td>-3.5</td></tr>
<tr><td>San Francisco 49ers</td><td>4.6</td></tr>
<tr><td>Seattle Seahawks</td><td>3.9</td></tr>
<tr><td>St. Louis Rams</td><td>-0.7</td></tr>
<tr><td>Tampa Bay Buccaneers</td><td>2.6</td></tr>
<tr><td>Tennessee Titans</td><td>-2.4</td></tr>
<tr><td>Washington Redskins</td><td>6.4</td></tr>
</tbody>
</table>

Das Top-Team sind also in dieser Metrik die Washington Redskins. Ihr PPA
von 6.4 bedeutet, dass sie pro Spiel mit ihrer Offense 6.4 projizierte
Punkte mehr machen als das durchschnittliche NFL-Team. Das
durchschnittliche Team trifft ziemlich genau auf die Detroit Lions zu.
(*Projizierte Punkte sind hierbei die Anzahl an Punkten, die gemäß den
Regressionskoeffizienten vorausgesagt werden.*)

Wenig überraschend sind die Cardinals mit Abstand das schlechteste Team.
Kein Wunder, sieht man sich ihr miserables Passing Game und ihr
durchschnittliches Laufspiel an. Die Cards haben pro Spiel fast 10
Punkte weniger gemacht als der Durchschnitt.

Doch das ist noch nicht alles, was man mit dieser Metrik machen kann.
Lineare Regressionen haben die nette Eigenschaft, dass man die
Prediktoren auch einzeln verwenden kann. Das führt dazu, dass man PPA
sehr einfach in zwei Untermetriken aufspalten kann: ein Pass-PPA, in das
NY/A und Interception Rate einfließt und ein Rush-PPA, das durch Rush
Y/A und Fumble Rate bestimmt wird.

Diese Eigenschaft von PPA war auch die eigentliche Hauptmotivation,
diese Metrik zu entwickeln. Deshalb gibt es hierzu mehr in einem
separaten Post.

Doch auch PPA ist natürlich nicht fehlerfrei. Ein erster großer
Schwachpunkt ist es, dass es recht aufwändig ist Daten zu finden,
wieviele Punkte eine Offense erzielt hat und nicht ein Team. Das heißt
mein Modell versucht auch Special Teams-Touchdowns und
Defense-Touchdowns anzupassen.

Darüber hinaus ist es nicht optimal die Laufyards pro Versuch als
Parameter zu benutzen. Der Grund ist recht einfach: ein 1-Yard-Lauf kann
genauso wichtig sein wie ein 8-Yard-Lauf. Daher gibt es Statistiken die
gemeinhin als *Success Rate* bezeichnet werden. Demnach gilt ein Lauf
als Erfolg, wenn er 50% der zum First Down nötigen Yards einbringt,
beziehungsweise bei Short Yardage-Situationen wenn ein First Down
erzielt wird.

Um die Success Rate allerdings zu berechnen bedarf es mehr als des
einfachen Spielberichtsbogens, man muss in die Play-by-Play-Daten
abtauchen und das ist dann mehr oder weniger aufwändig.

Doch bei PPA ging es mir nicht so sehr darum eine möglichst perfekte,
hochoptimierte Metrik zu erstellen, sondern ein einfaches Maß dafür, wie
gut eine Offense war.

Zum Abschluss und schonmal als Einstimmung auf das kommende Conference
Championship-Wochenende die 4 Playoff-Teams einzeln herausgestellt:

<table class="table">
<thead>
<tr><th>Team</th><th>PPA</th><th>Rang</th></tr>
</thead>
<tbody>
<tr><td>Atlanta Falcons</td><td>3.4</td><td>8</td></tr>
<tr><td>Baltimore Ravens</td><td>1.4</td><td>13</td></tr>
<tr><td>New England Patriots</td><td>4.3</td><td>4</td></tr>
<tr><td>San Francisco 49ers</td><td>4.6</td><td>3</td></tr>
</tbody>
</table>

  [wer ein Spiel gewinnen sollte]: http://www.advancednflstats.com/2007/07/what-makes-teams-win-part-1.html
