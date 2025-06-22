import dedent from "dedent";

export const defaultExamples = [
  {
    label: "Arithmetic Expression",
    grammar: dedent(`
      start : stmt_list
      
      stmt_list : stmt_list stmt
                | stmt

      stmt : assign
           | declare

      declare : TYPE ID ';'
      assign : ID '=' expr ';'
      
      expr : expr '+' term
           | expr '-' term
           | term
      
      term : term '*' factor
           | term '/' factor
           | factor
      
      factor : NUMBER
             | ID
             | '(' expr ')'
    `),
    code: dedent(`
      int a;
      int b;
      int x;
      x = (a + b) * 5;
    `),
  },
  {
    label: "If-else Statement",
    grammar: dedent(`
      start : stmt_list

      stmt_list : stmt_list stmt
                | stmt

      stmt : declare
           | assign
           | if_stmt

      declare : TYPE ID ';'
      assign : ID '=' expr ';'

      if_stmt : IF '(' cond ')' '{' assign '}' ELSE '{' assign '}'

      cond : ID RELOP ID
      expr : ID | NUMBER
    `),
    code: dedent(`
      int a;
      int b;
      int max;
      if (a > b) {
        max = a;
      } else {
        max = b;
      }
    `),
  },
  {
    label: "While Loop",
    grammar: dedent(`
      start : stmt_list

      stmt_list : stmt_list stmt
                | stmt

      stmt : declare
           | assign
           | while_stmt

      declare : TYPE ID ';'
      assign : ID '=' expr ';'

      while_stmt : WHILE '(' cond ')' '{' stmt_list '}'

      cond : ID RELOP NUMBER

      expr : expr '+' term | term
      term : ID | NUMBER
    `),
    code: dedent(`
      int i;
      int sum;
      i = 0;
      while (i < 10) {
        sum = sum + i;
        i = i + 1;
      }
    `),
  },
  {
    label: "For Loop",
    grammar: dedent(`
      start : stmt_list

      stmt_list : stmt_list stmt
                | stmt

      stmt : declare
           | assign
           | for_loop

      declare : TYPE ID ';'
      assign : ID '=' expr ';'

      for_loop : FOR '(' assign cond ';' assign ')' '{' stmt_list '}'

      cond : ID RELOP NUMBER

      expr : ID
           | NUMBER
           | expr '+' expr
           | expr '*' expr
    `),
    code: dedent(`
      int i;
      int sum;
      i = 0;
      for (i = 0; i < 10; i = i + 1) {
        sum = sum + i;
        i = i + 1;
      }
    `),
  },
  {
    label: "Switch Statement",
    grammar: dedent(`
      start : stmt_list

      stmt_list : stmt_list stmt
                | stmt

      stmt : declare
           | assign
           | switch_stmt

      declare : TYPE ID ';'
      assign : ID '=' expr ';'

      switch_stmt : SWITCH '(' ID ')' '{' case_list '}'

      case_list : case_list case
                | case

      case : CASE NUMBER ':' assign BREAK ';'
           | DEFAULT ':' assign

      expr : ID | NUMBER
    `),
    code: dedent(`
      int x;
      int y;
      switch (x) {
        case 1: y = 10; break;
        case 2: y = 20; break;
        default: y = 0;
      }
    `),
  },
  {
    label: "Function Call Expression",
    grammar: dedent(`
      start : stmt_list

      stmt_list : stmt_list stmt
                | stmt

      stmt : declare
           | assign

      declare : TYPE ID ';'
      assign : ID '=' expr ';'

      expr : ID '(' args ')'
           | ID
           | NUMBER

      args : expr
           | expr ',' args
           |
    `),
    code: dedent(`
      int result;
      int a;
      int b;
      result = add(a, b);
    `),
  },
];
