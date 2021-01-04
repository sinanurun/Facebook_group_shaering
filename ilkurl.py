import urllib.request

# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.request.urlopen("http://sinanurun.com/category/dersler/bilgisayar-bilimi-python-programlamanin-temelleri-dersleri/")
print(f.read())
ifadeler = f.read().split('\n')
print(ifadeler)