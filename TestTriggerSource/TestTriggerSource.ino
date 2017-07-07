/* Trigger source for testing
  -----------------------------------------------------------------------
  Copyright Mick Phillips, 2017.

  Reads keypresses over serial and:
    generates triggers on lines 8-11 (keys 1-4);
    toggles lines 12 and 13 (keys 5 and 6).

  ---------------------------------------------------------------------*/

int incomingByte = 0;
int line;

void keyToLine(char c) {
  // Map keys 1-4 to lines 8-11
  line = c - '0' + 7;
  if (line < 8 || line > 13) {
    line = -1;
  }
}

void setup() {
  Serial.begin(9600);
  DDRB = DDRB | B00111111;
  PORTB = B00000000;
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    keyToLine(incomingByte);
    unsigned int mask = 1 << line - 8;
    if (line >= 8 && line <= 11 ) {
      PORTB = PORTB ^ mask;
      delay(2);
      PORTB = PORTB ^ mask;
      Serial.print("Triggered line ");
      Serial.println(line);
    } 
    else if (line >= 12 && line <= 13) {
        PORTB = PORTB ^ mask;
        Serial.print("Toggled line ");
        Serial.println(line);
    }
  }
}
