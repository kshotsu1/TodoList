<template>
    <div class="modal-bg">
      <div class="modal">
        <div class="modal-content">
          <p>削除確認ダイアログ</p>
          <button @click="closeModal">ダイアログを閉じる</button>
        </div>
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
}


</style>