#!/usr/bin/python3
#
# Copyright John Levon <levon@movementarian.org>
#
# Extremely basic Atom parser for Apache Roller created feeds.
# This has been only slightly tested. All comments are ignored, and we
# don't make any attempt to translate from HTML to Markdown.
#
#

import feedparser
import sys
import os
import re

if len(sys.argv) < 3:
	sys.exit('usage: roller2hugo atomfeed.xml ~/blog/content/posts/')

feed = sys.argv[1]
outdir = sys.argv[2]

os.makedirs(outdir, exist_ok=True)

d = feedparser.parse(feed)

for entry in d.entries:
	published = entry.published_parsed

	# skip comments (we'd prefer to look at the xmlns, but it's not
	# available via feedparser)
	if hasattr(entry, 'thr_in-reply-to'):
		continue

	title = re.sub(r'[^A-Za-z0-9]+', '-', entry.title.lower())

	slug = ("%04d-%02d-%02d-%s" % (
		published.tm_year,
		published.tm_mon,
		published.tm_mday,
		title
		))

	categories = ''
	if hasattr(entry, 'categories'):
		categories = ','.join([str(v.label) for v in entry.categories])
		print(categories)

	path = os.path.join(outdir, slug + '.html')
	print('writing %s' % path)

	file = open(path, 'w')

	print('+++', file=file)
	print('author = "%s"' % entry.author, file=file)
	print('published = %s' % entry.published, file=file)
	print('slug = "%s"' % slug, file=file)
	print('categories = [%s]' % categories, file=file)
	print('title = "%s"' % entry.title, file=file)
	print('+++', file=file)
	print(entry.content[0].value, file=file)
	file.close()
