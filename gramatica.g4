grammar gramatica;

// La precedencia implícita: las primeras alternativas tienen menor prioridad.
// Asociatividad: por defecto izquierda; con <assoc=right> se cambia a derecha.

prog: (stat NEWLINE?)* EOF;
stat: expr                            # printExpr
    ;

expr: <assoc=right> expr '^' expr     # Pow          // asociativa derecha
    | expr op=('*'|'/') expr          # MulDiv       // asociativa izquierda
    | expr op=('+'|'-') expr          # AddSub       // asociativa izquierda
    | expr '=' expr                   # Assign       // asociativa izquierda
    | '!' expr                        # Not
    | INT                             # Int
    | ID                              # Var
    | '(' expr ')'                    # Parens
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
WS  : [ \t\r\n]+ -> skip ;
NEWLINE: [\r\n]+ ;
