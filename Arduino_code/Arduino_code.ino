const int pwmPin = 9;

void setup() {
  Serial.begin(9600);
  pinMode(pwmPin, OUTPUT);
  analogWrite(pwmPin, 0); // Inicia com 0%
  //while (!Serial); // Aguarda conexão (só necessário para Leonardo/32u4)
}

void loop() {
  if (Serial.available() > 0) {
    int receivedValue = Serial.parseInt(); // Lê diretamente o valor inteiro

    // Limita entre 0-100 e converte para PWM
    receivedValue = constrain(receivedValue, 0, 100);
    int pwmValue = map(receivedValue, 0, 100, 0, 255);

    analogWrite(pwmPin, pwmValue);

    // Feedback
    Serial.print("Recebido: ");
    Serial.print(receivedValue);
    Serial.println("%");
  }
}
