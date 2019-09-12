#!/usr/bin/python

import sys

denoms = [1, 5, 10, 25, 50]

cache = {}

def making_change(amount, denominations, cache=None):
  print(cache)

  if amount < 0:
    return 0
  if amount == 0:
    return 1
  elif amount in cache:
    return cache[amount]
  else:
    res = making_change(amount - 1, cache) + making_change(amount - 5, cache) + making_change(amount - 10, cache) + making_change(amount - 25, cache) + making_change(amount - 50, cache)
    cache[amount] = res
    return res


print(making_change(10, denoms, cache))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")