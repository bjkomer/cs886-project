# This script splits a file into smaller chunks
import sys

def main( file_name='ner.txt', size=10000 ):
  f_in = open( file_name, 'r' )
  f_out = open( file_name + '_' + str(size) + '_0', 'w' )
  lines = f_in.readlines()
  file_num = 0
  line_num = 0

  for line in lines:
    f_out.write( line )
    line_num += 1
    if line_num == size:
      line_num = 0
      file_num += 1
      f_out.close()
      f_out = open( file_name + '_' + str(size) + '_' + str(file_num), 'w' )
 
  f_in.close()
  f_out.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( sys.argv[1] )
  elif len( sys.argv ) == 3:
    main( sys.argv[1], int(sys.argv[2]) )
  else:
    main()
