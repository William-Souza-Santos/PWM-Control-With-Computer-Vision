#define PWM_PIN 9  // Pino de saída PWM

void setup() {
    Serial.begin(9600);  // Inicia comunicação serial
    pinMode(PWM_PIN, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        int contador = Serial.parseInt();  // Lê o número inteiro recebido
        if (contador >= 0 && contador <= 10) {
            int pwm_value = map(contador, 0, 10, 0, 255);  // Converte 0-10 para 0-255
            analogWrite(PWM_PIN, pwm_value);  // Aplica PWM na saída
            Serial.print("PWM ajustado para: ");
            Serial.println(pwm_value);
        }
    }
}
