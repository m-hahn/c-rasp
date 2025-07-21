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
    | count_expr LEQ count_expr
    | count_expr GEQ count_expr
    | bool_expr AND bool_expr
    | bool_expr OR bool_expr
    | NOT bool_expr
    | VARIABLE
    | LPAREN bool_expr RPAREN
    | TRUE
    | FALSE
    ;
    
count_expr:
    COUNT bool_expr
    | COUNT '[' VARIABLE ']' bool_expr
    | VARIABLE
    | INT_LITERAL
    | count_expr PLUS count_expr
    | count_expr MINUS count_expr
    | MAX LPAREN count_expr COMMA count_expr RPAREN
    | MIN LPAREN count_expr COMMA count_expr RPAREN
    | count_expr IF bool_expr ELSE count_expr // low precedence
    | LPAREN count_expr RPAREN
    ;
    



////////////////////////////////////////////////

// starts comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;

IMPORT: '#import';

VARIABLE: [a-zA-Z_][a-zA-Z_0-9]*;
STRING_LITERAL: '"' (~["])* '"';
INT_LITERAL : [0-9]+ ;
TRUE : 'true';
FALSE: 'false';

IF: 'if';
ELSE: 'else';

AND : '&&' ;
OR : '||';
NOT : '!' ;

EQ : '==' ;
LT : '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';

ASSIGN: '=';
QUESTION: '?';
COLON: ':';
PLUS: '+';
MINUS: '-';
MIN: 'min';
MAX: 'max';

COUNT : '#';
//LSQBK: '[';
//RSQBK: ']';

LPAREN : '(' ;
RPAREN : ')' ;
COMMA : ',';

NL
    : ('\r'? '\n')+
    ;

WS: [ \t]+ -> skip ;
