import urllib.request
from urllib import response as urlResponse
from urllib import error as urlError

hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}

def get_random_article(namespace=None):
    """ Download a random wikipiedia article"""
    print("Method beginning")
    try:
        url = 'https://fr.wikipedia.org/wiki/'
        if namespace != None:
            url += namespace
        else:
            url += 'Special:Random'
        print("url: " + str(url))
        req = urllib.request.Request(url, None, hrs)
        print("request: " + str(req))
        rep = urllib.request.urlopen(req).readlines()
        return rep
    except Exception as e:
        print("Failed to get article")
        print(str(e))
        raise

def save_article(namespace=None):
    try:
        page = get_random_article(namespace)
        if namespace != None:
            nameArticle = namespace
        else:
            nameArticle = 'random'
            saveFile = open(nameArticle + '.html', 'w')
            saveFile.write(str(page))
            saveFile.close()
    except Exception as e:
        print("Failed to save article")
        print(str(e))
        raise

#save_article('Jacques_Chirac') -> fonctionne
save_article()