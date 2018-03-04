Three kinds of nodes in the graph: leaf, rel, template.
Nodes are addressed with natural numbers,
I will use * to indicate the address of a thing, like in C.
A leaf X has arity 0, and value[X] :: string
A rel R has arity > 0, template[R] :: *template, and member[i,R] :: *node
  for i in [1, arity[R]]
A template T has arity[T] > 0, and joint[i,T] :: *leaf,
  for i in [1, 1+arity[T]]

Example: in the rel "Sometimes I like bugs"
  the template might be ["Sometimes","like",""],
  member 1 "I", and member 2 "bugs".