Title: Die vielen Gesichter der pythagoräischen Erwartung. Teil 1 (Update)
Date: 2012-03-05 16:52
Author: footballissexbaby
Tags: Baseball Prospectus, Bill James, Clay Davenport, David Smyth, Football Outsiders, Modelle..., NFL, Pythagenpat, Pythagenport, Pythagorean expectation, Taktik, Zahlen
Slug: die-vielen-gesichter-der-pythagoraischen-erwartung-teil-1


<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

In dieser Artikelreihe möchte ich mich ([mal wieder)][] mit der
pythagoräischen Erwartung  beschäftigen. Allerdings soll diesmal nicht
der eigentliche Zweck beleuchtet werden, sondern ich möchte drei
verschiedene "Arten" der pythagoräischen Erwartung analysieren und
vergleichen. In diesem ersten Teil soll es zunächst um die mathematische
Seite gehen: was unterscheidet die Methoden, welche korreliert am besten
mit den Ergebnissen?
 

**Welche Methoden gibt es?**

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

 

**Was unterscheidet die Methoden?**

Bevor wir uns ansehen, was die Methoden unterscheidet, erst einmal etwas
das alle drei Methoden gemein haben, nämlich die generelle
zugrundeliegende Gleichung:

$\\text{Wins} = \\frac{\\mathrm{PF}^x}{\\mathrm{PF}^x +
\\mathrm{PA}^x} \\text{bzw.} \\frac{1}{1 +
\\left(\\frac{\\text{PA}}{\\text{PF}}\\right)^x}$

*(Anmerkung: PF bezeichnet die eigenen Punkte (points for), PA die durch
den Gegner erzielten (points against), N steht, sofern nicht anders
vermerkt, für die Anzahl der Spiele = Woche.)*

Der Unterschied zwischen den drei Methoden besteht einzig darin, wie sie
den Exponenten $x$ berechnen:

**Pythagorean**: $x \\in \\mathbb{R}^+$ (d.h. der Exponent
$x$ kann jede beliebige Zahl größer Null sein).

**Pythagenport**: $x = 1.5 \* \\log\\left(\\frac{\\mathrm{PF} +
\\mathrm{PA}}{\\mathrm{N}}\\right) + 0.45$

**Pythagenpat**: $x = \\left(\\frac{\\mathrm{PF} +
\\mathrm{PA}}{\\mathrm{N}}\\right)^{0.287}$


Da ich jedoch kein Fan von dahergelaufenen Zahlen bin (und erst recht
nicht, wenn sie 1:1 vom Baseball auf Football übertragen werden), habe
ich für die letzten fünf Spielzeiten der NFL die jeweils besten
Parameter berechnet. (D.h. also für **Pythagorean** den ganzen
Exponenten, für **Pythagenport** habe ich die 1.5 und die 0.45 optimiert
und für **Pythagenpat** die 0.287.)

**Zeig mir Zahlen!**

Schauen wir uns also an, wie welche Methode mit den tatsächlichen
Ergebnissen korreliert, wenn man die berechneten optimalen Parameter
annimmt:

<table class="table">
<tbody>
<tr>
<td><strong>Saison 2007</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.92543</td>
<td>2.50850</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.93802</td>
<td>11.96681, -16.66700</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.92832</td>
<td>0.25062</td>
</tr>
</tbody>
</table>
</td>
<td><strong>Saison 2008</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.90727</td>
<td>2.62363</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.90752</td>
<td>1.30551, 0.53111</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.90748</td>
<td>0.26110</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><strong>Saison 2009</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.91411</td>
<td>2.28975</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.93097</td>
<td>10.74376, -14.88259</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.91744</td>
<td>0.22697</td>
</tr>
</tbody>
</table>
</td>
<td><strong>Saison 2010</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.90575</td>
<td>2.65693</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.90746</td>
<td>4.17667, -4.06568</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.90684</td>
<td>0.26402</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><strong>Saison 2011</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.90930</td>
<td>2.60967</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.91748</td>
<td>5.90139, -6.86662</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.91315</td>
<td>0.26116</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><strong>Durchschnitt 2007-2011</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>opt. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.91231</td>
<td>2.53770</td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.91822</td>
<td>6.81883, -8.39016</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.91466</td>
<td>0.25277</td>
</tr>
</tbody>
</table>
</td>
<td><strong>Durchschnitt mit Standardparametern</strong>
<table class="table">
<thead>
<tr>
<th>Methode</th>
<th>Korrelation</th>
<th>bek. Parameter</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pythagorean</td>
<td>0.91259</td>
<td><a href="http://www.pro-football-reference.com/blog/?p=337">2.37</a></td>
</tr>
<tr>
<td>Pythagenport</td>
<td>0.91360</td>
<td>1.5, 0.45</td>
</tr>
<tr>
<td>Pythagenpat</td>
<td>0.91395</td>
<td>0.287</td>
</tr>
</tbody>
</table>
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

$x = 1.5 \*
\\log\\left(\\frac{\\mathrm{PF}+\\mathrm{PA}}{\\mathrm{N}}\\right)$

Das hat den Vorteil, dass die Optimierung dadurch deutlich stabiler
wird. Die Korrelation für diese Formel mit den Spieldaten von 2007-2011
ist 0.91511. Optimiert man den Parameter, so ergibt sich anstatt 1.5 ein
optimaler Parameter von 1.58, allerdings bei einer etwas schlechteren
Korrelation. Aber wie bereits erwähnt, ist die Korrelation bei der
pythagoräischen Erwartung nicht alles.

**Update:**
*Ich hatte leider einen kleinen Fehler in der Berechnung meiner
**Pythagenport**-Formel. Das ist jetzt behoben und die obigen Ergebnisse
wurden korrigiert. Den Text unter der Tabelle habe ich entsprechend
angepasst.*

Weiterlesen:

-   [Teil 2][]
-   [Teil 3][]

  [mal wieder)]: |filename|sag-mir-deine-punkte-und-ich-sag-dir-wie-oft-du-gewinnst.md
  [Baseball Prospectus]: http://www.baseballprospectus.com/
  [Football Outsiders]: http://www.footballoutsiders.com/
  [2.37]: http://www.pro-football-reference.com/blog/?p=337
  [Teil 2]: |filename|die-vielen-gesichter-der-pythagoraischen-erwartung-teil-2.md
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 2"
  [Teil 3]: |filename|die-vielen-gesichter-der-pythagoraischen-erwartung-teil-3.md
    "Die vielen Gesichter der pythagoräischen Erwartung. Teil 3"
