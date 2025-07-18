grammar crasp;


program
    : NL* statement (NL+ statement)* NL* EOF
    ;

statement: 
    VARIABLE ASSIGN 
    (bool_expr | count_expr);

bool_expr:
    STRING_LITERAL
    | count_expr LT count_expr
    | count_expr EQ count_expr
    | bool_expr AND bool_expr
    | NOT bool_expr
    | VARIABLE
    | LPAREN bool_expr RPAREN
    | TRUE
    | FALSE
    ;
    
count_expr:
    COUNT bool_expr
    | VARIABLE
    | INT_LITERAL
    // | bool_expr QUESTION count_expr COLON count_expr
    | count_expr IF bool_expr ELSE count_expr
    | count_expr PLUS count_expr
    | count_expr MINUS count_expr
    | MAX LPAREN count_expr COMMA count_expr RPAREN
    | MIN LPAREN count_expr COMMA count_expr RPAREN
    | LPAREN count_expr RPAREN
    ;
    



////////////////////////////////////////////////


VARIABLE: [a-zA-Z_][a-zA-Z_0-9]*;
STRING_LITERAL: '"' (~["])* '"';
INT_LITERAL : [0-9]+ ;
TRUE : 'true';
FALSE: 'false';

IF: 'if';
ELSE: 'else';

AND : '&&' ;
NOT : '!' ;
EQ : '==' ;
LT : '<';

ASSIGN: '=';
QUESTION: '?';
COLON: ':';
PLUS: '+';
MINUS: '-';
MIN: 'min';
MAX: 'max';

COUNT : '#';

LPAREN : '(' ;
RPAREN : ')' ;
COMMA : ',';

NL
    : ('\r'? '\n')+
    ;

WS: [ \t]+ -> skip ;
