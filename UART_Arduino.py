import serial
import time
import PWM_Control_with_Computer_Vision

# Configurar a porta serial (ajuste conforme necessário)
porta_serial = serial.Serial('COM3', 9600, timeout=1)  # Para Linux, use '/dev/ttyUSB0'

time.sleep(2)  # Espera a conexão estabilizar

filled_width = int((contador * (20)/ max_counter) * width)

def enviar_contador(contador):
    """Envia o valor do contador para o Arduino."""
    dado = f"{contador}\n"  # Converte o valor em string
    porta_serial.write(dado.encode())  # Envia para a serial
    print(f"Enviado: {contador}")

while True:
    try:
        contador = int(input("Digite um valor para contador (0-10): "))
        if 0 <= contador <= 10:
            enviar_contador(contador)
        else:
            print("Valor fora do intervalo!")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

porta_serial.close()