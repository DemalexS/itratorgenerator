import json
import wikipediaapi
import hashlib

class CountryIter:
    def __init__(self, file_name, start):
        self.file = open(file_name, encoding='utf-8')
        self.json_data = json.load(self.file)
        self.wiki = wikipediaapi.Wikipedia('en')
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):

        if self.start == len(self.json_data):
            raise StopIteration

        country = self.json_data[self.start]['name']['common']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl

        self.start += 1
        return country, country_link


if __name__ == '__main__':
    output_file = open('countries-links.txt', 'w', encoding='utf-8')

    for country, link in CountryIter('countries.json', 0):
        output_file.write(str(country) + ' —> ' + str(link) + '\n')
        print('.', end='', flush=True)

    output_file.close()

def gen_md5(file_name):
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for item in gen_md5('countries-links.txt'):
    print(item)