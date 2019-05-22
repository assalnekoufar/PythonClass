from urllib.request import urlopen


class WebBrowser:
    def __init__(self, url):
        self.url = url

    def read_text(self):
        response = urlopen(self.url)
        html = response.read()
        text = html.decode("utf-8")
        return text



w = WebBrowser('http://wttr.in/tehran')
text = w.read_text()
print(text)
