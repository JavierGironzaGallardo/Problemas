

# Knigths exercise

MOVES= [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]
# La diferencia entre una Tuple y una List 
# es que la list se puede modificar después de hacerse

def knights_tour(n):
    # Caso base: tablero inválido
    if n <= 0:
        return []
    
    # Crear tablero n×n lleno de -1 (sin visitar)
    board = [[-1] * n for _ in range(n)] # Esto repite esa fila n veces, para tener n filas en total.
    board[0][0] = 0  # El caballo empieza en la esquina superior izquierda

# Comprobación: ¿está dentro del tablero?
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

 # Contar cuántas casillas libres tiene alrededor (heurística de Warnsdorff)
    def degree(x, y):
        count = 0
        for dx, dy in MOVES: #No es necesario definir nada porque se sabe que MOVES tiene dos valores
            nx = x + dx
            ny = y + dy
            if in_bounds(nx, ny) and board[nx][ny] == -1:
                count += 1
        return count
    

    # Ordenar los movimientos según el número de salidas (menor primero)
    def ordered_moves(x, y):
        opciones = []
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if in_bounds(nx, ny) and board[nx][ny] == -1:
                opciones.append((degree(nx, ny), nx, ny))
        opciones.sort()  # ordena por grado ascendente
        return [(nx, ny) for _, nx, ny in opciones]
    


    # Algoritmo recursivo (backtracking)
    # Step nos dice el orden de movimientos
    def backtrack(step, x, y):
        # Si ya visitó todas las casillas, éxito
        if step == n * n:
            return True
        # Probar cada movimiento válido, ordenado por heurística
        for nx, ny in ordered_moves(x, y):
            board[nx][ny] = step
            if backtrack(step + 1, nx, ny):
                return True
            # Si no funciona, deshacer el paso
            board[nx][ny] = -1
        return False

    return board if backtrack(1, 0, 0) else []

# ====== Bloque de ejecución ======
if __name__ == "__main__":
    n = 6
    result = knights_tour(n)
    if result:
        for fila in result:
            print(" ".join(f"{v:2d}" for v in fila))
    else:
        print("No hay solución.")
    
    



