# get nn
nn = "The quick brown fox jumped over the lazy dog"
jj = nn.split(" ")

# Just a demo
print(jj)

for i in jj:
    print(i, end=" | ")
print('\n')

# use del to delete a elem from a list
del jj[2]
print(jj)

jj[1] = 'slow'
print(jj)

jj.insert(2, 'white')
print(jj)
jj += ['this', 'morning']
print(jj)


kk = [8, 6, 7, 5, 3, 0, 9]
kk.sort()
print(kk)


#list[start:end:sequence]
print(kk[::2])
