tup=()
tup_rev=()

for i in range(1,5+1):

    tup=tup+(i,)

print(f"The tuple is {tup}")

for i in range((len(tup))-1,-1,-1):

    tup_rev=tup_rev+(tup[i],)

print(tup_rev)





