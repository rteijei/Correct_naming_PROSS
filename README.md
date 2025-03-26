# Correct_naming_PROSS
Script to name correctly PROSS output for MD simulations


PROSS output PDB files have a naming for the hydrogen atoms that is sometimes difficult for MD simulation programs to recognize: For example, atom HB2 in a PROSS output would be named 2HB, and AMBER FF do not recognize that nomenclature. Therefore, to prepare your files for your MD simulations, you can just run your PROSS output through this python script, and you will obtain a PDB file with the correct naming for AMBER!
