Title: Die vielen Gesichter der pythagoräischen Erwartung. Teil 1 (Update)
Date: 2012-03-05 16:52
Author: footballissexbaby
Tags: Baseball Prospectus, Bill James, Clay Davenport, David Smyth, Football Outsiders, Modelle..., NFL, Pythagenpat, Pythagenport, Pythagorean expectation, Taktik, Zahlen
Slug: die-vielen-gesichter-der-pythagoraischen-erwartung-teil-1

In dieser Artikelreihe möchte ich mich ([mal wieder)][] mit der
pythagoräischen Erwartung  beschäftigen. Allerdings soll diesmal nicht
der eigentliche Zweck beleuchtet werden, sondern ich möchte drei
verschiedene "Arten" der pythagoräischen Erwartung analysieren und
vergleichen. In diesem ersten Teil soll es zunächst um die mathematische
Seite gehen: was unterscheidet die Methoden, welche korreliert am besten
mit den Ergebnissen?

 

**<span style="text-decoration: underline;">Welche Methoden gibt
es?</span>**

Ich betrachte hier drei verschiedene Methoden zur Berechnung der
pythagoräischen Erwartung:

-   die "klassische" von Bill James entwickelte pythagoräische Erwartung
    (**Pythagorean**),
-   die von Clay Davenport von [Baseball Prospectus][] entwickelte
    **Pythagenport**-Formel, die mittlerweile auch von [Football
    Outsiders][] benutzt wird,
-   und die von David Smyth entwickelte (und für Baseball effektivste
    Formel) **Pythagenpat**. (Das *pat* leitet sich von Patriot ab,
    allerdings bin ich nicht sicher, woher das stammt.)

* (Soweit ich weiß, sind das die drei relevanten Formen. Falls es noch
mehr wichtige Formeln gibt, bitte nicht zögern einen Kommentar zu
hinterlassen!)*

 

**<span style="text-decoration: underline;">Was unterscheidet die
Methoden?</span>**

Bevor wir uns ansehen, was die Methoden unterscheidet, erst einmal etwas
das alle drei Methoden gemein haben, nämlich die generelle
zugrundeliegende Gleichung:

[latex]\\text{Wins} = \\frac{\\mathrm{PF}\^x}{\\mathrm{PF}\^x +
\\mathrm{PA}\^x} \\text{bzw.} \\frac{1}{1 +
\\left(\\frac{\\text{PA}}{\\text{PF}}\\right)\^x}[/latex]

*(Anmerkung: PF bezeichnet die eigenen Punkte (points for), PA die durch
den Gegner erzielten (points against), N steht, sofern nicht anders
vermerkt, für die Anzahl der Spiele = Woche.)*

Der Unterschied zwischen den drei Methoden besteht einzig darin, wie sie
den Exponenten [latex]x[/latex] berechnen:

**Pythagorean**: [latex]x \\in \\mathbb{R}\^+[/latex] (d.h. der Exponent
[latex]x[/latex] kann jede beliebige Zahl größer Null sein).

**Pythagenport**: [latex]x = 1.5 \* \\log\\left(\\frac{\\mathrm{PF} +
\\mathrm{PA}}{\\mathrm{N}}\\right) + 0.45[/latex]

**Pythagenpat**: [latex]x = \\left(\\frac{\\mathrm{PF} +
\\mathrm{PA}}{\\mathrm{N}}\\right)\^{0.287}[/latex]

 

Da ich jedoch kein Fan von dahergelaufenen Zahlen bin (und erst recht
nicht, wenn sie 1:1 vom Baseball auf Football übertragen werden), habe
ich für die letzten fünf Spielzeiten der NFL die jeweils besten
Parameter berechnet. (D.h. also für **Pythagorean** den ganzen
Exponenten, für **Pythagenport** habe ich die 1.5 und die 0.45 optimiert
und für **Pythagenpat** die 0.287.)

 

**<span style="text-decoration: underline;">Zeig mir Zahlen!</span>**

Schauen wir uns also an, wie welche Methode mit den tatsächlichen
Ergebnissen korreliert, wenn man die berechneten optimalen Parameter
annimmt:

<table border="0" cellspacing="20">
<tbody>
<tr>
<td>
**Saison 2007**

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- ---------------------
  Pythagorean    0.92543       2.50850
  Pythagenport   0.93802       11.96681, -16.66700
  Pythagenpat    0.92832       0.25062

</td>
<td>
**Saison 2008**

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- ------------------
  Pythagorean    0.90727       2.62363
  Pythagenport   0.90752       1.30551, 0.53111
  Pythagenpat    0.90748       0.26110

</td>
</tr>
<tr>
<td>
**Saison 2009**

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- ---------------------
  Pythagorean    0.91411       2.28975
  Pythagenport   0.93097       10.74376, -14.88259
  Pythagenpat    0.91744       0.22697

</td>
<td>
**Saison 2010**

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- -------------------
  Pythagorean    0.90575       2.65693
  Pythagenport   0.90746       4.17667, -4.06568
  Pythagenpat    0.90684       0.26402

</td>
</tr>
<tr>
<td>
**Saison 2011**

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- -------------------
  Pythagorean    0.90930       2.60967
  Pythagenport   0.91748       5.90139, -6.86662
  Pythagenpat    0.91315       0.26116

</td>
</tr>
<tr>
<td>
<span style="color: #ff0000;">**Durchschnitt 2007-2011**</span>

</p>
  Methode        Korrelation   opt. Parameter
  -------------- ------------- -------------------
  Pythagorean    0.91231       2.53770
  Pythagenport   0.91822       6.81883, -8.39016
  Pythagenpat    0.91466       0.25277

</td>
<td>
<span style="color: #ff0000;">**Durchschnitt mit
Standardparametern**</span>

</p>
  Methode        Korrelation   bek. Parameter
  -------------- ------------- ----------------
  Pythagorean    0.91259       [2.37][]
  Pythagenport   0.91360       1.5, 0.45
  Pythagenpat    0.91395       0.287

</td>
</tr>
</tbody>
</table>
*(Der Durchschnitt mittelt die jeweiligen Parameter. Diese wurden dann
wiederum auf alle Daten von 2007-2011 angewendet. Die Korrelation ergibt
sich aus den gemittelten fünf Einzelkorrelationen. Der "Durchschnitt mit
Standardparameter" ergibt sich aus der Berechnung der pyth. Erwartung
mit den nicht-optimierten Parametern.)*  
Die **Pythagenport**-Formel liefert also in *jeder*Saison die beste
Korrelation. Im Durchschnitt der letzten fünf Jahre ist die Korrelation
allerdings*weniger als 1%* besser als die von **Pythagorean** und
**Pythagenpat**. Gleichzeitig sieht man für **Pythagenport** einen
ziemlichen Ausreißer für die Fitparameter der Saison 2008. Die anderen
beiden Methoden liefern nicht so grobe Ausreißer, was einfach auch daran
liegt, dass es deutlich stabiler ist einen Parameter zu optimieren statt
zwei.  
Insgesamt finde ich persönlich die **Pythagenport**-Formel etwas zu
"umständlich". Darüber hinaus bedeutet die beste Korrelation im Falle
der pythagoräischen Erwartung nicht zwangsläufig die besten Ergebnisse,
da die pyth. Erwartung angibt, wie oft ein Team hätte gewinnen *sollen*,
nicht wie oft es tatsächlich gewonnen *hat*.  
Interessant ist, dass die **Pythagenpat**-Formel besser als
**Pythagenport** abschneidet, wenn man die Parameter *nicht optimiert*.

Football Outsiders setzt in seiner Pythagenport-Formel den 2. Parameter
übrigens gleich Null, ihre Formel lautet demnach:

[latex]x = 1.5 \*
\\log\\left(\\frac{\\mathrm{PF}+\\mathrm{PA}}{\\mathrm{N}}\\right)[/latex]

Das hat den Vorteil, dass die Optimierung dadurch deutlich stabiler
wird. Die Korrelation für diese Formel mit den Spieldaten von 2007-2011
ist 0.91511. Optimiert man den Parameter, so ergibt sich anstatt 1.5 ein
optimaler Parameter von 1.58, allerdings bei einer etwas schlechteren
Korrelation. Aber wie bereits erwähnt, ist die Korrelation bei der
pythagoräischen Erwartung nicht alles.

**<span style="text-decoration: underline;">Update</span>:** *Ich hatte
leider einen kleinen Fehler in der Berechnung meiner
**Pythagenport**-Formel. Das ist jetzt behoben und die obigen Ergebnisse
wurden korrigiert. Den Text unter der Tabelle habe ich entsprechend
angepasst.*

Weiterlesen:

-   [Teil 2][]
-   [Teil 3][]

  [mal wieder)]: http://footballissexbaby.de/2011/10/sag-mir-deine-punkte-und-ich-sag-dir-wie-oft-du-gewinnst/
  [Baseball Prospectus]: http://www.baseballprospectus.com/
  [Football Outsiders]: http://www.footballoutsiders.com/
  [2.37]: http://www.pro-football-reference.com/blog/?p=337
  [Teil 2]: http://footballissexbaby.de/2012/03/die-vielen-gesichter-der-pythagoraischen-erwartung-teil-2/
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 2"
  [Teil 3]: http://footballissexbaby.de/2012/06/die-vielen-gesichter-der-pythagoraischen-erwartung-teil-3/
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 3"
