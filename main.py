import sys
import webbrowser
from pathlib import Path
import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# 基本ディレクトリを判定する関数
def base_dir():
    return Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path("..")

# Flaskアプリケーションを初期化し、CORSを有効にする
app = Flask(__name__, template_folder="dist", static_folder="dist/static")
CORS(app)


"""
データベース接続を管理するコンテキストマネージャを作成する。
Returns:
    connection: sqlite3.Connection - データベース接続
"""
# データベース接続を管理するコンテキストマネージャ
def get_db_connection():
    connection = sqlite3.connect("todo.db")
    connection.row_factory = sqlite3.Row  # 行を名前でアクセス可能にする
    return connection


#==================GET==================
"""
GETメソッドでデータを取得するためのエンドポイントを作成する。
Returns:
    List[Dict]: todos - TODOリストのデータ
"""
# 全てのTODOを取得する
@app.route("/get_list", methods=["GET"])
def todos():
    query_sql = "SELECT id, content, limit_date, status FROM todos ORDER BY limit_date ASC"
    
    with get_db_connection() as conn:
        todos = conn.execute(query_sql).fetchall()

    return jsonify([dict(todo) for todo in todos])



#==================POST==================
"""
POSTメソッドでデータを受け取るためのエンドポイントを作成する。
リクエストボディにはJSON形式でデータを送信する。
Returns:
    Srting: message - 処理成功時のメッセージ
"""

# TODOを追加する
@app.route("/insert", methods=["POST"])
def insert_data():
    data = request.get_json(force=True)
    content, limit_date = data["content"], data["limit_date"]

    insert_sql = "INSERT INTO todos (content, status, limit_date) VALUES (?, ?, ?)"
    
    with get_db_connection() as conn:
        conn.execute(insert_sql, (content, 0, limit_date))
        conn.commit()

    return {"message": "～TODOリストに追加しました～"}


# TODOを更新する
@app.route("/edit", methods=["POST"])
def todo_update():
    data = request.get_json(force=True)
    update_sql = "UPDATE todos SET limit_date = ?, content = ? WHERE id = ?"
    
    with get_db_connection() as conn:
        conn.execute(update_sql, (data["limit_date"], data["content"], data["id"]))
        conn.commit()

    return {"message": "～TODOリストを更新しました～"}

# TODOを削除する
@app.route("/delete", methods=["POST"])
def todo_delete():
    data = request.get_json(force=True)
    delete_sql = "DELETE FROM todos WHERE id = ?"
    
    with get_db_connection() as conn:
        conn.execute(delete_sql, (data["id"],))
        conn.commit()

    return {"message": "～TODOリストを削除しました～"}

# TODOを履歴として更新し、リストに追加する（ステータスを0にリセット）
@app.route("/log_edit_add_list", methods=["POST"])
def todo_log_update():
    data = request.get_json(force=True)
    update_sql = "UPDATE todos SET limit_date = ?, content = ?, status = 0 WHERE id = ?"
    
    with get_db_connection() as conn:
        conn.execute(update_sql, (data["limit_date"], data["content"], data["id"]))
        conn.commit()

    return {"message": "～履歴からTODOを追加しました～"}

# 完了ステータスを切り替える
@app.route("/completion", methods=["POST"])
def completion():
    data = request.get_json(force=True)
    status = 1 if data["status"] == 0 else 0
    update_sql = "UPDATE todos SET status = ? WHERE id = ?"
    
    with get_db_connection() as conn:
        conn.execute(update_sql, (status, data["id"]))
        conn.commit()

    return {"message": "～TODOリストを更新しました～"}


# インデックスページを表示する
@app.route("/")
def index():
    return render_template("index.html")

# アプリケーションを実行する
def main():
    webbrowser.open("http://localhost:5000/", new=2, autoraise=True)
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
