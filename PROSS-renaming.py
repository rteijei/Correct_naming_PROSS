import re

# Dictionary of residue-specific atom renaming rules
residue_rename_dict = {
    "LYS": {  # Lysine
        "1HB": "HB3",
        "1HG": "HG3",
        "1HD": "HD3",
        "1HE": "HE3",
    },
    "LEU": {  # Leucine
        "1HB": "HB3",
    },
    "SER": {  # Serine
        "1HB": "HB3",
    },
    "ASP": {  # Aspartate
        "1HB": "HB3",
    },
    "PRO": {  # Proline
        "1HB": "HB3",
        "1HG": "HG3",
        "1HD": "HD3",
    },
    "TYR": {  # Tyrosine
        "1HB": "HB3",
    },
    "HID": {  # Histidine-D
        "1HB": "HB3",
        "HB1": "HB3",
        "HD1": "HD3",
        "1HD": "HD3",
    },
    "HIE": {  # Histidine-E
        "1HB": "HB3",
        "HB1": "HB3",
        "HD1": "HD2",
        "1HD": "HD2",
    },
    "HIS": {  # Histidine-E
        "1HB": "HB3",
        "HB1": "HB3",
        "HD1": "HD2",
        "1HD": "HD2",
    },
    "PHE": {  # Phenylalanine
        "1HB": "HB3",
    },
    "GLU": {  # Glutamate
        "1HB": "HB3",
        "1HG": "HG3",
    },
    "GLY": {  # Glycine
        "1HA": "HA3",
    },
    "ILE": {  # Isoleucine
        "1HG1": "HG13",
    },
    "TRP": {  # Phenylalanine
        "1HB": "HB3",
    },
    "ASN": {  # Asparagine
        "1HB": "HB3",
    },
    "GLN": {  # Glutamine
        "1HB": "HB3",
        "1HG": "HG3",
    },
    "ARG": {  # Arginine
        "1HB": "HB3",
        "1HG": "HG3",
        "1HD": "HD3",
    },
    "CYS": {  # Cysteine
        "1HB": "HB3",
    },
    "MET": {  # Methionine
        "1HG": "HG3",
        "1HB": "HB3",
    },

    
    # Add more residue-specific rules as needed
}

# Dictionary of general atom renaming rules:
general_rename_dict = {
    "1H": "H1",
    "2H": "H2",
    "3H": "H3",
    "1HB": "HB1",
    "2HB": "HB2",
    "3HB": "HB3",
    "1HG": "HG1",
    "2HG": "HG2",
    "1HD": "HD1",
    "2HD": "HD2",
    "1HE": "HE1",
    "2HE": "HE2",
    "3HE": "HE3",
    "1HZ": "HZ1",
    "2HZ": "HZ2",
    "3HZ": "HZ3",
    "1HA": "HA1",
    "2HA": "HA2",
    "1HD1": "HD11",
    "2HD1": "HD12",
    "3HD1": "HD13",
    "1HD2": "HD21",
    "2HD2": "HD22",
    "3HD2": "HD23",
    "1HG2": "HG21",
    "2HG2": "HG22",
    "1HG1": "HG11",
    "2HG1": "HG12",
    "3HG1": "HG13",
    "3HG2": "HG23",
    "1HE2": "HE21",
    "2HE2": "HE22",
    "1HE1": "HE11",
    "2HE1": "HE12",
    "3HE1": "HE13",
    "3HE2": "HE23",
    "1HH1": "HH11",
    "2HH1": "HH12",
    "3HH1": "HH13",
    "1HH2": "HH21",
    "2HH2": "HH22",
    "3HH2": "HH23",

    # Add more as needed
}

def rename_atoms_in_pdb(input_pdb, output_pdb, general_map, residue_map):
    with open(input_pdb, "r") as infile:
        lines = infile.readlines()

    updated_lines = []
    for line in lines:
        if line.startswith(("ATOM", "HETATM")):
            atom_name = line[12:16].strip()  # Extract atom name
            residue_name = line[17:20].strip()  # Extract residue name
            
            # Apply residue-specific renaming if the residue is in the dictionary
            if residue_name in residue_map and atom_name in residue_map[residue_name]:
                new_name = residue_map[residue_name][atom_name]
            # Otherwise, apply general renaming if applicable
            elif atom_name in general_map:
                new_name = general_map[atom_name]
            else:
                new_name = atom_name  # Keep the original name if no renaming applies
            
            # Ensure correct spacing in the PDB format
            line = line[:12] + new_name.rjust(4) + line[16:]

        updated_lines.append(line)

    with open(output_pdb, "w") as outfile:
        outfile.writelines(updated_lines)

# Run the function
rename_atoms_in_pdb("input.pdb", "output.pdb", general_rename_dict, residue_rename_dict)

