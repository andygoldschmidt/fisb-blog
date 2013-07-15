Title: Die Vor- und Nachteile des neuen ESPN Total Quarterback Rating
Date: 2011-08-07 20:03
Author: footballissexbaby
Tags: ESPN, NFL, Passer Rating, QBR, Total Quarterback Rating
Slug: die-vor-und-nachteile-des-neuen-espn-total-quarterback-rating

Kurz nachdem ich [hier](|filename|quarterback-rating-die-unnutzeste-statistik-im-football.md)
das NFL Passer-Rating kritisiert habe, hat
ESPN prompt ein brandneues und wirklich revolutionäres Rating
vorgestellt, dass den Namen *Quarterback Rating</*
durchaus verdient. ESPN nennt sein Rating daher auch vollmundig,
amerikanisch-bescheiden **Total Quarterback Rating** oder auch kurz
**QBR** (wieso man da gerade auf diese Abkürzung kommt bleibt mir
allerdings etwas schleierhaft.)

**Wie funktioniert das TotalQuarterback Rating?**

Ich möchte hier nur eine recht knappe Zusammenfassung geben, wer das
ganze etwas ausführlicher nachlesen möchte, dem sei [der Artikel direkt
bei ESPN empfohlen][].

ESPN hat nach eigenen Angaben die *play-by-play*-Daten aller NFL-Spiele
der vergangenen 10 Jahre ausgewertet. Aus diesen Daten hat man eine
Gewinnwahrscheinlichkeitsfunktion (*win probability function*)
ermittelt. Diese gibt an, wie wahrscheinlich es ist, dass ein Team bei
einer bestimmten Spielsituation am Ende das Spiel gewinnen wird. (Brian
Burke von advancednflstats.com hat dort die Vorarbeit geleistet, die ich
in den nächsten Wochen hier auch noch genauer vorstellen werde).

Mit Hilfe der Gewinnwahrscheinlichkeitsfunktion ist es nun möglich jeder
Spielsituation zu erwartende Punkte (*expected points*) zuzuweisen. Die
Wahrscheinlichkeit zum Punkten ist bei 1st & Goal mit viel Zeit auf der
Uhr natürlich deutlich höher, als bei 3rd & 10 an der eigenen 25 mit ein
paar Sekunden zu spielen. Diese Punkte sind die zu erwartenden Punkte
für das Team (*team expected points*).

Die Hauptaufgabe besteht nun darin zu ermitteln, wie hoch der Anteil
jedes einzelnen Spielers an den zu erwartenden Punkten ist. Dazu hat
ESPN ein eigenes Video-Tracking-System genutzt, mit Hilfe dessen man den
Einfluß von unterworfenen Pässen, Drops, Interceptions, etc. feststellen
konnte. So konnte ESPN nach eigenen Angaben zeigen, dass *yards after
catch (YAC)*wohl hauptsächlich dem Receiver zuzuschreiben sind, und nur
wenig dem Quarterback und auch, dass die *Pass Protection*hauptsächlich
ein Produkt des Spiels von O-Line und Quarterback ist, wer hätte
letzteres gedacht!

Als nächsten Schritt stellt ESPN für jeden Spielzug einen sogenannten
*clutch index* auf. Das ist ein Wert, der angibt, wie entscheidend und
wichtig ein Spielzug ist. Je wichtiger also ein Spielzug ist, umso
größer der Wert des *clutch index*. Einem "normalen" Spielzug weist ESPN
den Wert 1,0 zu. Der Index variiert grob zwischen 0,3 und 3,0. Das
Rating des Quarterbacks beeinflusst dies insofern, dass der *clutch
index* mit den zu erwartenden Punkten für den Quarterback für den
jeweiligen Spielzug multipliziert wird (und anschließend noch normiert
wird).

Der letzte Schritt, um das *Total Quarterback Rating* zu berechnen,
besteht nun darin, den erhaltenen Wert über alle Spielzüge so zu
skalieren, dass er zwischen 0 und 100 liegt. Die Werte sind so skaliert,
dass ein Wert von 50 dem durchschnittlichen Quarterback entspricht. Die
besten Quarterbacks sollten über eine gesamte Saison einen Wert von etwa
75 haben und in einzelnen Spielen haben Top-Quarterbacks Werte von etwa
90.

**Vorteile des Total Quarterback Rating:**

Der größte Vorteile des QBR sind ganz klar die schiere Menge an
analysierten Daten. ESPN hat die Ressourcen, um viele Menschen damit zu
beschäftigen Spielzüge auszuwerten, statistische Modelle zu entwerfen,
die von Leuten mit viel Football-Sachverstand auf ihre Sinnhaftigkeit
überprüft werden können und nicht zuletzt wurden sicher auch eine
Vielzahl von sehr fähigen Entwicklern angeheuert, um die Modelle in
effektiven, funktionierenden Code zu gießen. Alle anderen Modelle zu
neuen Quarterback-Ratings, wie die von Brian Burke oder von Football
Outsiders, beruhen letztendlich auf einer viel kleineren Anzahl von
Daten. Daher sollte allein durch die Menge an Daten und die
dahinterstehende Manpower mit entsprechendem Know-how schon ein sehr
durchdachtes System entstanden sein.

Ein weiterer Vorteil ist das Konzept als solches: jeder einzelne
Spielzug fließt in das Rating ein, egal ob Touchdown, Drop des
Receivers, Sack, Scramble oder Fumble. Damit ist ein großer Kritikpunkt
am "traditionellen" Passer Rating beseitigt worden. Durch den Einsatz
des Video-Tracking-Systems lassen sich die Einflüsse der einzelnen
Spielzüge darüber hinaus auch noch sinnvoll wichten. Das ist durch den
Einsatz von bloßen nackten Statistiken nicht möglich.

Desweiteren ist es sinnvoller, dass ein "perfekter" Quarterback ein
Rating von glatt 100 hat und nicht von 158,3. Beim normalen Passer
Rating hat der Durchschnitts-QB darüber hinaus auch nicht unbedingt ein
Rating von 79,15 (also 158,3 / 2). Das ist eine weitere Eigenschaft des
QBR, das die Vergleichbarkeit zwischen zwei Rating deutlich verbessert.

Aber natürlich gibt es wie immer auch hier Kritikpunkte...

**Nachteile des Total Quarterback Rating:**

Der allergrößte Kritikpunkt ist auch der offensichtlichste: ESPN verrät
freilich nicht, wie die genaue Formel zur Berechnung des QBR aussieht.
Man wird also quasi mit einer Blackbox konfrontiert, die am Ende einen
Wert ausspuckt und man muß ihm vertrauen.

Es ist daher nicht möglich zu sagen, ob wirklich die Unzulänglichkeiten
des alten Ratings komplett ausgemerzt sind, besonders die
Willkürlichkeit, die Ungenauigkeit und die Redundanz. Es kann natürlich
durchaus auch im QBR vorkommen, dass beispielsweise die *Completion
Percentage* zu hoch bewertet wird - siehe meinen Artikel über das Passer
Rating - allein beim QBR wird man es nie erfahren. (Da ESPN aber
scheinbar kräftig die Arbeit von Brian Burke nutzt, sollte dieser Punkt
berücksichtigt worden sein, da Burke oft und viel Kritik in diese
Richtung geäußert hat.)

Ein weiterer Kritikpunkt ist, dass das QBR nicht wirklich einfach ist.
Es ist keine Formel, die jeder, der die Quarterback-Stats kennt, selbst
nachrechnen kann (selbst wenn ESPN die Formel freigegeben würde ginge
das nicht), da *play-by-play*-Daten faktisch nicht verfügbar sind und
außer ESPN wohl auch nur wenige Institutionen genug Ressourcen haben, um
diese Daten dann auch entsprechend auszuwerten und aufzubereiten.

Einen anderen Kritikpunkt räumt ESPN sogleich selbst ein: Das QBR
behandelt jeden Sieg gleich, also egal ob es ein 45-3 ist oder ein
24-23. Auch wenn man etwas nebulös sagt, dass sehr wohl Details
eingingen, so dass diese Tatsache doch entsprechend berücksichtigt
werden würde. (Es wäre interessant zu erfahren, ob Reguar Season-Spiele
anders gewertet werden als Playoff- oder gar Super Bowl-Spiele).

Als letzten Kritikpunkt möchte ich den *clutch index* anführen. Auch
hier bleibt völlig ungewiss, wie er genau errechnet wird. Es lässt viel
Freiraum, wenn man einfach sagt, dass der *clutch index* berücksichtigt,
wie sehr ein Spielzug die Gewinnwahrscheinlichkeit beeinflusst. Auch der
*Handoff* zum Runningback wird nicht mit berücksichtigt, wie ESPN
zugibt. Dabei ist beispielsweise für einen guten *Draw*-Spielzug die
Fähigkeit eines Quarterbacks den Handoff zu verstecken durchaus
entscheidend und sollte deswegen mit in das Rating einfliessen.

**Fazit:**

Es gibt einiges am neuen *Total Quarterback Rating*zu kritisieren, vor
allem, dass die Details zur Berechnung unbekannt bleiben. Man muss ESPN
aber dafür loben, soviel Arbeit und auch Geld in die Entwicklung
gesteckt zu haben. Denn es ist das erste Quarterback-Rating, dass
wirklich jeden Spielzug berücksichtigt und versucht ihn sinnvoll
gewichtet mit in die Berechnung einfliessen zu lassen. Das ist ein
wirklich revolutionärer Ansatz!

Man sollte ESPN für das *QBR* Respekt zollen, aber nicht vergessen, dass
es am Ende nur eine Statistik ist, deren genaue Umstände man nie
erfahren wird und deren Bedeutung daher wohl auch recht gering bleiben
wird.

  [der Artikel direkt bei ESPN empfohlen]: http://espn.go.com/nfl/story/_/id/6833215/explaining-statistics-total-quarterback-rating
