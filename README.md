# Tarea 3 - Asociatividad y Precedencia de una Gramática

## Descripción
Este proyecto implementa un analizador sintáctico que permite verificar la **asociatividad** y **precedencia** de los operadores definidos en una gramática.

## Requisitos
- Python 3.12
- Java (para ejecutar ANTLR)
- ANTLR 4.13.1

## Instalación

### 1. Instalar Java
```bash
sudo apt update
sudo apt install default-jre -y
```

### 2. Descargar ANTLR
```bash
cd ~
wget https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

### 3. Crear entorno virtual e instalar dependencias
```bash
mkdir ~/tarea3_antlr_py
cd ~/tarea3_antlr_py
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime==4.13.1
```

## Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `gramatica.g4` | Gramática con reglas de asociatividad y precedencia |
| `main.py` | Script principal para probar expresiones |
| `gramaticaLexer.py` | Lexer generado por ANTLR |
| `gramaticaParser.py` | Parser generado por ANTLR |

## Generar el parser

```bash
java -jar ~/antlr-4.13.1-complete.jar -Dlanguage=Python3 gramatica.g4
```

## Ejecutar pruebas

```bash
python main.py "expresión"
```

## Resultados de las pruebas

### Prueba 1: Precedencia (`*` vs `+`)
```bash
python main.py "2+3*4"
```
**Salida:**
```
Expresión: 2+3*4
Árbol LISP: (prog (stat (expr (expr 2) + (expr (expr 3) * (expr 4)))) <EOF>)
=> La multiplicación (*) tiene MAYOR precedencia que la suma (+).
```

### Prueba 2: Asociatividad izquierda (`-`)
```bash
python main.py "4-3-2"
```
**Salida:**
```
Expresión: 4-3-2
Árbol LISP: (prog (stat (expr (expr (expr 4) - (expr 3)) - (expr 2))) <EOF>)
=> El operador '-' es asociativo IZQUIERDO.
```

### Prueba 3: Misma precedencia (`+` y `-`)
```bash
python main.py "2+3-4"
```
**Salida:**
```
Expresión: 2+3-4
Árbol LISP: (prog (stat (expr (expr (expr 2) + (expr 3)) - (expr 4))) <EOF>)
=> '+' y '-' tienen la MISMA precedencia y son asociativos izquierdos.
```

## Interpretación del árbol LISP

El árbol LISP muestra la estructura jerárquica de la expresión:

- `(expr 2)` → número 2
- `(expr (expr 3) * (expr 4))` → multiplicación `3*4`
- `(expr (expr 2) + (expr ...))` → suma de `2` con el resultado anterior

Esto confirma que `*` se evalúa antes que `+`.

## Conclusión

La gramática implementada respeta correctamente:
- **Precedencia**: Los operadores `*` y `/` tienen mayor precedencia que `+` y `-`
- **Asociatividad**: Los operadores binarios son asociativos a la izquierda
