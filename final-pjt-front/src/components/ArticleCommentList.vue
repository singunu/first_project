<template>
    <div>
      <h2 class="title">댓글 목록</h2>
      <ul class="comment-list">
        <li v-for="comment in filteredComments" :key="comment.id" class="comment">
          <div class="meta">{{ formatDate(comment.created_at) }}</div>
          <div class="content">작성자: {{ comment.user.username }}</div>
          <div class="content">{{ comment.content }}</div>
          <div v-if="comment.user.username === store.user.username" class="button-group">
            <button class="edit-button" @click="editComment(comment.id)">수정</button>
            <button class="delete-button" @click="deleteComment(comment.id)">삭제</button>
          </div>
        </li>
      </ul>
      <div v-if="editingComment" class="edit-form">
        <textarea v-model="editContent" placeholder="댓글을 입력하세요" class="comment-input"></textarea>
        <div class="button-group">
          <button class="update-button" @click="updateComment(editingComment)">저장</button>
          <button class="cancel-button" @click="cancelEdit">취소</button>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { useFinancialStore } from '@/stores/financial';
import { computed, ref } from 'vue';
import axios from 'axios';

const store = useFinancialStore();
const articleId = defineProps({
    articleId: Number
});

const filteredComments = computed(() => {
    return store.comments.filter(comment => comment.article === articleId.articleId);
});

const editingComment = ref(null);
const editContent = ref('');

const editComment = (commentId) => {
    const comment = store.comments.find(comment => comment.id === commentId);
    if (comment) {
        editingComment.value = comment;
        editContent.value = comment.content;
    }
};

const updateComment = async (comment) => {
    if (!comment) return;

    try {
        const response = await axios.put(`${store.API_URL}/articles/comments/${comment.id}/`, {
            content: editContent.value,
            article: comment.article // 기존의 article 값을 그대로 전송
        });
        // 댓글 업데이트 후 스토어의 댓글 목록 갱신
        const updatedComment = response.data;
        store.comments = store.comments.map(c =>
            c.id === updatedComment.id ? updatedComment : c
        );
        cancelEdit();
    } catch (error) {
        console.error('댓글 수정 중 오류 발생:', error);
    }
};

const cancelEdit = () => {
    editingComment.value = null;
    editContent.value = '';
};

const deleteComment = async (commentId) => {
    try {
        await axios.delete(`${store.API_URL}/articles/comments/${commentId}/`);
        // 삭제 성공 후 스토어의 댓글 목록 업데이트
        store.comments = store.comments.filter(comment => comment.id !== commentId);
    } catch (error) {
        console.error('댓글 삭제 중 오류 발생:', error);
    }
};

// 날짜 포맷팅 함수
const formatDate = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = (1 + date.getMonth()).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
};
</script>

<style scoped>
.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.comment-list {
  list-style-type: none;
  padding: 0;
}

.comment {
  margin-bottom: 20px;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 10px;
}

.meta {
  font-size: 12px;
  color: #888;
}

.content {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.button-group {
  display: flex;
}

button {
  margin-top: 10px;
  margin-right: 10px;
  padding: 8px 16px;
  font-size: 14px;
  border: 1px solid transparent; /* 투명한 테두리 */
  border-radius: 5px;
  cursor: pointer;
  transition: border-color 0.3s; /* 호버 시 테두리 색상 변화를 위한 트랜지션 */
}

.comment-input {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
  padding: 10px;
  font-size: 14px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.update-button,
.cancel-button {
  color: #4E5CBF; /* 버튼 글자 색상 */
  border-color: #4E5CBF; /* 테두리 색상 */
}

.update-button:hover,
.cancel-button:hover {
  border-color: #4E5CBF; /* 호버 시 테두리를 투명하게 변경 */
  transition: color 0.3s ease, border-color 0.3s ease;
}

.delete-button {
  color: #dc3545;
  border-color: #dc3545;
}

.delete-button:hover {
  border-color: #dc3545;
  transition: color 0.3s ease, border-color 0.3s ease;
}

.edit-button {
  color: #28a745;
  border-color: #28a745;
}

.edit-button:hover {
  border-color: #28a745; /* 호버 시 테두리를 투명하게 변경 */
  transition: color 0.3s ease, border-color 0.3s ease;
}

.update-button,
.cancel-button {
  background-color: transparent; /* 배경색 투명하게 */
}

.update-button:hover,
.cancel-button:hover {
  color: #000; /* 호버 시 글자 색상 변경 */
}

.update-button:hover,
.cancel-button:hover,
.edit-button:hover,
.delete-button:hover {
border-color: transparent; /* 호버 시 테두리를 투명하게 변경 */
transition: color 0.3s ease, border-color 0.3s ease;
}

.update-button:hover {
border-color: #4E5CBF; /* 저장 버튼의 테두리 색상 */
}

.cancel-button:hover {
border-color: #4E5CBF; /* 취소 버튼의 테두리 색상 */
}

.delete-button:hover {
border-color: #dc3545; /* 삭제 버튼의 테두리 색상 */
}

.edit-button:hover {
border-color: #28a745; /* 수정 버튼의 테두리 색상 */
}
</style>