Title: Die vielen Gesichter der pythagoräischen Erwartung. Teil 2
Date: 2012-03-18 20:43
Author: footballissexbaby
Tags: Baseball Prospectus, Bill James, Clay Davenport, David Smyth, Football Outsiders, Gaussian distribution, Modelle..., NFL, Overfitting, Poisson distribution, Pythagenpat, Pythagenport, Pythagorean expectation, Taktik, Zahlen
Slug: die-vielen-gesichter-der-pythagoraischen-erwartung-teil-2

Der erste Teil zu diesem Artikel ist [hier][] zu finden.

Bevor es im dritten und letzten Teil um die Ergebnisse geht, möchte ich
in diesem zweiten Teil noch einmal kurz auf die Exponenten der drei
Methoden eingehen. **Pythagenport** und **Pythagenpat** unterscheiden
sich hierbei grundlegend von der klassischen pythagoräischen Erwartung
(**Pythagorean**): Während bei der **Pythagorean**-Formel der Exponent
für alle Teams in der jeweiligen Woche gleich ist, so werden sie in den
beiden anderen Methoden für jedes Team einzeln anhand ihrer Punkte
angepasst.

Schauen wir uns also einmal an, wie die Exponenten aller drei Methoden
verteilt sind. Im Folgenden sind alle Exponenten der drei Methoden für
alle Spielwochen der Saisons 2007-2011 als Histogramm dargestellt:

[gallery order="DESC" orderby="title"]

*Von links nach rechts: Pythagorean, Pythagenport und Pythagenpat.*

**Pythagorean**hat weniger "Ereignisse", da wie oben beschrieben jedes
Team den gleichen Exponenten hat. Daher gibt es für **Pythagenport/
-pat** 32x mehr Exponenten.

Die Mittelwerte sind wie folgt:

-   **Pythagorean**: <!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->
    2.8196
-   **Pythagenport**: <!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->
    2.8575
-   **Pythagenpat**: <!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->
    2.8315

Es fällt auf, dass die Exponenten bei **Pythagenport** etwa symmetrisch
verteilt sind. Das erinnert an eine *Gauss-Verteilung*.
**Pythagorean**und **Pythagenpat**sind hingegen "linkslastig", dies
entspricht einer *Poisson-Verteilung*. Das ist insofern interessant, als
das die Gauss-Verteilung häufig auftritt und beispielsweise [in der
Physik und Statistik eine sehr zentrale Rolle spielt][]. Die
*Poisson-Verteilung* hingegen beschreibt Prozesse, [bei denen Ereignisse
selten vorkommen][]. Die Anzahl von Punkten in einem Teamspiel
entspricht ebenfalls einer solchen Verteilung. Der Exponent einer
"guten" pythagoräischen Erwartung sollte demzufolge ebenfalls ein
Poisson-artiges Verhalten zeigen.

Das führt mich zu der
*<span style="text-decoration: underline;">Vermutung</span>* (!!!), dass
die gaussverteilte **Pythagenport**-Methode "überangepasst" ist. Der
Exponent schwankt bei dieser Methode also mit einer gewissen
*Standardabweichung* (= Breite der Glockenkurve) um den *Mittelwert.*

Es ist bei komplexen Prozessen immer schwierig zu sagen, welche
Verteilung zu erwarten ist. Man kann nur anhand von gewissen Merkmalen
des jeweiligen Problems versuchen Vergleiche mit bekannten Prozessen
anzustellen.

Ein weiteres wichtiges - und von Clay Davenport selbst eingeräumtes
Problem - bei **Pythagenport** ist, dass es mit "kleinen" Werten nicht
korrekt umgeht. Im Baseball ist es das Problem, wenn ein Team einen Run
versucht hat, und mit diesem einem Run gepunktet hat. Im Football gibt
es dasselbe Problem, wenn eine Mannschaft beispielsweise nur ein Field
Goal geschossen und ein Field Goal kassiert hat. Dann nämlich kann wegen
des Logarithmus ein *negativer* Exponent entstehen. Das ist zugegeben
ein eher mathematisches als ein praktisches Problem. Jedoch sollte die
"richtige" pythagoräische Erwartung alle denkbaren Fälle sinnvoll
abdecken, auch wenn sie sehr sehr unwahrscheinlich sind.

Im dritten und letzten Teil werde ich mich dann endlich mit der
Vorhersagekraft der drei Methoden beschäftigen.

  [hier]: http://footballissexbaby.de/wordpress/2012/03/die-vielen-gesichter-der-pythagoraischen-erwartung-teil-1/
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 1 (Update)"
  [in der Physik und Statistik eine sehr zentrale Rolle spielt]: http://en.wikipedia.org/wiki/Normal_distribution#Occurrence
  [bei denen Ereignisse selten vorkommen]: http://en.wikipedia.org/wiki/Poisson_distribution#Occurrence
