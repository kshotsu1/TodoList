<template>
  <div class="modal-bg">
    <div class="modal">
      <p>タスクの編集</p>
      <p>締切日</p>
      <p>{{ todo.limit }}</p>
      <!-- 締切日の初期値を設定 -->
      <input name="date" type="date" v-model="dateValue" />
      <p>{{ todo.content }}</p>
      <!-- テキストの初期値を設定 -->
      <input type="text" v-model="textValue" />
      <p>
        <button>編集</button>
        <button @click="$emit('close')">閉じる</button>
      </p>
    </div>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      textValue: 'こんにちは', // テキストの初期値
      dateValue: '2024-09-30' // 日付の初期値
    };
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