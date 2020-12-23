friends = {"Bob", "Rolf", "Anne"} # set
abroad = {"Bob", "Anne","Janne"} # set

local_friends = friends.difference(abroad)

print(local_friends)

friends_union = abroad.union(friends)

print(friends_union)

friends_intersec = friends.intersection(abroad)

print(friends_intersec)