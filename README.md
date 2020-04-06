# roller2hugo

Converts Apache Roller XML feed into Hugo posts. This has only been
tested on one of my old feeds, so there's a good chance it might not
work properly for you.

Comments are ignored.

Requires Python 3 and `python3-feedparser`.

```
./roller2hugo.py ./atomfeed.xml ~/blog/content/posts/
```
