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
import ply.yacc as yacc
from js_lexer import tokens

VERBOSE = 1


def p_program(p):
    'program : FUNCTION ID LPAREN RPAREN LBLOCK declaration_list RBLOCK'
    pass


def p_declaration_list(p):
    '''declaration_list : declaration_list  declaration
                                            | declaration
    '''
    pass


def p_declaration(p):
  # let a;
  # a = 2;
  # let a = number;
    '''declaration : type ID SEMI
                    | ID EQUAL var SEMI
                    | type ID EQUAL var SEMI
                    | if_condition
                    | var INCREMENT var SEMI
                    | do_condition
                    | while_condition
    '''
    pass


def p_operation(p):
  # let a = 2+2;
  # a = 3+4;
    '''declaration : type ID EQUAL expression SEMI
                  | ID EQUAL expression SEMI
                  | type ID EQUAL expression_avanced SEMI
                  | ID EQUAL expression_avanced SEMI
    '''
    pass


def p_expression(p):
    '''expression : var PLUS var
                  | var MINUS var
                  | var TIMES var
                  | var DIVIDE var
    '''
    pass


def p_expression_avanced(p):
    '''expression_avanced : var PLUS LPAREN  expression RPAREN
                   | var MINUS LPAREN  expression RPAREN
                   | var TIMES LPAREN  expression RPAREN
                   | var DIVIDE LPAREN  expression RPAREN
     '''
    pass


def p_expression_bool(p):
    '''expression_bool : var ISEQUAL var
                   | var LESS var
                   | var GREATER var
                   | var GREATEREQUAL var
                   | var LESSEQUAL var
                   | var DEQUAL var
                   | DISTINT var 
     '''
    pass

def p_if_condition(p):
    '''if_condition : IF LPAREN expression_bool RPAREN LBLOCK declaration_list RBLOCK
                | IF LPAREN expression_bool RPAREN LBLOCK declaration_list RBLOCK ELSE LBLOCK declaration_list RBLOCK
    '''
    pass


def p_do_condition(p):
    '''do_condition : DO LBLOCK declaration_list RBLOCK WHILE LPAREN expression_bool RPAREN 
    '''
    pass


def p_while_condition(p):
    '''while_condition : 
                | WHILE LPAREN expression_bool RPAREN LBLOCK declaration_list RBLOCK 
    '''
    pass


def p_type(p):
    '''type : LET
          | CONST
          | VAR
    '''
    pass


def p_var(p):
    '''var : ID
           | NUM
           | STRING
     '''
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print(
                chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print("\t\tLine:  "+str(js_lexer.lexer.lineno))

    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        # print (scriptdata)

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        parser.parse(scriptdata, tracking=False)
        # print("Hola bebe, no tienes errores sintacticos")
        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print(chr(27)+"[0;31m" +
              "Pase el archivo de script JavaScript como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python js_parser.py" +
              chr(27)+"[1;31m"+" <filename>.js"+chr(27)+"[0m")