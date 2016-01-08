from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from Bio import SeqIO
 
import os
def hextract (hmmout, outname):
    f=file(hmmout)
    all=[]
    for lines in f.readlines():
        all.append(lines.strip())
    f.close()
    j=0
    output=[]
    temp=[]
    for i in range(len(all)):
        if len(all[i])==0:
            continue
        else:
            if all[i][0]=='=' and float(all[i][54:62].strip())<0.1:
                temp.append(all[i+4][3:9]+'_'+all[i][10])
                temp.append((all[i+4][27:all[i+4][27:].strip().find(" ")+28].replace('-','')).strip())
                output.append('')
                output[j]=temp
                temp=[]
                j=j+1
    rec=[]
    for i in range(len(output)):
        rec.append(SeqRecord(Seq(output[i][1],generic_protein),id=output[i][0]))
    handle=open(outname,'w')   
    SeqIO.write(rec,handle,'fasta')
    handle.close()
    print len(output)

if __name__=='__main__':
    hextract('total.out','test2')