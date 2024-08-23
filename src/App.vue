<script>
import EditModal from './components/EditModal.vue'; // モーダルコンポーネントのインポート
import AddModal from './components/AddModal.vue'; // モーダルコンポーネントのインポート
import DeleteModal from './components/DeleteModal.vue'; // モーダルコンポーネントのインポート

export default {
  components: {
    EditModal, 
    AddModal,
    DeleteModal
  },
  data() {
    return {
      showEditModal: false,
      showAddModal: false,
      showDeleteModal: false
    };
  }
};
</script>


<template>
<h1>TODO List</h1>
  <table>
    <tr>
      <th>完了</th>
      <th>期限</th>
      <th>TODO内容</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th><input type="checkbox"></th>
      <th>2024/08/31</th>
      <th>牛乳を買う</th>
      <th> 
        <!-- 編集モーダルを開くボタン -->
        <button  type="button" @click="showEditModal = true">編集</button> 
        <EditModal v-if="showEditModal" @close="showEditModal = false"></EditModal>
      </th>
      <th> 
        <!-- 削除ダイアログを開くボタン -->
        <button  type="button" @click="showDeleteModal = true">削除</button> 
        <DeleteModal v-if="showDeleteModal" @close="showDeleteModal = false"></DeleteModal>
      </th>
    </tr>
  </table>
  <!-- 登録モーダルを開くボタン -->
  <button  type="button" @click="showAddModal = true">登録</button> 
  <AddModal v-if="showAddModal" @close="showAddModal = false"></AddModal>
</template>

<style>

</style>
