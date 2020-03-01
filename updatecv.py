# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import re
import MySQLdb as mdb
with open('cv/alperinCV.html', 'r') as f:
    content = f.read()

# <codecell>

sections = content.split('<h3')[1:]

# <codecell>

sectiontitles = [re.match('.*id="(\w+)".*', s).group(1) for s in sections]
sections = [re.sub('.*id="(\w+)">.*?</h3>\s*', '', s) for s in sections]
d = {k: v for (k,v) in zip(sectiontitles, sections)}

# <codecell>

con = None
try:
	# connect
	con = mdb.connect(host = 'mysql.alperin.ca', user = 'alperinca', passwd = 'x99FvJPc', db = 'alperin_ca', use_unicode=True, charset="utf8")

	cur = con.cursor()

except mdb.Error, e:
	print "Errormb %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

# <codecell>

for s in ['publications', 'presentations', 'teaching']:
    cur.execute('UPDATE wp_posts SET post_content = %s WHERE post_name = %s;', (d[s], s))

