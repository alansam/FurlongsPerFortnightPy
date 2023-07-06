'''
   @see: https://en.wikipedia.org/wiki/FFF_system#Furlongs_per_fortnight
'''
def main():
  furlong   = lambda fur : fur / 8.0
  mile      = lambda mil : mil * 8.0
  week      = lambda wk  : wk * 7.0 * 24.0
  fortnight = lambda fnt : fnt * 7.0 * 24.0 * 2.0
  hour      = lambda hr  : hr / 7.0 / 24.0 / 2.0
  fph       = lambda mil : mil * mile(1.0)
  fpf       = lambda mph : fph(mph) * fortnight(1.0)

  fpf2mph   = lambda fpf : fpf * 3.720 * 10**-4
  fpf2kmph  = lambda fpf : fpf * 5.987 * 10**-4
  mph2fpf   = lambda fpf : fpf / (3.720 * 10**-4)
  kmph2fpf  = lambda fpf : fpf / (5.987 * 10**-4)

  fur = 8.0
  mil = 1.0
  fnt = 1.0

  dist = furlong(fur)
  print("{:7.3f} furlongs is {:7.3f} miles".format(fur, dist))

  dist = mile(mil)
  print("{:7.3f} miles is {:7.3f} furlongs".format(mil, dist))

  time = fortnight(fnt)
  print("{:7.3f} fortnights is {:10.9f} hours".format(fnt, time))
  print("{:7.3f} week       is {:10.9f} hours".format(1.0, week(1.0)))

  time = hour(fnt)
  print("{:7.3f} hours is {:10.9f} fortnights".format(fnt, time))

  print("{:7.3f} MPH = {:10.3f} Furlongs per Hour".format(1.0, fph(1.0)))
  print("{:7.3f} MPH = {:10.3f} Furlongs per Fortnight".format(1.0, fpf(1.0)))

  print('\n')

  time = 336.0
  print("{:14.9f} hours      is {:.18f} fortnights".format(time, hour(time)))
  time = 1.0 / 336.0
  print("{:14.9f} fortnights is {:.18f} hours".format(time, fortnight(time)))

  print("{:14.9f} miles per hour is {:.18f} furlongs per hour".format(1., fph(1.)))

  print('\n')

  p1f2m = 1.0
  p2f2m = 2688.17204301
  print("{:14.9f} furlongs per fortnight is {:14.9f} MPH".format(p1f2m, fpf2mph(p1f2m)))
  print("{:14.9f} furlongs per fortnight is {:14.9f} MPH".format(p2f2m, fpf2mph(p2f2m)))

  p1f2k = 1.0
  p2f2k = 1670.28561884
  print("{:14.9f} furlongs per fortnight is {:14.9f} km/h".format(p1f2k, fpf2kmph(p1f2k)))
  print("{:14.9f} furlongs per fortnight is {:14.9f} km/h".format(p2f2k, fpf2kmph(p2f2k)))

  print('\n')

  p2m2f = 0.000372
  p3k2f = 0.0005987
  p4m2f = 1.0
  p4k2f = 1.0
  print("{:14.9f} MPH  is {:14.9f} furlongs per fortnight".format(p2m2f, mph2fpf(p2m2f)))
  print("{:14.9f} MPH  is {:14.9f} furlongs per fortnight".format(p4m2f, mph2fpf(p4m2f)))

  print("{:14.9f} km/h is {:14.9f} furlongs per fortnight".format(p3k2f, kmph2fpf(p3k2f)))
  print("{:14.9f} km/h is {:14.9f} furlongs per fortnight".format(p4k2f, kmph2fpf(p4k2f)))

'''
....+....|....+....|....+....|....+....|....+....|....+....|....+....|
'''
if __name__ == "__main__":
  main()
