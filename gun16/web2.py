"""
HTML: hypertext markup language
    tag, element, etiket: <p>, <b>, <strongs>, <i>
CSS: cascading style sheets
JavaScript: tarayici uzerinde calisan bir programlama dili

request: gonderdigimiz istek. tarayici, sunucuya gonderiyor.
response: snucunun, tarayiciya gonderdigi cevap.
"""

import requests
import bs4  # beautiful soup 4

URL = "https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun"
URL = "https://eksisozluk.com/gokhan-gonulun-200-bin-tllik-saatini-kaybetmesi--5809553"
URL = "https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters"

response = requests.get(URL)
print(response.status_code)  # 200 ok
# not found: 404
# internal server error: 502

print(response.headers)
content = response.content
print(content)

soup = bs4.BeautifulSoup(content, features="html5lib")
a_elements = soup.find_all("a")
tables = soup.find_all("table")
for table in tables:
    print(table)
