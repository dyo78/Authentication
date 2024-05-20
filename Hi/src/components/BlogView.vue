<template>
    <div class="main min-h-screen flex justify-center items-center bg-pink-50">
      <div class="container flex flex-col bg-gray-100 rounded-3xl shadow-lg p-8">
        <h1 class="text-3xl font-bold mb-8">Blog Posts</h1>
        <div v-if="loading" class="text-center text-xl">Loading...</div>
        <div v-else>
          <div v-for="post in posts" :key="post.id" class="blog-post mb-4 p-4 border-2 border-pink-800 rounded">
            <h2 class="text-2xl font-semibold mb-2">{{ post.title }}</h2>
            <p class="text-gray-700 mb-4">{{ post.desc }}</p>
            <p class="text-sm text-gray-600"><strong>Author:</strong> {{ post.author }}</p>
            <p class="text-sm text-gray-600"><strong>Created At:</strong> {{ new Date(post.created_at).toLocaleString() }}</p>
            <p class="text-sm text-gray-600"><strong>Edited At:</strong> {{ new Date(post.edited_at).toLocaleString() }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        posts: [],
        loading: true,
      };
    },
    mounted() {
      this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No token found');
          return;
        }
  
        try {
          const response = await axios.get('http://localhost:8000/blog/detail/', {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          this.posts = response.data;
        } catch (error) {
        } finally {
          this.loading = false;
        }
      }
    }
  };
  </script>
  