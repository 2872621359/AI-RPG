from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/css/<path:filename>')
def serve_css(filename):
    css_files = {
        "1230characterselection-try.css": "1230characterselection-try.css",
        "chatpage-1227-try1.css": "chatpage-1227-try1.css",
        "1223homepage-try.css" : "1223homepage-try.css",
        "1223storycontext-try.css" : "1223storycontext-try.css"
    }
    return send_from_directory('css', css_files.get(filename, 'chatpage-1227-try1.css'))
#这里创建了一个css_files字典，用于存储不同 CSS 文件名及其对应的文件路径。如果filename在字典中，就返回对应的 CSS 文件；如果不在字典中，就返回chatpage-1227-try1.css作为默认文件。
  
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route('/')
def index():
    return render_template('1223homepage-try.html')

@app.route('/storycontextpage')
def storycontextpage():
    return render_template('1223storycontext-try.html')

@app.route('/characterselection')
def haracterselection():
    return render_template('1230characterselection-try.html')

@app.route('/chatpage')
def chatpage():
    card = request.args.get('card')
    if card == '1':
        content = {
            "image_path": "/static/images/characterimage1.png",
            "description": "This is card 1"
        }
        return render_template('chatpage-1227-try1.html', card=card, content=content)
    elif card == '2':
        content = {
            "image_path": "/static/images/characterimage2.png",
            "description": "This is card 2"
        }
        return render_template('chatpage-1227-try1.html', card=card, content=content)
    elif card == '3':
        content = {
            "image_path": "/static/images/characterimage3.png",
            "description": "This is card 3"
        }
        return render_template('chatpage-1227-try1.html', card=card, content=content)
    else:
        return render_template('chatpage-1227-try1.html')
    #return render_template('chatpage-1227-try1.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({'answer': 'Question is missing.'}), 400
    # 处理逻辑
    if question == "你是谁？这里发生了什么事？":
        answer = "哈哈，你很快就会知道的，跟随我的指引来吧。"
    elif question == "酒保，这个小镇最近不太平，让我想到了我那边的泰国发生的事。":
        answer = "酒保（沙哑的声音）：“咱这儿啊，最近老是有奇怪的声音，一到夜里，那动静就跟有什么东西在暗处窥视似的。你要是不想像那星星在泰国似的没了踪影，最好赶紧离开这儿。”"
    elif question == "失踪那天你见过他吗":
        answer = "嗯，那天晚上，他抱着一本书走向公墓，月光洒在他身上，像个吟游诗人。"
    elif question == "听说道格拉斯他常在这读书":
        answer = "嗯，他常坐在那块墓碑上看书。不过，有些事你们还是别深究的好。"
    else:
        answer = "您做出了超纲行为。"
    return jsonify({'answer': answer})

@app.route('/gamestart', methods=['GET'])
def gamestart():
    return jsonify({'message': '欢迎来到寻书人小镇，罗拉，你准备好迎接挑战了吗？'})

#随机数生成        
@app.route('/generate_random_number', methods=['GET'])
def generate_random_number():
    random_number = random.randint(1, 100)
    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    # 把 5000 改成 5001 或其他数字
    port = int(os.environ.get("PORT", 5001)) 
    app.run(host='0.0.0.0', port=port)
    