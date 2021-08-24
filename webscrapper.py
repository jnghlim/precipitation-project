import requests
from bs4 import BeautifulSoup
from save import save_to_file

min_year = 2002
w_url = f"https://www.cnrfc.noaa.gov/monthly_precip_2002.php"

def get_weather(max_year):

  for year in range(min_year, max_year):
    print(f"Scraping Precipitation of year: {year}")
    result = requests.get(f"https://www.cnrfc.noaa.gov/monthly_precip_{year}.php")
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table", {"class":"normal"})
    rows = table.find_all("tr")
    td_rows = []
    for x in rows:
      if len(x.find_all("td", {"class":"medBlue-background"}))>0:
        continue
      elif len(x.find_all("td")) == 0:
        continue
      else:
        td_rows.append(x.find_all("td"))
    
    strings_list = []
    temp_str = []
    for y in td_rows:
      for z in y:
        temp_str.append(z.string.strip())
      strings_list.append(temp_str)
      temp_str = []

    correct_list = []
    for l in strings_list:
      token = True
      for m in l:
        if m == 'M':
          token = False
          break
        continue
      if token == True:
        correct_list.append(l)
      else:
        continue
    
    final_list = []
    for x in correct_list:
      final_list.append({'ID':x[0], 'LOCATION':x[1], 'OCT':x[2], 'NOV':x[3], 'DEC':x[4], 'JAN':x[5], 'FEB':x[6], 'MAR':x[7], 'APR':x[8], 'MAY':x[9], 'JUN':x[10], 'JUL':x[11], 'AUG':x[12], 'SEP':x[13], 'WY Total':x[14], 'Pct Avg to Date':x[15]})
    
    save_to_file(final_list, year)
  return 0

print(get_weather(2021))