import random
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

intentsdict = {
    'hi' : ['hello','hey','hi!','hi'],
    'bye' : ['goodbye','buhbye','bye'],
    'depression' : ['depressed','sad','worried','despair','misery','bad'],
    'anxiety' : ['anxiety','anxious','nervous','stress','strain','tension','discomfort','tensed'],
    'paranoia' :['disbelieve', 'distrustful', 'doubting', 'incredulous','mistrustful', 'negativistic','questioning','show-me','skeptical','suspecting','suspicious','unbelieving'],
    'sleeping_disorder' :['restlessness','indisposition','sleeplessness','stress','tension','vigil','vigilance','wakefulness'],
    'substance_abuse' :['alcohol abuse','drug abuse','drug use','addiction','alcoholic addiction','alcoholism','chemical abuse','dipsomania','drug dependence','drug habit','narcotics abuse','solvent abuse'],
    'personality_disorder':['insanity','mental disorder','schizophrenia','craziness','delusions','depression','derangement','disturbed mind','emotional disorder','emotional instability',
                            'loss of mind','lunacy','madness','maladjustment','mania','mental disease','mental sickness','nervous breakdown','nervous disorder',
                            'neurosis','neurotic disorder','paranoia','phobia','psychopathy','psychosis','sick mind','troubled mind','unbalanced mind','unsoundness of mind'],
    'happy':['good','great','relieved','happy','okay']
}

# Dictionary containing predefined greetings and responses
greetdict = {
    "Hello": "Hello, Username!",
    "Konnichiwa" : "Good Morning in Japanese! How can I assist you today?",
    "Hola amigos": "Hello in Spanish! How can I assist you today?",
    'whatsup' : "Hello... What a cool ways to greetings! How can I assist you today?",
    "สวัสดี": "Hello in Thai! How I can assist you today?",
    }

resdict = ["I'm doing great here. Thank you for asking.", 'I am fine thank you', ]

devdict = {
    "ใครสร้างคุณขึ้นมา" : "ผมถูกสร้างขึ้นเพื่อส่งเข้าแข่งขันโดยทีมมหกรรมไม่ได้นอนในงาน 42Bangkok X AWS Hackathon เมื่อวันที่ 19 สิงหาคม 2566",
    "Who build you up" : "My Papa :)",
    "Who developed you" : "I am developed by Nonsleepfestival for enter 42Bangkok X AWS Hackathon competition in 19 Aug 2023",
    "What was you made for" : "I am here to help people getting better in any situation. My Recovery Must Come First So That Everything I Love In Life Doesn’t Have To Come Last!"
}

conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/chat", methods=["POST", "GET"])
def chat():
    data = request.get_json()
    if 'message' in data:
        message = data['message']
        print("Received message:", message)  # Debug print
        if message in greetdict:
            chatbot_response = greetdict[message]
        elif message in devdict:
            chatbot_response = devdict[message]
        else:
            # Debug print to see which branch is taken
            print("Using default response")  
            random_responses = ["I'm here to help!", "How can I assist you today?", "Feel free to ask any questions!"]
            chatbot_response = random.choice(random_responses)
        return jsonify({"response": chatbot_response, "conversation": conversation_history})
         
    else:
        return jsonify({"error": "Invalid request format"}), 400

def get_chatbot_response(message):
    # Extract username from the conversation history
    username = extract_username(conversation_history)
    # Implement your chatbot logic here
    if message.lower() == ("Who Developed you"):
        return f"Psyboost is Developed by Nonsleepfestival Team for 42Bangkok X AWS Hackathon in 19-20 August 2023 !",{username}
    elif message.lower() == greetdict:
        return chat()
    else:
        return f"Sorry, I don't understand what you said before."
    
def extract_username(conversation_history):
    # Extract username from the conversation history
    for entry in reversed(conversation_history):
        if "user" in entry:
            # Assuming the first user message is the username (for simplicity)
            return entry["user"]

    # Default username if not found
    return "User"

if __name__ == '__main__':
    app.run(debug=True)
