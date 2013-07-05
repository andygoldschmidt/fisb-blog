Title: Quarterback Rating - Die unnützeste Statistik im Football
Date: 2011-07-31 23:58
Author: footballissexbaby
Slug: quarterback-rating-die-unnutzeste-statistik-im-football

Es ist eine vetraute Statistik: Das *Quarterback Rating*, oder besser
gesagt, das *Passer Rating*.

Oftmals wird es herangezogen, um die Leistung eines Quarterbacks als
besonders gut oder besonders schlecht herauszuheben.

Entwickelt wurde das QB Rating Anfang der 70er Jahre. Es ist eine Zahl
zwischen 0 und 158,3. Es wurde so konzipiert, dass die besten
Quarterbacks in etwa ein Rating von 100 haben.

**Wie berechnet sich das QB-Rating?**

Das ist einigermaßen kompliziert. Als erstes bildet man 4 Faktoren, aus
denen man dann schlussendlich das Rating zusammensetzen kann:

C = (Completions / Attempts - 0,3) x 5  
Y = (Yards / Attempts - 3) x 0,25  
T = (Touchdowns / Attempts) x 20  
I = 2,375 - Interceptions / Attempts x 25

Und jetzt kommt etwas Zahlenspielerei: Man sucht erst das Minimum
zwischen den einzelnen Faktoren und 2,375 und danach bildet man das
Maximum zwischen 0 und dem vorher erhaltenen Minimum. Alles klar?

Nochmal in knapper Schreibweise:  
mm(x) = max(0, min(x, 2.375))  
Wobei x mit C, Y, T und I ersetzt werden muss.

Und nun fassen wir das alles zum eigentlichen Rating zusammen:

QBR = (mm(C) + mm(Y) + mm(T)+ mm(I)) x 100/6

Danke an die [Wikipedia][] für die übersichtliche Schreibweise!

**Das ist zwar nicht anschaulich, aber warum unnütz?**

Zuerst einmal sieht man auch als jemand, der doch ab und an mit
Mathematik zu tun hat sehr schnell, dass die Berechnung alles andere als
elegant oder gar anschaulich ist.  
Aber das ist nur ein ästhetischer Punkt, viel schlimmer ist, dass die
Formel auch noch dazu willkürlich, ungenau und unvollständig ist.

Zuerst zur Unvollständigkeit: In das Quarterback Rating fließen nur die
tatsächlich geworfenen Pässe ein, es ist also ein reines Passer Rating.  
Der größte Kritikpunkt ist wohl, dass in das Rating keine Sacks
einfließen. Ein guter Quarterback schafft es aber unter großem Druck den
Ball wegzuwerfen, statt für Raumverlust zu Boden gebracht zu werden. Im
Rating hätte das aber einen negativen Einfluss.  
Wenn man es gut meint kann man argumentieren, dass Sacks erst seit den
1980er Jahren als eine offizielle Statistik erfasst werden, also gut 10
Jahre nach Konzeption des Passer Ratings.  
(*Das ist aber natürlich längst kein Grund, das Rating nach 40 Jahren
nicht endlich mal anzupassen!*)

Der zweite Punkt der Unvollständigkeit besteht darin, dass modernes
Quarterback-Spiel eben nicht nur aus Passen besteht, sondern auch aus
dem sogenannten *Scrambling*, der QB läuft also selbst los. Diese Yards
fließen überhaupt nicht ins Rating ein, obwohl es bei einigen
Quarterbacks (Michael Vick, Vince Young, Aaron Rodgers, Ben
Roethlisberger, ...) für viele Yards und auch viele Touchdowns sorgt.

Ungenauigkeit erkennt man an einigen Stellen, beispielsweise, dass ein
Rating von 100 oder mehr fast nur in einzelnen Spielen, aber eigentlich
nie über eine volle Saison erreicht wird. Das große Problem ist aber,
dass die Completion Percentage doppelt gewichtet wird! Denn sie steht im
Faktor C als Completions / Attempt drin und indirekt im Faktor Y, denn
Yards / Attempt ist nichts anderes als:

Yards / Completion \* Completion / Attempt

Es wäre also richtiger die Yards pro Completion einfließen zu lassen
oder gleich die Yards pro Play, dann hätte man auch gleich alle
Nicht-Pässe mit erfasst!

Und zum Schluss das offensichtlichste: die Willkür. Warum beschränkt man
die einzelnen Faktoren zwischen 0 und 2,375 und nicht zm Beispiel
zwischen -10 und 10 oder 0 und 3,14? Es gibt einfach keine Erklärung.
Genauso sind die einzelnen Gewichtungen in den Faktoren willkürlich.
Warum wird das Touchdowns-zu-Versuch-Verhältnis mit 20 multipliziert und
nicht mit 100 oder mit 35?

Es gibt sehr fortschrittliche Methoden, die versuchen mittels
*Regressionsmodellen* den Einfluss des Quarterbacks auf das Spiel zu
ermitteln. Ein nettes Ergebnis ist, dass man mittels solcher Modelle
auch **sinnvolle** Gewichtungen der einzelnen Faktoren bekommt!  
(Brian Burke hat auf advancednflstats.com mal einen Artikel darüber
verfasst, bei Interesse einfach mal googlen).

Ich hoffe ihr seht, dass man diesem Passer Rating reichlich skeptisch
gegenüber stehen sollte, da es zwar Tendenzen erkennen lässt, durch
seine Willkür aber jegliche "echte" Bewertung unmöglich macht!

  [Wikipedia]: http://en.wikipedia.org/wiki/Passer_rating
