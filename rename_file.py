#!/usr/bin/python

import fnmatch
import os


for root, dirnames, filenames in os.walk('/disce/datastore/2017_BSBC/BR725'):
    for filename in fnmatch.filter(filenames, 'BR725_C086_*.xml'):
        oldfilename = os.path.basename(os.path.join(root, filename))
        rootdir = os.path.dirname(os.path.join(root, filename))
#        filesize = os.path.getsize(os.path.join(root, filename))
        newfilename = oldfilename.replace("BR725_C086", "BR725_C085")
        dst = '../../XML/%s' % newfilename
               
        if "XML" in rootdir:
           os.chdir(rootdir)
           os.rename(oldfilename, newfilename)
#           print "%s\t%s" % (oldfilename, newfilename) 
#           print (os.system("pwd"))
        elif "CA" in rootdir:
           os.chdir(rootdir)
           os.symlink(dst, newfilename)
           try:
              os.remove(oldfilename)
           except OSError:
              pass
#           print "%s\t%s" % (newfilename, dst)
#           print (os.system("pwd"))
        else:
           print "%s\t%s\t%s" % (rootdir, oldfilename, newfilename)

