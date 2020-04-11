const int red = 1;
const int green = 2;
const int blue = 3;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
}

void loop() {
  digitalWrite(blue, LOW);
  digitalWrite(red, HIGH);
  delay(1000);
  digitalWrite(red, LOW);
  digitalWrite(green, HIGH);
  delay(1000);
  digitalWrite(green, LOW);
  digitalWrite(blue, HIGH);
  delay(1000);
}
