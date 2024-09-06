<template>
  <div class="modal-bg">
    <div class="modal">
      <h2>～タスクの登録～</h2>
      <h3>締切日</h3>
      <input id="date" v-model="limit_date" type="date" placeholder="締切日を入力してください">
      <h3>TODO内容 ({{ content.length }}/50)</h3>
      <input id="content" v-model="content" type="text" placeholder="50文字以内で入力してください" maxlength="50">
      <p>
        <button @click="insert"  :disabled="!limit_date || !content">
          <!-- <img src="../assets/add.png" alt="追加" style="width: 24px; height: 24px;">-->
          追加
        </button>
        <button @click="$emit('close');">
          戻る
        </button>
      </p>
    </div>
  </div>
</template>
  
<script>
export default {
  data: () => ({
    limit_date: null,
    content: '',
    message: null,
  }),

  methods: {
    async insert(){
      if (!this.limit_date || !this.content) {
        return; // 日付またはTODO内容が未入力の場合
      }
      this.message = null;// 通信成功メッセージをリセット
      try{
        const req = JSON.stringify({limit_date: this.limit_date, content: this.content,});
        const response = await this.axios.post(`http://127.0.0.1:5000/insert`, req);
        this.$emit('insert_success', response.data.message);
        setTimeout(function() {
          window.location.reload();
        }, 1000); // 1秒 
        this.$emit('close'); // 'close' イベントを発火
      } catch (error) {
        console.error('編集エラー:', error);
      }
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
  font: size 16px;
  text-align: center;
}
#content {
    text-align: center; /* テキストとプレースホルダーを中央揃え */
    font-family: 'Arial', sans-serif;
    font-size: 16px;
}
</style>