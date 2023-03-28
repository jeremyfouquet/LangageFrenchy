from sly import Lexer

class BasicLexer(Lexer):
    """
    Analyseur lexical permettant de donner à chaque token un type et une valeur
    """
    tokens = { NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ, LT, LE, GT, GE, NE }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    EQEQ = r'=='
    LE   = r'<='
    LT   = r'<'
    GE   = r'>='
    GT   = r'>'
    NE   = r'!='
    ARROW = r'->'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NAME['SI'] = IF
    NAME['SINON'] = ELSE
    NAME['ALORS'] = THEN
    NAME['POUR'] = FOR
    NAME['FONC'] = FUN
    NAME['VERS'] = TO

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