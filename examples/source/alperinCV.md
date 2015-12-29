<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script type='text/javascript'>
  $( document ).ready(function() {
    // clean up some dd's that don't have a p
    $("dd:not(:has('p'))").each(function(i, element) { 
      $(element).wrapInner('<p></p>');
    });

    $.getScript('stats-ir.js', function() {
      article_stats = data[0]['stats']['articles'];

      $('a').each(function(i, element) { 
        var href = $(element)[0].getAttribute('href');
        if ($(element)[0].innerHTML.indexOf('doi.org') == 0 ) {

          var doi = $(element)[0].innerHTML;
          doi = doi.substr(doi.indexOf('/') + 1);  // strip out doi.org/ 
          $($(element)[0]).closest('dd').append('<div data-badge-popover="right" data-badge-type="2" data-doi="' + doi + '" data-hide-no-mentions="true" class="altmetric-embed"></div>');
            metrics = true;
        } else if (href.indexOf('scholar.google.com') > 0) {
          var gsid = href.substring(href.indexOf('cites=') + 6)
          for (var i=0; i<article_stats.length; i++) {
            if (article_stats[i][0].indexOf(gsid) > 0) {
              $($(element)[0]).closest('dd').append('<div class="google-scholar"><a href="' + href +'" ><img src="scholar_logo_long.png" align="left" /></a><span class="metricbubble">' + article_stats[i][1] + '</span></div>');
              $(element).remove()
            }
          }
        } 
      });  
    });

    $.getScript("https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js", function() {
        $('head').append('<link rel="stylesheet" href="altmetric-overrides.css" type="text/css" />')
    });

    // Do some link handling
    $("a").attr('target','_blank');

    // change links called "link" to icon
    $("a").filter(function() {
      return $(this).text() === "link";
    }).addClass("externalLink").attr('alt', 'link to open access version');

    // change links called "video" to icon
    $("a").filter(function() {
      return $(this).text() === "video";
    }).addClass("videoLink").attr('alt', 'link to video');

    // change links called "slides" to icon
    $("a").filter(function() {
      return $(this).text() === "slides";
    }).addClass("slidesLink").attr('alt', 'link to slides').attr('title', 'link to slides');

  });
</script>



# Juan Pablo Alperin
## Assistant Professor

> [Download PDF](alperinCV.pdf)
>

------

### Education {#education}

PhD Education, Stanford University 
: Multidisciplinary Studies in Education
  __2015__

Masters of Arts, University of Waterloo
: Geography
  __2008__

Bachelor of Mathematics, University of Waterloo
: Computer Science Honours, Combinatorics & Optimization Minor
  __2003__

------

### Employment {#employment}

Assistant Professor
  : Simon Fraser University
  __2014__

-------

### Research Interests {#research}

1. scholarly communication
2. altmetrics
3. open source
4. open access
5. higher education
6. publishing technologies
7. digital media
8.
9.

------

### Teaching {.singlespace}

Seminar Courses 
 : PUB802: Technology and the Evolving Forms of Publishing, Graduate [link](http://tkbr.ccsp.sfu.ca/pub802)
 __2015, 2016__
 : PUB401: Technology and the Evolving Book, Undergraduate  [link](http://tkbr.ccsp.sfu.ca/pub401)
__2014, 2015__

Project Courses
 : PUB607: Publishing Technology Project, Graduate [link](http://tkbr.ccsp.sfu.ca/pub607)
 __2014, 2015, 2016__ 

Lecture Courses
 : PUB101: Publication of Self in Everyday Life, Undergraduate
 __2014__

Guest Lectures
 : Escribir para Publicar, National University de Colombia 
 __Nov. 2014__
 : The Emergence of Latin American Science, University of Costa Rica
 __Mar. 2012__

Section Leader
 : STS1: The Public Life of Science Technology & Society
 __Winter 2013__

 Workshops
 : Web Scraping in Python, Stanford University
 __Summer 2013__
 
 : Latin American Open Access Publishing Workshop Series, nine countries
 __2007-2010__
 
------

### Research Projects {#funding .five-column}
1. Title
2. Role
3. Funder
4. Total
5. Year

1. Understanding Societal Impact of Research through Social Media
2. Principal Investigator
3. SSHRC
4. (Submitted) CA$285,901
5. 2015

1. Incentivizing Open Peer-Review
2. Co-Principal Investigator
3. OpenAire
4. U$27,600
5. 2015-2016

1. Engaging Publics in Openness Initiatives
2. Co-Principal Investigator
3. SIRCA-IDRC 
4. U$15,950 
5. 2015-2016

1. Smarter Texts for Advancing Public Knowledge
2. Co-Investigator
3. CIRA
4. CA$75,000 
5. 2015-2016

1. Open Access indicators: Assessing growth and use of OA
resources from developing regions
2. Principal Investigator
3. UNESCO
4. U$50,000
5. 2013-2014

1. Smarter Scholarly Texts
2. Consultant
3. MediaX (Stanford)
4. U$150,000
5. 2012-2016

1. Quality in the Open Scholarly Communication of Latin America
2. Co-Investigator
3. IDRC
4. U$350,000
5. 2011-2014

1. Strengthening Scholarly Communication in Latin America
2. Co-Investigator
3. IDRC
4. U$50,000 
5. 2007-2009

------
### Publications

Edited Volumes
: **Alperin, J.P.** *&* Fischman, G.E. *Made in Latin America: Open Access, Scholarly Journals, and Regional Innovations*, Buenos Aires: CLACSO. [link](http://www.clacso.org.ar/libreria-latinoamericana/libro_detalle.php?id_libro=1001&pageNum_rs_libros=0&totalRows_rs_libros=966)
__2015__

: **Alperin, J.P.**, Babini, D., *&* Fischman, G.E. *Open Access Indicators and Scholarly Communications in Latin America*, Buenos
Aires: CLACSO. [link](http://www.clacso.org.ar/libreria-latinoamericana/libro_detalle.php?id_libro=906&pageNum_rs_libros=1&totalRows_rs_libros=824) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=8352684746038389618)
__2014__

Select Peer-Reviewed Publications
: Carvalho Neto, S, Willinsky, J. & **Alperin, J.P.** Measuring, Rating, Supporting, and Strengthening Open Access Scholarly Publishing in Brazil. *Transinformaçao*.
__submitted__

: **Alperin, J.P.** The Public Impact of Latin America's Approach to Open Access. Doctoral Dissertation, Stanford University. [link](http://purl.stanford.edu/jr256tk1194) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=2304846227896743763) 
__2015__

: **Alperin, J.P.** Geographic variation in social media metrics: an analysis of Latin American journal articles, *Aslib Journal of Information Management* 67(3). [link](https://purl.stanford.edu/sr068mj0031) [doi.org/10.1108/AJIM-12-2014-0176](http://doi.org/10.1108/AJIM-12-2014-0176) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=14244773496994540438)
__2015__

 : Garnett, A., **Alperin, J.P.**, Willinsky, J. The Public Knowledge Project XML Publishing Service and meTypeset: Don't call it "Yet Another Word-to-JATS Conversion Kit", *JATS-Con Proceedings 2015*, Bethesda: National Center for Biotechnology Information. [link](http://www.ncbi.nlm.nih.gov/books/NBK279666/)
__2015__

: **Alperin, J.P**. Brazil's Exception to the World-Class University Movement. *Quality in Higher Education*, 19. [link](https://purl.stanford.edu/cp475cd5409) [doi.org/10.1080/13538322.2013.802573](http://doi.org/10.1080/13538322.2013.802573) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7663946573571325985)
__2013__

: **Alperin, J.P.**, Fischman, G.E., *&* Willinsky, J. Scholarly Communication Strategies in Latin America’s Research Universities. *Educación Superior y Sociedad*, 16. [link](https://purl.stanford.edu/fj828hg2133) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=603210712826963713)
__2011__

: Fischman, G.E., **Alperin, J.P.**, *&* Willinsky, J. Visibility and Quality in Spanish-Language Latin American Scholarly Publishing. *Information Technologies & International Development*, 6. [link](http://itidjournal.org/index.php/itid/article/view/639/274) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=2339300654326134976)
__2010__

: **Alperin, J.P.**, Fischman, G.E., *&* Willinsky, J. “Open Access and Scholarly Publishing in Latin America: Ten flavours and a few reflections”. *Liinc em Revista*, 4. [link](http://revista.ibict.br/liinc/index.php/liinc/article/view/269) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=18358168313039408295)
__2008__

Book Chapters 
: Shamash, K., **Alperin, J.P.** & Bordini, A.*Teaching Data Analysis in the Social Sciences: A Case Study with Article Level Metrics.* In Atenas, J. *&* Havemann, L. (Eds) Open Data as an Open Education Resource, London: Open Knowledge Foundation. [link](http://doi.org/10.6084/m9.figshare.1590031) [doi.org/10.6084/m9.figshare.1590031](http://doi.org/10.6084/m9.figshare.1590031)
__2015__

: **Alperin, J.P.** *&* Fischman, G.E. Scientific Journals Produced in Latin America. In **Alperin, J.P.** *&* Fischman, G.E. (eds.) (2015). *Made in Latin America Open Access, Scholarly Journals, and Regional Innovations*, Buenos Aires: CLACSO. [link](http://www.clacso.org.ar/libreria-latinoamericana/libro_detalle.php?id_libro=1001&pageNum_rs_libros=0&totalRows_rs_libros=966)
__2015__

: Fischman, G.E. *&* **Alperin, J.P.** About Lights and Shadows: Latin American Scientific Journals. In **Alperin, J.P.** *&* Fischman, G.E. (eds.) (2015). *Made in Latin America Open Access, Scholarly Journals, and Regional Innovations*, Buenos Aires: CLACSO. [link](http://www.clacso.org.ar/libreria-latinoamericana/libro_detalle.php?id_libro=1001&pageNum_rs_libros=0&totalRows_rs_libros=966)
__2015__

: **Alperin, J.P.** Assessing the Growth and Use of Open Access Resources from Developing Regions: The Case of Latin America, Open Access Indicators and Scholarly Communications. In **Alperin, J.P.**, Babini, D., *&* Fischman, G.E. (eds.) (2014). Open Access Indicators and Scholarly Communications in Latin America, Buenos Aires: CLACSO. [link](http://www.clacso.org.ar/libreria-latinoamericana/libro_detalle.php?id_libro=906&pageNum_rs_libros=1&totalRows_rs_libros=824) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=13918265887449564160)
__2014__

: Fischman, G.E., **Alperin, J.P.**, *&* Willisnky, J. Old and New Challenges for Scholarly Communications in Spanish. In Cetto A.M., *&* Alonso O. *Quality and Impact of Ibero-American Scientific Journals*. Mexico: UNAM.
__2011__

Invited Publications
: **Alperin, J.P.** *&* Taylor, M. Science without borders: are technology and policy limiting internationalization? *ResearchTrends.* 37. [link](http://www.researchtrends.com/issue-37-june-2014/science-without-borders/)
__2014__

: **Alperin, J.P.** Ask Not What Altmetrics Can Do for You, but What Altmetrics Can Do for Developing Countries. *Bulletin of the American Society for Information Science and Technology*, 39. [link](https://www.asis.org/Bulletin/Apr-13/AprMay13_Alperin.html) [doi.org/10.1002/bult.2013.1720390407](http://doi.org/10.1002/bult.2013.1720390407) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=17529319604071970957)
__2013__

: Willinsky, J. *&* **Alperin, J.P.** The Academic Ethics of Open Access to Research and Scholarship. *Ethics and Education.* 6. [link](https://purl.stanford.edu/dg951ry1612) [doi.org/10.1080/17449642.2011.632716](http://doi.org/10.1080/17449642.2011.632716) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=1154013045948546741)
__2012__

Other Publications
: **Alperin, J.P.,** Bordini, A., Pouyanne, S. PLOS, Please publish our articles on Wednesdays: A look at altmetrics by day of publication, *The Winnower*. [link](http://doi.org/10.15200/winn.142972.29198) [doi.org/10.15200/winn.142972.29198](http://doi.org/10.15200/winn.142972.29198)
__2015__

: **Alperin, J.P.** South America: Citation databases omit local journals, *Nature*. [doi.org/10.1038/511155c](http://doi.org/10.1038/511155c) [Google Scholar](https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7472416283065230354)
__2014__

: **Alperin, J.P.** Altmetrics could enable scholarship from developing countries to receive due recognition. *LSE Impact Blog.* [link](http://blogs.lse.ac.uk/impactofsocialsciences/2014/03/10/altmetrics-for-developing-regions/)
__March 10, 2014__

: **Alperin. J.P.** Academic Publishing in a Global Context: The Politics and Practices of Publishing in English. *Journal of Scholarly Publishing*, 42 (4), 545-549. [doi.org/10.1353/scp.2011.0034](http://doi.org/10.1353/scp.2011.0034)
__2011__

------

### Presentations 
Invited Presenations 
: **Alperin, J.P.** Openness in Higher Education: From the Classroom to the Research. *SFU/UBC Open Access Week*. [link](https://blogs.ubc.ca/bcrlglectures/2015/10/17/open-for-collaboration-a-special-event-for-open-access-week/) [slides](https://speakerdeck.com/jalperin/openness-in-higher-education-from-the-classroom-to-the-research)
__Oct. 22, 2015__

: **Alperin, J.P.** Do Things Get Better in Scholarly Publishing?. *PKP Scholarly Publishing Conference 2015.* Vancouver, Canada. [video](https://pkp.sfu.ca/pkp2015/paper/view/524/351)
__Aug. 13, 2015__

: **Alperin, J.P.** Students, Open Access *&* Libraries. *The SPARC-ACRL Forum on Emerging Issues in Scholarly Communication*. San Francisco, USA. [link](http://sparc.arl.org/advancing-%E2%80%98open%E2%80%99-through-library-partnerships-students-and-early-career-researchers)
__June 25, 2015__

: **Alperin, J.P.** The Public Impact of Open Access: A survey of the SciELO research portal. *Advancing Research and Scholarship Conference (ARCSCon)*. Philadelphia, USA. [link](http://doi.org/10.6084/m9.figshare.1391771) [doi.org/10.6084/m9.figshare.1391771](http://doi.org/10.6084/m9.figshare.1391771)
__Apr. 27, 2015__

: **Alperin.** **J.P.** Special Session: Critical DH (Digital Humanities) Interventions in Scholarly Communications and Publishing. *Modern Language Association Annual Meeting 2015*. Vancouver, Canada.
__Jan. 8, 2015__

: Lin, J., **Alperin, J.P**. *&* Ivimey-Cook, R. Three Publishers' Perspective on Using Altmetrics: PLOS, PKP, and eLife. *NISO Virtual Conference: Transforming Assessment: Alternative Metrics and: Other Trends*. Online. [link](http://www.niso.org/news/events/2014/virtual/assessment/)
__June 18, 2014__

: **Alperin, J.P.** Getting Altmetrics: What and who to consider. *Canadian Association of Learned Journals Annual Meeting*. St. Catherine’s, Canada.
__May 24, 2014__

: Garnett, A. *&* **Alperin, J.P.** Return of the Son of Automated Publishing: A Free, Modular Solution for Academic Typesetting. *MediaX: The future of content*. Stanford, USA. [video](https://www.youtube.com/watch?v=8ZBrtxKyog4)
__Feb. 5, 2014__

: Garnett, A. *&* **Alperin, J.P.** A New Solution for XML Publishing. *MediaX 2013 Conference,* Stanford, USA. [video](https://www.youtube.com/watch?v=j74Z6yTOUds)
__Jan. 8, 2013__

: **Alperin, J.P.** Open Access: Latin America Shows us How. *Open Science Summit.* Mountain View, USA.
__Oct. 19, 2012__

: **Alperin, J.P.** PKP, Open Access, and Open Source. *Latinoware*. Foz de Iguaçu, Brazil.
__Oct. 27, 2009__

: **Alperin, J.P.** Strengthening Scholarly Publications in Latin America. *Quality and Impact of Iberoamerican Journals.* San Jose, Costa Rica.
__Oct. 5, 2009__

: **Alperin, J.P.**, Smecher, A. PKP Experience - Development of Open Source Projects. *CRICS 8*. Rio de Janeiro, Brazil.
__Sep. 15, 2008__

Conference Presentations
: **Alperin, J.P.** Moving beyond counts: A method for surveying Twitter users. *Altmetrics15 Workshop*, *Altmetrics Conference*. Amsterdam, Netherlands. [link](http://altmetrics.org/altmetrics15/alperin/) 
__Oct 9, 2015__

: **Alperin, J.P.** Evolving altmetrics to capture impact outside the academy. *2:AM Altmetrics Conference.* Amsterdam, Netherlands. [slides](https://speakerdeck.com/jalperin/evolving-altmetrics-to-capture-impact-outside-the-academy)
__Oct. 7, 2015__

: **Alperin. J.P.** Exploring altmetrics in an emerging country context. *Altmetrics14 Workshop, WebScience Conference 2014.* Bloomington, USA. [link] [slides](https://speakerdeck.com/jalperin/exploring-altmetrics-in-an-emerging-country-context) [doi.org/10.6084/m9.figshare.1041797](http://dx.doi.org/10.6084/m9.figshare.1041797)
__June 23, 2014__

: **Alperin, J.P.** What it Means for PKP to Offer Article Level Metrics. *SciELO 15*. Sao Paolo, Brazil. [slides](https://speakerdeck.com/jalperin/what-it-means-for-pkp-to-offer-article-level-metrics)
__Oct. 25, 2013__

: **Alperin, J.P.** Are ALMs/Altmetrics Propagating Global Inequality? *Article Level Metrics Workshop 2013*. San Francisco, USA. [link](http://lanyrd.com/2013/alm13/scrdpy/) [slides](https://speakerdeck.com/jalperin/altmetrics-propagating-global-inequality)
__Oct. 12, 2013__

: **Alperin, J.P.** Visualizing Article-Level Metrics with d3.js? *Article Level Metrics Workshop 2013*. San Francisco, USA. [link](http://lanyrd.com/2013/alm13/scrdpm/) [slides](https://speakerdeck.com/jalperin/visualizing-article-level-metrics-in-d3-dot-js)
__Oct. 11, 2013__

: **Alperin, J.P.** The Skewed View from ISI: A Failed Attempt to Measure Regionalization in Latin America. *Latin American Studies Association Congress 2012*. San Francisco, USA.
__May 24, 2012__

: **Alperin, J.P.** *&* Fischman, G.E. Understanding the Challenges Facing Scholarly Communication in Latin America. *55th Annual Conference of the Comparative & International Education Society.* Montreal, Canada.
__May 2, 2011__

------ 

### Student Supervision {.singlespace}
Senior Supervisor
: Pouyanne, Sophie. *Designing a Non-linear, Academic Web Book with Scalar*. Master in Publishing.
__2016__

: Dunlop, Laura. *E-Cookbooks: An Analysis of Profitability*. Master in Publishing. 
__2016__

: Fleischmann, Ariane. *Getting SaaSy: The Implementation of Magazine Manager at Canada Wide Media.* Master in Publishing.
__2015__

: Simas Ferraz, João. *Improving Multi-Platform Workflow at Harbour Publishing and Douglas & McIntyre.* Master in Publishing.
__2015__

: Queitsch, Tilman. *Like, Tweet, Read: Exploratory Analyses of Social Media Data as an Indicator for Readership Behaviour in the Newspaper and Periodicals Industries.* Master in Publishing.
__2014__

Supervisor
: Blom, Sophia. *Consistency and Community in* The New Quarterly’s *Bringing the Writer Home: Past and Future*. Master in Publishing.
__2015__

: Garby, Taisha. *Publishing Translated Works: Examining the Process*. Master in Publishing.
__2015__

: Zhang, Summer. *The Case Study of the Jinglun Digital Publishing Platform*. Master in Publishing.
__2015__

: Ross, Emily. *Quiet Content: Digital Publishing Through the Lens of a Startup.* Master in Publishing
__2015__

: Soto, Arley. *Evaluation of non-core PKP services.* International Master in Digital Library Learning, University of Parma.
__2015__

--------
### Professional Activities {.singlespace.noheading}
&nbsp;
: Researcher
Public Knowledge Project 
__2007 — present__

: Chief Academic
The Winnower
__2015 — present__

--------
### Professional Service {.singlespace}
Board Memberships
: Steering Committee: 
*Scholarly Publishing and Academic Resources Coalition (SPARC) Steering Committee*
__2015 — present__

: Scientific Academic Advisory Board: *Redalyc, Biblioteca Digital CTS
Iberoamericana*
__2014 — present__

Conference Activities
: Application Review Team: 
*OpenCon: The student and early career academic professional conference on Open Access, Open Education, and Open Data*
__2015__

: Organizing Committee: 
*OpenCon: The student and early career
academic professional conference on Open Access, Open Education, and
Open Data*
__2014__

: Conference Director: 
*PKP Scholarly Publishing Conference 2013, Mexico City, Mexico (250 participants)*
__2013__

Editorial Teams
: Founding Editorial Team, *Scholarly and Research Communication*
__2010 — present__

: Technical Editor, *Education Policy Analysis Archives*
__2008 — present__

Reviewer
: *Aslib Proceedings, Scientometrics, Scholarly and Research
Communication, Palabra Clave, Education Policy Analysis Archives,
Revista Facultad de Odontología*

Memberships
: SPARC Student Advisory Group, CrossRef DOI Event Tracker Committee

--------
### Departmental Service {.singlespace.noheading}
&nbsp;
: Graduate Program Chair
__2015 — present__
: Open Access Advisory
__2015 – present__
: Undergraduate Program
__2014 — present__
: two faculty search committees
__2014—2016__
: Graduate Program
__2014—2015__

--------
### Media Coverage {.singlespace.noheading}
&nbsp;
: *Scholarly Kitchen.* Celebrating Five Years of Altmetrics.
[link](http://scholarlykitchen.sspnet.org/2015/10/20/celebrating-five-years-of-altmetrics/)
__Oct. 20, 2015__

: *Times Higher Education.*  Part of problem, not solution, warns academic. [link](https://www.timeshighereducation.com/news/altmetrics-risk-becoming-part-problem-not-solution-warns-academic)
__Oct. 7, 2015__

: *Foro TV: Fractal.*  Científico mundial. [link](http://noticieros.televisa.com/foro-tv-fractal/1508/fractal-13-agosto-2015/)
__Aug. 13, 2015__

: *PLOS Blogs.*  Momentum for Article-Level Metrics: New Uses.
[link](http://blogs.plos.org/plos/2015/09/momentum-article-level-metrics-new-uses/)
__Sept. 21, 2015__

: *OK Cast.*  Alperin: Open Access Advocacy. [link](http://okcast.org/2014/11/opencon-2014-interview-with-juan-pablo-alperin-open-access-advocacy/)
__Nov. 14, 2014__

: *Universia.* Superior al que se registra internacionalmente. [link](http://noticias.universia.edu.uy/ciencia-nn-tt/noticia/2014/07/29/1101337/papel-ciencia-uruguay-superior-registra-internacionalmente.html)
__July 29, 2014__

: *SciDev.* Ciencia sudamericana subestimada. [link](http://www.scidev.net/america-latina/publicacion/noticias/ciencia-sudamericana-subestimada.html)
__July 21, 2014__

: *Revista FAPESP.* Retweet or Perish. [link](http://revistapesquisa.fapesp.br/en/2014/07/21/retweet-perish/)
__July 21, 2014__

: *Nature*. Brazil fêtes open-access site. [link](http://www.nature.com/news/brazil-f%C3%AAtes-open-access-site-1.13997)
__Oct. 22, 2013__

: *Noticias Universidad de Costa Rica*. Especialista recomienda a
investigadores utilizar redes de comunicación.
[link](http://www.ucr.ac.cr/noticias/2012/05/15/especialista-recomienda-a-investigadores-utilizar-redes-de-comunicacion.html)
__May 15, 2012__

: *Stanford Daily.*  Freeing Knowledge. [link](http://www.stanforddaily.com/2011/01/26/freeing-knowledge/)
__Jan. 26, 2011__

-------
### Awards {.singlespace}
Travel Scholarships
: 2AM Altmetrics Confernece
__2015__
: ARCS Conference
__2015__
: Stanford University GSE
__2012, 2013__
: ALM Workshop
__2013, 2014__
: FORCE11
__2013__

Fellowships
: Haas Centre Graduate Public Service Fellow: *Stanford University)*
__2012 - 2013__


------ 

### Footer {#footer}

Juan Pablo Alperin -- [juan@alperin.ca]

------
