Title: Sag' mir deine Punkte und ich sag' dir wie oft du gewinnst!
Date: 2011-10-05 12:16
Author: footballissexbaby
Tags: Football, Prediction, Pythagorean expectation, Sabermetrics, Stats
Slug: sag-mir-deine-punkte-und-ich-sag-dir-wie-oft-du-gewinnst

Ich habe in diesem Blog ja schon recht viel über die Sagarin-Rankings
gesagt, die ich sehr mag und die meiner Meinung nach auch gut zur
Vorhersage von Spielergebnissen taugen. Jedoch kann ich damit nur sagen,
welches Team das stärkste ist und wie ein bestimmtes Spiel wohl ausgehen
würde. Ich weiß damit aber noch nicht, wie oft denn eine Mannschaft am
Ende tatsächlich gewinnen wird.

Um das zu schaffen, gibt es eine Größe, die sich pythagoräische
Erwartung (engl. *"Pythagorean expectation"*) nennt. Sie wurde in den
früher 80ern von Bill James entwickelt, um im Baseball anhand von
erlaubten und erzielten Runs einfach feststellen zu können, wie oft
welche Mannschaft gewinnen wird. Die Formel ist verblüffend einfach:

![Pythagorean Expectation][]

Im Football sind PF die erzielten Punkte (*Points for*) und PA sind die
Punkte, die der Gegner erzielen konnte (*Points against*). In Bill
James' ursprünglicher Formel war x = 2. Daher auch der Name
pythagoräische Erwartung, da diese Gleichung eine gewisse Ähnlichkeit
zum Satz von Pythagoras hat.

Für Football klappt das mit dem Exponenten 2 aber nicht wirklich gut.
Daher wurde (wohl recht willkürlich) gesagt, dass für die NFL ein
Exponent von 2.37 am besten passt. Das war allerdings auch nie ein
wirklich passender Exponent.

Ist die pythagoräische Erwartung also ein schlechtes Maß im Football
oder wurde sie einfach nie richtig benutzt?

Dieser Frage hat sich der von mir sehr geschätzte David Myers von Code
and Football [etwas genauer angenommen][]. Er hat die Formel in der
obigen Form genommen und hat mittels vorhandenen
Sieg-Niederlagen-Verhältnissen für vergangene Saisons den jeweils am
besten passenden Exponenten ermittelt.

Sein Ergebnis für die Saison 2010: x = 2.657!

Das einzige Problem ist: Wenn man den Exponenten nach der Saison
ermittelt, dann sagt er einem nur, wie jedes Team hätte abschneiden
*sollen*, aber nicht, wie es tatsächlich abgeschnitten *hat*.

Ermittelt man aber den aktuellen Exponenten, also nach nur einem Viertel
der Saison, dann wird vernachlässigt, dass Spiele im Winter ganz anders
ausgehen, als Spiele im September und Oktober. Man hat dann also eine zu
optimistische Schätzung vorgenommen, da die Ergebnisse im letzten
Saisondrittel für gewöhnlich niedriger ausfallen.

Das beste wäre es daher, den Exponenten der Vorsaison und den aktuellen
Exponenten *angemessen*zu wichten. Dazu habe ich zwar einige Ideen, aber
leider hatte ich noch keine Zeit, das zu verfolgen
(Pro-Football-Reference hat dazu [hier][] schon was getan, allerdings
bin ich mit dem Ansatz nicht richtig zufrieden).

Daher habe ich meine Implementierung der pythagoräischen Erwartung, die
schon seit Monaten in irgendeiner Schublade lag, genommen und geschaut,
was sich mit diesem Exponenten von 2.657 für die
<span style="text-decoration:underline;">aktuelle</span> NFL-Saison
ergeben sollte. Danach habe ich den aktuellen Exponenten ausgerechnet (x
= 3.872) und die Berechnung wiederholt.

Das Ergebnis sieht wie folgt aus:

![PythExp2011][]

*PW new x*sind die Siege gemäß pythagoräischer Erwartung mit dem
aktuellen Koeffizienten, *PW old x* ist dasselbe mit dem Koeffizienten
aus 2010 und *Scaled Rec* ist der momentane Record jedes Teams mit 4
multipliziert, da wir ja gerade das erste Saisonviertel hinter uns
haben.

Obwohl der Exponent für die laufende Saison fast 50% größer ist als der
für 2010, so ist die Siegvorhersage doch recht ähnlich, es ist nie mehr
als ein Sieg Abweichung. Der Scaled Record ist natürlich nicht
aussagekräftig, ich habe ihn nur zur Veranschaulichung hinzugefügt, um
einen besseren Eindruck zu bekommen.

Die pythagoräische Erwartung trifft also mit sehr wenigen Annahmen
starke Vorhersagen. Ähnlich wie in die Sagarin-Rankings gehen nur die
Punkte ein, hier jedoch nicht für jedes einzelne Spiel, sondern die
kumulativen Punkte jedes Teams. Außerdem ist man im Gegensatz zu den
Sagarin-Rankings in der Lage, Aussagen über eine *Saison*und nicht nur
über ein einzelnes Spiel zu treffen.

Wie immer muss man eine solche Größe natürlich mit gewisser Vorsicht
betrachten. Aber die pythagoräische Erwartung ist ein guter Indikator,
ob ein Team bisher viel Pech hatte (z. B. Minnesota Vikings) oder ob es
schon einige glückliche Siege eingefahren hat (Cleveland Browns).

 

  [Pythagorean Expectation]: http://footballissexbaby.de/wordpress/wp-content/uploads/2011/10/pythexp.png
    "PythExp.png"
  [etwas genauer angenommen]: http://codeandfootball.wordpress.com/2011/04/22/the-pythagorean-expectation-in-football/
  [hier]: http://www.pro-football-reference.com/blog/?p=337
  [PythExp2011]: http://footballissexbaby.de/wordpress/wp-content/uploads/2011/10/pythexp2011.png
    "PythExp2011.png"
