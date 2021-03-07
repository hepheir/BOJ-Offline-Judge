import ssl
import urllib.request


class Html:
    def __init__(self, url:str):
        self.url = url
        self.html = self.get_html()

    
    def innerHTML(self, tag_opening:str) -> str:
        # Construct tag closing
        tmp = tag_opening.split()
        tmp_hasAttributes = len(tmp) > 1
        tmp = list(tmp[0])
        tmp.insert(1, '/')
        if tmp_hasAttributes:
            tmp.append('>')
        tag_closing = ''.join(tmp)
        # Search
        start = self.html.find(tag_opening)
        if start == -1:
            return ''
        start += len(tag_opening)
        end = self.html.find(tag_closing, start)
        return self.html[start:end].rstrip()


    def get_html(self):
        if self.url.startswith('https://'):
            with urllib.request.urlopen(self.url, context=ssl.SSLContext()) as https:
                return https.read().decode('utf-8')
        else:
            with urllib.request.urlopen(self.url) as http:
                return http.read()
