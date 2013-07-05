Title: PythagoreanExpectation class
Date: 2012-03-12 18:35
Author: footballissexbaby
Slug: pythagoreanexpectation-class-footballmetrics-1-0-documentation

 

<div class="related">
### <span class="Apple-style-span" style="font-size: 26px;">PythagoreanExpectation class[¶][]</span>

</div>
<div class="document">
<div class="documentwrapper">
<div class="bodywrapper">
<div class="body">
<div id="module-pythagoreans" class="section">
*class*`pythagoreans.`{.descclassname}`PythagoreanExpectation`{.descname}<big>(</big>*dataDict*<big>)</big>[¶][1]
:   Implementation of the classical Pythagorean expectation.
    </p>
    `getOptimalFitParams`{.descname}<big>(</big><big>)</big>[¶][2]
    :   Returns the optimal fit parameters retrieved from
        scipy.optimize.fmin in calculatePythagorean().
        </p>

    `calculatePythagorean`{.descname}<big>(</big>*optimize=True*, *staticParams=None*<big>)</big>[¶][3]
    :   Returns the predictions and power for all given teams. An
        optimatization for the exponent formula is performed, if
        optimize is set to True. If set to False the static exponent
        parameters need to be given as a list.
        </p>

</div>
</div>
</div>
</div>
</div>
 

<div class="sphinxsidebar">
<div class="sphinxsidebarwrapper">
#### Previous topic

[Pythagorean class][]

#### Next topic

[Pythagenport class][]

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
-   [The Pythagoreans module][] »

</div>
<div class="footer">
© Copyright 2012, Andy Goldschmidt. Created using [Sphinx][] 1.1.2.

</div>
 

  [¶]: #module-pythagoreans "Permalink to this headline"
  [1]: #pythagoreans.PythagoreanExpectation
    "Permalink to this definition"
  [2]: #pythagoreans.PythagoreanExpectation.getOptimalFitParams
    "Permalink to this definition"
  [3]: #pythagoreans.PythagoreanExpectation.calculatePythagorean
    "Permalink to this definition"
  [Pythagorean class]: http://footballissexbaby.de/wordpress/?page_id=464
    "previous chapter"
  [Pythagenport class]: http://footballissexbaby.de/wordpress/?page_id=463
    "next chapter"
  [Show Source]: _sources/PythagoreanExpectationClass.txt
  [index]: http://footballissexbaby.de/wordpress/?page_id=468
    "General Index"
  [modules]: http://footballissexbaby.de/wordpress/?page_id=470
    "Python Module Index"
  [next]: http://footballissexbaby.de/wordpress/?page_id=463
    "Pythagenport class"
  [previous]: http://footballissexbaby.de/wordpress/?page_id=464
    "Pythagorean class"
  [Footballmetrics 1.0 documentation]: http://footballissexbaby.de/wordpress/?page_id=469
  [The Pythagoreans module]: http://footballissexbaby.de/wordpress/?page_id=471
  [Sphinx]: http://sphinx.pocoo.org/
