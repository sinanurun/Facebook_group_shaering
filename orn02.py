import urllib.request

url = urllib.request
connection = url.urlopen('https://www.facebook.com/groups/?ref=bookmarks')

content = connection.read()
content = content.decode('utf-8')

f = open("deneme.txt","a")
f.write(content)
f.close()
f = open("deneme.txt","r")
for a in f.readlines():
    print(a)
    if "src='http://sinanurun.com/" in a:
        k = a.split("src='")
        z= k[1].split("'")
        print(z[0])