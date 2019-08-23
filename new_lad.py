from schrodinger import structure
import sys
import json
import numpy as np


def has_ring(st):
    ring_list = []
    for ring in st.ring:
        ring_list.append(ring)
    if len(ring_list) != 0:
        return True
    else:
        return False

def bond_belongs_to_ring(bond, st):
    if has_ring(st):
        ring_atom_list = []
        for ring in st.ring:
            for atom in ring.atom:
                ring_atom_list.append(atom.index)
        if (bond.atom1.index in ring_atom_list or bond.atom2.index in ring_atom_list):
            return True
        else:
            return False
    else:
        return False

bond_dict = {}

sts = structure.StructureReader(sys.argv[1])
for st in sts:
    for bond in st.bond:
        # print(bond.length, bond.order, bond.type, bond.atom1.atomic_number, bond.atom2.atomic_number)
        # bond_name = "%d_%d_%d"%(bond.atom1.atomic_number, bond.atom2.atomic_number, bond.order)
        if bond_belongs_to_ring(bond, st):
            continue
        if bond.atom1.atomic_number < bond.atom2.atomic_number:
            bond_name = "%s_%s_%d"%(bond.atom1.element, bond.atom2.element, bond.order)
        else:
            bond_name = "%s_%s_%d"%(bond.atom2.element, bond.atom1.element, bond.order)
        if bond_name in bond_dict.keys():
            bond_dict[bond_name].append(bond.length)
        else:
            bond_dict[bond_name] = [bond.length]

new_bond_dict = {}
for key, value in bond_dict.items():
    new_bond_dict[key] = np.average(value)

with open("bond_data.json",'w') as fh:
    json.dump(new_bond_dict, fh, indent=4)
