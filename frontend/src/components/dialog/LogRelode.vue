<template>
  <div class="modal-bg">
    <div class="modal">
      <button @click="$emit('close')">戻る</button>

      <p>以下のTODO内容で未完了リストに追加しますか？</p>
      <p>締切日</p>
      <p>{{ limit_date }}</p>
      <p>TODO内容</p>
      <p>{{ content }}</p>
      <p>
        <button @click="log_edit_add_list()">追加する</button>
        <button @click="log_only_update()">履歴のみ更新</button>
      </p>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    todo: {
      type: Object,
      required: true
    }
  },
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
    
    log_edit_add_list(){
      //履歴の追加ボタンが押されたときの処理
      const req = JSON.stringify({
        id: this.id,
        limit_date: this.limit_date,
        content: this.content
      });
      this.axios
        .post(`http://127.0.0.1:5000/log_edit_add_list`, req)
      this.$emit('close'); // 編集が完了したらモーダルを閉じる
      this.$emit('close'); // 編集が完了したらモーダルを閉じる
    },

    log_only_update(){
      // 履歴の更新ボタンが押されたときの処理
      const req = JSON.stringify({
        id: this.id,
        limit_date: this.limit_date,
        content: this.content
      });
      this.axios
        .post(`http://127.0.0.1:5000/edit`, req)
      this.$emit('close'); // 編集が完了したらモーダルを閉じる
      this.$emit('close'); // 編集が完了したらモーダルを閉じる
    }
  }
  };
  
  // console.log(this.todo)
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