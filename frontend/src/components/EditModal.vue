<template>
  <div class="modal-bg">
    <div class="modal">
      <p>タスクの編集</p>
      <p>締切日</p>
      <!-- 締切日の初期値を設定 -->
      <p><input name="date" type="date" v-model="limit_date" /></p>
      <!-- テキストの初期値を設定 -->
      <p>TODO内容</p>
      <p><input type="text" v-model="content" /></p>
      <p>
        <button @click="edit()">編集</button>
        <button @click="$emit('close')">閉じる</button>
      </p>
    </div>
  </div>
</template>
  
<script>
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
    edit(){
      console.log("edit");
      // 編集ボタンが押されたときの処理
      const req = JSON.stringify({
        id: this.id,
        limit_date: this.limit_date,
        content: this.content
      });
      this.axios
        .post(`http://127.0.0.1:5000/edit`, req)
      this.$emit('close'); // 編集が完了したらモーダルを閉じる
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

  /* モーダル内のコンテンツを中央揃え */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}


</style>