Title: Pythagorean class
Date: 2012-03-12 18:35
Author: footballissexbaby
Slug: pythagorean-class-footballmetrics-1-0-documentation

 

<div class="related">
### <span class="Apple-style-span" style="font-size: 26px;">Pythagorean class[¶][]</span>

</div>
<div class="document">
<div class="documentwrapper">
<div class="bodywrapper">
<div class="body">
<div id="module-pythagoreans" class="section">
*class*`pythagoreans.`{.descclassname}`Pythagorean`{.descname}<big>(</big>*dataDict*<big>)</big>[¶][1]
:   This is a super class for the different types of the Pythagorean
    expectation. It is called with a dictionary containing the teams,
    scores and number of played games (i.e. given week).
    </p>
    -   self.calculateExponent - Formula for the exponent x.
    -   self.guess - Initial guess for the optimization

    `calculatePythagorean`{.descname}<big>(</big>*optimize=True*, *staticParams=None*<big>)</big>[¶][2]
    :   Returns the predictions and power for all given teams. An
        optimatization for the exponent formula is performed, if
        optimize is set to True. If set to False the static exponent
        parameters need to be given as a list.
        </p>

    `getOptimalFitParams`{.descname}<big>(</big><big>)</big>[¶][3]
    :   Returns the optimal fit parameters retrieved from
        scipy.optimize.fmin in calculatePythagorean().
        </p>

</div>
</div>
</div>
</div>
</div>
 

<div class="sphinxsidebar">
<div class="sphinxsidebarwrapper">
#### Previous topic

[The Pythagoreans module][]

#### Next topic

[PythagoreanExpectation class][]

### This Page

-   [Show Source][]

<div id="searchbox" style="display: none;">
### Quick search

<form class="search" action="search.html" method="get">
<input type="text" name="q"></input>
<input type="submit" value="Go"></input>
<input type="hidden" name="check_keywords" value="yes"></input>
<input type="hidden" name="area" value="default"></input>

</form>
Enter search terms or a module, class or function name.

</div>
<p>
<script type="text/javascript">// <br />
$('#searchbox').show(0);<br />
// </script>
</p>
</div>
</div>
<div class="clearer">
</div>
<div class="related">
### Navigation

-   [index][]
-   [modules][] |
-   [next][] |
-   [previous][] |
-   [Footballmetrics 1.0 documentation][] »
-   [The Pythagoreans module][4] »

</div>
<div class="footer">
© Copyright 2012, Andy Goldschmidt. Created using [Sphinx][] 1.1.2.

</div>
 

  [¶]: #module-pythagoreans "Permalink to this headline"
  [1]: #pythagoreans.Pythagorean "Permalink to this definition"
  [2]: #pythagoreans.Pythagorean.calculatePythagorean
    "Permalink to this definition"
  [3]: #pythagoreans.Pythagorean.getOptimalFitParams
    "Permalink to this definition"
  [The Pythagoreans module]: http://footballissexbaby.de/wordpress/?page_id=471
    "previous chapter"
  [PythagoreanExpectation class]: http://footballissexbaby.de/wordpress/?page_id=465
    "next chapter"
  [Show Source]: _sources/PythagoreanClass.txt
  [index]: http://footballissexbaby.de/wordpress/?page_id=468
    "General Index"
  [modules]: http://footballissexbaby.de/wordpress/?page_id=470
    "Python Module Index"
  [next]: http://footballissexbaby.de/wordpress/?page_id=465
    "PythagoreanExpectation class"
  [previous]: http://footballissexbaby.de/wordpress/?page_id=471
    "The Pythagoreans module"
  [Footballmetrics 1.0 documentation]: http://footballissexbaby.de/wordpress/?page_id=469
  [4]: http://footballissexbaby.de/wordpress/?page_id=471
  [Sphinx]: http://sphinx.pocoo.org/
