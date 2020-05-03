from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h5>헬로 파이썬</h5>"


if __name__ == "__main__":
    app.run(debug=True)

# 직접 실행이 되었느냐, 아니면 모듈에서 임포트 되어 실행이 되었느냐
# 직접실행 했기 때문에 이 구간이 실행됩니다