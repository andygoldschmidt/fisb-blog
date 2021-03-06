Title: PPA: Die Effizienz des Pass- und Laufspiels
Date: 2013-01-16 16:08
Author: footballissexbaby
Tags: Football, NFL, PPA
Slug: ppa-die-effizienz-des-lauf-und-des-passspiels

In meinem [ersten Artikel zu PPA][] habe ich gezeigt, wie man mit vier
Parametern eine Metrik konstruieren kann, mit der man die Qualität einer
Offense messen kann.

Der PPA-Wert gibt dabei an, wieviele projizierte Punkte ein Team
gegenüber dem Ligadurchschnitt gemacht (oder nicht gemacht) hat.
Projizierte Punkte sind hier nicht gleich die echten Punkte, sondern
vielmehr der Wert, der sich anhand der Regressionskoeffizienten ergibt.

Ich hatte im ersten Artikel schon angesprochen, dass es möglich ist, bei
linearen Regressionen die einzelnen Parameter zu separieren. Das heißt
in diesem Fall, man kann die Koeffizienten sehr einfach in ein Pass-PPA
und ein Rush-PPA aufteilen.

Hier kommt erst die eigentliche Stärke von PPA ins Spiel. Denn es ist
natürlich nicht übermäßig aussagekräftig zu berechnen, wieviele Punkte
eine Offense gemacht hat. Schließlich kann man das im Box-Score
nachlesen. Es ist aber sehr wohl interessant zu wissen, wieviele Punkte
man dem Passspiel und wie viele dem Laufspiel zuschreiben kann.

Das ist eine Aufgabe, die man allein mit dem Box-Score nicht
bewerkstelligen kann. Beispielsweise kann ein Team fast ausschließlich
auf den Pass setzen, aber macht die Touchdowns ausschließlich durch
kurze Laufspielzüge. Das heißt nicht, dass das Laufspiel für den Erfolg
der Offense zuständig ist, vielmehr hat der Erfolg des Passspiels in
diesem Szenario dazu geführt, dass man überhaupt erst in die Situation
kommen konnte mit dem Laufspiel zu punkten.

Es ist sehr einfach, die Aufteilung in Pass und Lauf durchzuführen. Mit
Hilfe der bereits im ersten Artikel vorgestellten Koeffizienten ergeben
sich folgende Gleichungen:

Pass:  
$\text{passPPA} = 4.1 \cdot \text{NY/A} - 52.61 \cdot \text{Int/A}$

Lauf:  
$\text{rushPPA} = 1.48 \cdot \text{RushYd/A} - 143.49 \cdot \text{FL/A}$

Man sieht allerdings gleich ein Problem, die beide Gleichungen haben.
Verliert ein Team kein Fumble, beziehungsweise wirft ein Team keine
Interception, dann wird die Metrik allein durch die Yards pro Versuch
bestimmt. Das ist ein generelles Problem mit Interceptions und vor allem
mit Fumbles. Interceptions treten noch einigermaßen gleichmäßig auf,
aber verlorene Fumbles sind sehr vereinzelte Ereignisse.

Das heißt, die Metriken machen für ein einzelnes Spiel nur bedingt Sinn,
sind aber nützlich, wenn es darum geht eine Offense über mehrere Spiele
oder eine ganze Saison zu bewerten.

Doch wie bereits im ersten Artikel zu PPA geschrieben, geht es hier
nicht um eine unglaublich ausgereifte, hochoptimierte Metrik, sondern
darum mit möglichst einfachen Parametern ein sinnvolles Bild von der
Stärke einer Offense zu bekommen.

Und das diese Metrik ganz brauchbare und vor allem nachvollziehbare
Werte liefert, zeigt die folgende Tabelle:

<table class="table table-striped1">
<thead>
<tr><th>Team</th><th>PassPPA</th><th>RushPPA</th></tr>
</thead>
<tbody>
<tr><td>Arizona Cardinals</td><td>-7.6</td><td>-1.6</td></tr>
<tr><td>Atlanta Falcons</td><td>3.3</td><td>0.1</td></tr>
<tr><td>Baltimore Ravens</td><td>0.6</td><td>0.9</td></tr>
<tr><td>Buffalo Bills</td><td>-1.4</td><td>0.1</td></tr>
<tr><td>Carolina Panthers</td><td>3.2</td><td>0.4</td></tr>
<tr><td>Chicago Bears</td><td>-2.6</td><td>0.2</td></tr>
<tr><td>Cincinnati Bengals</td><td>-0.8</td><td>-0.2</td></tr>
<tr><td>Cleveland Browns</td><td>-2.5</td><td>-0.0</td></tr>
<tr><td>Dallas Cowboys</td><td>2.1</td><td>-0.9</td></tr>
<tr><td>Denver Broncos</td><td>5.1</td><td>-1.0</td></tr>
<tr><td>Detroit Lions</td><td>0.8</td><td>-0.7</td></tr>
<tr><td>Green Bay Packers</td><td>2.1</td><td>-0.1</td></tr>
<tr><td>Houston Texans</td><td>1.6</td><td>0.9</td></tr>
<tr><td>Indianapolis Colts</td><td>-0.3</td><td>-0.4</td></tr>
<tr><td>Jacksonville Jaguars</td><td>-3.6</td><td>-0.5</td></tr>
<tr><td>Kansas City Chiefs</td><td>-4.7</td><td>-0.2</td></tr>
<tr><td>Miami Dolphins</td><td>-1.4</td><td>-0.7</td></tr>
<tr><td>Minnesota Vikings</td><td>-3.8</td><td>1.6</td></tr>
<tr><td>New England Patriots</td><td>3.7</td><td>0.6</td></tr>
<tr><td>New Orleans Saints</td><td>3.8</td><td>0.9</td></tr>
<tr><td>New York Giants</td><td>2.2</td><td>1.1</td></tr>
<tr><td>New York Jets</td><td>-4.1</td><td>-1.7</td></tr>
<tr><td>Oakland Raiders</td><td>-0.1</td><td>-0.6</td></tr>
<tr><td>Philadelphia Eagles</td><td>-2.1</td><td>-1.1</td></tr>
<tr><td>Pittsburgh Steelers</td><td>-0.1</td><td>-1.6</td></tr>
<tr><td>San Diego Chargers</td><td>-2.3</td><td>-1.2</td></tr>
<tr><td>San Francisco 49ers</td><td>3.1</td><td>1.5</td></tr>
<tr><td>Seattle Seahawks</td><td>2.8</td><td>1.1</td></tr>
<tr><td>St. Louis Rams</td><td>-0.9</td><td>0.2</td></tr>
<tr><td>Tampa Bay Buccaneers</td><td>1.7</td><td>0.9</td></tr>
<tr><td>Tennessee Titans</td><td>-2.4</td><td>-0.0</td></tr>
<tr><td>Washington Redskins</td><td>4.4</td><td>2.1</td></tr>
</tbody>
</table>

Es wird niemanden überraschen, dass die Redskins dank Alfred Morris und
Robert Griffin III das effektivste Laufspiel haben und auch nicht, dass
die Vikings mit Adrian Peterson auf Platz 2 folgen. Auch hier kann man
die Zahlen wie folgt interpretieren: Die Minnesota Vikings erzielen pro
Spiel 1.6 Punkte mehr durch ihr Laufspiel als der Ligadurchschnitt.

Auch bei den Zahlen zum PassPPA gibt es keine echten Überraschungen. Das
ist ein Fakt, den ich im Zusammenhang mit einer neuen Metrik immer
erstmal beruhigend finde.

Zur Visualisierung ist es noch interessant, beide Metriken gegeneinander
aufzutragen *(Ein Klick vergrößert das Ganze auch nochmal)*:

[![pass\_vs\_rush\_ppa](|filename|/images/pass_vs_rush_ppa-1024x744.png)](|filename|/images/pass_vs_rush_ppa.png)

Es ist interessant festzustellen, dass alle vier verbleibenden
Playoff-Teams sowohl im PassPPA als auch im RushPPA positive Werte
haben, also sowohl Pass- als auch Laufspiel überdurchschnittlich
erfolgreich sind.

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

  [ersten Artikel zu PPA]: |filename|ppa-wie-gut-ist-eine-offense.md
