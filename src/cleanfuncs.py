#Functions

#Note: some of the functions in this document have been defined just
#for experiemntal purposes and thus have not been used or applied during
#this project

import datetime
import datefinder as dfi

def sub_df(name, tag):
    ''' 
    This function slices a part of a dataframe for a given country, renames the column
    containing import data as Imports and generates a new column to track the country
    which has been targeted. A df is returned.
    '''
    df = pd.DataFrame(BI_trade[['Time',f'{name}']]).rename({f'{name}': 'Imports'}, axis=1)
    df['Country'] = [f'{tag}' for v in range (0,263)]
    return df





def del_p(x):
    ''' This function which takes a string as argument, returns the same string
    that was entered but without (p) in case there are any of these in the original
    string
    '''
    try:
        return x.replace('(p)', '')
    except:
        pass
    
def del_total(x):
    ''' This function which takes a string as argument, returns the same string
    that was entered but without (p) in case there are any of these in the original
    string
    '''
    try:
        return x.replace('_Total', '')
    except:
        pass
    
def del_acumulado(x):
    ''' This function which takes a string as argument, returns the same string
    that was entered but without (p) in case there are any of these in the original
    string
    '''
    try:
        return x.replace('_Acumulado', '')
    except:
        pass

def del_years(x):
    ''' This function returns a nan if the given argument (must be a string)
    has 4 or less characters. Otherwise  it returns the intact original string.
    The original purpose of this function was to delete cells with year info but 
    no month info.
    '''
    import numpy as np
    if len(x.strip()) < 5:
        return 'tbd'
    else:
        return x
    
def type_el(x):
    '''Returns the type of an element'''
    print(type(x))
    
def del_spaces(x):
    ''' Function to apply the strip method for strings'''
    return x.strip()

def translate_month(x):
    ''' This function translates months in spanish to english'''
    if 'Enero' in x:
        return x.replace('Enero', 'January')
    elif 'Febrero' in x:
        return x.replace('Febrero', 'February')
    elif 'Marzo' in x:
        return x.replace('Marzo', 'March')
    elif 'Abril' in x:
        return x.replace('Abril', 'April')
    elif 'Mayo' in x:
        return x.replace('Mayo', 'May')
    elif 'Junio' in x:
        return x.replace('Junio', 'June')
    elif 'Julio' in x:
        return x.replace('Julio', 'July')
    elif 'Agosto' in x:
        return x.replace('Agosto', 'August')
    elif 'Septiembre' in x:
        return x.replace('Septiembre', 'September')
    elif 'Octubre' in x:
        return x.replace('Octubre', 'October')
    elif 'Noviembre' in x:
        return x.replace('Noviembre', 'November')
    elif 'Diciembre' in x:
        return x.replace('Diciembre', 'December')
    else:
        return x

def translate_number(x):
    ''' This function transform month acronyms 'MXX' into months in english'''
    if 'M01' in x:
        return x.replace('M01', ' January')
    elif 'M02' in x:
        return x.replace('M02', ' February')
    elif 'M03' in x:
        return x.replace('M03', ' March')
    elif 'M04' in x:
        return x.replace('M04', ' April')
    elif 'M05' in x:
        return x.replace('M05', ' May')
    elif 'M06' in x:
        return x.replace('M06', ' June')
    elif 'M07' in x:
        return x.replace('M07', ' July')
    elif 'M08' in x:
        return x.replace('M08', ' August')
    elif 'M09' in x:
        return x.replace('M09', ' September')
    elif 'M10' in x:
        return x.replace('M10', ' October')
    elif 'M11' in x:
        return x.replace('M11', ' November')
    elif 'M12' in x:
        return x.replace('M12', ' December')
    else:
        return x

    
def datematcher(x):
    '''Function to extract a datetime object from a string
    (Based on the datefinder library)'''
    
    matches = dfi.find_dates(x)
    for match in matches:
        return(match)
    
    
def dateconverter(x):  
    ''' Converts a datetime.datetime object into a  datetime.date object and returns it'''
    return datetime.datetime.date(x)

def index_b_count(w, x, v, h):
    '''
    Return a dictionary containing the ratio between the count of two given categorical variables for the rows of a df
    whose index has a given value as value, and the index of refference of the dataframe as key
    Where w is a dataframe, x is a list of indices, v is the column that will serve as basis for the count
    and h is the column from which the values making up x have been taken
    '''
    emptydict = {}
    
    
    for i in x:
        w_temp = w[w[h] == i]
        if len(w_temp[v].value_counts().value_counts()) > 1:
            a = len(w_temp[v])
            b = w_temp[v].value_counts()[1]
            c = b/a
            emptydict[i] = c
        else:
            emptydict[i] = 0
            
    
    return emptydict

def punct_num(x):
    '''
    Eliminates dots and substitutes commas for dots in numeric strings
    in order to make them convertible to float
    '''
    y = x.replace(".", "")
    return y.replace(",",".")

def punct_num_str(x):
    '''
    Eliminates dots and substitutes commas for dots in numeric strings
    in order to make them convertible to float
    '''
    try:
        y = str(x).replace(".", "")
        return int(str(y).replace(",","."))
    except:
        y = x.replace(".", "")
    return y.replace(",",".")


def no_dots(x):
    ''' 
    Substitutes strings containing three dots
    for np.nan objects
    '''
    if '...' in str(x):
        return  np.nan
    else:
        pass
