from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hermes Agent</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #0f172a; color: #fff; }
            #chat { height: 300px; border: 1px solid #334155; padding: 10px; overflow-y: scroll; margin-bottom: 10px; border-radius: 8px; background: #1e293b; }
            input { width: 75%; padding: 10px; border-radius: 4px; border: 1px solid #334155; background: #0f172a; color: #fff; }
            button { width: 20%; padding: 10px; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h2>Hermes Agent</h2>
        <div id="chat"></div>
        <input type="text" id="msg" placeholder="اكتب سؤالك هنا...">
        <button onclick="send()">إرسال</button>

        <script>
            async function send() {
                let input = document.getElementById('msg');
                let chat = document.getElementById('chat');
                let text = input.value;
                if(!text) return;
                
                chat.innerHTML += "<div><b>أنت:</b> " + text + "</div>";
                input.value = "";
                
                let res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: text})
                });
                let data = await res.json();
                chat.innerHTML += "<div style='color: #60a5fa;'><b>Hermes:</b> " + data.reply + "</div><br>";
                chat.scrollTop = chat.scrollHeight;
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_msg = data.get('message', '')
    # هنا سيتم ربط منطق الـ Agent والـ Vector DB لاحقاً
    reply = f"تم استقبال رسالتك بنجاح: {user_msg}"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run()
