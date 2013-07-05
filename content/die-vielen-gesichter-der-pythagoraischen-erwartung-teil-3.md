Title: Die vielen Gesichter der pythagoräischen Erwartung. Teil 3
Date: 2012-06-24 15:18
Author: footballissexbaby
Tags: Baseball Prospectus, Bill James, Clay Davenport, David Smyth, Football Outsiders, Modelle..., NFL, Overfitting, Pythagenpat, Pythagenport, Pythagorean expectation, Taktik, Zahlen
Slug: die-vielen-gesichter-der-pythagoraischen-erwartung-teil-3

Im [ersten Teil][] der Serie habe ich drei verschiedene Methoden zur
Berechnung der pythagoräischen Erwartung vorgestellt. Im [zweiten
Teil][] habe ich die verwendeten Exponenten genauer untersucht.

Im dritten Teil werde ich mich nun den Ergebnissen zuwenden und
versuchen darzustellen, welche Methode meiner Meinung nach die beste der
drei ist.

Ohne viele Worte folgen nun fünf Grafiken, die jeweils die Vorhersagen
von **Pythagorean**, **Pythagenport** und **Pythagenpat** zeigen, sowie
die tatsächliche Siegquote:

[gallery orderby="title"]

 

Man sieht, dass die drei Methoden sich teils erheblich unterscheiden.
Gerade die **Pythagenport**-Methode weicht oftmals stark von den anderen
beiden ab, sowohl nach oben als auch nach unten. Man hat den Eindruck,
als ob **Pythagenport** oftmals näher am tatsächlichen Ergebnis ist.  
Um das zu quantifizieren bediene ich mich hier der Methode der
mittleren quadratischen Abweichung (*mean squared error, MSE*). Diese
ist wie folgt definiert:

[latex]\\text{MSE} = \\sum\\limits\_{i=0}\^{N}\\left(x\_i -
\\bar{x}\\right) \^{2}[/latex]

Das heißt, man quadriert für jedes Team die Abweichung zwischen
pythagoräischer Erwartung und tatsächlichem Ergebnis und summiert die
Werte von allen Teams.

Die folgende Tabelle zeigt die mittlere quadratische Abweichung für alle
drei Methoden:

  Jahr   Pythagorean   Pythagenport   Pythagenpat
  ------ ------------- -------------- -------------
  2007   0.195         0.161          0.187
  2008   0.238         0.238          0.238
  2009   0.207         0.170          0.199
  2010   0.195         0.192          0.193
  2011   0.226         0.205          0.216

Die kleinste Abweichung gibt es in allen fünf Saisons bei
**Pythagenport**. Das heißt also, dass hier die Abweichung zwischen
Theorie und Praxis am kleinsten ist. Das mag erst einmal gut klingen,
ist in Wahrheit aber fatal, denn die pythagoräische Erwartung dient ja
gerade dazu, abzuschätzen, wie oft ein Team hätte gewinnen *sollen* und
nicht wie oft es tatsächlich gewonnen *hat*.

Das ist ein weiteres Indiz dafür, dass **Pythagenport** an Überanpassung
(*Overfitting*) leidet. Einen ähnlichen Trend, wenngleich nicht ganz so
ausgeprägt, sieht man im Übrigen auch bei **Pythagenpat**.

Alles in allem führt mich das zur Schlussfolgerung, dass man natürlich
versuchen kann, eine empirische Formel wie die pythagoräische Erwartung
(also **Pythagorean**) zu verbessern, indem man sie erweitert und
anpassbarer macht. Jedoch leidet zum ersten die Einfachheit und
Schlichtheit der ursprünglichen Gleichung darunter und man muss darüber
hinaus auch Abstriche bei der Vorhersagekraft machen.

Am Ende muss jeder für sich selbst entscheiden, welches Kriterium das
entscheidende ist: ist die Korrelation zum Sieg-Niederlagen-Verhältnis
der entscheidende Faktor, dann sollte man sicher die
**Pythagenport**-Formel heranziehen. Ist man an einer möglichst
einfachen Formel interessiert, die am besten das "Was hätte passieren
*sollen*?" repräsentiert, dann ist sicher die klassische
**Pythagorean**-Methode das Mittel der Wahl.  
Die **Pythagenpat**-Methode steht meiner Meinung nach für einen guten
Kompromiss; hier hat man eine bessere Korrelation als in der klassischen
Erwartung, jedoch (scheinbar) kein so starkes Overfitting wie bei
**Pythagenport**.

  [ersten Teil]: http://footballissexbaby.de/wordpress/2012/03/die-vielen-gesichter-der-pythagoraischen-erwartung-teil-1/
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 1 (Update)"
  [zweiten Teil]: http://footballissexbaby.de/wordpress/2012/03/die-vielen-gesichter-der-pythagoraischen-erwartung-teil-2/
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 2"
