import csv


def save_to_file(weathers, year):
  file = open(f"weather of {year}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["ID", "LOCATION", "OCT", "NOV", "DEC", "JAN", "FEB","MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "WY Total", "Pct Avg to Date"])
  for weather in weathers:
    writer.writerow(list(weather.values()))
  return