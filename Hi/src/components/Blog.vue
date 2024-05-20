<template>
  <div class="main min-h-screen flex justify-center items-center bg-pink-50">
    <div class="container flex flex-col bg-gray-100 rounded-3xl shadow-lg p-8">
      <div class="mb-4 w-full">
        <label for="title" class="block text-black text-sm font-bold mb-2"><b>Title</b></label>
        <input v-model="title" type="text" placeholder="Title" name="title" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2" required>
      </div>
      <div class="mb-4 w-full">
        <label for="desc" class="block text-black text-sm font-bold mb-2"><b>Description</b></label>
        <textarea v-model="desc" placeholder="Description" name="desc" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2" required></textarea>
      </div>
      <div class="inline-flex items-center justify-center m-5 w-full">
        <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="addBlog">Add Blog</button>
      </div>
      <div class="inline-flex items-center justify-between m-5 w-full">
        <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="showAllBlogs">Show All Blogs</button>
        <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="showUserBlogs">Show My Blogs</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      desc: ''
    };
  },
  methods: {
    async addBlog() {
      const token = localStorage.getItem('refresh_token');
      console.log("Token from localStorage:", token);

      if (!token) {
        console.error('No token found');
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/blog/detail/', {
          title: this.title,
          desc: this.desc
        }, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        console.log('Blog added successfully', response.data);
        this.$router.push({ name: 'showblog' });

        this.title = '';
        this.desc = '';
      } catch (error) {
        if (error.response && error.response.status === 401) {
          console.error('Token expired or invalid, please login again');
        } else {
          console.error('Error adding blog:', error.response.data);
        }
      }
    },
    showAllBlogs() {
      this.$router.push({ name: 'showblog' });
    },
    showUserBlogs() {
      this.$router.push({ name: 'myprofile' });
    }
  }
};
</script>
