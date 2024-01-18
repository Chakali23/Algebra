#include <Arduino.h>
#ifdef ESP32
  #include <WiFi.h>
  #include <AsyncTCP.h>
#else
  #include <ESP8266WiFi.h>
  #include <ESPAsyncTCP.h>:
#endif
#include <ESPAsyncWebServer.h>
#include"matfun.h"

AsyncWebServer server(80);

const char* ssid = "Suresh";
const char* password = "987654321";

const char* input_parameter00 = "input00";
const char* input_parameter01 = "input01";
const char* input_parameter10 = "input10";
const char* input_parameter11 = "input11";
const char* input_parameter20 = "input20";
const char* matrix1[2]={input_parameter00,input_parameter01};     // matrix for vertex A
const char* matrix2[2]={input_parameter10,input_parameter11};     // matrix for vertex B
const char* matrix3[1]={input_parameter20};     // Angle

const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML><html><head>
    <title>TRIANGLE PROPERTIES</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      html {font-family: Times New Roman; display: inline-block; text-align: center;}
      h2 {font-size: 2.0rem; color: blue;}
    </style> 
    </head><body>
    <h2>TO CHECK PROPERTIES OF TRIANGLES</h2> 
    <p>Enter the values of points A, B and theta
    <form action="/get">
      Enter the values of Point A: <input type="number" name="input00"> <input type="number" name="input01"><br><br>
      Enter the values of Point B: <input type="number" name="input10"> <input type="number" name="input11"><br><br>
      Enter the value of angle: <input type="number" name="input20"><br><br>
      <input type="submit" value="Submit">
    </form><br>
  </body></html>)rawliteral";

void notFound(AsyncWebServerRequest *request) {
  request->send(404, "text/plain", "Not found");
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  if (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("Connecting...");
    return;
  }
  Serial.println();
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", index_html);
  });

server.on("/get", HTTP_GET, [] (AsyncWebServerRequest *request) {




double **A,**B;//declaring matrices names
double **P;//declare P midpoint
double AD,BE,BP,AP,EB,DA;//direction vectors
double r; //Length of AD and BE
int m = 2, n = 2, o = 1;
double **theta;
theta=load_ser(request,matrix3,1);
double angle = theta[0][0]*(M_PI/180);


A = load_ser(request,matrix1,2);
B = load_ser(request,matrix2,2);

//mid-point
P = Matsec(A,B,m,o);

r = Matnorm(Matsub(A,B,m,n),m);

double **D = createMat(m,o);
D = Mat_2(A,r,angle);

double **E = createMat(m,o);
E = Mat_1(B,r,angle);

BP = Matnorm(Matsub(B,P,m,o),m);
AP = Matnorm(Matsub(A,P,m,o),m);
EB = Matnorm(Matsub(E,B,m,o),m);
DA = Matnorm(Matsub(D,A,m,o),m);
 
String response;

if ((BP == AP) && (EB == DA)) {

        response += "<p>&#9651; DAP  &#8773; &#9651; EBP (congruent By SAS Congruency)</p>";
    } else {
        response += "<p>&#9651; DAP &#x2247; &#9651; EBP (is NOT congruent)</p>";
    };

//length of AD, BE
AD = Matnorm(Matsub(A,D,m,o),m);
BE = Matnorm(Matsub(B,E,m,o),m);

if(AD == BE)
	response += "<p>AD is equal to BE</p>";
else
	response += "<p> AD is not equal to BE</p>";

    
	response += "<br><a href=\"/\">Return to Home Page</a>";
    // Send the HTML response with dynamic content
    request->send(200, "text/html", response);
});
  server.onNotFound(notFound);
  server.begin();
}
void loop() { 
}
