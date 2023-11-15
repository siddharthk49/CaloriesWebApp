import requests
from selectorlib import Extractor
class Temperature:
    """
    Represents temperature value extracted from timeanddate.com/weather
    """
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'
    def __init__(self, country, city):
        self.country = country.replace(" ","-")
        self.city = city.replace(" ","-")

    def build_url(self):
        url = self.base_url+self.country+"/"+self.city
        return url

    def scrape(self):
        url = self.build_url()
        extractor = Extractor.from_yaml_file(yaml_filename=self.yml_path)
        req = requests.get(url)
        src = req.text
        raw_result = extractor.extract(src)
        return  raw_result


    def get(self):
        """
        returns clean result
        """
        scraped_text = self.scrape()
        result = float(scraped_text["temp"].replace("\xa0°C","").strip())
        return result

if __name__ == '__main__':
    t = Temperature('usa', 'san-francisco')
    t.get()






