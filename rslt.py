# see types.md for the menaing of arity, value, member, joint, template
from pyDatalog import pyDatalog as pd
import mypy
pd.create_terms('arity','value','member','joint','template','show'
                ,'showJoint')
pd.create_terms('W','X','Y','Z')
pd.create_terms('J1','J2','J3')
pd.create_terms('S1','S2','S3')

if True: # make some data
  (arity[X] == 0) <= (Y == value[X])
  +(value[-1] == "")
  +(value[0] == "cats")
  +(value[1] == "mice")
  +(value[2] == "hunt")

  +(arity[3] == 2) # the template "_ hunt _"
  +(joint[1,3] == -1)
  +(joint[2,3] == 2)
  +(joint[3,3] == -1)

  +(arity[4] == 2) # the rel "cats #hunt mice"
  +(template[4] == 3)
  +(member[1] == 0)
  +(member[2] == 1)

if True: # show
  # Better than this: Don't jump straight from graph to show.
  # Instead go from graph to some ADT.
  (show[X] == Y) <= (value[X] == Y) # if value is defined, show that
  (show[X] == Y) <= ( (arity[X] == 2)
          & (joint[1,X] == J1) & (show[J1] == S1)
          & (joint[2,X] == J2) & (show[J2] == S2)
          & (joint[3,X] == J3) & (show[J3] == S3)
          & (Y == '#' + S1 + ' _ #' + S2 + ' _ #' + S3) )

  # not sure I need
    # (showJoint[X] == "#_") <= (value[X] == "")
    # (showJoint[X] == Y) <= ( (Y == show[X])
    #                          & (Y != "") )

