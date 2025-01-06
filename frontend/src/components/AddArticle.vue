<template>
    <b-container>
      <b-form @submit.prevent="addArticle">
        <b-form-group label="標題" label-for="title-input">
          <b-form-input
            id="title-input"
            v-model="title"
            placeholder="輸入文章標題"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-form-group label="內容" label-for="content-input">
          <b-form-textarea
            id="content-input"
            v-model="content"
            placeholder="輸入文章內容"
            rows="3"
            required
          ></b-form-textarea>
        </b-form-group>
  
        <b-form-group label="縮圖 URL" label-for="thumbnail-input">
          <b-form-input
            id="thumbnail-input"
            v-model="thumbnail"
            placeholder="輸入縮圖的 URL"
          ></b-form-input>
        </b-form-group>
  
        <b-button type="submit" variant="primary">提交文章</b-button>
      </b-form>
    </b-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        content: '',
        thumbnail: ''
      };
    },
    methods: {
      async addArticle() {
        const newArticle = {
          id: Date.now(),
          title: this.title,
          content: this.content,
          thumbnail: this.thumbnail
        };
        await axios.post('http://localhost:5000/api/articles', newArticle);
        this.$emit('article-added');
        this.title = '';
        this.content = '';
        this.thumbnail = '';
      }
    }
  };
  </script>