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
[latex]\\text{passPPA} = 4.1 \\cdot \\text{NY/A} - 52.61 \\cdot
\\text{Int/A}[/latex]

Lauf:  
[latex]\\text{rushPPA} = 1.48 \* \\text{RushYd/A} - 143.49 \*
\\text{FL/A}[/latex]

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

*(Zum Sortieren auf den Spaltennamen klicken.)*

  Team                   PassPPA   RushPPA
  ---------------------- --------- ---------
  Arizona Cardinals      -7.6      -1.6
  Atlanta Falcons        3.3       0.1
  Baltimore Ravens       0.6       0.9
  Buffalo Bills          -1.4      0.1
  Carolina Panthers      3.2       0.4
  Chicago Bears          -2.6      0.2
  Cincinnati Bengals     -0.8      -0.2
  Cleveland Browns       -2.5      -0.0
  Dallas Cowboys         2.1       -0.9
  Denver Broncos         5.1       -1.0
  Detroit Lions          0.8       -0.7
  Green Bay Packers      2.1       -0.1
  Houston Texans         1.6       0.9
  Indianapolis Colts     -0.3      -0.4
  Jacksonville Jaguars   -3.6      -0.5
  Kansas City Chiefs     -4.7      -0.2
  Miami Dolphins         -1.4      -0.7
  Minnesota Vikings      -3.8      1.6
  New England Patriots   3.7       0.6
  New Orleans Saints     3.8       0.9
  New York Giants        2.2       1.1
  New York Jets          -4.1      -1.7
  Oakland Raiders        -0.1      -0.6
  Philadelphia Eagles    -2.1      -1.1
  Pittsburgh Steelers    -0.1      -1.6
  San Diego Chargers     -2.3      -1.2
  San Francisco 49ers    3.1       1.5
  Seattle Seahawks       2.8       1.1
  St. Louis Rams         -0.9      0.2
  Tampa Bay Buccaneers   1.7       0.9
  Tennessee Titans       -2.4      -0.0
  Washington Redskins    4.4       2.1

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

[![pass\_vs\_rush\_ppa][]][]

Es ist interessant festzustellen, dass alle vier verbleibenden
Playoff-Teams sowohl im PassPPA als auch im RushPPA positive Werte
haben, also sowohl Pass- als auch Laufspiel überdurchschnittlich
erfolgreich sind.

  [ersten Artikel zu PPA]: http://footballissexbaby.de/2013/01/ppa-wie-gut-ist-eine-offense/
    "PPA: Wie gut ist eine Offense?"
  [pass\_vs\_rush\_ppa]: http://footballissexbaby.de/wp-content/uploads/2013/01/pass_vs_rush_ppa-1024x744.png
  [![pass\_vs\_rush\_ppa][]]: http://footballissexbaby.de/wp-content/uploads/2013/01/pass_vs_rush_ppa.png
