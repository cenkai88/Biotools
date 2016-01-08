# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 16:54:48 2016

@author: cenkai
"""

def phy2meg(inpath, outpath):
    lineone = {}
    tmp = []
    with open(inpath) as raw:
        tmpch = ''
        for line in raw.readlines():
            if line[0] == '1':
                tmp.append(line)
            elif line[0]!=' ' and line!='\n':
                if tmpch!='':
                    tmp.append(tmpch+'\n')
                    print len(tmpch)
                tmpch = line.split('   ')[-1].replace(' ','').strip()
                tmp.append(line.split('   ')[0])
            else:
                tmpch = tmpch + line.replace(' ' ,'').strip()
        tmp.append(tmpch)


    for i in xrange(len(tmp[2])):
        lineone[i]=tmp[2][i]

    final = tmp
    for i in xrange((len(tmp)-1)/2):
        for j in xrange(len(tmp[i+2])):
            if tmp[i+2][j] == '.':
                final[i+2] = final[i+2][:j]+lineone[j]+final[i+2][j+1:]

    with open(outpath, 'w') as output:
        for line in final:
            output.write(line+'\n')

