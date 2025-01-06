<template>
  <div id="app">
    <h1>心情札記</h1>
    <AddArticle @article-added="fetchArticles" />
    <ArticleGrid :articles="articles" />
  </div>
</template>

<script>
import axios from 'axios';
import ArticleGrid from './components/ArticleGrid.vue';
import AddArticle from './components/AddArticle.vue';

export default {
  data() {
    return {
      articles: []
    };
  },
  components: {
    ArticleGrid,
    AddArticle
  },
  methods: {
    async fetchArticles() {
      const response = await axios.get('http://localhost:5000/api/articles');
      this.articles = response.data;
    }
  },
  created() {
    this.fetchArticles();
  }
};
</script>
