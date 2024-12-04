#Código generado por chatgpt posteriormente con una ligera modificación para que cuente las palabras. Lo subo por motivos docentes.

def cargar_sopa_de_letras(archivo):
    """Carga la sopa de letras desde un archivo de texto."""
    with open(archivo, 'r') as f:
        sopa = [linea.strip() for linea in f]
    return sopa

def buscar_palabra(sopa, palabra):
    """Busca una palabra en una sopa de letras en todas las direcciones."""
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud = len(palabra)
    direcciones = [
        (0, 1),   # Derecha
        (0, -1),  # Izquierda
        (1, 0),   # Abajo
        (-1, 0),  # Arriba
        (1, 1),   # Diagonal abajo-derecha
        (-1, -1), # Diagonal arriba-izquierda
        (1, -1),  # Diagonal abajo-izquierda
        (-1, 1)   # Diagonal arriba-derecha
    ]
    
    def dentro_limites(x, y):
        return 0 <= x < filas and 0 <= y < columnas

    def buscar_direccion(x, y, dx, dy):
        for i in range(longitud):
            nx, ny = x + i * dx, y + i * dy
            if not dentro_limites(nx, ny) or sopa[nx][ny] != palabra[i]:
                return False
        return True
    
    count = 0
    for x in range(filas):
        for y in range(columnas):
            for dx, dy in direcciones:
                if buscar_direccion(x, y, dx, dy):
                    count = count+1
    
    return count

# Ejemplo de uso
archivo = "input4"  # Nombre del archivo que contiene la sopa de letras
palabra = "XMAS"    # Palabra a buscar

sopa = cargar_sopa_de_letras(archivo)
resultado = buscar_palabra(sopa, palabra)
print(resultado)

