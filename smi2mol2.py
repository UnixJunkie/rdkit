#!/usr/bin/python2

from __future__ import print_function

# import numpy # to troubleshoot numpy install
# print numpy.__path__

import sys

from rdkit import Chem
from rdkit.Chem import AllChem

from rdkit.Chem.Mol2Writer import MolToMol2Block, MolToMol2File, \
                                  Mol2MolSupplier, Mol2Writer

argc = len(sys.argv)
if argc != 3:
    #                    0  1          2
    print("fatal: usage: %s <file.smi> <file.mol2>" %
          sys.argv[0], file=sys.stderr)
    exit(1)

mol_reader = Chem.SmilesMolSupplier(sys.argv[1])
output = open(sys.argv[2], 'w')
i = 0
for mol in mol_reader:
    try:
        mol2 = MolToMol2Block(mol)
        output.write(mol2)
    except:
        print("%s: error at index %d" % (sys.argv[0], i),
              file=sys.stderr)
    i = i + 1
output.close()
