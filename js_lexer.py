# Copyright 2016 Carlos Gutierrez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import ply.lex as lex

# TOKENS http://php.net/manual/es/tokens.php
tokens = (

    # RESERVERD WORDS LIST
    # http://php.net/manual/es/reserved.keywords.php
    
    'CONSOLE', 'LET','VAR', 'CONST', 'PUSH','POP', 'UNSHIFT','SHIFT', 'SLICE', 'SPLICE',
    'REVERSE', 'SPLIT', 'JOIN','SORT','INDEXOF','FIND','ARROW_FUNCTION','FINDINDEX', 'NEW', 'SET',
    'OF','FOREACH','SOME','EVERY', 'LENGTH', 'MAP','FILTER', 'REDUCE', 'DOLAR','FOR', 'INCREMENT',
    'TOFIXED','PARSEINT','PARSEFLOAT','MATHFLOOR','MATHRAMDOM','THIS', 'METHOD_DELETE',
    'OBJECT_PROPTOTYPE','STRING_PROPTOTYPE','IN','HASOWNPROPERTY','OBJECT_ASSIGN','LEGS','LASTINDEXOF',
    'INCLUDES','STARTSWITH','ENDSWITH','REPLACE','SUBSTR','RETURN', 'PROMPT','ALERT', 'OPERATION_TERNARIO',
    'ARRAY','BREAK','CASE','CATCH','CLASS','DEFAULT','DO','ELSE','ELSEIF','ENDSWITCH','EVAL','EXTENDS',
    'FUNCTION','IF','IMPLEMENTS','INCLUDE','INSTANCEOF','INTERFACE','OR','PRINT','PRIVATE',
    'PROTECTED','PUBLIC','REQUIRE', 'STATIC','SWITCH','THROW','TRY','USE','WHILE',
    
    #boolean
    'TRUE','FALSE',

    # SYMBOLS
    'PLUS','PLUSPLUS','PLUSEQUAL','MINUS','MINUSMINUS','MINUSEQUAL','TIMES',
    'TIMESTIMES','DIVIDE','LESS','LESSEQUAL','GREATER','GREATEREQUAL','ISEQUALTYPE','EQUAL',
    'DEQUAL','DISTINT','ISEQUAL','SEMI','COMMA','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG','DOT','QUOTES',
    'APOSTROPHE','DOT_DOT',

    # OTHERS
    'COMMENTS','COMMENTS_C99','ID','IDVAR','NUM','STRING','VOID',
)


# RE Tokens

# Take from: http://www.dabeaz.com/ply/example.html
# Ignored characters
t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)

# RE RESERVERD WORDS LIST

def t_CONSOLE(t):
    r'console.log'
    return t

def t_LET(t):
    r'let'
    return t

def t_VAR(t):
    r'var'
    return t

def t_CONST(t):
    r'const'
    return t

def t_PUSH(t):
    r'push'
    return t

def t_POP(t):
    r'pop'
    return t

def t_UNSHIFT(t):
    r'unshift'
    return t

def t_SHIFT(t):
    r'shift'
    return t

def t_SLICE(t):
    r'slice'
    return t

def t_SPLICE(t):
    r'splice'
    return t

def t_REVERSE(t):
    r'reverse'
    return t

def t_SPLIT(t):
    r'split'
    return t

def t_JOIN(t):
    r'join'
    return t

def t_SORT(t):
    r'sort'
    return t

def t_INDEXOF(t):
    r'indexOf'
    return t

def t_FINDINDEX(t):
    r'findIndex'
    return t

def t_FIND(t):
    r'find'
    return t

def t_NEW(t):
    r'new'
    return t

def t_SET(t):
    r'\bSet\b'
    return t

def t_OF(t):
    r'\bof\b'
    return t

def t_FOREACH(t):
    r'forEach'
    return t

def t_SOME(t):
    r'some'
    return t

def t_EVERY(t):
    r'every'
    return t

def t_LENGTH(t):
    r'length'
    return t

def t_MAP(t):
    r'map'
    return t

def t_FILTER(t):
    r'filter'
    return t

def t_REDUCE(t):
    r'reduce'
    return t

def t_TOFIXED(t):
    r'toFixed'
    return t

def t_PARSEINT(t):
    r'parseInt'
    return t

def t_PARSEFLOAT(t):
    r'parseFloat'
    return t

def t_MATHFLOOR(t):
    r'Math.floor'
    return t

def t_MATHRAMDOM(t):
    r'Math.random'
    return t

def t_THIS(t):
    r'this'
    return t

def t_METHOD_DELETE(t):
    r'delete'
    return t

def t_OBJECT_PROPTOTYPE(t):
    r'Object.getPrototypeOf'
    return t

def t_OBJECT_ASSIGN(t):
    r'Object.assign'
    return t

def t_STRING_PROPTOTYPE(t):
    r'String.prototype'
    return t

def t_IN(t):
    r'[ ]in[ ] '
    return t

def t_HASOWNPROPERTY(t):
    r'hasOwnProperty'
    return t

def t_LEGS(t):
    r'legs'
    return t

def t_LASTINDEXOF(t):
    r'lastIndexOf'
    return t

def t_INCLUDES(t):
    r'includes'
    return t

def t_STARTSWITH(t):
    r'startsWith'
    return t

def t_ENDSWITH(t):
    r'endsWith'
    return t

def t_REPLACE(t):
    r'replace'
    return t

def t_SUBSTR(t):
    r'substr'
    return t
    
def t_RETURN(t):
    r'return'
    return t

def t_PROMPT(t):
    r'prompt'
    return t

def t_ALERT(t):
    r'alert'
    return t

def t_OPERATION_TERNARIO(t):
    r'\?'
    return t

def t_ARRAY(t):
    r'Array'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'\bdo\b'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_ENDSWITCH(t):
    r'endswitch'
    return t

def t_EVAL(t):
    r'eval'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_OR(t):
    r'or|\|\||OR'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'
    return t


def t_TRY(t):
    r'try'
    return t

def t_USE(t):
    r'use'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

# RE SYMBOLS
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUAL     = r'='
t_DISTINT   = r'!'
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMI      = r';'
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBLOCK    = r'{'
t_RBLOCK    = r'}'
t_COLON     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_DOT       = r'\.'
t_QUOTES    = r'\"'
t_APOSTROPHE = r'\''

def t_ARROW_FUNCTION(t):
    r'=>'
    return t

def t_INCREMENT(t):
    r'\+='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_ISEQUALTYPE(t):
    r'==='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


# RE OTHERS


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\')|(\`[^\`]*\`))'
    return t


lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)
        lexer.input(scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print ("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t-->  "+str(tok.value))
            i += 1

        print (chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script JAVASCRIPT como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python js_lexer.py"+chr(27)+"[1;31m"+" <filename>.js"+chr(27)+"[0m")

