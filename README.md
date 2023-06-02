# Chatbot

Jeg har laget en chatbot som svarer på enkle spørsmål som du stiller. Jeg har brukt python for å lage chatboten.

## Hvordan det fungerer
Det første jeg gjorde var å importere et bibliotek som jeg skal bruke i koden.
```
import random 
```
Denne delen av koden lager en ordbok over svar koblet til inputen.
```
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm good, thanks!", "I'm doing well!", "All is good!"],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?", "I'm still learning."]
}
```
Dette er funksjonen for svar
```
def get_response(message):
    message = message.lower()
```

Denne delen av koden sjekker om du har valgt en melding fra ordboken og om du har gjort det så vil boten velge et tilfeldig svar som er koblet til meldingen.
Hvis du ikke har skrevet en melding som er i ordboken så vil boten et tilfeldig svar fra "default"
```
    if message in responses:
    return random.choice(responses[message])
else:
    return random.choice(responses["default"])
```

Dette er en loop av chatboten. 
Brukeren skriver en melding og får et svar som er basert på meldingen din. Til slutt skriver den ut svaret.
```
while True:
    user_input = input("User: ")    
    response = get_response(user_input)    
    print("ChatBot:", response)    
```
