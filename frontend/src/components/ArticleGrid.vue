<template>
    <b-container fluid>
      <b-row>
        <b-col
          v-for="article in articles"
          :key="article.id"
          cols="12"
          md="6"
          lg="4"
          class="mb-4"
        >
          <b-card
            :title="article.title"
            img-src="article.thumbnail"
            img-alt="Article Image"
            img-top
          >
            <b-card-text>
              {{ article.content.substring(0, 100) }}...
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script>
  export default {
    props: ['articles']
  };
  </script>
  
  <style scoped>
  .card-img-top {
    max-height: 200px;
    object-fit: cover;
  }
  </style>
  