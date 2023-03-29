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