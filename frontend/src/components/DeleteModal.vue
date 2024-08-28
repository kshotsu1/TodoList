<template>
    <div class="modal-bg">
      <div class="modal">
        <p>以下のTODOを削除しますか？</p>
        <p>締切日</p>
        <p>YYYY/mm/dd</p>
        <p>TODO内容</p>
        <p>~~~~~~~~</p>
        <p>
          <button @click="closeModal">はい</button>
          <button @click="closeModal">いいえ</button>
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
}


</style>