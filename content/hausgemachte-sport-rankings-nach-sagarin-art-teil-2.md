Title: Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 2
Date: 2011-06-07 23:03
Author: footballissexbaby
Tags: Football, Python, Ranking-Systeme, Sagarin, Stats, SVD
Slug: hausgemachte-sport-rankings-nach-sagarin-art-teil-2

In diesem Post will ich die Sagarin Sport-Rankings, die ich [hier][]
schon vorgestellt hatte, etwas näher beleuchten.

Meine Implementierung des Ranking Systems benutzt ausschließlich die
erzielten und zugelassenen Punkte pro Team um eine Wertung zu ermitteln
(Jeff Sagarin nennt das *Pure Points*). Hierfür muss jedes Team
natürlich schon einmal gespielt haben, ansonsten ist natürlich die
Zuweisung eines Rankingwertes nicht möglich (bzw. ist er dann nur ein
zufälliger Wert).

Man betrachtet also nun alle bisher ausgetragenen Begegnungen und
bestimmt für jedes Spiel die Punktedifferenz (der Einfachheit halber
bezogen auf das Heimteam).

Um nun aber zu wissen, wie *zukünftige* Spiele ausgehen werden, muss man
anhand der vorhandenen Daten ein Rating für jedes Team ermitteln. Das
ist natürlich nicht ganz trivial, da jedes Teamrating natürlich von den
Ratings der anderen Teams, gegen die es schon gespielt hat, abhängt.

Nehmen wir als Beispiel die GFL: Hier spielen 14 Teams, je 7 in der
Nord- und Südstaffel. Jedes Team tritt zweimal gegen jedes andere Team
aus seiner Division an und 2x gegen eine Interconference-Gegner. Das
macht also in der Summe 14 Spiele pro Team.

In unserem Beispiel gehen wir vereinfachend (und nicht realitätsgemäß)
davon aus, dass jedes Team pro Spieltag einmal spielt. Nach zwei
Spieltagen wären dann also 14 Spiele absolviert; das ergibt mathematisch
gesehen, ein lineares Gleichungssystem von 14 Gleichung mit 15
Unbekannten (14 Teams + Heimvorteil). Dieses Problem kann man iterativ
lösen, wie bereits in Teil 1 kurz umrissen. 

Dabei geht man wie folgt vor:

1.  Festlegen eines Anfangsratings und eines Heimvorteils
2.  Vergleichen der echten Punktedifferenz mit der Differenz der
    jeweiligen Ratings
3.  Quadrieren der Abweichung
4.  Alle quadrierten Abweichungen aufsummieren
5.  Teamratings und Heimvorteil solange variieren und Schritt 2-4 mit
    den aktualisierten Ratings wiederholen, bis die Summe der
    quadrierten Abweichungen hinreichend klein ist

Man sieht schnell ein, dass dieses Verfahren nicht unbedingt sehr
elegant ist. Daher nutze ich ein anderes Verfahren. Wie oben bereits
angedeutet, lässt sich das Problem als Gleichungssystem auffassen. Mit
Hilfe eines herkömmlichen Computers kann man selbst große
Gleichungssysteme schnell und einfach lösen.

(Die Idee und viele Hilfen bei der Implementierung habe ich übrigens auf
der hervorragenden Seite [Code and Football](http://codeandfootball.wordpress.com)
gefunden!)

Das Problem ist hierbei, dass sich die Art des Gleichungssystems ändert.
Hat man weniger Gleichungen als Unbekannte (sprich weniger Gesamtspiele
als Teams), so spricht man von einem *unterbestimmten Gleichungssystem*,
diese Art ist zwar immer lösbar, allerdings hat aber unendlich viele
Lösungen, so dass man für diesen Fall keine Ratings bestimmen kann. Hat
man hingegen mehr Gleichungen als Unbekannte (Anzahl der Spiele ist
größer als Anzahl der Teams), so spricht man von einem *überbestimmten
Gleichungssystem*, diese sind generell nicht eindeutig lösbar, oftmals
besitzen sie jedoch überhaupt keine Lösung. Eine eindeutige Lösung
erhält man nur bei Gleichungssystemen, in dem die Anzahl der Gleichungen
gleich der Anzahl der Unbekannten ist (*quadratisches
Gleichungssystem*).

Anmerkung: Die Aussagen im vorigen Absatz sind nur gültig, wenn die
Gleichungen voneinander *linear unabhängig* sind, für unseren Fall ist
das aber immer gegeben.

Schaut man sich unser GFL-Beispiel an, so sieht man, dass man es zumeist
mit überbestimmten Gleichungssystemen zu tun hat. Ab dem dritten von 14
Spieltag hat man mehr Spiele als Teams.

Wie kann man nun diese Art von Gleichungssystemen numerisch lösen?

Die Antwort gibt die sogennante Singulärwertzerlegung (*SVD, engl.
singular value decomposition*). Ich will nicht allzu genau darauf
eingehen, nur soviel:

Man kann die Spiele als Matrix schreiben, indem pro Zeile jedem Team
eine Spalte zugewiesen wird. Die Matrix besteht anfangs nur aus Nullen.
In jeder Zeile (die je ein Spiel repräsentiert) schreibt man nun an die
Stelle des Heimteams eine *1*, an die Stelle des Auswärtsteams eine
*-1*und ganz ans Ende nochmal eine *1*(Heimvorteil). Nun kann man das in
Matrixdarstellung folgendermaßen schreiben:

**Ax = y**

**A** ist hierbei die *Koeffizientenmatrix*, in der die ganzen Nullen
und Einsen stehen, sie ist eine m x n-Matrix. **x** ist ein Vektor, in
dem die Ratings stehen und **y** ist ein Vektor, der die tatsächlichen
Punktdifferenzen der einzelnen Spiele enthält. Gesucht ist also
offensichtlich **x**.

Hier kommt nun die SVD ins Spiel. Diese zerlegt die Matrix **A** in 3
Matrizen, so dass:

**A = U \* S \* V\_t**

**U** und **V\_t** sind hierbei *orthogonale Matrizen*, dass heißt die
transponierte Matrix ist gleich der inversen Matrix (das wird in einer
Sekunde noch wichtig). **U** ist eine m x m-Matrix und **V\_t** ist eine
n x n-Matrix. **S** ist, wie **A**, eine m x n-Matrix, die n
*Singulärwerte* auf den ersten n Diagonalelementen enthält.

Eingesetzt in unsere 1. Gleichung ergibt sich also:

**U \* S \* V\_t x = y**

Jetzt kann man ausnutzen, dass **U** und **Vh** orthogonale Matrizen
sind, man kann die letzte Gleichung einfach umformen und erhält:

**x = U\_t \* S' \* V y**

**S'** erhält man, in dem man die n Singulärwerte aus
**S** invertiert, bzw. Null setzt, falls
sie kleiner als ein gewisser Schwellwert sind (abhängig von der
numerischen Genauigkeit des Computers).

Nun hat man also den Vektor **x** berechnet, der alle gewünschten Teamratings
beinhatet. *Voila*!

Oder etwa doch nicht? Hab ich nicht vorher noch geschrieben, dass ein
überbestimmtes Gleichungssystem eben nicht eindeutig lösbar ist und
oftmals gar nicht? Ja, das stimmt. Allerdings liefert diese Matrix immer
eine Lösung (zumindest habe ich noch nie etwas anderes festgestellt).
Ich bin mir nicht sicher, ob das allein schon deswegen zustande kommt,
dass die lineare Unabhängigkeit erfüllt ist. 

Zum anderen Punkt, der Eindeutigkeit: Die SVD liefert nur eine Näherungslösung, 
das Problem **||Ax = y||^2** wird hierbei
minimiert.

Man erhält also unterm Strich die gleiche Lösung, die man auch mit dem
iterativen Verfahren erhalten hätte, allerdings mathematisch eleganter
und vor allem deutlich schneller!

Ich hoffe das war jetzt nicht allzu mathematisch und man konnte dem
Ganzen noch folgen ;)

Es war jedenfalls ganz hilfreich, dass ganze mal ordentlich
aufzuschreiben, da man schnell vergisst, was hinter der Berechnung
steckt, wenn man sie nur anwendet.

  [hier]: |filename|hausgemachte-sport-rankings-nach-sagarin-art-teil-1.md
