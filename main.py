import sys
import webbrowser
from pathlib import Path
import todo_db
import sqlite3
from flask import Flask, render_template, request
from flask_cors import CORS


def base_dir():
    if hasattr(sys, "_MEIPASS"):
        # 実行ファイルで起動した場合、展開先ディレクトリを基点とする。
        return Path(sys._MEIPASS)
    else:
        # python コマンドで起動した場合、プロジェクトディレクトリを基点とする。
        return Path("..")

app = Flask(
    __name__,
    template_folder="dist",
    static_folder="dist/static"
)
CORS(app)




@app.route("/insert", methods=["POST"])
def insert_data():
    conection = sqlite3.connect("todo.db")
    cursor = conection.cursor()

    data = request.get_json(force=True)

    # 入力を数値に変換する。
    content = data["content"]
    limit = data["limit"]

    insert_sql = """
        INSERT INTO todos (content, status, 'limit')VALUES (?, ?, ?)
    """
    cursor.execute(insert_sql, (content, 0, limit))
    conection.commit()
    conection.close()

    return {"message": 'TODOリストに追加しました。'}


@app.route("/")
def index():
    """フロントエンド側のページを表示する。

    Returns:
        str: HTML
    """
    return render_template("index.html")



def main():
    webbrowser.open("http://localhost:5000/", new=2, autoraise=True)
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()