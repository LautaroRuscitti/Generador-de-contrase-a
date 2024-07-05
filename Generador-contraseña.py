import random
import string

def generador_contraseñas(longitud, usar_mayusculas=True, usar_numeros=True, usar_especiales=True):
    caracteres = string.ascii_lowercase  # letras minúsculas por defecto
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation
        
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    longitud = int(input("Longitud de la contraseña: "))
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's' 
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's' 
    
    contraseña = generador_contraseñas(longitud, incluir_mayusculas, incluir_numeros, incluir_especiales)
    print(f"Contraseña generada: {contraseña}")

if __name__ == "__main__":
    main()
