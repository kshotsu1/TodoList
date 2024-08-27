<script>
import { ref } from 'vue';
import EditModal from './components/EditModal.vue'; 
import LogEditModal from './components/LogEditModal.vue'; 
import AddModal from './components/AddModal.vue'; 
import DeleteModal from './components/DeleteModal.vue'; 

const todo_data = ref([
  {
    id: 1,
    content: '牛乳を買う',
    status: true,
    limit: '2024/09/31',
    insertdate: '2024/08/31'
  },
  {
    id: 2,
    content: '砂糖を買う',
    status: true,
    limit: '2024/09/31',
    insertdate: '2024/08/31'
  },
  {
    id: 3,
    content: '卵を買う',
    status: true,
    limit: '2024/09/31',
    insertdate: '2024/08/31'
  }
]);

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
      todos: todo_data,
      isOpen: false // 折りたたみ状態を管理する
    };
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen; // 折りたたみ状態を切り替える
    }
  }
};
</script>


<template>
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
      <p v-if="allStatusTrue">すべてのタスクが完了しました！</p>
        
      <tr v-for="todo in todos" :key="todo.id">
        <template v-if="!todo.status">
          <th><input type="checkbox"></th>
          <th>{{ todo.limit }}</th>
          <th>{{ todo.content }}</th>
          <th> 
            <!-- 編集モーダルを開くボタン -->
            <button  type="button" @click="showEditModal = true">編集</button> 
            <EditModal v-if="showEditModal" @close="showEditModal = false"></EditModal>
          </th>
          <th> 
            <!-- 削除ダイアログを開くボタン -->
            <button  type="button" @click="showDeleteModal = true">削除</button> 
            <DeleteModal v-if="showDeleteModal" @close="showDeleteModal = false"></DeleteModal>
          </th>
        </template>
      </tr>
    </tbody>
  </table>
  <!-- 登録モーダルを開くボタン -->
  <button  type="button" @click="showAddModal = true">登録</button> 
  <AddModal v-if="showAddModal" @close="showAddModal = false"></AddModal>
  

 <!-- 履歴のアコーディオンメニュー -->
  <div @click="toggle()" class="list-header">
    <h2>DONE</h2>
    <span>{{ isOpen ? '▲' : '▼' }}</span> <!-- 折りたたみ状態を表示 -->
  </div>
  <div v-if="isOpen" class="list-content">
    <tr v-for="todo in todos" :key="todo.id">
      <template v-if="todo.status">
        <th><input type="checkbox"></th>
        <th>{{ todo.limit }}</th>
        <th>{{ todo.content }}</th>
        <th> 
          <!-- 編集モーダルを開くボタン -->
          <button  type="button" @click="showLogEditModal = true">編集</button> 
          <LogEditModal v-if="showLogEditModal" @close="showLogEditModal = false"></LogEditModal>
        </th>
        <th> 
          <!-- 削除ダイアログを開くボタン -->
          <button  type="button" @click="showDeleteModal = true">削除</button> 
          <DeleteModal v-if="showDeleteModal" @close="showDeleteModal = false"></DeleteModal>
        </th>
      </template>
    </tr>
  </div>



</template>

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
</style>
