from pyDatalog import pyDatalog as pd
pd.create_terms('arity','value','member','joint','template','show'
                ,'showJoint')
pd.create_terms('W','X','Y','Z')
pd.create_terms('J1','J2','J3')
pd.create_terms('S1','S2','S3')

(show[X] == Y) <= (value[X] == Y) # if value is defined, show that
(showJoint[X] == "_") <= (value[X] == "")
(showJoint[X] == Y) <= ( (Y == show[X])
                         & (Y != "") )
(arity[X]==2)
& (joint[1,X] == J1)
& (showJoint[J1] == S1)
& (joint[2,X]==J2)
& (showJoint[J2] == S2)
& (joint[3,X]==J3)
& (showJoint[J3] == S3)
& (Y == S1 + ' ' + 

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
