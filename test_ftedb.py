import json
import urllib.request
import collections

data = urllib.request.urlopen("https://raw.githubusercontent.com/KaniyamFoundation/Free-Tamil-Ebooks/master/booksdb.json").read().decode()
obj = json.loads(data)

print("Total Length : "+str(len(obj['books'])))

bookIds = list()
for book in obj['books']:
    bookIds.append(book['bookid'])

# bookIds = list(dict.fromkeys(bookIds))

print(len(bookIds))

print([item for item, count in collections.Counter(bookIds).items() if count > 1])