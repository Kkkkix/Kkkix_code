import urllib.request

# response = urllib.request.urlopen("https://placekitten.com/500/500")
req = urllib.request.Request("https://placekitten.com/500/500")
response = urllib.request.urlopen(req)
cat_img = response.read()

with open('cat_500_500.jpg','wb') as f:
    f.write(cat_img)