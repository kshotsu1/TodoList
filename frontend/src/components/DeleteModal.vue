<template>
  <div class="modal-bg">
    <div class="modal">
      <p>以下のTODOを削除しますか？</p>
      <h3>締切日</h3>
      <p>{{ limit_date }}</p>
      <h3>TODO内容</h3>
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
    todo: {type: Object,required: true},
    onClickSubmit: {type: Function, default: null}
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
    async del() {
      console.log("delete");
      try {
        const req = { id: this.todo.id };
        await this.axios.post('http://127.0.0.1:5000/delete', req);
        window.location.reload();
        this.$emit('close'); // 'close' イベントを発火
      } catch (error) {
        console.error('削除エラー:', error);
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
  background: white;
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
