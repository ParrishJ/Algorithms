#!/usr/bin/python

import math

rec = {
  'bread': 2,
  'cheese': 1
}

ing = {
  'bread': 6,
  'cheese': 5
}

def recipe_batches(recipe, ingredients):
  totals =[]
  min = 0

  if len(recipe) != len(ingredients):
    return 0

  else:
    for item in recipe:
        totals.append(ingredients[item] // recipe[item])

    totals.sort()

    if len(totals) == 0:
      # print(min)
      return min
    else:
      # print(totals[0])
      return totals[0]

recipe_batches(rec, ing)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))