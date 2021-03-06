from pyDatalog import pyDatalog as pd

# variables
pd.create_terms('W','X','Y','Z')
pd.create_terms('J1','J2','J3')
pd.create_terms('S1','S2','S3')

# see types.md for (a little) more detail on the meaning of arity, value, member, joint, template
pd.create_terms(
    'value'        # templates and relationships are made out of values
  , 'arity'        # describes the number of members in a relationship
                   # templates and relationship both have arity
  , 'member'       # relationships have members
  , 'template'     # "_ are _ when _" is the template of the previous relationship
  , 'joint'        # a template for an arity-n relationship has n+1 joints
                   # For example, "_ is _" is an arity-2 template. Its first and last joints are empty.
  , 'show'         # turns something into a string
  , 'rslt_type' )  # possibilities include value, template and relationship

(rslt_type[X] == 'value')        <= (Y == value[X])    # if it has a value, it is a val
(rslt_type[X] == 'template')     <= (Y == joint[0,X])  # if it has any joints, it is a template
(rslt_type[X] == 'relationship') <= (Y == template[X]) # if it has a template, it is a relationship

if True: # show
  # Better than this: Don't jump straight from graph to show.
  # Instead go from graph to some ADT.
  (show[X] == Y) <= (value[X] == Y) # if value is defined, show that
  (show[X] == Y) <= ( (arity[X] == 2)
          & (joint[1,X] == J1) & (show[J1] == S1)
          & (joint[2,X] == J2) & (show[J2] == S2)
          & (joint[3,X] == J3) & (show[J3] == S3)
          & (Y == '#' + S1
                + ' _ #' + S2
                + ' _ #' + S3) )
