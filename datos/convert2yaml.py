#!/usr/bin/python3

# https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python
# Usage:
# -i --input     ruta de archivo o enlace (si utiliza la bandera -u)
# -o --output    ruta y nombre del archivo de salida, si no se especifica se utilizarán los datos de entrada
# -m --model     nombre del modelo (app.tabla)
# -d --delimiter especifica el caracter delimitador (por defecto se usará ;)
# -u --url       bandera que indica que la entrada es una URL y debe tratarse como tal
# -f --folder    bandera que indica que la entrada es un directorio y debe tratarse como tal
# -h --help      muestra la forma de uso del comando

# csv delimitado por ;
# convert2yaml.py -i ../db_access/Adherentes.csv -o adherentes.yaml

import yaml
import os
import csv
import codecs
from urllib.request import urlopen
import getopt
import sys

root = os.getcwd()
MODEL = "app_name.model_name"
DELIMITER = ";"
QUOTECHAR = '"'

def csvToYaml2(csvFile, output):
    global MODEL
    global DELIMITER
    global QUOTECHAR

    f = open(output, 'w', encoding="utf-8")
    csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'), delimiter=DELIMITER, quotechar=QUOTECHAR)
    data_headings = []

    for i, row in enumerate(csvOpen):
        if i == 0:
            data_headings = row
        else:
            for cell_index, cell in enumerate(row):
                cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")

                if cell_heading == 'id':
                    f.write('- model: ' + MODEL + '\n')
                    f.write('  pk: {}\n'.format(cell))
                    f.write('  fields:\n')
                else:
                    if cell:
                        cell_text = "    " + cell_heading + ": " + cell.replace("\n", ", ") + "\n"
                        f.write(cell_text)
    f.close()

# takes a csvFile name and output file name/path
def csvToYaml(csvFile, output):
    global DELIMITER
    global QUOTECHAR

    stream = open(output, 'w',encoding="utf-8")
    # https://stackoverflow.com/questions/18897029/read-csv-file-from-url-into-python-3-x-csv-error-iterator-should-return-str
    # need to decode bytes
    csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'), delimiter=DELIMITER, quotechar=QUOTECHAR)
    keys = next(csvOpen)
    for row in csvOpen:
        yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False)

# converts single url file
def urlCSV(url, output=None):
    csvFile = urlopen(url)
    output = output if output else root+'/'+(url.split('/')[-1].replace('.csv','.yaml'))
    csvToYaml(csvFile, output)

# converts all csv file in this folder
def localCSV(folder=root):
    # print folder
    for f in os.listdir(folder):
        if f.endswith('.csv'):
            csvFile = os.path.join(folder, f)
            output = os.path.join(folder, f.replace('.csv','.yaml'))
            print(output)
            singleCSV(csvFile, output)

# converts only one csv file
def singleCSV(csvFile, output=None):
    output = output if output else root+'/'+(csvFile.split('/')[-1].replace('.csv','.yaml'))
    with open(csvFile, 'rb') as csvFile:
        csvToYaml2(csvFile, output)

# print -h --help
def usage():
    msg = "Uso: \n"
    msg = msg + "-i --input     ruta de archivo o enlace (si utiliza la bandera -u) \n"
    msg = msg + "-o --output    ruta y nombre del archivo de salida, si no se especifica se utilizarán los datos de entrada \n"
    msg = msg + "-m --model     nombre del modelo (app.tabla) \n"
    msg = msg + "-d --delimiter especifica el caracter delimitador (por defecto se usará ;) \n"
    msg = msg + "-u --url       bandera que indica que la entrada es una URL y debe tratarse como tal \n"
    msg = msg + "-f --folder    bandera que indica que la entrada es un directorio y debe tratarse como tal \n"
    msg = msg + "-h --help      muestra la forma de uso del comando \n"
    print(msg)

def main():
    global DELIMITER
    global MODEL

    try:
        opts, args = getopt.getopt(sys.argv[1:], 
                                   'h:i:o:m:d:u:f', 
                                   ['help', 'input','output', 'model', 'delimiter', 'url', 'folder'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    csvFile = None
    output = None
    url = False
    folder = False
    if len(opts) == 0:
        localCSV()
        exit()
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-i', '--input'):
            csvFile = a.strip()
        elif o in ('-o', '--output'):
            output = a.strip()
        elif o in ('-m', '--model'):
            MODEL = a.strip()
        elif o in ('-d', '--delimiter'):
            DELIMITER = a.strip()
        elif o in ('-u', '--url'):
            url = True
        elif o in ('-f', '--folder'):
            folder = True
        else:
            print('opción no controlada')
    if url:
        urlCSV(csvFile, output)
        exit()
    elif folder:
        localCSV(csvFile)
        exit()
    singleCSV(csvFile, output)


if __name__ in ("__main__"):
    main()
