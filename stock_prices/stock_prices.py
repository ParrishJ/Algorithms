#!/usr/bin/python

# testArr = [10, 7, 5, 8, 11, 9]

import argparse

def find_max_profit(prices):
  maxProf = prices[1] - prices[0]
  for price in range(len(prices) - 2):
    for j in range(price + 1, len(prices) - 1):
      currProf = prices[j] - prices[price]
      if(currProf > maxProf):
        maxProf = currProf
  return maxProf

# find_max_profit(testArr)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))