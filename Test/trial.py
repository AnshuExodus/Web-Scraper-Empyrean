from urllib.request import urlopen

html = urlopen("http://www.imdb.com/")
print(html.read())