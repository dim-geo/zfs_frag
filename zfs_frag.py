#!/usr/bin/env python2                                                                                                                     
                                                                                                                                           
import sys,re                                                                                                                              
from collections import defaultdict
import operator

file_total_blocks={};
file_fragmented_blocks={};
file_not_fragmented_blocks={};

file_total_blocks = defaultdict(lambda:0,file_total_blocks)
file_fragmented_blocks=defaultdict(lambda:0,file_fragmented_blocks)
file_not_fragmented_blocks=defaultdict(lambda:0,file_not_fragmented_blocks)

file_number=0
next_block=0
filename=''
for line in open(sys.argv[1]):
  #print line
  matchObj = re.match( r'\tpath\t(.*)', line)
  if matchObj:
    filename= matchObj.group(1)
    file_total_blocks[filename]=0;
    file_fragmented_blocks[filename]=0;
    file_not_fragmented_blocks[filename]=0;
    #print filename
  matchObj = re.match( r'Indirect blocks', line)
  if matchObj:
    file_number+=1
    next_block = 0
  matchObj = re.match( r'.*L0\s+.*:(.*):(.*?)\s+.+',line)
  if matchObj:
    #print "@",matchObj.group(1),"@",matchObj.group(2),"@",line
    this_block=int(matchObj.group(1),16)
    this_block_size=int(matchObj.group(2),16)
    file_total_blocks[filename]+=1
    if next_block != 0:
      #print next_block,this_block
      if next_block == this_block:
        file_not_fragmented_blocks[filename]+=1
        #print 'not fragmented'
      else:
        file_fragmented_blocks[filename]+=1
        #print 'fragmented'
    next_block=this_block+this_block_size

print 'There are {} files.'.format( file_number )

fragmented=sum(file_fragmented_blocks.values())
not_fragmented=sum(file_not_fragmented_blocks.values())
total_fragment_blocks = fragmented + not_fragmented

print "There are {} blocks and {} fragment blocks.".format(sum(file_total_blocks.values()), total_fragment_blocks )
print "There are {} fragmented blocks {:.2%}.".format(fragmented, float(fragmented)/total_fragment_blocks )
print "There are {} contiguous blocks {:.2%}.".format(not_fragmented, float(not_fragmented)/total_fragment_blocks )

fragmented_files={}
for filename in file_total_blocks:
  if file_total_blocks[filename]>1 and file_fragmented_blocks[filename]>0:
    #print filename,":",file_fragmented_blocks[filename]+file_not_fragmented_blocks[filename],":",file_fragmented_blocks[filename]
    fragmented_files[filename]=(file_fragmented_blocks[filename]+file_not_fragmented_blocks[filename],file_not_fragmented_blocks[filename])

sorted_fragmented_files = sorted(fragmented_files.items(), key=operator.itemgetter(1))
for item in sorted_fragmented_files:
  if item[0]=='':
    continue
  print "Name: {} Blocks: {} Fragmentation {:.2%}".format(item[0],item[1][0],float(item[1][0]-item[1][1])/item[1][0])
