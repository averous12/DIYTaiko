int pinStart = 2; //Start of the pin used for button
int pinEnd = 5; //End of the pin used for button
int ButtonCount = 4; //store how many button will be used
String Buttons[] = {"LeftO", "LeftI", "RightI", "RightO"}; //button labels

String ButtonPress(int pin) { //function to determine button state
  if (digitalRead(pin) != HIGH) {
    return "\"Hit\"";
  }
  else {
    return "\"Off\"";
  }
}

void setup() {
  Serial.begin(115200);
  for (int i = pinStart; i <= pinEnd; i++) { //set button pinMode
    pinMode(i, INPUT_PULLUP);
  }
  for (int i = 0; i < ButtonCount; i++) { //iterate through Buttons[] to put double quote
    Buttons[i] = '\"' + Buttons[i] + '\"';
  }
}

void loop() {
  String json = "{";
  for (int i = 0; i < ButtonCount; i++) { //iterate to append button and state
    int j = pinStart + i;
    json += Buttons[i] + ":" + ButtonPress(j);
    if (j != pinEnd) { //add a ',' at the end except for last iteration
      json += ",";
    }
  }
  json += "}";
  Serial.println(json); //output json to serial to be processed with python app
  delay(25);
}
