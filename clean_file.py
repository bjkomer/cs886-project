# This script removes all blank lines from a file
import sys

def main( file_name='ner.txt' ):
  f_in = open( file_name, 'r' )
  f_out = open( 'clean_' + file_name, 'w' )
  lines = f_in.readlines()

  for line in lines:
    if len( line.strip() ) == 0:
      continue
    else:
      f_out.write( line )
 
  f_in.close()
  f_out.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( sys.argv[1] )
  else:
    main()
