#!/usr/bin/env python
ga_score = []
with open('wrn_result_score.txt') as fp:
    l = fp.readline()
    while l:
        id, score = l.strip().split()
        score = float(score)
        if score > 0.6:
            ga_score.append( (id, score) )
        else:
            print("%s score is low: %10.4f"%(id, score))
        l = fp.readline()
        
ga_score.sort(key=lambda x:x[1], reverse=True)

fout = open('After_Filter.txt','w')
for id, score in ga_score:
    F = '%s-ali_struct.pdb.output'%id
    contents = open(F).readlines()
    Nalign = len(contents)-5
    if Nalign > 10:
        fout.write('%s\t%8.4f\t%8d\n'%(id, score, Nalign))
    else:
        print("%s has fewer aligned residues: %d"%(id, Nalign))
fout.close()
