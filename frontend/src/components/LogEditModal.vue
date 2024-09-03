<template>
  <div class="modal-bg">
    <div class="modal">
      <p>履歴タスクの編集</p>
      <h3>締切日</h3>
      <!-- 締切日の初期値を設定 -->
      <p><input name="date" type="date" v-model="limit_date" /></p>
      <!-- テキストの初期値を設定 -->
      <h3>TODO内容</h3>
      <p><input type="text" v-model="content" /></p>
      <p>
        <button @click="openLogRelodeModal(limit_date, content, id)">
          <img src="../assets/edit.png" alt="編集" style="width: 24px; height: 24px;">
        </button>

        <!-- selectedRelodeTodoが設定されたときにRelodeModalを表示 -->
        <RelodeModal 
          v-if="selectedRelodeTodo" 
          :todo="selectedRelodeTodo"
          @close="selectedRelodeTodo = null"
        ></RelodeModal>
        <button @click="$emit('close');">
          <img src="../assets/back.png" alt="戻る" style="width: 24px; height: 24px;">
        </button>
      </p>
    </div>
  </div>
</template>

<script>
import RelodeModal from './dialog/LogRelode.vue'; 

export default {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },
  components: {
    RelodeModal
  },
  data() {
    return {
      showRelodeModal: false, // 編集モーダルの表示状態
      selectedRelodeTodo: null, // 編集するTODOを保持
      id: this.todo.id, // 初期値として todo.content を設定
      content: this.todo.content, // 初期値として todo.content を設定
      limit_date: this.formatDate(this.todo.limit_date), // 日付の初期値として todo.limit を設定
    };
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // 月は 0-based なので +1
      const day = String(date.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    openLogRelodeModal(limit_date, content, id) {
      // console.log("Logedit");
      const todo = {
        content: content,
        limit_date: limit_date,
        id: id,  // IDを自動生成する関数などを使う
      };
      this.selectedRelodeTodo = todo; // クリックされたTODOを選択
    }
  }
};
</script>
  
<style>
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

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  height: 600px;
  width: 1000px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
