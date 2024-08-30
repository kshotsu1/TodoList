import sys
import webbrowser
from pathlib import Path
import todo_db
import sqlite3
from flask import Flask, render_template, request, jsonify
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



# 登録処理
@app.route("/insert", methods=["POST"])
def insert_data():
    conection = sqlite3.connect("todo.db")
    cursor = conection.cursor()

    data = request.get_json(force=True)

    # 入力を数値に変換する。
    content = data["content"]
    limit_date = data["limit_date"]

    insert_sql = """
        INSERT INTO todos (content, status, 'limit_date')VALUES (?, ?, ?)
    """
    cursor.execute(insert_sql, (content, 0, limit_date))
    conection.commit()
    conection.close()

    return {"message": 'TODOリストに追加しました。'}

# 取得処理
def get_todos():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, content, limit_date, status FROM todos")
    todos = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'content': row[1], 'limit_date': row[2], 'status':row[3] } for row in todos]

@app.route("/get_list", methods=["GET"])
def todos():
    print(get_todos())
    return jsonify(get_todos())


# 更新処理
@app.route("/edit", methods=["POST"])
def todo_update():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()

    data = request.get_json(force=True)

    # 入力を数値に変換する。
    id = data["id"]
    limit_date = data["limit_date"]
    content = data["content"]

    update_sql = """
        UPDATE todos SET limit_date = ?, content = ? WHERE id = ?
    """
    cursor.execute(update_sql, (limit_date, content, id))
    connection.commit()
    connection.close()

    return {"message": 'TODOリストを更新しました。'}
    

# 削除処理
@app.route("/delete", methods=["POST"])
def todo_telete():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()

    data = request.get_json(force=True)
    id = data["id"]

    delete_sql = """
        DELETE FROM todos WHERE id = ?
    """
    cursor.execute(delete_sql, (id,))
    connection.commit()
    connection.close()

    return {"message": 'TODOリストを削除しました。'}


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