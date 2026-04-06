import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser

def main():
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    else:
        input_str = "2+3*4"
    
    input_stream = InputStream(input_str)
    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.prog()
    
    print("Expresión:", input_str)
    print("Árbol LISP:", tree.toStringTree(recog=parser))
    
    # Análisis simple para casos comunes de asociatividad y precedencia
    if input_str == "2+3*4":
        print("=> La multiplicación (*) tiene MAYOR precedencia que la suma (+).")
    elif input_str == "4-3-2":
        print("=> El operador '-' es asociativo IZQUIERDO.")
    elif input_str == "2^3^2":
        print("=> El operador '^' es asociativo DERECHO.")
    elif input_str == "2+3-4":
        print("=> '+' y '-' tienen la MISMA precedencia y son asociativos izquierdos.")
    elif input_str == "a=b=c=5":
        print("=> El operador '=' es asociativo IZQUIERDO (a=(b=(c=5))).")
    elif input_str == "!!1":
        print("=> El operador '!' unario puede repetirse (asociativo derecho en la práctica).")
    else:
        print("=> Observa el árbol LISP para deducir la agrupación.")

if __name__ == '__main__':
    main()
