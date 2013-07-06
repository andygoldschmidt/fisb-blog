Title: Wie sehr unterscheiden sich ESPN's Total Quarterback Rating und das traditionelle Passer Rating?
Date: 2011-09-14 14:14
Author: footballissexbaby
Tags: ESPN, NFL, Passer Rating, QBR, Quarterback Rating, Total Quarterback Rating
Slug: wie-sehr-unterscheiden-sich-espns-total-quarterback-rating-und-das-traditionelle-passer-rating

Der erste NFL-Spieltag liegt hinter uns. Es gab einige Überraschungen,
wie die starke Leistung der Washington Redskins (sowohl in der Offense
als auch in der Defense), der Auftritt von Cam Newton (allerdings gegen
eine unterirdische Cardinals-Secondary) oder auch die offensive
Feuerkraft der Buffalo Bills.

Aber worüber ich mich persönlich am meisten freue sind die ersten Total
Quarterback Rankings von ESPN ([hier][] zu finden, überraschenderweise
etwas versteckt). Nach der Vorstellung vor einigen Monaten wurde heftig
über das neue Rating diskutiert, auch [in diesem Blog][]. Jetzt hat man
endlich die Zahlen aller Quarterbacks für ein einzelnes Spiel und nicht
nur für ganze Saisons.

Das gibt mir die Möglichkeit, das neue Total QBR, von mir hier kurz als
*TQBR* bezeichnet, mit dem traditionellen Passer Rating (Kritik ist
[hier][1] zu finden), das ich im Folgenden einfach *QBR* nenne, zu
vergleichen.

Da das *TQBR* in einem Intervall von 0 bis 100 liegt, das *QBR* aber
Werte zwischen 0 und 158.3 annehmen kann, muss man Letzeres noch etwas
modifizieren, das ganze nenne ich einfach mal *Scaled QBR*.

Das *Scaled QBR* ist einfach berechnet. Es multipliziert das *QBR*
einfach mit 0.63 (der Quotient aus 100 und 158.3), so dass die Werte
zwischen 0 und 100 skaliert sind und addiert am Ende noch die
durchschnittliche Abweichung von *TQBR* und *QBR* hinzu. Für die besten
20 Quarterbacks (nach *TQBR*) betrug die Differenz am ersten Spieltag
etwa 2.35 Punkte.

Schauen wir uns also mal an, wie die beiden Ratings im Vergleich
aussehen:

 

![Comparison tqbr qbr][]

 

Aufgelistet sind ESPN's Total Quarterback Rating, das oben erwähnte
Scaled Quarterback Rating, die Abweichung des *Scaled QBR* zum *TQBR*
und abschließend noch zum Vergleich das ganz klassische Passer Rating.
Rot markiert sind alle Abweichungen die größer als 10 Prozent sind.

Es fällt auf, dass die besten *TQBR*-Quarterbacks ein sehr ähnliches
*Scaled QBR* haben. Bei den Top 8-QB's ist die Abweichung nur zweimal
(knapp) größer als 10 Prozent. Jedoch sieht man genauso schnell, dass
der umgekehrte Fall nicht gilt: die Quarterbacks mit dem besten *QBR*
haben nicht zwingend das beste *TQBR*. Beispielsweise hat Kevin Kolb von
den Arizona Cardinals ein Passer Rating vonn 130.0, was einem *Scaled
QBR* von 84.5 entspricht. Er ist damit der drittbeste *QBR*-Quarterback.
Jedoch ist er nur auf dem abgeschlagenen 18. Platz in ESPN's Rating mit
einem Rating von 44.0, das ist also eine unterdurchschnittliche Leistung
von Kolb gewesen, da das *TQBR* so angelegt ist, dass ein Wert von 50
den durchschnittlichen Quarterback auszeichnet. Ausschlaggebend für das
geringere ESPN-Rating dürften Kolbs zwei Fumbles sein, von denen er
eines für einen Raumverlust von 8 Yards verlor. Noch dazu stehen vier
Läufe für Kolb auf seinem Konto, jedoch für einen Yard Raumverlust (*Ich
habe das Spiel nicht gesehen, denke aber, dass Kolb wohl abgekniet hat.
Es wäre interessant zu wissen, inwiefern das in das*TQBR*einfließt.*)

Weiterhin fällt auf, dass das *Scaled QBR* bei den besseren Quarterbacks
immer unter dem Wert des *TQBR*liegt und für die schlechteren
Quarterbacks über dem Wert des *TQBR*. Das ist ein ermutigendes Zeichen
für die Arbeit von ESPN. Denn ein guter Quarterback muss nicht nur gut
werfen, sondern auch Fehler vermeiden, seinen Team ab und an mit einem
Scrambling aushelfen und Pässe in wichtigen Momenten (*clutch plays* wie
ESPN das so schön nennt) an die Receiver bringen. Daher sollten die
besten Quarterbacks besser sein, als es die reinen Passstatistiken
vermuten lassen.  
Andererseits ist es auch plausibel, dass die schlechteren Quarterbacks
ein niedrigeres Rating haben, als es das einfache Passer Rating
ausdrückt. Schließlich berücksichtigt das *QBR* nicht, in welchem Moment
ein Pass unvollständig ist (beim 4th & Goal ist das natürlich
gravierender als bei 1st & 10 an der Mittellinie) oder wieviele Fumbles
ein Quarterback hatte oder wie oft er gesackt wurde. All das hat
gravierenden Einfluß auf den Spielverlauf und wird im *TQBR*
berücksichtigt und scheinbar mit Erfolg.

Insgesamt habe ich nach dem ersten Spieltag den Eindruck, dass das Total
Quarterback Rating die subjektive Wahrnehmung besser abbildet als es das
Passer Rating tut.

Zum Abschluss habe ich die beiden Quarterback-Ratings noch in einem
Scatter Plot aufgetragen und die Korrelation zwischen beiden berechnen
lassen:

 

![Correlation tqbr qbr][]

 

Man sieht, dass es ein paar Ausreißer gibt (hauptsächlich allerdings bei
schlechteren *TQBR*'s), beispielsweise den Punkt links oben, das ist
Kevin Kolb. Dennoch kommt man auf einen Korrelationskoeffizienten von
0.57, das ist schon ein ernstzunehmender Wert (jedoch bei einer sehr
wenigen Datenpunkten). Aber das ist natürlich konsistent mit den
Erwartungen: Schließlich ist und bleibt die Hauptaufgabe eines
Quarterbacks das Passen, daher wäre es bedenklich, wenn zwischen beiden
Ratings gar keine Korrelation bestehen würde.

 

Als Fazit bleibt festzuhalten, dass ich überrascht bin, wie gut das
Total Quarterback Rating ist. Es war zwar nur ein Spieltag, aber es gibt
Grund zu der Annahme, dass ESPN ein echter Fortschritt in der Bewertung
von Quarterbacks gelungen ist.

  [hier]: http://espn.go.com/nfl/story/_/id/6943920/nfl-week-1-total-qbr-leaders
  [in diesem Blog]: https://footballissexbaby.wordpress.com/2011/08/07/die-vor-und-nachteile-des-neuen-espn-total-quarterback-rating/
  [1]: https://footballissexbaby.wordpress.com/2011/07/31/quarterback-rating-die-unnutzeste-statistik-im-football/
  [Comparison tqbr qbr]: http://footballissexbaby.de/wp-content/uploads/2011/09/comparison_tqbr_qbr.png
    "comparison_tqbr_qbr.png"
  [Correlation tqbr qbr]: http://footballissexbaby.de/wp-content/uploads/2011/09/correlation_tqbr_qbr.png
    "correlation_tqbr_qbr.png"
