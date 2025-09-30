from flask import Flask, render_template, request

app = Flask(__name__)

# 홈 페이지
@app.route("/")
def home():
    return render_template("home.html")

# 구구단 페이지
@app.route("/gugudan", methods=["GET", "POST"])
def gugudan():
    result = []
    if request.method == "POST":
        try:
            dan = int(request.form["dan"])
            # 입력값 dan에 대해 1부터 9까지 곱한 결과를 리스트에 저장
            result = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]
        except (ValueError, KeyError):
            result = ["잘못된 입력입니다. 숫자를 입력해 주세요."]
    return render_template("gugudan.html", result=result)

# 계산기 페이지
@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["op"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                # 0으로 나누는 경우 예외 처리
                if num2 == 0:
                    result = "0으로 나눌 수 없습니다."
                else:
                    result = num1 / num2
        except (ValueError, KeyError):
            result = "잘못된 입력입니다. 숫자를 입력해 주세요."
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)