<template>
  <div class="modal-bg">
    <div class="modal">
      <h2>～タスクの編集～</h2>
      <h3>締切日</h3>
      <!-- 締切日の初期値を設定 -->
      <input id="date" type="date" v-model="limit_date">
      <!-- テキストの初期値を設定 -->
      <h3>TODO内容</h3>
      <input id="content" type="text" v-model="content">
      <p>
        <button @click="edit()" :disabled="!limit_date || !content">
          実行
        </button>
        <button @click="$emit('close')">
          戻る
        </button>
      </p>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
export default {
  data() {
    return {
      content: this.todo.content, // テキストの初期値として todo.content を設定
      limit_date: this.formatDate(this.todo.limit_date), // 日付の初期値として todo.limit を設定
      id: this.todo.id
    };
  },
  methods: {
    formatDate(dateString) {
      // 日付が 'YYYY-MM-DD' 形式であることを確認するための補助関数
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth()+1).padStart(2, '0'); // 月は 0-based なので +1
      const day = String(date.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    async edit(){
      console.log("edit");
      const req =  JSON.stringify({ id: this.todo.id, limit_date: this.limit_date, content: this.content });
      const response = await this.axios.post(`http://127.0.0.1:5000/edit`, req);
      await axios.get('http://127.0.0.1:5000/get_list');
      this.$emit('edit_success', response.data.message);
      this.$emit('close'); // 'close' イベントを発火
      
    }
  },
  props: ['todo']
};
</script>


<style>
.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #ffffff; /* 背景色を白に */
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal { /* モーダル内の背景設定 */
  background: #ffffff; /* 背景色を白に */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 軽い影を追加 */
  max-width: 600px; /* モーダルの幅を設定 */
  width: 90%; /* モーダルの幅を90%に設定 */
  box-sizing: border-box; /* パディングとボーダーを幅に含める */
}

.modal p {
  margin: 10px 0;
  color: #000000; /* 文字色を黒に */
}

input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  margin-bottom: 15px;
  box-sizing: border-box; /* パディングとボーダーを幅に含める */
}

button {
  background-color: #007bff;
  color: #ffffff; /* ボタンの文字色を白に */
  border: none;
  border-radius: 6px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  margin-right: 10px;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
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