<template>
    <div class="main min-h-screen flex justify-center items-center bg-pink-50">
      <div class="container flex flex-col bg-gray-100 rounded-3xl shadow-lg p-8">
        <h1 class="text-3xl font-bold mb-8">My Blog Posts</h1>
        <div v-if="loading" class="text-center text-xl">Loading...</div>
        <div v-else>
          <div v-for="post in userPosts" :key="post.id" class="blog-post mb-4 p-4 border-2 border-pink-800 rounded">
            <h2 class="text-2xl font-semibold mb-2">{{ post.title }}</h2>
            <p class="text-gray-700 mb-4">{{ post.desc }}</p>
            <p class="text-sm text-gray-600"><strong>Author:</strong> {{ post.author }}</p>
            <p class="text-sm text-gray-600"><strong>Created At:</strong> {{ new Date(post.created_at).toLocaleString() }}</p>
            <p class="text-sm text-gray-600"><strong>Edited At:</strong> {{ new Date(post.edited_at).toLocaleString() }}</p>
            <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="toggleEdit(post)">Edit</button>
            <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="deletePost(post.id)">Delete</button>
            <div v-if="post.editing">
              <form @submit.prevent="saveEdit(post)">
                <label for="title" class="block text-black text-sm font-bold mb-2"><b>Title</b></label>

                <input type="text" v-model="post.updatedTitle" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2">
                <label for="desc" class="block text-black text-sm font-bold mb-2"><b>Description</b></label>

                <textarea v-model="post.updatedDesc" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2"></textarea>
                <button type="submit" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Save</button>
              </form>
            </div>
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
    computed: {
      userPosts() {
        return this.posts;
      }
    },
    async mounted() {
      await this.fetchPosts();
    },
    methods: {
      async fetchPosts() {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No token found');
          this.loading = false;
          return;
        }
        
        console.log('Token found:', token);  
  
        try {
          const response = await axios.get('http://localhost:8000/blog/my-blogs/', {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          this.posts = response.data.map(post => ({
            ...post,
            editing: false,
            updatedTitle: post.title,
            updatedDesc: post.desc
          }));
        } catch (error) {
          console.error('Error fetching posts:', error.response ? error.response.data : error.message);
        } finally {
          this.loading = false;
        }
      },
      toggleEdit(post) {
        post.editing = !post.editing;
      },
      async saveEdit(post) {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No token found');
          return;
        }
  
        try {
          const response = await axios.patch(`http://localhost:8000/blog/my-blogs/${post.id}/`, {
            title: post.updatedTitle,
            desc: post.updatedDesc
          }, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          console.log('Post updated:', response.data);
          // Update the post in the list with the edited values
          const updatedPostIndex = this.posts.findIndex(p => p.id === post.id);
          if (updatedPostIndex !== -1) {
            this.posts[updatedPostIndex] = {
              ...this.posts[updatedPostIndex],
              ...response.data,
              editing: false
            };
          }
        } catch (error) {
          console.error('Error updating post:', error.response ? error.response.data : error.message);
        }
      },
      async deletePost(postId) {
        const token = localStorage.getItem('access_token');
        if (!token) {
          console.error('No token found');
          return;
        }
  
        try {
          const response = await axios.delete(`http://localhost:8000/blog/my-blogs/${postId}/`, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          });
          console.log('Post deleted:', response.data);
          // Remove the deleted post from the list
          this.posts = this.posts.filter(post => post.id !== postId);
        } catch (error) {
          console.error('Error deleting post:', error.response ? error.response.data : error.message);
        }
      }
    }
  };
  </script>
  