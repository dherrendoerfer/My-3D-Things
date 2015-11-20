#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   count = 0
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'm180sanify.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   if inputfile == '' or outputfile == '':
     sys.exit()
     
   print 'Input file is ', inputfile
   print 'Output file is ', outputfile
   f1 = open(inputfile, 'r')
   f2 = open(outputfile, 'w')
   for line in f1:
       if line in ("T0\n", "T1\n"):
         f2.write(line.replace('T0', 'M108 T0').replace('T1', 'M108 T1'))
         count += 1
       else:
         f2.write(line)
   f1.close()
   f2.close()
   print 'Replaced ',count,' tool change calls.'

if __name__ == "__main__":
   main(sys.argv[1:])
