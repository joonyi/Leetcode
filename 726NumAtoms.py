"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters,
representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1.
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form:
the first name (in sorted order), followed by its count (if that count is more than 1),
followed by the second name (in sorted order), followed by its count (if that count is more than 1),
and so on.
"""

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # ascii of '0':48 to '9':57
        stack = []
        ret = {}
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                if 48 <= ord(stack[-1]) <= 57:
                    temp = stack.pop()
                    elem = stack.pop()
                    ret[elem] = temp
                elif 97 <= ord(stack[-1]) <= 122:
                    temp = stack.pop()
                    elem = stack.pop() + temp
                    ret[elem] = 1
                else:
                    ret[stack.pop()] = 1
                i += 1
            elif formula[i] == ")":
                factor = int(formula[i+1])
                while stack and stack[-1] != "(":
                    elem = stack.pop()
                    if 48 <= ord(elem) <= 57:
                        pass
                    else:
                        ret[elem] = factor
                # stack.pop() # pop out "("
                i += 2
            else:
                stack.append(formula[i])
                i += 1

        return ret

    def countOfAtoms2(self, formula):
        import re
        from collections import defaultdict
        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        stack, i = [defaultdict(int)], 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(defaultdict(int))
            else:
                count = 1
                # Check if next token is a number.
                if i + 1 < len(tokens) and re.search('^\d+$', tokens[i + 1]):
                    count, i = int(tokens[i + 1]), i + 1
                atoms = stack.pop() if token == ')' else {token: 1}
                # Combine counts of atoms.
                for atom in atoms:
                    stack[-1][atom] += atoms[atom] * count
            i += 1
        return ''.join([atom + (str(count) if count > 1 else '') for atom, count in sorted(stack[-1].items())])

formula = "Mg(OH)2"
print(Solution().countOfAtoms2(formula))
