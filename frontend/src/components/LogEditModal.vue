<template>
  <div class="modal-bg">
    <div class="modal">
      <h2>～履歴の編集～</h2>
      <h3>締切日</h3>
      <!-- 締切日の初期値を設定 -->
      <input id="date" type="date" v-model="limit_date">
      <!-- テキストの初期値を設定 -->
      <h3>TODO内容</h3>
      <input id="content" type="text" v-model="content">
      <p>
        <button @click="openLogRelodeModal(limit_date, content, id)" :disabled="!limit_date || !content">
          実行
        </button>
        <button @click="$emit('close');">
          戻る
        </button>
      </p>
      <!-- selectedRelodeTodoが設定されたときにRelodeModalを表示 -->
      <RelodeModal   
        v-if="selectedRelodeTodo" 
        v-on:log_edit_success="recieve_log_edit_success"
        :todo="selectedRelodeTodo"
        @close="selectedRelodeTodo = null"
      ></RelodeModal>
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
      message: null,
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
    /**
     * LogRelodeModal(履歴の更新確認ダイアログ)を表示する
     * @param limit_date 
     * @param content 
     * @param id 
     */
    openLogRelodeModal(limit_date, content, id) {
      console.log("Logedit");
      const todo = {
        content: content,
        limit_date: limit_date,
        id: id, 
      };
      this.selectedRelodeTodo = todo; // クリックされたTODOを選択
    },

    /**
     * LogRelodeModalから受け取ったメッセージｗを親コンポーネントに渡す
     * @param value 子コンポーネントから受け取ったメッセージ
     */
    async recieve_log_edit_success(value) {
      this.$emit('log_edit_success', value);
    },

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

input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  margin-bottom: 15px;
  box-sizing: border-box; /* パディングとボーダーを幅に含める */
}

#date{
  font-family:'Roboto', sans-serif;
  font: size 20px;
  text-align: center;
}
#content {
    text-align: center; /* テキストとプレースホルダーを中央揃え */
    font-family: 'Arial', sans-serif;
    font-size: 16px;
}
</style>
