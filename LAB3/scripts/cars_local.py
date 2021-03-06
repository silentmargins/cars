#!/usr/bin/env python3
import os
import json
import locale
import sys
import operator
import reports
import emails

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_total_sales = {"total_sales": 0}
  all_years = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item['total_sales'] > max_total_sales["total_sales"]:
      max_total_sales = item
    # TODO: also handle most popular car_year
    if item['car']['car_year'] not in all_years:
      all_years[item['car']['car_year']] = 1
    else:
      all_years[item['car']['car_year']] += 1

  sorted_all_years = sorted(all_years.items(), key=operator.itemgetter(1))
  that_year  = sorted_all_years[-1][0]
  print(that_year)
  year_sales = 0
  for item in data:
    if item['car']['car_year'] == that_year:
      year_sales = year_sales + item['total_sales']
  
  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]), "The {} had the most sales: {}".format(format_car(max_total_sales["car"]), max_total_sales["total_sales"]), "The most popular year was {} with {} sales.".format(that_year, year_sales)
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data



def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("../car_sales.json")
  summary = process_data(data)
  print(summary)
  summary_with_brakes = ""
  summary_with_lines = ""
  for item in summary:
    summary_with_brakes += item + '<br/>'
    summary_with_lines += item + '\n'
  print(summary_with_brakes)
  # TODO: turn this into a PDF report
  table_data = cars_dict_to_table(data)
  reports.generate("/tmp/cars.pdf", "Cars", summary_with_brakes, table_data)
  # TODO: send the PDF report as an email attachment
  recipient = "{}@example.com".format(os.environ.get('USER'))
  message = emails.generate('automation@example.com', recipient, 'Sales summary for last month', summary_with_lines, "/tmp/cars.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
You have mail in /var/mail/student-04-4bcc43d3ad5f

