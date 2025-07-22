grammar crasp;


program
    : NL* statement (NL+ statement)* NL* EOF
    ;

statement: 
    VARIABLE ASSIGN (bool_expr | count_expr)
    | IMPORT VARIABLE
    ;


bool_expr:
    STRING_LITERAL
    | count_expr LT count_expr
    | count_expr GT count_expr
    | count_expr EQ count_expr
    | count_expr NEQ count_expr
    | count_expr LEQ count_expr
    | count_expr GEQ count_expr
    | bool_expr AND bool_expr
    | bool_expr OR bool_expr
    | NOT bool_expr
    | TRUE
    | FALSE
    | VARIABLE
    | LPAREN bool_expr RPAREN
    ;
    
count_expr:
    COUNT bool_expr
    | COUNT '[' VARIABLE ']' bool_expr
    | VARIABLE
    | INT_LITERAL
    | count_expr PLUS count_expr
    | count_expr MINUS count_expr
    | INT_LITERAL TIMES count_expr
    | MAX LPAREN count_expr COMMA count_expr RPAREN
    | MIN LPAREN count_expr COMMA count_expr RPAREN
    | count_expr IF bool_expr ELSE count_expr // low precedence
    | LPAREN count_expr RPAREN
    ;
    



////////////////////////////////////////////////

// starts comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// define keywords before variables
IMPORT: '#import';
TRUE : 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
MIN: 'min';
MAX: 'max';


VARIABLE: [a-zA-Z_][a-zA-Z_0-9]*;
STRING_LITERAL: '"' (~["])* '"';
INT_LITERAL : [0-9]+ ;


AND : '&&' ;
OR : '||';
NOT : '!' ;

EQ : '==' ;
NEQ : '!=' ;
LT : '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';

ASSIGN: '=';
QUESTION: '?';
COLON: ':';
PLUS: '+';
MINUS: '-';
TIMES: '*';

COUNT : '#';

LPAREN : '(' ;
RPAREN : ')' ;
COMMA : ',';

NL
    : ('\r'? '\n')+
    ;

WS: [ \t]+ -> skip ;
