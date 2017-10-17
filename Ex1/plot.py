import matplotlib.pyplot as plt

N_L3 = [3000000,4000000,6000000,7000000,1000000]
 
copy_L3 = [11527.4,11834.2,11524.8,11854.6,11822.0]
scale_L3 = [11605.2,11725.7,11667.4,12028.5,11472.8]
add_L3 = [11846.0,12739.0,11912.6,12811.7,12558.3]
triad_L3 = [12392.4,12791.6,12311.8,13238.9,12414.1]

N_L2 = [500000,1000000,1500000,2000000,2500000]

copy_L2 = [15716.4,12037.5,11713.2,12116.8,11771.8]
scale_L2 = [14979.7,11817.0,11391.1,11913.5,11803.3]
add_L2 = [15210.5,12134.0,11730.5,12941.2,12378.7]
triad_L2 = [14961.8,12429.1,12085.4,12962.9,12788.2]

N_L1 = [125000,200000,250000,350000,450000]

copy_L1 = [16644.1,17499.1,18620.7,14031.1,13332.9]
scale_L1 = [15391.9,16925.3,20510.0,13300.2,13239.4]
add_L1 = [17747.4,17644.7,24105.2,14582.8,13433.7]
triad_L1 = [17647.8,17207.4,23519.5,13975.5,13218.1]

bandwidth = copy_L1 + copy_L2 + copy_L3 + scale_L1 + scale_L2 + scale_L3 + add_L1 + add_L2 + add_L3 + triad_L1 + triad_L2 + triad_L3 
copy_words = [x*2 for x in N_L1] + [x*2 for x in N_L2] + [x*2 for x in N_L3]
scale_words = copy_words
add_words = [x*3 for x in N_L1] + [x*3 for x in N_L2] + [x*3 for x in N_L3]
triad_words = add_words
words = copy_words + scale_words + add_words + triad_words

plt.plot(copy_words, copy_L1 + copy_L2 + copy_L3, 'rx', label='copy')
plt.plot(scale_words, scale_L1 + scale_L2 + scale_L3, 'bs', label='scale')
plt.plot(add_words, add_L1 + add_L2 + add_L3, 'g^', label='add')
plt.plot(triad_words, triad_L1 + triad_L2 + triad_L3, 'co', label='triad')
#plt.plot(words, [108800]*len(words), 'y--', label='peak cache bandwidth')
plt.xscale('log')
plt.ylabel('Bandwidth (MB/s)')
plt.xlabel('Words (in log scale)')
plt.legend(loc='upper right')
plt.title('Plot of bandwidth for each subbenchmark')

plt.show()

