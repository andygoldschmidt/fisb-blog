Title: Spieglein, Spieglein an der Wand...
Date: 2013-01-31 18:47
Author: footballissexbaby
Category: Footballmetrics
Tags: Baltimore Ravens, Football, NFL, San Francisco 49ers, Team Similarity
Slug: spieglein-spieglein-an-der-wand

Betrachtet man Matchups in der NFL, dann zieht man immer wieder
Vergleiche zu ähnlichen Aufeinandertreffen. Team A hat gegen Team B gut
gespielt, Team C ist ähnlich wie Team B, also wird Team A auch gegen C
gut aussehen.

Abgesehen davon, dass diese Transitivität nie erfüllt ist, ist es doch
eine Überlegung wert, welche Teams einem bestimmten Team am ähnlichsten
sind.

Um die Ähnlichkeit zwischen zwei Teams zu berechnen, reicht es nicht,
einfach die Differenz zwischen den Offense-Yards der beiden Teams zu
berechnen. Vielmehr braucht man möglichst aussagekräftige Parameter, die
die Leistung eines Teams möglichst gut widerspiegeln.

Hat man diese Parameter, kann man die Differenz zwischen beiden Teams
berechnen und die Unterschiede zwischen allen Parametern summieren. Doch
dabei kommt nix Brauchbares rum. Warum ist ganz einfach erklärt: Ist der
eine Parameter beispielsweise die Pass-Yards pro Versuch, so hat der die
Größenordnung von sagen wir 7 Yards pro Versuch. Nehmen wir als zweiten
Parameter die Interception-Quote, dann ist ein typischer Wert 0.03.

Bildet man also nur die Differenzen und addiert diese zusammen, dann
wird alles von der Abweichung in den Pass-Yards pro Versuch bestimmt.
Wir brauchen also Koeffizienten, die uns sagen, wie wir jeden einzelnen
Parameter gewichten müssen. Dazu greife ich dreisterweise auf [die
hervorragende Arbeit von Brian Burke zurück][].

Die verwendeten Parameter mitsamt Koeffizienten sind:

<table class="table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Wert</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Off NY/A</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>Off Rush Y/A</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Off Int Rate</td>
      <td>-19.4</td>
    </tr>
    <tr>
      <td>Off Fmb Rate</td>
      <td>-19.4</td>
    </tr>
    <tr>
      <td>Def NY/A</td>
      <td>-0.62</td>
    </tr>
    <tr>
      <td>Def Rush Y/A</td>
      <td>-0.25</td>
    </tr>
  </tbody>
</table>

Nun ist es ein leichtes die Abweichung zwischen Team A und Team B zu
berechnen:

[latex size="1"]\\Delta = \\sum\_i \\left(c\_i \\cdot \\left(A\_i -
B\_i\\right)\\right) \^ 2[/latex]

Es wäre sehr unübersichtlich die Ähnlichkeit aller 32 Teams mit 31
anderen Teams hier zu zeigen, daher stellvertretend die
Ähnlichkeitsgraphen für die beiden diesjährigen Super Bowl-Teilnehmer.
Die Daten sind so skaliert, dass das ähnlichste Team den Wert 1 hat und
das unähnlichste den Wert 0, je höher ein Wert umso ähnlicher.

### Baltimore Ravens

[![Ravens Team Similarity][]][Ravens Team Similarity]

### San Francisco 49ers

[![49ers Team Similarity][]][49ers Team Similarity]

**Ein kleines Tool, um die Ähnlichkeiten aller Teams anzuzeigen,  
[habe ich hier veröffentlicht][].**

Das alles ist natürlich eher eine Spielerei als eine echte Analyse,
dennoch ist es interessant zu sehen, welche Teams sich gleichen und
welche grundverschieden sind. Viel Spaß beim Rumspielen!

<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">

  MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
    }
  });
</script>

  [die hervorragende Arbeit von Brian Burke zurück]: http://www.advancednflstats.com/2009/01/how-model-works-detailed-example.html
  [Ravens Team Similarity]: |filename|/images/ravens.png
  [49ers Team Similarity]: |filename|/images/49ers.png
  [habe ich hier veröffentlicht]: http://footballissexbaby.de/team-similarity/
