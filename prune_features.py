# This script takes a file with existing probability features
# and prunes it by either removing some features, or combining
# features together (i.e. those with similar probabilities)
import sys

def main( file_name='schunk_output_200000.txt', 
          removal= '11111111111',
          condense='00000000000' ):
  f_in = open( file_name, 'r' )
  f_out = open( "pruned_" + file_name, 'w' )

  lines = f_in.readlines()
  for line in lines:
    if len( line.strip() ) == 0:
      f_out.write( line )
    else:
      split_line = line.split(" ")
      rebuild_list = [ split_line[0] ] # Put the word at the front
      # Iterate through all the features
      for i,f in enumerate( split_line[1:-1] ):
        if removal[i] == '0': # Don't remove this feature
          if condense[i] == '0': # Don't condense this feature
            rebuild_list.append( f )
          else:
            rebuild_list.append( f[:-1] ) # Remove the last decimal point
      rebuild_list.append( split_line[-1] ) # Put the label at the end
      f_out.write( " ".join( rebuild_list ) )

  f_out.close()
  f_in.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( sys.argv[1] )
  elif len( sys.argv ) == 3:
    main( sys.argv[1], sys.argv[2] )
  elif len( sys.argv ) == 4:
    main( sys.argv[1], sys.argv[2], sys.argv[3] )
  else:
    main()
