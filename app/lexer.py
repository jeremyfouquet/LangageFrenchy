"""
Ce fichier contient la classe BasicLexer, qui est un analyseur lexical permettant d'attribuer un type et une valeur à chaque jeton (token).
"""

__author__ = "Jeremy Fouquet"
__version__ = "1.0.0"
__credits__ = "Réalisé dans le cadre du cours de Interprétation & Compilation de L3 Informatique de L IED"
__description__ = "Ce fichier contient la classe BasicLexer, qui est un analyseur lexical pour un langage de programmation basique."

from sly import Lexer

class BasicLexer(Lexer):
    """
    Analyseur lexical permettant de donner à chaque token un type et une valeur
    """
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ, LT, LE, GT, GE, NE, WRITE}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    EQEQ = r'EGALE A'
    LE   = r'INFERIEUR OU EGALE A'
    LT   = r'INFERIEUR A'
    GE   = r'SUPERIEUR OU EGALE A'
    GT   = r'SUPERIEUR A'
    NE   = r'DIFFERENT DE'
    ARROW = r'->'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['SI'] = IF
    NAME['SINON'] = ELSE
    NAME['ALORS'] = THEN
    NAME['POUR'] = FOR
    NAME['FONC'] = FUN
    NAME['VERS'] = TO
    NAME['ECRIT'] = WRITE

    STRING = r'\".*?\"'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')