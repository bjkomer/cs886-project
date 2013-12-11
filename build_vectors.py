# This script takes an input file, and gives each unique word a unique vector
import sys

def get_word( line ):
  if len( line ) > 0:
    line_list = line.split(" ")
    return line_list[0]
  return False

def main( file_name='schunk.txt', max_lines=0 ):
  f_in = open( file_name, 'r' )
  f_out = open( 'list_' + file_name, 'w' )
  lines = f_in.readlines()
  word_list = []
  if max_lines == 0:
    max_lines = len(lines)

  for i in xrange( max_lines ):
    word = get_word( lines[i] )
    if word == False:
      continue
    if word not in word_list:
      word_list.append( word )
      f_out.write( word + '\n' )
 
  f_in.close()
  f_out.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( file_name = sys.argv[1])
  elif len( sys.argv ) == 2:
    main( file_name = sys.argv[1], max_lines=int(sys.argv[2]) )
  else:
    main()
