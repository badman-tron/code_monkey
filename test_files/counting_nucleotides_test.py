seq = 'AGGGGTGTGTCACACACACACAGGTTGTGATGTGA'

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for char in seq:
    if char == 'A':
       a_count +=1
       
for char in seq:
    if char == 'C':
       c_count +=1

for char in seq:
    if char == 'G':
       g_count +=1      
       
for char in seq:
    if char == 'T':
       t_count +=1 

print "A: %s, C: %s, G: %s, T: %s" % (a_count, c_count, g_count, t_count)