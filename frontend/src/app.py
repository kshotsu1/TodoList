from flask import Flask, render_template, request
import db

app = Flask(__name__, template_folder='./frontend')


@app.route('/')
def show_data():
    databace = db.get_db()
    list = databace.execute("SELECT * FROM todos").fetchall()
    db.close_db()
    return render_template('App.vue', lists=list)

# @app.route('/insert', methods=['POST'])
# def show_data():
#     databace = db.get_db()
#     list = databace.execute("SELECT * FROM todos").fetchall()
#     db.close_db()
#     return render_template('index.html', lists=list)



# # DBを指定して接続
# connection = sqlite3.connect('todo.db')
# # SQLを実行するために必要なカーソルと呼ばれるものを取得
# cursor = connection.cursor()

# cursor.execute("""
#     INSERT INTO todos (content, statas, `limit`) 
#     VALUES ('本を返す', 0, '2024-9-15');
# """)
# connection.commit()

# cursor.close()
# connection.close()