import requests #this is used to give http requests
import re #does stuff
from bs4 import BeautifulSoup #this can read the web pages, this does like most of the work

def philosophy():
    loops = int(100)
    philosophyend: bool = False
    visitedurls = set()


    headers = {
        'User-Agent': 'philosophyspider 1.1' #technically 1.1 cuz i finished this at 3 hours but lowk locked in and added a lot of features to it 
    }

    #general setup
    WikiBaseURL = input("input your starting wikipedia page here:") #you need to have the https thing before the link
    WikiEndURL = "https://en.wikipedia.org/wiki/Philosophy" #optional choice, you can use this to try and conect two people, like those videos where they connect trumnp with einstein, you just find their wikis and it will find a link between them. sometimes it can fail tho
    numberofturns = 0


    def status(url): #this tells you if the website actyaully works, like if im ablke to read it
        # Ensure URL has a proper schema before making the request
        if not url.startswith(("http://", "https://")):
            if url.startswith("//"):
                url = "https:" + url
            elif url.startswith("/"):
                url = "https://en.wikipedia.org" + url
            else:
                url = "https://" + url

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("we found the page!!!")
                return response
            else:
                print(f"couldnt fetch page, status code: {response.status_code}")
                return None
        except requests.exceptions.MissingSchema:
            print("invalid URL schema provided!")
            return None

    def pagename(response): #this looks at the wiki page and finds the title oif the wiki, like for philosophy pagem, its philosophy
        match = re.search(r'"wgPageName"\s*:\s*"([^"]+)"', response.text) #couldnt tell you how this works to save my life

        if match:
            PageName = match.group(1).replace("_", " ") #makes long page names readable
            print(PageName)
            return PageName
        else:
            print("couldnt find page name eh idk")
            return None

    def firstlink(response):
        # parses html and searches for the first link
        soup = BeautifulSoup(response.text, "html.parser")
        first_link = None

        for p in soup.find_all("p"):
            if p.find_parent(class_=["sidebar", "infobox", "navbox", "hatnote", "vector-header", "vector-footer"]):
                continue

            for a in p.find_all("a", attrs={"rel": "mw:WikiLink"}, href=True):
                href = a['href']

                if not ("/wiki/" in href) or any(prefix in href for prefix in ("/wiki/File:", "/wiki/Help:", "/wiki/Special:", "/wiki/Wikipedia:", "/wiki/Category:", "/wiki/Talk:", "/wiki/Template:")): #help
                    continue

                first_link = a
                break

            if first_link:
                break

        if first_link:
            link_text = first_link.text
            if first_link['href'].startswith("http"):
                link_url = first_link['href']
            else:
                link_url = "https://en.wikipedia.org" + first_link['href']
                
            print(link_text)
            print(link_url)
            return link_url
        else:
            print("couldnt find first link :(")

    endpoint=input("do you want to search for philosophy (type 'P') or add a custom endpoint link (type 'C')?")

    if endpoint == "P":
        WikiEndURL="https://en.wikipedia.org/wiki/Philosophy"
    elif endpoint == "C":
        WikiEndURL = input("please enter custom endpoint url (https://en.wikipedia.org/wiki/yourendpointhere): ")

        resp2 = status(WikiEndURL)

        print(f"you have chosen {pagename(resp2)}")

    print(f"You have chosen {WikiBaseURL}!")

    resp_end = status(WikiEndURL)
    TargetPageName = pagename(resp_end) if resp_end else "Philosophy"


    for x in range(loops):
        if WikiBaseURL in visitedurls:
            print("im going in circles ahhh")
            break
        visitedurls.add(WikiBaseURL)

        resp = status(WikiBaseURL)
        if not resp:
            break

        currentpage = pagename(resp)

        if (
            currentpage
            and TargetPageName
            and currentpage.lower() == TargetPageName.lower()
        ):
            philosophyend = True
            break

        nexturl = firstlink(resp)

        if nexturl:
            WikiBaseURL = nexturl
        else:
            print("keep crawling bozo")
            break
        
    print(f"THE BIG REVEAL... DO THEY CONNECT??: {philosophyend}")

philosophy() 