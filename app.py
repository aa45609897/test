from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Welcome to the Test Page 3!</h1>"

if __name__ == '__main__':
    # 设置 host 为 0.0.0.0 使应用可以被外部访问
    # 设置 port 为 5000 或其他您想要的端口
    app.run(host='0.0.0.0', port=5000, debug=True)
