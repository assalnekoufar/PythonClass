from urllib.request import urlopen
response = urlopen('https://www.python.org/')
html = response.read()
print(type(html))
text = html.decode("utf-8")
print(type(text))
