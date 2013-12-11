# This script takes an input file, and gives each unique label a unique vector
import sys

def get_label( line ):
  if len( line ) > 0:
    line_list = line.split(" ")
    return line_list[-1]
  return False

def main( file_name='schunk.txt', max_lines=0 ):
  f_in = open( file_name, 'r' )
  f_out = open( 'label_' + file_name, 'w' )
  lines = f_in.readlines()
  label_list = []
  if max_lines == 0:
    max_lines = len(lines)

  for i in xrange( max_lines ):
    label = get_label( lines[i] )
    if label == False:
      continue
    if label not in label_list:
      label_list.append( label )
      f_out.write( label + '\n' )
 
  f_in.close()
  f_out.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( file_name = sys.argv[1])
  elif len( sys.argv ) == 2:
    main( file_name = sys.argv[1], max_lines=int(sys.argv[2]) )
  else:
    main()
