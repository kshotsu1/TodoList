<template>
  <div>
    <h1>TODO List</h1>
    <h2>UNDONE</h2>
    <table>
      <thead>
        <tr>
          <th>完了</th>
          <th>期限</th>
          <th>TODO内容</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="allStatusTrue">
          <td colspan="5" class="no-tasks">
            現在のTODOはありません。<br>
            登録する場合は下の登録ボタンを押してください。<br>
            ↓<br>
          </td>
        </tr>
        <tr v-for="todo in todos" :key="todo.id">
          <template v-if="!todo.status">
          <td><button @click="completeTask(todo.id)">完了</button></td>
          <td>{{ todo.limit_date }}</td>
          <td>{{ todo.content }}</td>
          <td><button @click="openEditModal(todo)">編集</button></td>
          <td><button @click="openDelModal(todo)">削除</button></td>
          </template>
        </tr>
      </tbody>
    </table>
    
    <!-- 登録ボタン -->
    <button type="button" class="register-button" @click="showAddModal = true">登録</button>

    
    <EditModal v-if="selectedEsitTodo" :todo="selectedEsitTodo" @close="selectedEsitTodo = null"></EditModal>
    <DeleteModal v-if="selectedDelTodo" :todo="selectedDelTodo" @close="selectedDelTodo = null"></DeleteModal>
    <AddModal v-if="showAddModal" @close="showAddModal = false"></AddModal>
    
    <div @click="toggle()" class="list-header">
      <h2>DONE</h2>
      <span>{{ isOpen ? '▲' : '▼' }}</span>
    </div>
    <div v-if="isOpen" class="list-content">
      <table>
        <thead>
          <tr>
            <th>期限</th>
            <th>TODO内容</th>
            <th></th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="allStatusFlase">
            <td colspan="4" class="no-tasks">
              現在の完了済みTODOはありません。
            </td>
          </tr>
          <tr v-for="todo in todos" :key="todo.id">
            <template v-if="todo.status">
            <td>{{ todo.limit_date }}</td>
            <td>{{ todo.content }}</td>
            <td><button @click="openLogEditModal(todo)">編集</button></td>
            <td><button @click="openDelModal(todo)">削除</button></td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>
    
    <LogEditModal v-if="selectedLogEditTodo" :todo="selectedLogEditTodo" @close="selectedLogEditTodo = null"></LogEditModal>
    <DeleteModal v-if="selectedDelTodo" :todo="selectedDelTodo" @close="selectedDelTodo = null"></DeleteModal>
  </div>
</template>

<script>
import EditModal from './components/EditModal.vue'; 
import LogEditModal from './components/LogEditModal.vue'; 
import AddModal from './components/AddModal.vue'; 
import DeleteModal from './components/DeleteModal.vue'; 
import axios from 'axios';

export default {
  components: {
    EditModal, 
    AddModal,
    DeleteModal,
    LogEditModal
  },
  data() {
    return {
      showEditModal: false,
      showAddModal: false,
      showDeleteModal: false,
      showLogEditModal: false,
      selectedEsitTodo: null,
      selectedDelTodo: null,
      selectedLogEditTodo: null,
      todos: [],
      isOpen: false,
    };
  },
  computed: {
    allStatusTrue() {
      return this.todos.every(todo => todo.status === 1);
    },
    allStatusFlase() {
      return this.todos.every(todo => todo.status === 0);
    }
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen;
    },
    openEditModal(todo) {
      this.selectedEsitTodo = todo;
    },
    openDelModal(todo) {
      this.selectedDelTodo = todo;
    },
    openLogEditModal(todo) {
      this.selectedLogEditTodo = todo;
    },
    list_get(){
      axios.get('http://127.0.0.1:5000/get_list')
      .then(response  => {
        this.todos = response.data; // 取得したデータをtodosに設定
      });
    },
    async completeTask(id) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/completion', { id: id });
        if (response.status === 200) {
          this.status = 'TODOリストが更新されました！';
          this.refreshTasks();
        } else {
          this.status = '処理に失敗しました';
        }
      } catch (error) {
        console.error('完了処理エラー:', error);
        this.status = '処理に失敗しました';
      }
    },
    async refreshTasks() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/get_list');
        this.todos = response.data;
      } catch (error) {
        console.error('タスクリスト取得エラー:', error);
      }
    }
  },
  mounted() {
    this.list_get();
    this.refreshTasks();
  }
};
</script>

<style>
/* 全体のレイアウト */
body {
  font-family: 'Roboto', sans-serif;
  margin: 20px;
  padding: 60px;
  background-color: #ffffff; /* 背景色を白に */
  color: #000000; /* 文字色を黒に */
}



/* テーブルのスタイル */
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th, td {
  padding: 16px;
  text-align: left;
  border-bottom: 2px solid #ddd;
}

th {
  background-color: #ffffff; /* 背景色を白に */
  color: #000000; /* 文字色を黒に */
  font-weight: bold;
}

td {
  background-color: #ffffff; /* 背景色を白に */
}

tr:nth-child(even) {
  background-color: #f8f9fa; /* 奇数行の背景色を少しグレーに */
}

tr:hover {
  background-color: #e2e6ea; /* ホバー時の背景色 */
}

/* ボタンのスタイル */
button {
  background-color: #007bff;
  color: #ffffff; /* ボタンの文字色を白に */
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

/* 登録ボタンのスタイル */
button.register-button {
  background-color: #007bff;
  color: #ffffff; /* 文字色を白に */
  border: none;
  border-radius: 6px;
  padding: 10px 160px; /* 横長にするために左右のパディングを増やす */
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  display: block; /* ブロック要素にして */
  margin: 20px auto; /* 上下のマージンを設定して中央に配置 */
}

button.register-button:hover {
  background-color: #0056b3;
}


/* モーダルのスタイル */
.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal { /* モーダル内の背景設定 */
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 軽い影を追加 */
  height: 600px; /* モーダルの高さを設定 */
  width: 1000px; /* モーダルの幅を設定 */
}

/* アコーディオンメニュー */
.list-header {
  background-color: #ffffff; /* 背景色を白に */
  padding: 15px;
  cursor: pointer;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
  font-weight: bold;
  color: #000000; /* 文字色を黒に */
  border: 1px solid #ddd;
}

.list-header:hover {
  background-color: #f1f1f1; /* ホバー時の背景色 */
}

.list-content {
  padding: 15px;
  border-radius: 8px;
  background-color: #ffffff; /* 背景色を白に */
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}

.no-tasks {
  text-align: center;
  color: #000000; /* 文字色を黒に */
}

p {
  margin: 0;
  color: #000000; /* 文字色を黒に */
}

h1, h2 {
  margin-top: 0;
  color: #000000; /* 文字色を黒に */
}

.add-button {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  margin-bottom: 20px;
}

.add-button:hover {
  background-color: #0056b3;
}
</style>
