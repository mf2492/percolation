#################################################
#Author: Michelle Austria Fernandez
#Uni: mf2492
#
#Program: A4.py
#Overview: This program reads and writes text files
#and determines whether the given grid can percolate. 
#################################################

import percolate

def main():
    """ Runs all of the functions available, giving an
        over view of the functionality of this program"""

    percolates = percolate.defaultFile("allones.txt")
    result(percolates)

    percolates = percolate.defaultFile("allzeros.txt")
    result(percolates)

    percolates = percolate.defaultFile("test.txt")
    result(percolates)

    percolates = percolate.defaultFile("large.txt")
    result(percolates)

    run = 'y'
    while (run == 'y'):
        percolates = percolate.gridFile()
        result(percolates)
        run = raw_input("Run simulation again (y/n)? ")
    

def result(percolates):
    """Displays whether the grid perculates"""
    if percolates == True:
        print("This grid percolates.\n")
    else:
        print("This grid does not percolate.\n")
    
    
main()
