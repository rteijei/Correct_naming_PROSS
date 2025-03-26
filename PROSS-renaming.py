import re

def fix_hydrogen_naming(pdb_file, output_file):
    with open(pdb_file, "r") as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            atom_name = line[12:16].strip()
            # Match names like 3HZ or 2HD1
            match = re.match(r"(\d)([A-Z]+)", atom_name)
            if match:
                new_name = f"{match.group(2)}{match.group(1)}"
                line = line[:12] + new_name.rjust(4) + line[16:]
        fixed_lines.append(line)

    with open(output_file, "w") as f:
        f.writelines(fixed_lines)

# Example usage
fix_hydrogen_naming("input.pdb", "output.pdb")
