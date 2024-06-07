class Parser:
    def __init__(self):
        # Se omite la tabla de parsing para brevedad.
        self.parsing_table = {
            # Tabla de parsing aquí...
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
tokens = ['CREATE', 'DATABASE', '<nombre_BD>', ';']
result = parser.parse(tokens)
print(result)





class Parser:
    def __init__(self):
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
                'CREATE': ['Crear_BD -> CREATE DATABASE <nombre_BD>;']
            },
            'Crear_TBL': {
                'CREATE': ['Crear_TBL -> CREATE TABLE <nombre_TBL> (<Columnas_TBL>);']
            },
            'Crear_IDX': {
                'CREATE': ['Crear_IDX -> CREATE INDEX <nombre_IDX> ON <nombre_TBL>(<nombre_COL> <order>);']
            },
            'order': {
                'ASC': ['order -> ASC'],
                'DESC': ['order -> DESC'],
                'EOF': ['order -> ε'],
                '<nombre_COL>': ['order -> ε']
            },
            'Columnas_TBL': {
                '<nombre_COL>': ['Columnas_TBL -> Columna_TBL , Columnas_TBL', 'Columnas_TBL -> Columna_TBL']
            },
            'Columna_TBL': {
                '<nombre_COL>': ['Columna_TBL -> <nombre_COL> <SPACE> <column_definition>']
            },
            'column_definition': {
                'TINYINT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'SMALLINT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'MEDIUMINT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'INT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'INTEGER': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'BIGINT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'REAL': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'DOUBLE': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'FLOAT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'DECIMAL': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'NUMERIC': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'DATE': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'TIME': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'DATETIME': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'VARCHAR': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'TINYTEXT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'TEXT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'MEDIUMTEXT': ['column_definition -> <data_type> <SPACE> <data_type_options>'],
                'LONGTEXT': ['column_definition -> <data_type> <SPACE> <data_type_options>']
            },
            'data_type_options': {
                'NOT': ['data_type_options -> NOT NULL'],
                'NULL': ['data_type_options -> NULL'],
                'AUTO_INCREMENT PRIMARY KEY': ['data_type_options -> AUTO_INCREMENT PRIMARY KEY'],
                'PRIMARY KEY': ['data_type_options -> PRIMARY KEY'],
                'EOF': ['data_type_options -> ε'],
                ')': ['data_type_options -> ε']
            },
            'data_type': {
                'TINYINT': ['data_type -> TINYINT(<length>)'],
                'SMALLINT': ['data_type -> SMALLINT(<length>)'],
                'MEDIUMINT': ['data_type -> MEDIUMINT(<length>)'],
                'INT': ['data_type -> INT(<length>)'],
                'INTEGER': ['data_type -> INTEGER(<length>)'],
                'BIGINT': ['data_type -> BIGINT(<length>)'],
                'REAL': ['data_type -> REAL(<length>,<decimals>)'],
                'DOUBLE': ['data_type -> DOUBLE(<length>,<decimals>)'],
                'FLOAT': ['data_type -> FLOAT(<length>,<decimals>)'],
                'DECIMAL': ['data_type -> DECIMAL(<length>,<decimals>)'],
                'NUMERIC': ['data_type -> NUMERIC(<length>,<decimals>)'],
                'DATE': ['data_type -> DATE'],
                'TIME': ['data_type -> TIME'],
                'DATETIME': ['data_type -> DATETIME'],
                'VARCHAR': ['data_type -> VARCHAR(<length>)'],
                'TINYTEXT': ['data_type -> TINYTEXT'],
                'TEXT': ['data_type -> TEXT'],
                'MEDIUMTEXT': ['data_type -> MEDIUMTEXT'],
                'LONGTEXT': ['data_type -> LONGTEXT']
            },
            'Instruccion_Listar': {
                'SELECT': ['Instruccion_Listar -> SELECT <list_FLD> FROM <table_references> <Where> <Group> <OrderBY>']
            },
            'Where': {
                'WHERE': ['Where -> WHERE <SPACE> <condition>'],
                'EOF': ['Where -> ε'],
                'GROUP BY': ['Where -> ε'],
                'ORDER BY': ['Where -> ε']
            },
            'Group': {
                'GROUP BY': ['Group -> GROUP BY <SPACE> <lista_Columnas>'],
                'EOF': ['Group -> ε'],
                'ORDER BY': ['Group -> ε']
            },
            'OrderBY': {
                'ORDER BY': ['OrderBY -> ORDER BY <SPACE> <lista_Columnas> <SPACE> <order>'],
                'EOF': ['OrderBY -> ε']
            },
            'lista_Columnas': {
                '<nombre_COL>': ['lista_Columnas -> <nombre_COL> , <lista_Columnas>', 'lista_Columnas -> <nombre_COL>']
            },
            'list_FLD': {
                '<nombre_FLD>': ['list_FLD -> <nombre_FLD> , <list_FLD>', 'list_FLD -> <nombre_FLD>']
            },
            'table_references': {
                '<table_reference>': ['table_references -> <table_reference> , <table_references>', 'table_references -> <table_reference>']
            },
            'table_reference': {
                '<table_factor>': ['table_reference -> <table_factor>', 'table_reference -> <joined_table>']
            },
            'table_factor': {
                '<nombre_TBL>': ['table_factor -> <nombre_TBL> <alias>']
            },
            'alias': {
                'AS': ['alias -> AS <alias_name>'],
                '<alias_name>': ['alias -> <alias_name>', 'alias -> ε'],
                'EOF': ['alias -> ε']
            },
            'joined_table': {
                'INNER JOIN': ['joined_table -> INNER JOIN <table_factor> <join_specification>'],
                'LEFT JOIN': ['joined_table -> LEFT JOIN <table_factor> <join_specification>'],
                'RIGHT JOIN': ['joined_table -> RIGHT JOIN <table_factor> <join_specification>']
            },
            'join_specification': {
                'ON': ['join_specification -> ON <condition>'],
                'EOF': ['join_specification -> ε']
            },
            'condition': {
                '<expr>': ['condition -> <expr> OR <expr>', 'condition -> <expr> || <expr>', 'condition -> <expr> XOR <expr>',
                            'condition -> <expr> AND <expr>', 'condition -> <expr> && <expr>', 'condition -> NOT <expr>',
                            'condition -> ! <expr>', 'condition -> <boolean_primary>']
            },
            'boolean_primary': {
                '<boolean_primary>': ['boolean_primary -> <boolean_primary> IS [NOT] NULL', 'boolean_primary -> <boolean_primary> <COMPARISON_OPERATOR> <simple_expr>',
                                        'boolean_primary -> <boolean_primary> <COMPARISON_OPERATOR> (<subquery>)', 'boolean_primary -> <simple_expr>']
            },
            'simple_expr': {
                '<literal>': ['simple_expr -> <literal>'],
                '<identifier>': ['simple_expr -> <identifier>'],
                '<variable>': ['simple_expr -> <variable>']
            },
            'Instruccion_Insertar': {
                'INSERT': ['Instruccion_Insertar -> INSERT INTO <nombre_TBL> (<lista_Columnas>) VALUES (value_list)']
            },
           
