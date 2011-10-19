#! /usr/bin/env python

import os, sys
import configuration # this refers to the local file configuration.py

def usage ():
    print ("Usage: " + sys.argv[0] + " <template> <name>")
    print ("\ttemplate - the template file to use. If it does not name an\n" +
           "\texisting file, looks in " + configuration.template_dir + "\n")
    print ("\tname - the name to substitute into the template. Also used\n" +
           "\tfor the filename of the output, with " + configuration.extension +
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

# The __name__ variable is "__main__" when the program is run directly from
# the command line. Putting all the main code in a function and calling it only
# when the test is true allows for this program to be used as a module by
# other Python programs, if you really want to. You would use "import template"
# and then could call template.main() to get the effects of calling it from the
# command line.

if __name__ == "__main__":
    main ()
