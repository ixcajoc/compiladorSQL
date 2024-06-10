class Parser:
    
    def __init__(self):
        
        self.nombre = ''
        self.parsing_table = {
            'S': {
                'CREATE': ['S -> SQLIns'],
        
                'SELECT': ['S -> SQLIns'],
                'INSERT': ['S -> SQLIns'],
                'UPDATE': ['S -> SQLIns'],
                'DELETE': ['S -> SQLIns'],
                'EOF': ['']
            },
            'SQLIns': {
                'CREATE': ['SQLIns -> Instruccion_Crear'],
                'SELECT': ['SQLIns -> Instruccion_Listar'],
                'INSERT': ['SQLIns -> Instruccion_Insertar'],
                'UPDATE': ['SQLIns -> Instruccion_Actualizar'],
                'DELETE': ['SQLIns -> Instruccion_Eliminar'],
                'EOF': ['']
            },
            'Instruccion_Crear': {
                'CREATE': ['Instruccion_Crear -> Crear_BD', 'Instruccion_Crear -> Crear_TBL', 'Instruccion_Crear -> Crear_IDX']
            },
            'Crear_BD': {
                #'CREATE': ['Crear_BD -> CREATE DATABASE <nombre_BD>;']
                'CREATE': ['Crear_BD -> CREATE DATABASE <nombre_BD>']
                #'CREATE': ['Crear_BD -> CREATE DATABASE <char_sequence>']
            },
            
            'nombre_BD': {
                '<char_sequence>': ['nombre_BD -> <char_sequence>']
            },
            
            'char_sequence': {
                '<char>': ['char_sequence -> <char><char_sequence>', 'char_sequence -> <char>']
            },
            'char': {
                '<LETTER>': ['char -> <LETTER>'],
                '<DIGIT>': ['char -> <DIGIT>'],
                '_': ['char -> _']
            },
            'Length': {
                '<DIGITS>': ['Length -> <DIGITS>']
            },
            'DIGITS': {
                '<DIGIT>': ['DIGITS -> <DIGIT>', 'DIGITS -> <DIGIT><DIGITS>']
            },
            'expr': {
                '<char_sequence>': ['expr -> <char_sequence>', 'expr -> <numeric_expr>']
            },
            'numeric_expr': {
                '<numeric_literal>': ['numeric_expr -> <numeric_literal>', 'numeric_expr -> <arithmetic_expr>']
            },
            'numeric_literal': {
                '<DIGITS>': ['numeric_literal -> <DIGITS><fraction_part>']
            },
            'SPACE': {
                ' ': ['SPACE -> " "']
            },
            'OTHER_CHAR': {
                '#': ['OTHER_CHAR -> #'],
                '$': ['OTHER_CHAR -> $'],
                '%': ['OTHER_CHAR -> %'],
                '&': ['OTHER_CHAR -> &'],
                '(': ['OTHER_CHAR -> ('],
                ')': ['OTHER_CHAR -> )'],
                ',': ['OTHER_CHAR -> ,'],
                ';': ['OTHER_CHAR -> ;'],
                '.': ['OTHER_CHAR -> .'],
                '?': ['OTHER_CHAR -> ?'],
                '¡': ['OTHER_CHAR -> ¡']
            },
            'ARITHMETIC_OPERATOR': {
                '+': ['ARITHMETIC_OPERATOR -> +'],
                '-': ['ARITHMETIC_OPERATOR -> -'],
                '*': ['ARITHMETIC_OPERATOR -> *'],
                '/': ['ARITHMETIC_OPERATOR -> /']
            },
            'LETTER': {
                'a': ['LETTER -> a'],
                'b': ['LETTER -> b'],
                'c': ['LETTER -> c'],
                'd': ['LETTER -> d'],
                'e': ['LETTER -> e'],
                'f': ['LETTER -> f'],
                'g': ['LETTER -> g'],
                'h': ['LETTER -> h'],
                'i': ['LETTER -> i'],
                'j': ['LETTER -> j'],
                'k': ['LETTER -> k'],
                'l': ['LETTER -> l'],
                'm': ['LETTER -> m'],
                'n': ['LETTER -> n'],
                'o': ['LETTER -> o'],
                'p': ['LETTER -> p'],
                'q': ['LETTER -> q'],
                'r': ['LETTER -> r'],
                's': ['LETTER -> s'],
                't': ['LETTER -> t'],
                'u': ['LETTER -> u'],
                'v': ['LETTER -> v'],
                'w': ['LETTER -> w'],
                'x': ['LETTER -> x'],
                'y': ['LETTER -> y'],
                'z': ['LETTER -> z'],
                'A': ['LETTER -> A'],
                'B': ['LETTER -> B'],
                'C': ['LETTER -> C'],
                'D': ['LETTER -> D'],
                'E': ['LETTER -> E'],
                'F': ['LETTER -> F'],
                'G': ['LETTER -> G'],
                'H': ['LETTER -> H'],
                'I': ['LETTER -> I'],
                'J': ['LETTER -> J'],
                'K': ['LETTER -> K'],
                'L': ['LETTER -> L'],
                'M': ['LETTER -> M'],
                'N': ['LETTER -> N'],
                'O': ['LETTER -> O'],
                'P': ['LETTER -> P'],
                'Q': ['LETTER -> Q'],
                'R': ['LETTER -> R'],
                'S': ['LETTER -> S'],
                'T': ['LETTER -> T'],
                'U': ['LETTER -> U'],
                'V': ['LETTER -> V'],
                'W': ['LETTER -> W'],
                'X': ['LETTER -> X'],
                'Y': ['LETTER -> Y'],
                'Z': ['LETTER -> Z']
            },

            'DIGIT': {
                '0': ['DIGIT -> 0'],
                '1': ['DIGIT -> 1'],
                '2': ['DIGIT -> 2'],
                '3': ['DIGIT -> 3'],
                '4': ['DIGIT -> 4'],
                '5': ['DIGIT -> 5'],
                '6': ['DIGIT -> 6'],
                '7': ['DIGIT -> 7'],
                '8': ['DIGIT -> 8'],
                '9': ['DIGIT -> 9']
            },
        }


    def parse(self, tokens):
        stack = ['S']
        output = []
        while stack:
            top = stack.pop()
            if top in self.parsing_table:
                token = tokens[0] if tokens else 'EOF'
                if token in self.parsing_table[top]:
                    rules = self.parsing_table[top][token][0]
                    if rules != '':
                        rule_parts = rules.split(' -> ')[1].split()
                        stack.extend(reversed(rule_parts))
                    output.append(rules)
                else:
                    raise ValueError(f"Error de sintaxis: token inesperado '{token}' en el contexto de '{top}'")
            elif top.startswith('<') and top.endswith('>'):
                if tokens and tokens[0] == top:
                    tokens.pop(0)
                else:
                    raise ValueError(f"Error de sintaxis: se esperaba '{top}' pero se encontró '{tokens[0] if tokens else 'EOF'}'")
            else:
                if tokens and tokens[0] == top:
                    tokens.pop(0)
                elif top != 'ε':
                    raise ValueError(f"Error de sintaxis: se esperaba '{top}' pero se encontró '{tokens[0] if tokens else 'EOF'}'")
        return output

# Ejemplo de uso
parser = Parser()

tokens = ['CREATE', 'DATABASE', '<nombre_BD>']
result = parser.parse(tokens)
print(result)

tokens = ['CREATE', 'DATABASE', '<miDB>']
result = parser.parse(tokens)
print(result)




