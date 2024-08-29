<template>
  <div class="modal-bg">
    <div class="modal">
      <p>タスクの登録</p>
      <p>締切日</p>
      <input 
        id="date" 
        v-model="limit"
        type="date"
        placeholder="締切日を入力してください"
        >
      <p>TODO内容</p>
      <input 
        id="content" 
        v-model="content "
        type="text"
        placeholder="TODO内容を入力してください"
        >
      <p>
        <button @click="insert" :disabled="!limit || !content">登録</button>
        <button @click="closeModal">閉じる</button>
      </p>
    </div>
  </div>
</template>
  
<script>
export default {
  data: () => ({
    limit: null,
    content: null,
    success: null,
  }),

  methods: {
    closeModal() {
      this.$emit('close'); // 親コンポーネントにモーダルを閉じるイベントを送信
    },
    insert(){
      if (!this.limit || !this.content) {
        return; // 日付またはTODO内容が未入力の場合
      }

      this.success = null;// 通信成功メッセージをリセット

      const req = JSON.stringify({
        limit: this.limit,
        content: this.content,
      });

      this.axios
        .post(`http://127.0.0.1:5000/insert`, req)
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