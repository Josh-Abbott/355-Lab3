# CptS 355 - Spring 2023 - Lab 3
# Josh Abbott

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 getNumCases 
def getNumCases(data,counties,months): 
     cases_count = 0
     for county in data:
          if county in counties:
               for month in data[county]:
                    if month in months:
                         cases_count += data[county][month]
     return cases_count

## problem 2 getMonthlyCases
def getMonthlyCases(data):
     monthly_cases = {}
     for county, monthly_data in data.items():
          for month, cases_count in monthly_data.items():
               if month not in monthly_cases:
                    monthly_cases[month] = {}
               monthly_cases[month][county] = cases_count
     return monthly_cases

from functools import reduce
## problem 3 mostCases 
def mostCases(data):
     monthly_cases = getMonthlyCases(data)
     month_max, case_max = max(
          map(lambda month: (month, reduce(lambda a, b: a + b, monthly_cases[month].values())), monthly_cases.keys()), 
          key = lambda x: x[1]
     )
     return month_max, case_max

## problem 4a) searchDicts(L,k)
def searchDicts(L,k):
     for key in L[::-1]:
          if k in key:
               return key[k]
     return None


## problem 4b) searchDicts2(L,k)
def searchDicts2(L, k):
     def searchDicts2_h(L, k, i):
          if i < 0 or i >= len(L):
               return None
          t = L[i]
          d = t[1]
          next_index = t[0]
          if k in d:
               return d[k]
          else:
               if next_index == 0:
                    return searchDicts2_h(L, k, i-1)
               else:
                    return searchDicts2_h(L, k, next_index)
     return searchDicts2_h(L, k, len(L)-1)

## problem 5 - getLongest
def getLongest(L):
     long_string = ''
     for item in L:
          if isinstance(item, list):
               sub_long = getLongest(item)
               if len(sub_long) > len(long_string):
                    long_string = sub_long
          elif isinstance(item, str):
               if len(item) > len(long_string):
                    long_string = item
     return long_string

## problem 6 - apply2nextN 
# class apply2NextN():
