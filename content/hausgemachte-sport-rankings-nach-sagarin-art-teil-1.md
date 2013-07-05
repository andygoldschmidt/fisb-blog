Title: Hausgemachte Sport-Rankings nach Sagarin-Art, Teil 1
Date: 2011-05-31 00:41
Author: footballissexbaby
Tags: Football, GFL, Ranking-Systeme, Sagarin
Slug: hausgemachte-sport-rankings-nach-sagarin-art-teil-1

So, dann wollen wir doch gleich mal anfangen!

In meinem ersten Eintrag möchte ich mich mit "[Homemade Sagarin
Ratings"][] beschäftigen.

Jeff Sagarin veröffentlicht seit den 1980er Jahren seine
computergenerierten Sport-Rankings für verschiedene US-Ligen, zu finden
sind diese auf usatoday.com. Seine Vorhersagen werden oftmals für die in
den USA beliebten Fantasy-Ligen benutzt und auch in die Rankings der
College-Football-Liga fließen seine Modelle ein.

Wie macht Sagarin das?

Das ist natürlich nicht so ganz klar, allerdings beschreibt Sagarin auf
seiner Seite, dass er eine Methode hat, die ganz und gar nur die Siege
und Niederlagen der Teams heranzieht (Elochess-Methode) und eine andere,
in die nur die erzielten Punkte einfließen, kombiniert mit einem
gewissen Heimvorteil.

In diesem Artikel wollen wir uns mit letzterer Methode beschäftigen.

Vorweg noch ein Kommentar: Da in diese Ranking-Methode nur die jeweilig
erzielten Punkte einfließen ist es auf so ziemlich jede (Team-)Sportart
anwendbar, egal ob Football, Fußball oder Volleyball!

Die "Homemade Sagarin Ratings" lassen sich nun relativ leicht berechnen.
Man braucht lediglich die Ergebnisse der bisher ausgetragenen Ligaspiele
und muss wissen, wer jeweils das Heimteam war. Nun legt man einen
beliebigen Heimvorteil fest, im Football ist es wohl sinnvoll 3 Punkte,
also ein Field Goal, anzunehmen, im Fußball geht man von einem Tor extra
aus (dieser Wert wird nachher mit angepasst, so dass der Anfangswert
nicht so kritisch ist). Zusätzlich gibt man jedem Team der Liga ein
Anfangs-Rating, auch das ist nicht so kritisch, man kann beispielsweise
allen Teams den Wert 1 zuweisen.

Nun berechnet man für alle bisherigen Partien den vorhergesagten Ausgang
(also Rating des Heimteams minus Rating des Auswärtsteams) und zieht
diese Differenz von der tatsächlichen Punktdifferenz ab und addiert
abschließend noch den Heimvorteil. Die Abweichung die sich ergibt wird
nun noch quadriert (man berechnet die Varianz) und alle einzelnen
Abweichungen werden summiert (quadratische Abweichung).

Das Ziel ist es, diese quadratische Abweichung möglichst klein zu
machen, also das Modell in Übereinstimmung mit der Wirklichkeit zu
bringen. Das geschieht, in dem man alle Team-Ratings und den Wert des
Heimvorteils variiert.

(Wie man so etwas programmatisch löst, wird im 2. Teil beschrieben)

Was kommt nun heraus, wenn man diese Methode auf die German Football
League loslässt? Nicht überraschendes, alles ist plausibel und jeder der
sich in der Liga etwas auskennt, wird mit der Reihenfolge der Teams grob
übereinstimmen.

Im Anschluß ein Bild der Situation vorm letzten Spieltag (Stand: 25. Mai
2011):

![Ratings gfl][]

 

 

 

 

 

 

 

 

Das beste Team sind die Kiel Baltic Hurricanes, was bei einer makellosen
Bilanz von 3 Siege nicht weiter überrascht und schlechteste Teams sind
Essen und Plattling, die noch sieglos auch nicht ganz grundlos dort
unten stehen.

Versuchen wir mit der Methode doch einmal die Begegnungen vom Wochenende
28./29. 5. vorherzusagen:

Dresden Monarchs - Düsseldorf Panther: **Monarchs +2**, Abweichung: 3

Mönchengladbach Mavericks - Kiel Baltic Hurricanes: **Baltic Hurricanes
+4**, Abweichung: 3

Wiesbaden Phantoms - Marburg Mercenaries: **Mercenaries + 26**,
Abweichung: 12

Saarland Hurricanes - Munich Cowboys: **Hurricanes +3**, Abweichung: 9

Essen Assindia Cardinals - Braunschweig FFC: **Braunschweig +34**,
Abweichung: 8

Plattling Black Hawks - Stuttgart Scorpions: **Scorpions +26**,
Abweichung: 20

 

Es wurde nur bei einem Spiel der falsche Sieger vorhergesagt! (Saarland
- München). Zwar wichen die tatsächlichen Scores teils erheblich ab,
doch die Tendenz stimmt fast immer! Nicht zu vergessen, dass manche
Teams zu dem Zeitpunkt erst 2 Spiele gespielt haben, z.B. Marburg, was
natürlich die Vorhersage unsicherer macht, als wenn schon die Hälfte der
Saison gespielt ist!

Man sieht also, dass man mit sehr einfachen Annahmen einen guten
Eindruck bekommen kann, wer in welchem Spiel die beste Siegchance hat
und für Optimisten sogar, wie deutlich der Sieg ausfallen wird.

 

Beim nächsten Post gibt es dann eine Erklärung, wie man das Ganze nun
tatsächlich umsetzen kann und wie jeder selbst mit den Ratings
rumspielen kann.

Bis dahin!

  [Homemade Sagarin Ratings"]: http://www.advancednflstats.com/2008/05/homemade-sagarin-ratings.html
  [Ratings gfl]: http://footballissexbaby.de/wordpress/wp-content/uploads/2011/05/ratings_gfl.png
    "ratings_gfl.png"
