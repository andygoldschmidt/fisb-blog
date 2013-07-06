Title: Stiefelriemen für die Sagarin-Rankings
Date: 2011-10-02 18:22
Author: footballissexbaby
Tags: Bootstrapping, Football, New York Giants, Ranking-Systeme, Resampling, Sabermetrics, Sagarin, Stats
Slug: stiefelriemen-fur-die-sagarin-rankings

Wie der ein oder andere aufmerksame Leser dieses Blogs wohl noch weiß,
habe ich vor einigen Wochen die erste größere Verbesserung für meine
Ratings angekündigt. Jetzt ist es endlich soweit: der neue Algorithmus
ist getestet, für gut befunden und liefert saubere Ergebnisse.

 

**Was habe ich getan?**

Mein netter Bürokollege Christoph hat mich auf ein statistisches
Verfahren aufmerksam gemacht, dass insbesondere in der Psychologie
verwendet wird, um die Qualität von Stichproben zu erhöhen. Das
Verfahren nennt sich *Bootstrapping*und ist eine Methode aus dem Bereich
des sogenannten *Resamplings*.

Um die Funktionsweise zu verstehen, nehmen wir ein einfaches Beispiel:
Wir wählen zufällig 100 Personen aus und bestimmen ihre Körpergröße und
anschließend ziehen wir Rückschlüsse auf die Durchschnittsgröße der
Bevölkerung. 100 Personen sind leider nicht viel, daher wird der Fehler
am Ende wohl recht groß sein. Beispielsweise würde ein Proband wie Dirk
Nowitzki unter Umständen das Resultat in die Höhe treiben.

Führt man solche kleinen Stichproben mehrfach durch, so erhält man recht
unterschiedliche Ergebnisse. Manchmal ist es aber nicht möglich, die
Stichprobe zu wiederholen oder die Anzahl der Probanden zu erhöhen.

In diesem Fall kann man mittels Bootstrapping *im Nachhinein*die
Stichprobe variieren, um verzerrende Einflüße zu minimieren. Dafür
stellt man sich die Stichprobe viele hundert oder tausend Male neu
zusammen, indem man wahllos 100 Probanden mit Zurücklegen aus dem Topf
nimmt. Dadurch kann es also sein, dass Proband 42 vier Mal gezogen wird,
Dirk Nowitzki dagegen gar nicht. Da man dieses Verfahren aber sehr oft
wiederholt, kann man damit dennoch eine Verbesserung in der Ermittlung
der Durchschnittsgröße erzielen. Jede einzelne Stichprobe mag zwar noch
verzerrter sein als die Originalprobe, aber durch das Iterieren
"glättet" man verzerrende Einflüße.

Das klingt jetzt vielleicht noch etwas theoretisch und unglaubwürdig,
aber es klappt wie wir gleich sehen werden wirklich.

 

**Und was hat das mit Football zu tun?**

Wie ich bereits in meinen beiden Beitragen zu den Sagarin-Rankings
geschrieben habe, ist der Algorithmus relativ anfällig gegen extreme
Abweichungen. Sollte ein Team also eigentlich knapp gewinnen, verliert
aber aufgrund verschiedener Ereignisse haushoch, so lässt sich das
Ranking davon schnell beeinflussen.

Das Problem ist, dass diese Ausreißer verschiedenste Gründe haben
können, Verletzungen, Wetterbedingungen, Bedeutung des Spiels, etc. Dem
Algorithmus ist das aber egal, er guckt nur auf das Ergebnis und spuckt
am Ende eine dazu passende Zahl aus.

Und hier kommt das Bootstrapping ins Spiel: Zieht man wahllos Spiele, so
wird es Berechnungen geben, in die diese Ausreißer nicht mit einfließen
(und natürlich auch welche, in die sie gleich mehrfach einfließen). Nach
mehreren tausend Iterationen ist der Einfluß des einen Extremspiels also
reduziert und die Rankings sind etwas glatter und sauberer.

Pro Team hat man also jetzt tausende einzelne Ratings. Um jetzt den
richtigen Wert zu bestimmen, werden die Daten zu einem Histogramm
zusammengefasst und anschließend wird ein Gauss-Fit daran gelegt. Der
Erwartungswert der sich daraus ergebenden Gauss-Verteilung ist unser
gesuchter Wert.

 

**Zeig' her deine Ergebnisse!**

Um zu zeigen, wie das mit der Verteilung der einzelnen Rankings
aussieht, schauen wir uns doch mal die aktuelle Saison an und picken uns
die New York Giants raus.

Ohne jedes Bootstrapping ergibt sich ein Rankingwert von -4.85 für die
Giants. Schauen wir uns doch mal an, wie sich das verhält, wenn man 100,
1.000, 10.000 und 100.000 Iterationen durchlaufen lässt:

![Nyg 100][]

![Nyg 1000][]

![Nyg 10000][]

![Nyg 100000][]

Im Bootstrap-Ranking ergibt sich für die Giants also ein Wert von -5.04.
Das klingt zunächst nicht so, als wäre das ein Riesenunterschied, aber
das war ja auch erst ein Rating. Aber man sieht hier bereits, dass man
es nicht mit einem Zufallswert zu tun hat. Mit jeder Erhöhung der
Iterationen verbessert sich nicht nur die Glockenkurve, sondern man
erkennt auch, dass die Ratings gegen einen Wert konvergieren. Wie sieht
es aber nun mit den anderen 31 Teams aus? Schauen wir uns mal die
Ratings für alle Teams mit und ohne Bootstrapping an:

![Ratings][]

 

Hierbei bezeichnet "Rating BS" das Rating mit Bootstrapping, "Rating"
sind die normalen Sagarin-Ratings, so wie sie sich durch lösen des
Gleichungssystems ergeben. Die Unterschiede sind oftmals nicht sehr
dramatisch, aber es gibt eben auch Teams, die scheinbar im normalen
Rating etwas bevorzugt werden, wie beispielsweise die Redskins. Dagegen
sind die Chiefs zwar immer noch schlecht, aber doch immerhin 3 Punkte
besser als ohne Bootstrapping.

Ich habe die neuen Ratings bisher noch nicht zur Vorhersage genutzt,
daher weiß ich nicht, ob sie wirklich genauer sind und 3 Spieltage sind
bisher auch noch nicht die ganz große Datenmenge. Aber ich habe viel
Grund zur Hoffnung ;)

Nach dem Spieltag werde ich mich der Vorhersagekraft nochmal annehmen.

 

Einen schönen Footballsonntag allen zusammen!

  [Nyg 100]: http://footballissexbaby.de/wp-content/uploads/2011/10/nyg_1002.png
    "nyg_100.png"
  [Nyg 1000]: http://footballissexbaby.de/wp-content/uploads/2011/10/nyg_10002.png
    "nyg_1000.png"
  [Nyg 10000]: http://footballissexbaby.de/wp-content/uploads/2011/10/nyg_100002.png
    "nyg_10000.png"
  [Nyg 100000]: http://footballissexbaby.de/wp-content/uploads/2011/10/nyg_1000002.png
    "nyg_100000.png"
  [Ratings]: http://footballissexbaby.de/wp-content/uploads/2011/10/ratings.png
    "ratings.png"
