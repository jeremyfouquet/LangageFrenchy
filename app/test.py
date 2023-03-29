from io import StringIO
import unittest
from unittest.mock import patch
from lexer import BasicLexer
from parser import BasicParser
from interpreter import BasicExecute

class TestInterpreter(unittest.TestCase):
    """
    Test l'interpretation de l'arbre syntaxique
    """
    def test_operations(self):
        ''' Test les différentes opérations '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        # Addition
        tree = parser.parse(lexer.tokenize('1+1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '2\n')
        # Soustraction
        tree = parser.parse(lexer.tokenize('1-1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '0\n')
        # Multiplication
        tree = parser.parse(lexer.tokenize('1*1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '1\n')
        # Division
        tree = parser.parse(lexer.tokenize('1/1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '1\n')

    def test_priorite(self):
        ''' Test la priorité arithmétique '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('1+1*2'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '3\n')

    def test_comparaison(self):
        ''' Test les différentes comparaisons '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('1==1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Vrai\n')
        tree = parser.parse(lexer.tokenize('1<1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Faux\n')
        tree = parser.parse(lexer.tokenize('1<=1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Vrai\n')
        tree = parser.parse(lexer.tokenize('1>1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Faux\n')
        tree = parser.parse(lexer.tokenize('1>=1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Vrai\n')
        tree = parser.parse(lexer.tokenize('1!=1'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), 'Faux\n')

    def test_Condition_IF_ELSE(self):
        ''' Test condition if/else '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('SI 1==1 ALORS 1 SINON 0'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '1\n')
        tree = parser.parse(lexer.tokenize('SI 1!=1 ALORS 1 SINON 0'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '0\n')

    def test_boucle_for(self):
        ''' Test boucle for '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('POUR x=0 VERS 2 ALORS x'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '0\n1\n')

    def test_commentaire(self):
        ''' Test commentaire '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('#commentaire'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '')

    def test_fonction(self):
        ''' Test la creation et l'appel de fonction commentaire '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('FONC mafonction() -> a="salut"'))
        BasicExecute(tree, env)
        tree = parser.parse(lexer.tokenize('mafonction()'))
        BasicExecute(tree, env)
        tree = parser.parse(lexer.tokenize('a'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '"salut"\n')

    def test_echo(self):
        ''' Test le retour de chaine '''
        lexer = BasicLexer()
        parser = BasicParser()
        env = {}
        tree = parser.parse(lexer.tokenize('ECRIT "salut"'))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            BasicExecute(tree, env)
            self.assertEqual(fake_out.getvalue(), '"salut"\n')

if __name__ == '__main__' :
    unittest.main()