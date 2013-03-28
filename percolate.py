#################################################
#Author: Michelle Austria Fernandez
#Uni: mf2492
#
#Program: percolate.py
#Overview: Contains functions that runs the
#percolation simulations
#################################################


import numpy as np
import os



def gridFile():
    """Prompts user to either enter an existing file or create
    a new file"""
    choice = ' '
    while (choice != 'r' and choice != 'c'):
        choice = raw_input("Would you like to read(r) an existing file"
                           + " or create(c) a new file? ")
        
    if (choice == 'r'):
        existing_file = raw_input("Enter name of file: ")
        bool_array_r = readFile(existing_file)
        return percolate(bool_array_r)
    
    elif (choice == 'c'):
        new_file = raw_input("Enter name of output file: ")
        p,n = probability()
        percolates = writeFile(new_file, p, n)
        return percolates


def defaultFile(i_file):
    """Runs simulation with given files without prompting the user"""
    bool_array_r = readFile(i_file)
    return percolate(bool_array_r)


def probability():
    """Prompts user to enter probability factor and size"""
    p = input("Enter probability factor (between 0-1): ")
    n = input("Enter grid size: ")
    return p, n


def readFile(existing_file):
    """reads in the file and converts it to an array"""
    f = open(existing_file, 'r')
    size = f.readline()
    print size.rstrip('\n')
    line = f.readline()
    array = []
    while line:
        print line.rstrip('\n')
        array_line = line.split()
        array_line = [int(item) for item in array_line]
        array_line = [bool(item) for item in array_line]
        array_line = np.invert(array_line)
        array_line = array_line.astype(int)
        array.append(array_line)
        line = f.readline()
    full_array = np.vstack(array)
    f.close()

    return full_array


def writeFile(file_name, probability, grid_size):
    """Writes out the file and runs the percolation program"""
    grid = np.random.random(size = (grid_size,grid_size)) < probability
    does_percolate = percolate(grid)
    grid = grid.astype(bool)
    grid = np.invert(grid)
    grid = grid.astype(int)
    grid  = '\n'.join(' '.join(str(cell) for cell in row) for row in grid)
    print(grid)
    f = open(file_name, "w")
    f.write(str(grid_size)+ '\n')
    f.write(str(grid))
    f.close

    return does_percolate


def flow(bool_array):
    """Starts from the top of the grid to test percolation"""
    x = bool_array.shape[0]
    full = np.zeros(shape = (x, x))
    for i in range(x):
        flowFull(bool_array, full, 0, i)
    return full


def flowFull(sites, full, i, j):
    """Goes through neighboring sites to fill"""
    x = sites.shape[0]

    if (i < 0 or i >= x): return;
    if (j < 0 or j >= x): return;
    if (not (sites[i][j])): return;
    if (full[i][j]): return;

    full[i][j] = True

    flowFull(sites, full, i+1, j);   
    flowFull(sites, full, i, j+1);   
    flowFull(sites, full, i, j-1);  


def percolate(site):
    """Determines wether the grid percolates"""
    x = site.shape[0]
    full = flow(site)
    for i in range(x):
        if (full[x-1][i]):
            return True
        else:
            return False
    
