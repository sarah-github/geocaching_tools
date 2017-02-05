#!/usr/bin/python3
#coding: utf-8

from itertools import permutations

count = 0
solutions = []

for a, b, c, d, e, f, g, h, i in permutations(range(1, 10)):
    result = a * 10 / b + c / d + 11 / e + f + 12 + g + h - i + 13

    if result == 43:
        solution = [a, b, c, d, e]
        # check if permutation of a - e already exists in solutions list
        # to get only unique permutations of a - e
        found = False
        for sol in solutions:
            if sol == solution:
                found = True
                break

        if not found:
          print("-----")
          solutions.append(solution)
          print(str(solution))
          count = count + 1
          print("No", count)

          # N  50° E(D+B).0(D*(D+C))
          # E 006° (E-D)D.(E-C+B)BA

          # get carryover
          db = d+b
          if db > 9:
              e = e + int(str(db)[:1])
              db = int(str(db)[1:])
          
          print("N 50° " + str(e) + str(db) + ".0" + str(d*(d+c)) +
                ", E 006° " + str(e-d) + str(d) + "." + str(e-c+b) + str(b) + str(a))
