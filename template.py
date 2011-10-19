#! /usr/bin/env python

import os, sys
import configuration

def usage ():
    print ("Usage: " + sys.argv[0] + " <template> <name>")
    print ("\ttemplate - the template file to use. If it does not name an " +
           "existing file, looks in " + configuration.template_dir)
    print ("\tname - the name to substitute into the template. Also used " +
           "for the filename of the output, with " + configuration.extension +
           " added.")

def main ():
    if len(sys.argv) < 3:
        usage ()
        exit()

        if os.path.exists (sys.argv[1]):
            template = open (sys.argv[1])
        elif os.path.exists (configuration.template_dir + sys.argv[1]):
            template = open (configuration.template_dir + sys.argv[1])
        else:
            raise IOError ("Template file " + sys.argv[1] + " not found.")
        
        new_file = open (sys.argv[2] + configuration.extension, "w")
        
        output = template.read().replace (configuration.name_placeholder,
                                          sys.argv[2])
        
        new_file.write (output)

if __name__ == "__main__":
    main ()
