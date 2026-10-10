# philosophy-spider
theres an old myth that if you click the first link in every wikipedia page, starting from a random one, you will always get to the philosophy page. i tried it and it worked for some and not for others.

So... I made a python script that you can input Wikipedia links for articles, either as a endpoint, a start-point or both. It will try connect the 2 by clicking the first link in every page, and tells you which pages are in between the 2, with names, and links! The maximum amount of turns allowed is a variable which can be adjusted to whatever you want, but it will take longer! In my testing, the maximum moves any 2 pages took was about 45 pages, but its impossible to say for sure. The crawler can also sometimes get in a loop, where the first links in each Wikipedia page link to each other, either directly or otherwise; I have added a way for it to be able to tell when it is in a loop, and it stops.

To use it, please input a Wikipedia page in the format, https://en.wikipedia.org/wiki/yourpagehere, and then choose either P or C depending on whether you want to have a custom endpoint or use philosophy.

[https://youtu.be/o9-dZyMrTuA](https://youtu.be/SfKU9cKbPHQ) watch it working here!

### Requirements

It uses 3 main libraries, 1 of which, re, is included with python on install. The rest can be easily installed using pip in the terminal.

https://pypi.org/project/beautifulsoup4/

https://pypi.org/project/requests/

~~~
import requests
import re
from bs4 import BeautifulSoup
~~~

### Credits

Thanks to MostLime for organising the YSWS event, crawl, and allowing me to create this, and recieve FREE MINECRAFT!!!!!!!!!!!!!!

### AI transparency
I have used minimal amounts of AI within this project, only a few lines which required debugging, and only for things I was too lazy to do, rather than things I didn't know how to do

<img width="1524" height="716" alt="Screenshot 2026-10-10 012910" src="https://github.com/user-attachments/assets/e0d52b61-099b-41e5-9449-64ad10299534" />

