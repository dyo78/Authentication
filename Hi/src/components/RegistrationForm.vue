<template>
  
  <div class="main min-h-screen flex justify-center items-center">
    <div class="bg-white p-8 max-w-md rounded-3xl border-2 border-black	">
      <form  @submit.prevent="submitForm">
        <div class="mb-4">
          <label class="block text-black text-sm font-bold mb-2" for="name">Name</label>
          <input type="text" v-model="info.name" id="name" class=" border-black	 rounded w-full py-2 px-3 text-black  border-2" />
        </div>

        <div class="mb-4">
          <label class="block text-black text-sm font-bold mb-2" for="email">Email</label>
          <input type="email" v-model="info.email" id="email" class=" border-black	 rounded w-full py-2 px-3 text-black border-2 " />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
          <input type="password" v-model="info.password" id="password" class=" border-black	 rounded w-full py-2 px-3 text-black border-2" />
        </div>

        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="phone">Phone</label>
          <input type="tel" v-model="info.phone" id="phone" class=" border-black	 rounded w-full py-2 px-3 text-black border-2"/>
        </div>

        <div class="flex items-center justify-center">
          <button type="submit" class=" bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {toast} from 'vue3-toastify'; 
import 'vue3-toastify/dist/index.css'
import axios from 'axios';

export default {
  data() {
    return {
      info: {
        id: null,
        name: '',
        email: '',
        password:'',
        phone: ''
      }
    };
  },
  methods: {
    submitForm() {
      if (!this.info.name || !this.info.email || !this.info.phone) {
        toast.error('Please fill out the form');
        return;
      }
      
      axios.post('http://127.0.0.1:8000/myapp/user/', this.info)
        .then(response => {
          if (response.status === 201) {
            this.clearForm();
            toast.success('Form submitted successfully');
          }
        })
        .catch(error => {
          toast.error('Error submitting form');
        });
    },
    clearForm() {
      this.info = { id: null, name: '', email: '', password:'',phone: '' };
    }
  }
};
</script>
<!-- 
<style scoped>
.background-container{
background-color: #407450;}


.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #fff;
  
}

form {
  padding: 30px;
  border-radius: 15px;
  background-color: #fff;
  max-width: 400px;
  width: 100%;
  border: 1px solid #4a7c59;border-radius: 47px;
  background: #fff;
  box-shadow:  22px 22px 44px #bebebe,
               -22px -22px 44px #ffffff;
    }

label {
  font-size: 16px;
  color: #070707;
  margin-bottom: 8px;
  display: block;
}

input {
  padding: 12px;
  border-radius: 8px;
  border: 1px solid  #4a7c59;
  width: calc(100% - 24px);
  font-size: 16px;
  margin-bottom: 16px;
  color: #070707;
}

button {
  background-color: #4a7c59;
  color: #fff;
  padding: 15px;
  border-radius: 8px;
  border: none;
  width: 100%;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #070707;
}
</style> -->
<!-- <style>
main{
  background-image: "./assets/bg.jpeg";
}

</style> -->