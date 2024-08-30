<template>
  <div class="modal-bg">
    <div class="modal">
      <p>以下のTODOを削除しますか？</p>
      <p>締切日</p>
      <p>{{ limit_date }}</p>
      <p>TODO内容</p>
      <p>{{ content }}</p>
      <p>
        <button @click="del()">はい</button> 
        <button @click="$emit('close')">いいえ</button>
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
      content: this.todo.content, // 初期値として todo.content を設定
      limit_date: this.formatDate(this.todo.limit_date) // 初期値として todo.limit_date を設定
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
    del(){
      console.log("delete");
      // 削除ボタンが押されたときの処理
      const req = JSON.stringify({
        id: this.todo.id
      });
      this.axios
      .post(`http://127.0.0.1:5000/delete`, req)
      this.$emit('close');
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

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
}
</style>
