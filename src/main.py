# run this with
  # exec( open( "src/main.py" ).read() )

# I wanted to use import statements instead of exec commands.
# That would obviate the need for this file.
# But if I try to extend pyDatalog functions (e.g. arity[]) defined in datalog.py from data.py,
# I get errors (along the lines of "arity doesn't exist").

exec( open( "src/datalog.py" ).read() )
exec( open( "src/data.py" ).read() )
