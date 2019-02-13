mmls = find and print partition types
fsstat = print filesystem statistics
  usage: `fsstat \[image\]`

## filesystem commands
fls = print files by filename
  usage: `fls -f \[filetype\] -o \[offset\] image`

## metadata layer commands
istat = print statistics about the inode specified
  usage: `istat -f \[filetype\] -o \[offset\] image inode`

icat = cat the file associated with specified inode
  usage: `icat -f \[filetype\] -o \[offset\] image inode > filetowriteto`

## data layer commands
blkstat = print allocation status of block
  usage: `blkstat -f \[filetype\] -o \[offset\] image address`
