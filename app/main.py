"""
Ce fichier contient un programme qui utilise un interpréteur pour exécuter du code en langage Frenchy.
"""

__author__ = "Jeremy Fouquet"
__version__ = "1.0.0"
__credits__ = "Réalisé dans le cadre du cours de Interprétation & Compilation de L3 Informatique de L IED"
__description__ = "Programme d'interprétation du langage Frenchy"

from lexer import BasicLexer
from parser import BasicParser
from interpreter import BasicExecute

if __name__ == '__main__':
    """
    Fonction principale permettant de rentrer des lignes de code et d'en afficher la sortie de l’interpréteur.
    """
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('LangageFrenchy > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)

