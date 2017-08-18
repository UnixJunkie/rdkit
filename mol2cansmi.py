#!/usr/bin/python2

from __future__ import print_function

import sys

from rdkit import Chem
from rdkit.Chem import AllChem

from rdkit.Chem.Mol2Writer import MolToMol2Block, MolToMol2File, \
                                  Mol2MolSupplier, Mol2Writer

argc = len(sys.argv)
if argc != 3:
    #                    0  1           2
    print("fatal: usage: %s <file.mol2> <file.can.smi>" %
          sys.argv[0], file=sys.stderr)
    exit(1)

mol_reader = Chem.Mol2MolSupplier(sys.argv[1])
output = open(sys.argv[2], 'w')
i = 0
for mol in mol_reader:
    try:
        can_smi = Chem.MolToSmiles(mol)
        name = mol.GetProp("_Name")
        print("%s %s" % (can_smi, name), file = output)
    except:
        print("%s: error at index %d" % (sys.argv[0], i),
              file=sys.stderr)
    i = i + 1
output.close()
