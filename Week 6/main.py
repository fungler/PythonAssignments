import somemodule

sm = somemodule.SomeModule(["https://www.gutenberg.org/files/1342/1342-0.txt", "https://www.gutenberg.org/files/84/84-0.txt", "https://www.gutenberg.org/files/20228/20228-8.txt"])

#sm.download("https://www.gutenberg.org/files/1342/1342-0.txt")

#print(sm.multi_download())


# forstår ikke hvorfor jeg skal bruge en generator, når listen allerede er i min class. Her er i hvert fald et eksempel på brugen af generator
#links = sm.url_get()
#print(next(links))
#print(next(links))
#print(next(links))


#sm2 = somemodule.SomeModule(["https://www.gutenberg.org/files/1342/1342-0.txt", "https://www.gutenberg.org/files/84/84-0.txt", "https://www.gutenberg.org/cache/epub/25525/pg25525.txt"])

# test af iter() og next()
#print(next(iter(sm2)))
#print(next(iter(sm2)))
#print(next(iter(sm2)))
#print(next(iter(sm2))) #raise StopIteration

avg = sm.getAvgVowels("20228-8.txt")
print(avg)

print(sm.getHighest())