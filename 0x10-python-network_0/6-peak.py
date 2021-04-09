#!/usr/bin/python3
'''module: peak'''

def find_peak(list_of_integers):
    ''' funcion: find the peak number '''
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return(list_of_integers[0])
