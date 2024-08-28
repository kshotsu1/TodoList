<template>
  <div class="modal-bg">
    <div class="modal">
      <p>タスクの登録</p>
      <p>締切日</p>
      <input name="date" type="date" />
      <p>TODO内容</p>
      <input type="text" />
      <p>
        <button>登録</button>
        <button @click="closeModal">閉じる</button>
      </p>
    </div>
  </div>
</template>
  
<script>
export default {
  methods: {
    closeModal() {
      this.$emit('close'); // 親コンポーネントにモーダルを閉じるイベントを送信
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