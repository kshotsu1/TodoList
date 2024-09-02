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
      <p v-if="allStatusTrue">
        現在のTODOはありません。<br>
        登録する場合は下の登録ボタンを押してください。<br>
        ↓<br>
      </p>
      <tbody v-else>
        <tr v-for="todo in todos" :key="todo.id">
          <template v-if="!todo.status">
            <!-- <th><input type="checkbox"  @change="handleChange"></th> -->
            <th><button @click="completion(todo.id)">完了</button></th>
            <th>{{ todo.limit_date }}</th>
            <th>{{ todo.content }}</th>
            <th> 
              <!-- 編集モーダルを開くボタン -->
              <button  @click="openEditModal(todo)">編集</button>             
            </th>
            <th> 
              <!-- 削除ダイアログを開くボタン -->
              <button  @click="openDelModal(todo)">削除</button> 
            </th>
          </template>
        </tr>
      </tbody>
    </table>
    <!-- 登録モーダルを開くボタン --> 
    <button  type="button" @click="showAddModal = true">登録</button>
    
    <EditModal v-if="selectedEsitTodo" :todo="selectedEsitTodo" @close="selectedEsitTodo = null"></EditModal>
    <DeleteModal v-if="selectedDelTodo" :todo="selectedDelTodo" @close="selectedDelTodo = null"></DeleteModal>
    <AddModal v-if="showAddModal" @close="showAddModal = false"></AddModal>
    

    <!-- 履歴のアコーディオンメニュー -->
    <div @click="toggle()" class="list-header">
      <h2>DONE</h2>
      <span>{{ isOpen ? '▲' : '▼' }}</span> <!-- 折りたたみ状態を表示 -->
    </div>
    <div v-if="isOpen" class="list-content">
      <div v-if="allStatusFlase">
        現在の完了済みTODOはありません。<br>
      </div>
      <div v-else>
        <tr v-for="todo in todos" :key="todo.id">
          <template v-if="todo.status">
            <!-- <th><input type="checkbox"></th> -->
            <th>{{ todo.limit_date }}</th>
            <th>{{ todo.content }}</th>
            <th> 
              <!-- 編集モーダルを開くボタン -->
              <button @click="openLogEditModal(todo)">編集</button> 
              <LogEditModal v-if="selectedLogEditTodo" :todo="selectedLogEditTodo" @close="selectedLogEditTodo = null"></LogEditModal>
            </th>
            <th> 
              <!-- 削除ダイアログを開くボタン -->
              <button  @click="openDelModal(todo)">削除</button> 
              <DeleteModal v-if="selectedDelTodo" :todo="selectedDelTodo" @close="selectedDelTodo = null"></DeleteModal>
            </th>
          </template>
        </tr>
      </div>
    </div>
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
      selectedEsitTodo: null, // 選択されたEditTODOのデータを格納
      selectedDelTodo: null, // 選択されたDelTODOのデータを格納
      selectedLogEditTodo: null, // 選択されたLogEditTODOのデータを格納
      // todos: [{'id': 1, 'content': '牛乳を買う', 'limit_date': '2024-09-01', 'status': 0}, {'id': 2, 'content': '卵を買う', 'limit_date': '2024-10-15', 'status': 0}, {'id': 3, 'content': '砂糖を買う', 'limit_date': '2024-09-05', 'status': 1}, {'id': 4, 'content': '電気代の支払い', 'limit_date': '2024-09-03', 'status': 0}, {'id': 5, 'content': '大根を買う', 'limit_date': '2024-09-03', 'status': 0}, {'id': 6, 'content': 'キッチンペーパー', 'limit_date': '2024-08-20', 'status': 0}], // データベースから取得したタスク
      todos: [],
      isOpen: false, // 折りたたみ状態を管理する
      
    };
  },
  computed: {
    allStatusTrue() {
      return this.todos.every(todo => todo.status === true);
    },
    allStatusFlase() {
      return this.todos.every(todo => todo.status === false);
    }
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen; // 折りたたみ状態を切り替える
    },
    openEditModal(todo) {
      this.selectedEsitTodo = todo; // 選択されたTODOを設定
    },
    openDelModal(todo) {
      this.selectedDelTodo = todo; // 選択されたTODOを設定
    },
    openLogEditModal(todo) {
      console.log(todo);
      this.selectedLogEditTodo = todo; // 選択されたTODOを設定
    },
    isOverdue(limitDate) {
      const today = new Date().toISOString().split('T')[0]; // 今日の日付をYYYY-MM-DD形式で取得 登録時の時間の初期値として使用
      return limitDate < today;
    },
    list_get(){
      axios.get('http://127.0.0.1:5000/get_list')
      .then(response  => {
        this.todos = response.data; // 取得したデータをtodosに設定
      });
    },
    handleChange(event) {
      // チェックボックスの状態を取得
      if (event.target.checked) {
        this.chenge_status();
      }
    },
    completion(id){
      const req = JSON.stringify({
        id: id,
      });
      this.axios
      .post('http://127.0.0.1:5000/completion', req)
    }

  },
  mounted() {
    this.list_get(); // コンポーネントがマウントされたらタスクを取得
  }
};
</script>




<style>
.list-header {
  background-color: #f0f0f0;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.list-content {
  background-color: #e0e0e0;
  padding: 10px;
  margin-top: 5px;
  border-radius: 5px;
}

.overdue {
  color: red;
  font-weight: bold;
}
</style>
