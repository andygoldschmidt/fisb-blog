Title: Quarterbacks 2013 - In die Schublade gesteckt
Date: 2014-02-16 18:00
Author: footballissexbaby
Category: Analyse
Tags: Quarterbacks, Clustering
Slug: quarterbacks-2013-in-die-schublade-gesteckt


*Es ist bereits eine Weile her, seitdem ich über die [Time of Possession](|filename|time-of-possession-irrelevant-oder-nuetzlich.md) geschrieben habe. Seitdem war es bis auf einen [Gastbeitrag für Sideline Reporter](http://sidelinereporter.wordpress.com/2013/12/01/nfl-sonntagsvorschauer-2013-week-13/) mal wieder ziemlich ruhig. Doch jedes Warten hat irgendwann eine Ende und so gibt es jetzt endlich mal wieder einen neuen Beitrag.*


Der Super Bowl ist vorbei. Bis zur Free Agency und zum Draft vergeht noch etwas Zeit. Was also in der Zwischenzeit machen? Wie wäre es mit einer Runde des allseits beliebten: *Welcher Quarterback ist Elite und wer ist einfach nur doof*. Doch in diesem Blog verlasse ich mich wie immer nicht auf *Pundits*, sondern vielmehr auf statistische und mathematische Methoden und Modelle.

Wer die folgende mathematische (aber einfach nachzuvollziehende) Ausführung überspringen will, [kommt hier direkt zu den Ergebnissen](#results).

## Die Mathematik hinter der Kategorisierung

Es gibt unzählige Möglichkeiten, um Dinge zu kategorisieren bzw. zu *klassifizieren*, um es korrekt auszudrücken. Generell unterscheidet man aber zwei Arten: *supervised* und *unsupervised* classification; also überwachtes und nicht-überwachtes Klassifizieren.

Überwacht heißt in diesem Zusammenhang, dass man eine sogenannte Trainingsmenge hat, bei der man das Ergebnis bereits kennt und das Modell anhand dieser bekannten Daten lernen lässt. Beispielsweise könnte man ein paar Zahlen auf ein Blatt Papier malen und ein Modell trainieren, das anhand dessen zukünftige Zahlen eigenständig erkennen kann.

Nicht-überwachte Klassifizierung kann man immer dann nutzen, wenn man keine vorher bekannten Ergebnisse hat. Man hat also eine Reihe an Messwerten bzw. Beobachtungen, weiß aber nicht, wie die korrekte Einteilung ist. Genau dieses Problem haben wir bei der Einordnung von Quarterbacks: wir kennen zwar die jeweiligen Statistiken aller Spieler, aber wir haben keine Kategorien und erst recht keine Einteilung in diese, die in irgendeiner Weise objektiv wäre.

Die einfachste Methode, die es bei der nicht-überwachten Klassifizierung hat, ist das sogenannte [**k-means clustering**](http://de.wikipedia.org/wiki/K-Means-Algorithmus).

### k-means clustering

Der Ausdruck *k-means* bezieht sich auf die Anzahl der Cluster (bzw. Kategorien) **k** und die Tatsache, dass man in seinen Daten nach genau k Mittelwerten (*means*) sucht.

Um das Verfahren zu erläutern, ist es am einfachsten, dass man sich eine 2-dimensionale Ebene vorstellt, durch die die Daten dargestellt werden; beispielsweise die Körpergröße und das Gewicht. Auf dieser Ebene findet man nun alle möglichen Kombinationen von Größe und Gewicht. Nun sagen wir einfach, es gibt 2 Cluster (also k=2). Dazu setzen wir willkürlich 2 Punkte in die Ebene und ermitteln für jeden einzelnen Messwert, ob er näher zu Cluster 1 oder Cluster 2 liegt. Anschließend verschieben wir den Mittelpunkt des Clusters in das Zentrum der zum Cluster gehörenden Messpunkte. Wieder schaut man, welcher Cluster für jeden einzelnen Messpunkt am nächsten ist und wiederholt diese Prozedur, bis sich nicht mehr wesentlich etwas ändert.

Man hat also folgenden Ablauf (**Lloyd-Algorithmus**):

1. Cluster-Mittelpunkte willkürlich verteilen
2. Jedem Messpunkt dem nächstliegenden Cluster zuweisen (**assignment step**, Zuordnung)
3. Cluster-Mittelpunkt in das Zentrum der zugehörigen Messwerte verschieben (**update step**, Aktualisierung)

Die Schritte 2 und 3 wiederholt man, bis zur Konvergenz.

*Anmerkung: Im praktischen Einsatz verwendet man klügere Anfangsbedingungen und ausgefeiltere Methoden, um eine möglichst schnelle, rechenarme Konvergenz zu erreichen.*

### Die Datenlage

Um die Statistiken von Spielern zu bekommen, gibt es weiterhin keinen besseren Ort als [Pro Football Reference](http://pro-football-reference.com). Dort gibt eine [hervorragende Übersicht](http://www.pro-football-reference.com/years/2013/passing.htm) über alle Passing-Leistungen des vergangenen Jahres.

Natürlich braucht man nicht alle Statistiken, um einen Quarterback zu kategorisieren, zumal viele auch redundant wären. Ich habe daher folgende 5 Statistiken ausgewählt:

* Completion Percentage
* Touchdown Percentage
* Interception Percentage
* Sack Percentage
* Net Yards per Attempt (NY/A)

Ich bevorzuge es, wenn möglich, immer mit relativen Werten (sprich Prozenten) zu rechnen, da somit der Einfluss von besonders vielen/wenigen Versuchen reduziert wird und in ein entsprechendes Verhältnis zur Anzahl der Passversuche gesetzt wird.

In *NY/A* wird die Passerleistung gewissermaßen mit den Sacks bereinigt: man reduziert die Yards durch Passing um die Sack-Yards (*Net Yards*) und rechnet die Anzahl der Pässe mit der Anzahl an Sacks zusammen, anschließend dividiert man beide durcheinander. Man sieht also, dass die letzten beiden Metriken nicht komplett unabhängig voneinander sind; jedoch ist NY/A nicht allzu sehr von den Sacks beeinflusst, so dass es gerechtfertigt scheint, die Sacks als extra Variable in die Berechnung einfließen zu lassen.

Nur Spieler, die mehr als 100 Passversuche hatten, wurden betrachtet; damit wurden also Quarterbacks, die nur 2-3 Series gespielt haben sowie Trickspieler, wie WR, die mal einen Pass werfen, ausgeschlossen.

Bevor wir in die Kategorisierung gehen, lohnt es sich anzusehen, wie die Verteilung der Datenpunkte zwischen den einzelnen Metriken ist:

![](|filename|/images/qb2013_clustering.png)

Auf der Diagonalen sieht man die sogenannte **Kernel Density Estimation (KDE)**, vereinfacht gesagt ist das die Verteilung der Werte für die jeweilige Größe. In den anderen Feldern sieht man für jede Kombination die Auftragung aller Metrik-Pärchen gegeneinander.

Einige Plots sehen sehr zufällig aus, beispielsweise *Int% - Sk%*, wogegen man bei einigen anderen schon mit bloßen Auge gewisse "Kategorien" erahnen kann, z.B. bei *Cmp% - NY/A*.

### Die Berechnung

Um das eigentlich Klassifizieren durchzuführen, braucht man eigentlich nur noch recht wenig machen. Tools wie die Programmiersprache Python nehmen einem den Großteil der Arbeit ab, in dem man auf hervorragende Pakete zur Datenverarbeitung und -Analyse zurückgreifen kann.

Exemplarisch im Folgenden der Code, um auf den heruntergeladenen (und gefilterten) Daten eine Clusterung durchzuführen:

	:::python
	import pandas as pd
	from sklearn.cluster import KMeans
	df = pd.read_csv("qb2013.csv")
	cluster = KMeans(n_clusters=4)
	cluster.fit(df)

Man lädt zwei zusätzliche Module, einmal Pandas für die Datenanalyse und KMeans fürs Clustering. Danach liest man in der 3. Zeile die Daten ein, initialisiert den K-Means-Algorithmus in der folgenden Zeile und zum Abschluss wendet man den Algorithmus auf die eingelesenen Daten an... *easy as pie*!

Wie man in Zeile 3 sehen kann, haben wir *n_clusters* auf 4 gesetzt, d.h. wir wollen die Quarterbacks in 4 Cluster einteilen.
Die folgende Tabelle zeigt die Mittelwerte der Metriken für jede der resultierenden Kategorien:

<table class="table">
	<thead>
		<tr>
			<th>Gruppe</th>
			<th>Cmp%</th>
			<th>TD%</th>
			<th>Int%</th>
			<th>Sack%</th>
			<th>NY/A</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td><td>67.27</td><td>6.34</td><td>1.57</td><td>5.60</td><td>7.42</td>
		</tr>
		<tr>
			<td>2</td><td>61.64</td><td>4.57</td><td>2.80</td><td>5.55</td><td>6.29</td>
		</tr>
		<tr>
			<td>3</td><td>60.23</td><td>3.89</td><td>2.66</td><td>8.71</td><td>5.73</td>
		</tr>
		<tr>
			<td>4</td><td>54.99</td><td>3.30</td><td>3.54</td><td>6.49</td><td>5.94</td>
		</tr>
	</tbody>
</table>

Es lässt sich streiten, ob es sinnvoll ist, vier Kategorien zu nehmen oder doch lieber 5 oder nur 3. Aber genau das ist das Problem bei k-means und nicht-überwachtem Klassifizieren im Allgemeinen: man muss raten und handelt sich damit immer etwas Subjektivität ein. Ein Anzeichen, warum vier Cluster nicht allzu schlecht sind, ist die Interpretierbarkeit:

Der 1. Cluster enthält offensichtlich die Überflieger: hohe Completion Percentage, hohe NY/A, viele Touchdowns und wenige Interceptions. Cluster 4 beinhaltet Quarterbacks mit deutlich schlechterer Completion Percentage und einer viel höheren Fehlerquote und deutlich weniger Raumgewinn pro Versuch.

Die Cluster 2 und 3 unterscheiden sich zwar nicht in der Completion Percentage, aber in der relativen Anzahl an Touchdowns und Sacks eben schon, auch die NY/A sind bei Gruppe 2 deutlich höher, diese QB's erzielen fast einen halben Yard mehr pro Versuch.

Doch kommen wir nun endlich zu den Ergebnissen.


## <a name="results"></a>Die Ergebnisse

### Gruppe 1: Die Elite

Diese Gruppe beinhaltet die statistisch allerbesten Quarterbacks der Saison 2013. Der Cluster-Algorithmus hat 7 Spieler in diese Kategorie einsortiert.

<table class="table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Cmp %</th>
            <th>TD %</th>
            <th>Int %</th>
            <th>Sack %</th>
            <th>Net Yards/Attempt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
			<td>Aaron Rodgers</td><td>GNB</td><td>66.6</td><td>5.9</td><td>2.1</td><td>6.8</td><td>7.78</td>
		</tr>
		<tr>
			<td>Nick Foles</td><td>PHI</td><td>64.0</td><td>8.5</td><td>0.6</td><td>8.1</td><td>7.88</td>
		</tr>
		<tr>
			<td>Josh McCown</td><td>CHI</td><td>66.5</td><td>5.8</td><td>0.4</td><td>4.7</td><td>7.63</td>
		</tr>
		<tr>
			<td>Philip Rivers</td><td>SDG</td><td>69.5</td><td>5.9</td><td>2.0</td><td>5.2</td><td>7.54</td>
		</tr>
		<tr>
			<td>Drew Brees</td><td>NOR</td><td>68.6</td><td>6.0</td><td>1.8</td><td>5.4</td><td>7.16</td>
		</tr>
		<tr>
			<td>Matt Ryan</td><td>ATL</td><td>67.4</td><td>4.0</td><td>2.6</td><td>6.3</td><td>6.07</td>
		</tr>
		<tr>
			<td>Peyton Manning</td><td>DEN</td><td>68.3</td><td>8.3</td><td>1.5</td><td>2.7</td><td>7.91</td>
		</tr>
    </tbody>
</table>

Es überrascht wenig, dass die unstrittig besten Quarterbacks in dieser Kategorie landen: Peyton Manning, Aaron Rodgers, Drew Brees und Philip Rivers.

Überraschender sind schon Nick Foles und Josh McCown. Beide haben gut gespielt, vor allem Foles auch über viele Spiele, aber beide profitieren auch von einer extrem geringen Interception-Quote von weniger als einer Interception  in 100 Versuchen, die auf lange Sicht so nicht haltbar ist. Aber man muss beiden zugute halten, dass sie in den anderen Metriken nicht hinter dem Rest der Gruppe zurückliegen und teils auch da Spitzenwerte erreichen.

Während Foles und McCown Ausreißer in einer einzelnen Metrik sind, muss man sagen, dass Matt Ryan ein ganz typischer *Outlier* (statistischer Ausreißer) ist. Er hat eine gute Completion Percentage, aber das war es auch schon. In keiner Kategorie außer der Sackquote kann er auch nur ansatzweise mit dem Rest mithalten. Doch solche Ausreißer gehören leider bei solchen Analysen dazu und sind eine bekannte Schwachstelle der meisten (simplen) Clustering-Algorithmen. Ryan würde mit seiner Leistung eher zur 2. Garde gehören.


### Gruppe 2: Die 2. Garde

Die 2. Garde besteht aus Quarterbacks, die jeden Fan zufriedenstellen sollten, aber die niemandem zu permantenten Begeisterungsstürmen verleiten. Sie sind in allen Kategorien signifikant schwächer als die "Elite-Gruppe", auch wenn ihre Leistungen für sich betrachtet immer noch gut sind.

<table class="table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Cmp %</th>
            <th>TD %</th>
            <th>Int %</th>
            <th>Sack %</th>
            <th>Net Yards/Attempt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
			<td>Matt Cassel</td><td>MIN</td><td>60.2</td><td>4.3</td><td>3.5</td><td>5.9</td><td>6.38</td>
		</tr>
		<tr>
			<td>Ryan Fitzpatrick</td><td>TEN</td><td>62.0</td><td>4.0</td><td>3.4</td><td>5.7</td><td>6.32</td>
		</tr>
		<tr>
			<td>Jay Cutler</td><td>CHI</td><td>63.1</td><td>5.4</td><td>3.4</td><td>5.1</td><td>6.66</td>
		</tr>
		<tr>
			<td>Matt Schaub</td><td>HOU</td><td>61.2</td><td>2.8</td><td>3.9</td><td>5.5</td><td>5.67</td>
		</tr>
		<tr>
			<td>Carson Palmer</td><td>ARI</td><td>63.3</td><td>4.2</td><td>3.8</td><td>6.7</td><td>6.5</td>
		</tr>
		<tr>
			<td>Tom Brady</td><td>NWE</td><td>60.5</td><td>4.0</td><td>1.8</td><td>6.0</td><td>6.12</td>
		</tr>
		<tr>
			<td>Andy Dalton</td><td>CIN</td><td>61.9</td><td>5.6</td><td>3.4</td><td>4.7</td><td>6.69</td>
		</tr>
		<tr>
			<td>Ben Roethlisberger</td><td>PIT</td><td>64.2</td><td>4.8</td><td>2.4</td><td>6.7</td><td>6.36</td>
		</tr>
		<tr>
			<td>Sam Bradford</td><td>STL</td><td>60.7</td><td>5.3</td><td>1.5</td><td>5.4</td><td>5.74</td>
		</tr>
		<tr>
			<td>Tony Romo</td><td>DAL</td><td>63.9</td><td>5.8</td><td>1.9</td><td>6.1</td><td>6.24</td>
		</tr>
		<tr>
			<td>Andrew Luck</td><td>IND</td><td>60.2</td><td>4.0</td><td>1.6</td><td>5.3</td><td>5.97</td>
		</tr>
		<tr>
			<td>Matthew Stafford</td><td>DET</td><td>58.5</td><td>4.6</td><td>3.0</td><td>3.5</td><td>6.82</td>
		</tr>
    </tbody>
</table>

Die meisten der 12 Namen sind nicht sonderlich überraschend. Klar, Quarterbacks wie Tom Brady verbindet man instinktiv mit dem Begriff *Elite*, schaut man sich seine Metriken aber an, sieht man, dass statistisch eben schon noch einiges dafür fehlt, um mit Drew Brees oder gar Peyton Manning im gleichen Satz genannt zu werden (zumindest 2013).

Mir fällt in dieser Gruppe kein Quarterback auf, dem ich das Label "2. Garde" entziehen oder den ich als krassen Ausreißen betrachten würde. Jeder einzelne dieser Quarterbacks ist in der Lage NFL-Spiele zu gewinnen und alle haben es auch bereits unter Beweis gestellt.


### Gruppe 3: Die zaudernden Checkdown-Captains?

Oh, was für ein Name! Aber wenn ich auf die Zahlen schaue, fällt mir einfach kein besserer Name ein. Wenige Fehler, aber vor allem wenige Touchdowns und wenige Yards pro Versuch. Und das ganze begleitet von einer beachtlich hohen Sackquote (ja, die Sackquote beeinflusst die NY/A).

<table class="table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Cmp %</th>
            <th>TD %</th>
            <th>Int %</th>
            <th>Sack %</th>
            <th>Net Yards/Attempt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
			<td>Russell Wilson</td><td>SEA</td><td>63.1</td><td>6.4</td><td>2.2</td><td>9.8</td><td>6.84</td>
		</tr>
		<tr>
			<td>EJ Manuel</td><td>BUF</td><td>58.8</td><td>3.6</td><td>2.9</td><td>8.4</td><td>5.43</td>
		</tr>
		<tr>
			<td>Kellen Clemens</td><td>STL</td><td>58.7</td><td>3.3</td><td>2.9</td><td>8.0</td><td>5.84</td>
		</tr>
		<tr>
			<td>Colin Kaepernick</td><td>SFO</td><td>58.4</td><td>5.0</td><td>1.9</td><td>8.6</td><td>6.52</td>
		</tr>
		<tr>
			<td>Mike Glennon</td><td>TAM</td><td>59.4</td><td>4.6</td><td>2.2</td><td>8.8</td><td>5.03</td>
		</tr>
		<tr>
			<td>Christian Ponder</td><td>MIN</td><td>63.6</td><td>2.9</td><td>3.8</td><td>10.2</td><td>5.75</td>
		</tr>
		<tr>
			<td>Robert Griffin III</td><td>WAS</td><td>60.1</td><td>3.5</td><td>2.6</td><td>7.7</td><td>5.93</td>
		</tr>
		<tr>
			<td>Cam Newton</td><td>CAR</td><td>61.7</td><td>5.1</td><td>2.7</td><td>8.3</td><td>5.9</td>
		</tr>
		<tr>
			<td>Chad Henne</td><td>JAX</td><td>60.6</td><td>2.6</td><td>2.8</td><td>7.0</td><td>5.54</td>
		</tr>
		<tr>
			<td>Matt Flynn</td><td>3TM</td><td>62.0</td><td>4.0</td><td>2.5</td><td>10.7</td><td>5.61</td>
		</tr>
		<tr>
			<td>Alex Smith</td><td>KAN</td><td>60.6</td><td>4.5</td><td>1.4</td><td>7.1</td><td>5.67</td>
		</tr>
		<tr>
			<td>Terrelle Pryor</td><td>OAK</td><td>57.4</td><td>2.6</td><td>4.0</td><td>10.2</td><td>5.26</td>
		</tr>
		<tr>
			<td>Thaddeus Lewis</td><td>BUF</td><td>59.2</td><td>2.5</td><td>1.9</td><td>10.3</td><td>5.67</td>
		</tr>
		<tr>
			<td>Ryan Tannehill</td><td>MIA</td><td>60.4</td><td>4.1</td><td>2.9</td><td>9.0</td><td>5.44</td>
		</tr>
		<tr>
			<td>Joe Flacco</td><td>BAL</td><td>59.0</td><td>3.1</td><td>3.6</td><td>7.3</td><td>5.42</td>
		</tr>
		<tr>
			<td>Jake Locker</td><td>TEN</td><td>60.7</td><td>4.4</td><td>2.2</td><td>8.0</td><td>5.78</td>
		</tr>
    </tbody>
</table>

Sieht man sich die Namen auf der Liste ein, dann weiß man, warum ich ein Fragezeichen hinter die Gruppenbezeichnung gesetzt habe. Es sind eben vor allem die mobilen Quarterbacks, die in diese Gruppe fallen.

Das erklärt auch zu einem guten Teil die hohe Sackquote, da mobile Quarterbacks im Allgemeinen nicht die Geduldigsten in der Pocket sind und dadurch eben oft im Backfield zu Fall gebracht werden. Vor allem Russell Wilson würde wohl mit einer niedrigeren Sackquote in die 2. oder sogar die 1. Gruppe aufrücken.

Da diese Quarterbacks eine teilweise komplett andere (durch die Metriken nicht gut abgedeckte) Spielweise haben, ist es eigentlich etwas ungerecht sie in eine 3. Gruppe zu stecken, vielmehr sind sie eine Art *Gruppe 2b*.


### Gruppe 4: Die Fehlerteufel

Im Gegensatz zur 3. Gruppe werden die Fehlerteufel ihrem Namen vollkommen gerecht. Diese Spieler bringen nicht viele Pässe an den Mann, finden kaum die Endzone und werfen zu viele Interceptions. Noch dazu ist die Ausbeute ihrer Pässe auch yardmäßig nicht gut.

<table class="table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Cmp %</th>
            <th>TD %</th>
            <th>Int %</th>
            <th>Sack %</th>
            <th>Net Yards/Attempt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
			<td>Case Keenum</td><td>HOU</td><td>54.2</td><td>3.6</td><td>2.4</td><td>7.0</td><td>5.73</td>
		</tr>
		<tr>
			<td>Matt McGloin</td><td>OAK</td><td>55.9</td><td>3.8</td><td>3.8</td><td>2.8</td><td>6.88</td>
		</tr>
		<tr>
			<td>Michael Vick</td><td>PHI</td><td>54.6</td><td>3.5</td><td>2.1</td><td>9.6</td><td>7.15</td>
		</tr>
		<tr>
			<td>Jason Campbell</td><td>CLE</td><td>56.8</td><td>3.5</td><td>2.5</td><td>4.8</td><td>5.74</td>
		</tr>
		<tr>
			<td>Kirk Cousins</td><td>WAS</td><td>52.3</td><td>2.6</td><td>4.5</td><td>3.1</td><td>5.14</td>
		</tr>
		<tr>
			<td>Geno Smith</td><td>NYJ</td><td>55.8</td><td>2.7</td><td>4.7</td><td>8.8</td><td>5.62</td>
		</tr>
		<tr>
			<td>Eli Manning</td><td>NYG</td><td>57.5</td><td>3.3</td><td>4.9</td><td>6.6</td><td>5.99</td>
		</tr>
		<tr>
			<td>Brandon Weeden</td><td>CLE</td><td>52.8</td><td>3.4</td><td>3.4</td><td>9.2</td><td>5.28</td>
		</tr>
    </tbody>
</table>

Keine Überraschungen in dieser Gruppe: Jeder der die NFL verfolgt hat, weiß, dass jeder dieser Spieler es verdient hat in der Schlussgruppe zu landen.


## Fazit

Football ist ein sehr komplexer Sport und es ist nie leicht oder vollkommen richtig, wenn man mit wenigen Zahlen versucht Spieler in eine Schublade zu stecken. Zumal der angewendete Algorithmus ebenfalls sehr einfach ist (sowohl von der Benutzung als auch der inneren Funktionsweise).

K-Means-Clustering neigt darüber hinaus zur Nichtinterpretierbarkeit. Doch wenn man nur wenige Datenpunkte in wenige Kategorien einsortiert (wie in diesem Fall) ist das ein umgehbares Problem; auch wenn Gruppe 3 gewisse Tücken in der Interpretation aufweist.

Insgesamt finde ich, dass diese Einteilung der Quarterbacks durchaus die subjektiv wahrgenommenen Leistungen widerspiegelt, jedoch ohne Wert auf vergangene Erfolge zu legen, was bei Experten eigentlich immer ein Problem ist.


### P.S.

Wer sich die Auswertung genauer ansehen möchte, [findet die Analyse hier](https://prod-vz-22.wakari.io:9008/notebook_relative/football/QB_2013_clustering.ipynb).
