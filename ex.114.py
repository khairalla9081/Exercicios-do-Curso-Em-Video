import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site fora do ar!')
else:
    print('Ta tudo ok')