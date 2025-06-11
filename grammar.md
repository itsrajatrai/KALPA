<program>         ::= <statement>*

<statement>       ::= <assignment>
                    | <arithmetic>
                    | <print>
                    | <if_statement>
                    | <repeat>

<assignment>      ::= "Let" <identifier> "be" <value>

<arithmetic>      ::= "Let" <identifier> "be" <identifier> <operator> <identifier>

<print>           ::= "Print" <value>

<if_statement>    ::= "If" <condition> ", then" <print>

<repeat>          ::= "Repeat" <number> "times:" <print>

<condition>       ::= <identifier> "is greater than" <value>
                    | <identifier> "is less than" <value>
                    | <identifier> "is equal to" <value>

<operator>        ::= "plus" | "minus" | "times" | "divided by"

<value>           ::= <number> | <string> | <identifier>

<identifier>      ::= /[a-zA-Z_][a-zA-Z0-9_]*/

<number>          ::= /[0-9]+/

<string>          ::= "\"" .*? "\""
