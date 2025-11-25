# Add the import statements for functions from string_utils.py and equation_utils.py here



import string_utils
import equation_utils
from string_utils import  parse_chemical_reaction
from string_utils import count_atoms_in_reaction
from string_utils import  build_equations
from equation_utils import my_solve
from equation_utils import sympy
from sympy import solve as sympy_solve
def split_at_number (formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    prefix = formula[:digit_location]
    number = int(formula[digit_location:])

    return prefix, number


def split_by_capitals(formula):
    # Handle empty string
    if formula == "":
        return []

    start = 0
    end = 1
    split_formula = []

    # Loop through characters starting at index 1
    for ch in formula[1:]:
        if ch.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1

    # Append the final section
    split_formula.append(formula[start:end])

    return split_formula

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atom_counts[atom_name] = atom_count
        # Step 2: Update the dictionary with the atom name and count
    return atom_counts
    # Step 3: Return the completed dictionary

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = count_atoms_in_reaction(products)

    # 2.build equation and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]

