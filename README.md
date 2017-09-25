# ZFS fragmentation analysis
Script to find most fragmented files on ZFS. Unfortunately this info cannot be used to defrag ZFS even via userspace utilities.
If someone knows how to defrag ZFS via userspace programs, please contact me and I will incorporate the needed functionality.
How can I allocate continuous space in ZFS?

Inspiration: http://daemonforums.org/showthread.php?t=8386

The tool prints the files that are fragmented from smaller to larger and from most fragmented to less fragmented.

# Usage:

```
zdb -ddddd pool/dataset > data.txt
zfs_frag.py data.txt
```

# Sample output:
```
There are 1382 files.
There are 7141 blocks and 4422 fragment blocks.
There are 3812 fragmented blocks 86.21%.
There are 610 contiguous blocks 13.79%.

Name: /mobile_data/.thumbnails/.sync-conflict-20160416-144740.thumbindex3--1967290299 Blocks: 3 Fragmentation 100.00%
Name: /mobile_data/.thumbnails/.sync-conflict-20160419-203503.thumbindex3--1967290299 Blocks: 3 Fragmentation 33.33%
Name: /mobile_data/.thumbnails/.sync-conflict-20160417-102638.thumbindex3--1967290299 Blocks: 3 Fragmentation 33.33%
Name: /mobile_data/.thumbnails/.sync-conflict-20160421-183320.thumbindex3--1967290299 Blocks: 3 Fragmentation 33.33%
Name: /mobile_data/.thumbnails/.sync-conflict-20160428-222324.thumbindex3--1967290299 Blocks: 4 Fragmentation 50.00%
Name: /mobile_data/.thumbnails/.thumbindex3--1967290299 Blocks: 4 Fragmentation 25.00%
Name: /mobile_data/.thumbnails/.sync-conflict-20160417-102638.thumbdata3--1967290299 Blocks: 6 Fragmentation 66.67%
Name: /mobile_data/.thumbnails/.sync-conflict-20160416-144828.thumbdata3--1967290299 Blocks: 6 Fragmentation 66.67%
Name: /mobile_data/.thumbnails/.sync-conflict-20160420-183603.thumbdata3--1967290299 Blocks: 7 Fragmentation 57.14%
Name: /mobile_data/.thumbnails/.sync-conflict-20160423-012613.thumbdata3--1967290299 Blocks: 7 Fragmentation 42.86%
Name: /mobile_data/.thumbnails/.sync-conflict-20160421-183320.thumbdata3--1967290299 Blocks: 7 Fragmentation 42.86%
Name: /mobile_data/.thumbnails/.sync-conflict-20160428-221518.thumbdata3--1967290299 Blocks: 10 Fragmentation 60.00%
Name: /mobile_data/.thumbnails/.sync-conflict-20160428-222324.thumbdata3--1967290299 Blocks: 10 Fragmentation 40.00%
Name: /mobile_data/.thumbnails/.thumbdata3--1967290299 Blocks: 11 Fragmentation 36.36%
```
