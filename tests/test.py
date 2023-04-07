import re

def get_urls_from_string(string):
    # regular expression to match URLs
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    # find all matches
    urls = re.findall(url_regex, string)

    return [x[0] for x in urls]

string = 'This is a sample string with a URL: http://www.example.com/path/to/page and we know that https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ'
urls = get_urls_from_string(string)
print(urls)

# import pywhatkit

# pywhatkit.playonyt("https://www.youtube.com/watch?v=Tz4sUyA1F_k")