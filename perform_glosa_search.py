#!/usr/bin/env python
import glob, os, sys
import subprocess
from subprocess import PIPE
from multiprocessing import Pool

### Modify here ###
query_pdb = 'WRN_0532_1235_model.pdb'
logfile = 'wrn_result_score.txt'
outdir = 'wrn_result'
###

## 
# GA_score Threshold.
ga_score_thres = 0.6 # GA_Score threshold. 
# Chemical Feature file.
query_cf = query_pdb[:-4]+'-cf.pdb'
# Output files of G-Losa program
output_files = ('product_graph.rst', 'pairs.rst', 'matrix.txt', 'ali_struct.pdb')

# reference binding site files, downloaded from https://compbio.lehigh.edu/GLoSA/
rootdir = os.getcwd()
bs_files = sorted( glob.glob('%s/07-2018_nr-ligand-bs-70/*BS-[0-9].pdb' % rootdir) )#, reverse=True)
# Save GA scores into the list
score_list = []
# Output log file.
fout = open(logfile, 'w')

def perform_glosa(pdb):
    # Perform G-LoSA calculations using the downloaded library.
    id = pdb.split('/')[-1][:-4]
    commands = ['%s/glosa.exe'%rootdir, '-s1', query_pdb, '-s1cf', query_cf, '-s2', pdb, '-s2cf', pdb[:-4]+'-cf.pdb']
    print(' '.join(commands))

    try:
        p = subprocess.run(commands, check=True, stdout = subprocess.PIPE)
    except:
        return id, -1.0
    
    if p.returncode ==0:
        output = p.stdout
        # Parsing G-LoSA output
        log = output.split()

        ga_score = float(log[9])
        score_list.append( (id, ga_score) )
        fout.write('%s\t%10.4f\n'%(id, ga_score))
        
        if ga_score > ga_score_thres:
            for f in output_files:
                os.rename(f, './%s/%s-%s'%(outdir, id, f))

        return id, ga_score

    else:
        
        return id, -1.0


def collect_results(x):
    print('CALLback:', x)
    score_list.append(x)
    
if __name__=='__main__':

    # Generate chemical feature file.
    command = 'java AssignChemicalFeatures %s' % query_pdb
    #p = subprocess.run(command, check=True, stdout = subprocess.PIPE)
    os.system(command)

    # Create outdir if it does not exist.
    if not os.path.exists(outdir): os.mkdir(outdir)

    # Iterate G-LoSA calculations.
    for idx, pdb in enumerate(bs_files):
        print( '( %d / %d )'%(idx, len(bs_files)))
        perform_glosa(pdb)
