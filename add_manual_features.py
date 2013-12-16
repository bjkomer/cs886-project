import sys

# starting with a capital letter
def add_capital( line ):
  if len( line ) > 0:
    if line[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      line_list = line.split(" ")
      new_line_list = line_list[0:-1] + ['CAPITAL'] + [line_list[-1]]
      new_line = " ".join( new_line_list )
      return new_line
  return line

# ending in -land
def add_landsuffix( line ):
  if "land " in line:
    line_list = line.split(" ")
    new_line_list = line_list[0:-1] + ['LANDSUFFIX'] + [line_list[-1]]
    new_line = " ".join( new_line_list )
    return new_line
  return line

# ending in -s
def add_plural( line ):
  if "s " in line:
    line_list = line.split(" ")
    new_line_list = line_list[0:-1] + ['SSUFFIX'] + [line_list[-1]]
    new_line = " ".join( new_line_list )
    return new_line
  return line

# ending in -tion
def add_tionsuffix( line ):
  if "tion " in line:
    line_list = line.split(" ")
    new_line_list = line_list[0:-1] + ['TIONSUFFIX'] + [line_list[-1]]
    new_line = " ".join( new_line_list )
    return new_line
  return line

# mark words with 3 or less letters
def add_smallword( line ):
  if len( line ) > 1:
    line_list = line.split(" ")
    if len( line_list[0] ) < 4:
      new_line_list = line_list[0:-1] + ['SMALL'] + [line_list[-1]]
      new_line = " ".join( new_line_list )
      return new_line
  return line

# mark punctuation
def add_punctuation( line ):
  if len( line ) > 0:
    if line[0] in "~!@#$%^&*()_+{}[]:;',./<>?=`'" + '"':
      line_list = line.split(" ")
      new_line_list = line_list[0:-1] + ['PUNC'] + [line_list[-1]]
      new_line = " ".join( new_line_list )
      return new_line
  return line

# ending in -er
def add_ersuffix( line ):
  if "er " in line:
    line_list = line.split(" ")
    new_line_list = line_list[0:-1] + ['ERSUFFIX'] + [line_list[-1]]
    new_line = " ".join( new_line_list )
    return new_line
  return line

def add_suffix( line ):
  return add_ersuffix( add_tionsuffix( add_landsuffix( line ) ) )

def main( file_name ):
  f_in = open( file_name, 'r' )
  f_all = open( 'all_' + file_name, 'w' )

  lines = f_in.readlines()
  for line in lines:
    f_all.write( add_plural( add_capital( add_punctuation( add_smallword(
      add_suffix(line) ) ) ) ) )

  f_in.close()
  f_all.close()

if __name__ == "__main__":
  if len( sys.argv ) == 2:
    main( sys.argv[1] )
  else:
    print( "missing input file name" )
