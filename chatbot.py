import random 

# Meldingene og svarene du kan bruke til chatboten
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm good, thanks!", "I'm doing well!", "All is good!"],
    "bye": ["Goodbye!", "Farewell!", "Take care!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?", "I'm still learning."]
}

# Funksjon for svar
def get_response(message):
    message = message.lower()
    
    
    if message in responses:                        # Sjekker om du kan bruke meldingen til chatboten
        return random.choice(responses[message])    # Hvis du har brukt en gyldig melding så vil den velge et tilfeldig svar
    else: 
        return random.choice(responses["default"])  # Hvis du ikke har brukt en gyldig melding så velger boten et tilfeldig svar fra "default"

# Loop for chatboten
while True:
    user_input = input("User: ")     # Brukeren skriver en melding
    response = get_response(user_input)     # Gir et svar basert på hva du skrev
    print("ChatBot:", response)       # Skriver ut svaret
