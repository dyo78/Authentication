<template>
  <div class="main min-h-screen flex justify-center items-center bg-pink-50">
    <div class="container flex w-3/4 bg-gray-100 rounded-3xl shadow-lg">
      <div class="flex justify-center items-center w-1/2">
        <img src="../assets/pink.jpg" class="h-full object-cover rounded-2xl">
      </div>
      <form @submit.prevent="submit" class="w-1/2 flex flex-col justify-center items-center p-8">
        <div class="p-8 rounded-3xl w-full h-full flex flex-col justify-center">
          <h2 class="text-2xl font-bold mb-6 text-center">Welcome to Login</h2>
          <div class="mb-4">
            <label for="uname" class="block text-black text-sm font-bold mb-2"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2" v-model="login.email" required>
          </div>
          <div class="mb-4">
            <label for="psw" class="block text-black text-sm font-bold mb-2"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" class="rounded w-full py-2 px-3 text-black overflow-hidden focus:outline-none border-pink-800 border-2" v-model="login.password" required>
          </div>
          <div class="inline-flex items-center justify-center m-5">
            <button type="submit" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Login</button>
          </div>
          <div class="inline-flex items-center justify-center m-5">
            <button type="button" class="bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="signup">SignUp</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { toast } from 'vue3-toastify';
import axios from 'axios';

export default {
  data() {
    return {
      login: {
        email: '',
        password: ''
      }
    };
  },
  methods: {
    async submit() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/myapp/login/', this.login);
        
        // Assuming the response contains the tokens
        const { access_token, refresh_token } = response.data;
        
        // Store tokens in local storage
        localStorage.setItem('access_token', access_token);
        localStorage.setItem('refresh_token', refresh_token);
        

        
        // Redirect to the blog page
        this.$router.push({ name: 'blog' });
        toast.success("Login successful");
      } catch (error) {
        toast.error("Login failed");
      }
    },
    signup() {
      this.$router.push({ name: 'registrationForm' });
    }
  }
};
</script>

