import requests as rq
import shutil as st
import threading
from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing import Process
from os import cpu_count
import glob

class SomeModule:

    def __init__(self, url_list):
        self.url_list = url_list
        self.curr = 0
    
    def download(self, url):
        local_filename = url.split('/')[-1]
        with rq.get(url, stream=True) as r:
            with open(local_filename, 'wb') as f:
                st.copyfileobj(r.raw, f)

        return local_filename


    def __iter__(self):
        return self

    def __next__(self):
        if self.curr == len(self.url_list):
            raise StopIteration
        else:
            self.curr += 1
            return self.url_list[self.curr - 1]



    def multi_download(self):
        links = self.url_get()
        filenames = []

        with ThreadPoolExecutor(5) as ex:
            for link in links:
                filenames.append(next(ex.map(self.download, (link,))))

        return filenames

    def url_get(self):
        for url in self.url_list:
            yield url


    def getAvgVowels(self, filename):
        file = open(filename, 'r', errors='ignore') #normalt ville jeg bruge encoding='utf-8', men har konstant problemer med det, så nu bliver det på denne måde
        data = file.read()

        allChars = 0
        vowels = 0

        for char in data:
            allChars += 1

            if char in "aeiouAEIOU":
                vowels += 1

        avg = vowels / allChars * 100

        return float("%.2f" % avg)
        
    def getHighest(self):
        procs = []
        alltxt = glob.glob('*.txt')
        for i in range(cpu_count()):
            proc = Process(target=self.getAvgVowels, args=(alltxt[i],))
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()
                
    


