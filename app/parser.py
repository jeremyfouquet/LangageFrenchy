"""
Ce fichier contient la classe BasicParser, qui est un analyseur syntaxique permettant de convertir un flux de jetons en arbre syntaxique en utilisant des règles de grammaire.
"""

__author__ = "Jeremy Fouquet"
__version__ = "1.0.0"
__credits__ = "Réalisé dans le cadre du cours de Interprétation & Compilation de L3 Informatique de L IED"
__description__ = "Ce fichier contient la classe BasicParser, qui est un analyseur syntaxique pour un langage de programmation basique."


from sly import Parser
from lexer import BasicLexer

class BasicParser(Parser):
    """
    Analyseur syntaxique permettant de converti les flux de tokens en arbre syntaxique à partir de règle de grammaire
    """
    tokens = BasicLexer.tokens

    precedence = (
        # EQEQ à une priorité faible et est non-associatif
        ('nonassoc', EQEQ, GT, GE, LT, LE, NE),
        # “+” et “-” ont le même niveau de priorité et sont associatifs à gauche
        ('left', '+', '-'),
        # “*” et “/” ont la même priorité et sont associatifs à gauche
        ('left', '*', '/'),
        ('right', 'UMINUS')
        )

    def __init__(self):
        self.env = { }

    # Dans le cas d'une ligne vide
    @_('')
    def statement(self, p):
        pass

    # Dans le cas d'une Boucle FOR
    @_('FOR var_assign TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    # Dans le cas d'une condition IF/ELSE
    @_('IF expr THEN statement ELSE statement')
    def statement(self, p):
        return ('if_stmt', p.expr, ('branch', p.statement0, p.statement1))

    # Dans le cas d'une Déclaration de fonction
    @_('FUN NAME "(" ")" ARROW statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)

    # Dans le cas d'un appel de fonction
    @_('NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.NAME)

    # Dans le cas d'une comparaison "=="
    @_('expr EQEQ expr')
    def expr(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    # Dans le cas d'une comparaison "<"
    @_('expr LT expr')
    def expr(self, p):
        return ('condition_lt', p.expr0, p.expr1)

    # Dans le cas d'une comparaison "<="
    @_('expr LE expr')
    def expr(self, p):
        return ('condition_le', p.expr0, p.expr1)

    # Dans le cas d'une comparaison ">"
    @_('expr GT expr')
    def expr(self, p):
        return ('condition_gt', p.expr0, p.expr1)

    # Dans le cas d'une comparaison ">="
    @_('expr GE expr')
    def expr(self, p):
        return ('condition_ge', p.expr0, p.expr1)

    # Dans le cas d'une comparaison "!="
    @_('expr NE expr')
    def expr(self, p):
        return ('condition_ne', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    # Dans le cas d'une déclaration de variable
    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    # Dans le cas d'une déclaration de chaine
    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    # Dans le cas d'un echo
    @_('WRITE STRING')
    def statement(self, p):
        return ('write', p.STRING)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    # Dans le cas des opérateurs simple
    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)
    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)
    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)
    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    # Dans le cas d'un appel de variable
    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    # Méthode error pour la gestion des erreurs de syntaxe
    def error(self, token):
        # Obtention des informations du jeton
        token_type = token.type

        # Texte d'erreur personnalisé en fonction du type de jeton
        if token_type == 'EQEQ':
            print(f"Erreur : Opération 'EGALE A' non valide.")
        elif token_type == 'LT':
            print(f"Erreur : Opération 'INFERIEUR A' non valide.")
        elif token_type == 'LE':
            print(f"Erreur : Opération 'INFERIEUR OU EGALE A' non valide.")
        elif token_type == 'GT':
            print(f"Erreur : Opération 'SUPERIEUR A' non valide.")
        elif token_type == 'GE':
            print(f"Erreur : Opération 'SUPERIEUR OU EGALE A' non valide.")
        elif token_type == 'NE':
            print(f"Erreur : Opération 'DIFFERENT DE' non valide.")
        else:
            print(f"Erreur : '"+ token_type +"' non valide.")

        # Réinitialisation de l'analyseur syntaxique
        self.restart()