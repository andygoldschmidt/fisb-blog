Title: Das optimierte SRS oder warum einfach manchmal besser ist
Date: 2012-11-15 14:30
Author: footballissexbaby
Tags: Football, Home field advantage, NFL, Optimierung, Point spread, Python, SciPy, Simple Ranking System
Slug: das-optimierte-srs-oder-warum-einfach-manchmal-besser-ist

Nachdem ich vor einiger Zeit schon [das Simple Ranking System
vorgestellt habe][], habe ich gestern eine Methode vorgestellt, [um das
SRS in Offense- und Defense-Komponenten zu zerlegen][].

In dem Artikel habe ich auf teils große Abweichungen zum Modell von
[pro-football-reference.com][] - das als Vorbild diente - verwiesen:

> Vergleicht man die Werte mit denen von Pro-Football-Reference, so
> erkennt man teilweise gravierende Unterschiede. Das kommt daher, dass
> mein SRS nicht "gedeckelt" ist. Das heißt, wenn ein Team mit 40
> Punkten Vorsprung gewinnt, so fließt das auch so in den Algorithmus
> ein. Andere Implementationen deckeln die Punktdifferenz,
> typischerweise ab etwa 21 Punkten.

In den Kommentaren zu OSRS und DSRS hat korsakoff von [Sideline
Reporter][] die Frage aufgeworfen, ob man denn die Deckelung nicht so
anpassen könnte, dass dadurch die Vorhersagekraft maximiert wird.

Da ich kein Freund von "zufälligen" Werten bin und etwas Zeit hatte,
habe ich mich der Frage gleich angenommen.

Ich habe also als Erstes eine gedeckelte Version meines SRS entwickelt
und anschließend die Optimierung eingebaut.

Die Optimierung funktioniert so, dass ich die realen Punktdiffenzen mit
den SRS-Differenzen für alle Spiele verglichen habe:

[latex]\\text{R} = \\text{PS} - \\left(\\text{SRS}\_{x\_1} +
x\_2\\right)[/latex]

PS ist dabei die Punktdifferenz, x1 bezeichnet den Deckelungswert, mit
dem das SRS berechnet wurde und x2 ist ein freier Parameter.

Ziel ist es nun also x1 und x2 so anzupassen, dass R minimal wird. Ich
habe das mit dem Python-Paket SciPy gemacht, man kann da aber auch viele
andere Software-Lösungen finden, die das können.

Was sind nun aber die Werte der optimierten Parameter?

Sieht man sich das Ergebnis für die bisherige 2012er Saison an, ist das
Ergebnis doch überraschend:  
Der **optimale Deckelungswert ist 40** und der **freie Parameter ist
0.88**.

0.88, das kommt [dem geneigten Leser vielleicht vertraut vor][]. Das ist
nämlich ziemlich exakt der Heimvorteil, den das FISB-Ranking ausspuckt!

Wiederholt man die Optimierung mit anderen Saisons ergibt sich ein
ähnliches Bild: der Deckelungswert ist mal 40, mal 45, manchmal sogar 60
und der Heimvorteil entspricht immer in etwa dem des FISB-Rankings.

Das heißt also, dass eine Deckelung überflüssig ist! Seit 2000 gab es
gerade einmal 28 Spiele, die mit 40 oder mehr Punkten Differenz
entschieden wurden (die größte Punktdifferenz war beim 59:0 der Patriots
gegen die Titans 2009). Die Deckelung würde also nur in etwa zwei
Spielen pro Jahr überhaupt greifen.

Das heißt aber auch, dass alle Implementierungen, die eine Deckelung
haben (wie erwähnt meist etwa ab 21 Punkten), einen künstliche Schranke
einbauen, die zwar die Ergebnisse "sinnvoller" erscheinen lässt, aber in
Wirklichkeit absolut willkürlich und mathematisch schlicht falsch ist.

Wesentlich sinnvoller ist dagegen eine andere Annahme. Nämlich die, dass
Ergebnisse von zurückliegenden Wochen zunehmend unwichtiger werden
sollten. Angesichts von Verletzungen, Wetter und genereller Form ist
dieses "Vergessen" eine naheliegende und vernünftige Erweiterung.

Die Jungs von [FootballPerspective.com][] haben, wie von korsakoff
erwähnt, [ein solches System schon eingeführt][].

Auch da erscheint wieder ein mysteriöser Wert von 0.95, aber um die
Optimierung dieses Wertes kümmere ich mich ein anderes Mal.

  [das Simple Ranking System vorgestellt habe]: http://footballissexbaby.de/2012/09/simple-ranking-system-einfach-aber-gut/
    "Simple Ranking System – einfach aber gut"
  [um das SRS in Offense- und Defense-Komponenten zu zerlegen]: http://footballissexbaby.de/2012/11/offenses-und-defenses-bewerten-mit-dem-simple-ranking-system/
    "Offenses und Defenses bewerten mit dem Simple Ranking System"
  [pro-football-reference.com]: http://www.pro-football-reference.com
  [Sideline Reporter]: http://sidelinereporter.wordpress.com
  [dem geneigten Leser vielleicht vertraut vor]: http://footballissexbaby.de/2012/11/die-nfl-in-zahlen-woche-10/
    "Die NFL in Zahlen: Woche 10"
  [FootballPerspective.com]: http://www.footballperspective.com/
  [ein solches System schon eingeführt]: http://www.footballperspective.com/checkdowns-weighted-nfl-srs-ratings-through-sunday-101412/
