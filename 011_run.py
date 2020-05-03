from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/write", methods=["GET", "POST"])
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")        
        contents = request.form.get("contents")
    else:
        return render_template("write.html")


if __name__ == "__main__":
    app.run(debug=True)

# 직접 실행이 되었느냐, 아니면 모듈에서 임포트 되어 실행이 되었느냐
# 직접실행 했기 때문에 이 구간이 실행.