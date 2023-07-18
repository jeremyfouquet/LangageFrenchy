"""
Ce programme contient la classe BasicExecute qui évalue et exécute un arbre syntaxique de manière hiérarchique dans un processus récursif.
"""

__author__ = "Jeremy Fouquet"
__version__ = "1.0.0"
__credits__ = "Réalisé dans le cadre du cours de Interprétation & Compilation de L3 Informatique de L IED"
__description__ = "Ce programme utilise la classe BasicExecute pour évaluer et exécuter un arbre syntaxique de manière hiérarchique."

class BasicExecute:
    """
    Evalue l'arbre syntaxique de manière hiérarchique dans un processus récursif pour executer et afficher la réponse
    """
    def __init__(self, tree, env):
        """
        Initialise l'environnement avec l'environnement passé en paramettre
        Appel la methode d'évaluation d'arbre 'walkTree()' avec l'abre syntaxique passé en paramettre
        Affiche le résultat obtenue par 'walkTree()'
        """
        self.env = env
        result = self.walkTree(tree)
        # il est important d'utiliser is et non pas "==" pour ne pas avoir d'ambiguité avec (0 et False) et (1 et True)
        # Remplace True par Vrai
        if result is True:
            result = 'Vrai'
        # Remplace False par Faux
        elif result is False:
            result = 'Faux'
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)
        if isinstance(result, str) and result in ['Vrai', 'Faux']:
            print(result)

    def walkTree(self, node):
        """
        Evalue l'arbre syntaxique en fonction du node[0]
        """
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])
        elif node[0] == 'condition_gt':
            return self.walkTree(node[1]) > self.walkTree(node[2])
        elif node[0] == 'condition_ge':
            return self.walkTree(node[1]) >= self.walkTree(node[2])
        elif node[0] == 'condition_lt':
            return self.walkTree(node[1]) < self.walkTree(node[2])
        elif node[0] == 'condition_le':
            return self.walkTree(node[1]) <= self.walkTree(node[2])
        elif node[0] == 'condition_ne':
            return self.walkTree(node[1]) != self.walkTree(node[2])

        if node[0] == 'fun_def':
            self.env[node[1]] = node[2]

        if node[0] == 'fun_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Undefined function '%s'" % node[1])
                return 0

        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return int(self.walkTree(node[1]) / self.walkTree(node[2]))

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'write':
            return self.walkTree(node[1])

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("La variable \'"+node[1]+"\' n'est pas définie.")
                return None

        if node[0] == 'for_loop':
            if node[1][0] == 'for_loop_setup':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count+1, loop_limit+1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        print(res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == 'for_loop_setup':
            return (self.walkTree(node[1]), self.walkTree(node[2]))