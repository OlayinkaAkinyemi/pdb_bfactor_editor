#!pip install biopython ### biopython needs to be installed
import Bio
import pandas as pd
from Bio.PDB.PDBParser import PDBParser as pdbp
from Bio.PDB.PDBIO import PDBIO
parser = pdbp(PERMISSIVE=1)

def pdb_bfactor_editor(inputfile, bfactor_list, outputfile):
	# bfactor_list is a python list of data to replace the bfactor column
	structure_id = "input"
	structure = parser.get_structure(structure_id, inputfile)
	for i in range(1, len(bfactor_list)+1):
		residue = structure[0][" "][i]
		for atom in residue:
			atom.bfactor = bfactor_list[i-1]
	io = PDBIO()
	io.set_structure(structure)
	io.save(outputfile)

### Example

# supply a python list of SHAPE reactivities or any other data to replace the bfactor column. 
new_bfactor = pd.read_excel("/Users/oakinyemi/Desktop/for_griffin/c31u_shape.xlsx")["C31U bnd 2"].tolist()

# supply the file path for the PDB to be edited
filepath = "/Users/oakinyemi/Desktop/Holo-without-bfactors.pdb"

# supply the output name for the new pdb
outputfile = "/Users/oakinyemi/Desktop/for_griffin/C31U_bnd2.pdb"

# call the function
pdb_bfactor_editor(filepath, new_bfactor, outputfile)


#### from command line, implement as: python bfactor_editor.py
