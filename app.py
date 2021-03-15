from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

# http://35.237.182.83:3000/users/sign_in

try:
    url = urlopen("http://35.237.182.83:3000/users/")
except HTTPError as erro:
    print(erro)
except URLError:
    print('Servidor inativo')
else:
    res = BeautifulSoup(url.read(),"html5lib")
    if res.input is None:
        print('Login')
    else:
        print('Servidor Ativo')
