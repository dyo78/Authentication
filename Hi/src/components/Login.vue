<template><div class="bg">
 
  <div class="main min-h-screen flex justify-center items-center">
    <!-- <div class=" flex justify-left h-">
      <img src="../assets/pink.jpg">
    </div> -->
<form @submit.prevent="submit">

  <div class="container  bg-white min-h-screen flex justify-center items-center">
    <div class="bg-white p-8 max-w-md rounded-3xl border-2 border-black	">
      <div class="mb-4">
    <label for="uname" class="block text-black text-sm font-bold mb-2 "><b>Email</b></label>
    <input type="email" placeholder="Enter Email" name="email" class=" border-black	 rounded w-full py-2 px-3 text-black border-2" v-model="login.email"required>
</div>  <div class="mb-4">
    <label for="psw" class="block text-black text-sm font-bold mb-2 "><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw"class=" border-black	 rounded w-full py-2 px-3 text-black border-2" v-model="login.password"required>
        </div>
        <div class=" inline-flex items-center justify-center m-5" >
          <button type="submit" class=" bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Login</button>
          </div>
          <div class="inline-flex items-center justify-center m-5">
            <button type="SignUp" class=" bg-pink-800 hover:bg-pink-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="signup">SignUp</button>
            </div>

          
  </div>

</div>
</form>
</div>
</div>

</template>
<script>
import {toast} from 'vue3-toastify';
import axios from 'axios';
export default {
  data() {
    return {
      login:{
      email: '',
      password: ''
      }
    };
  },
  methods: {
    submit() {
    axios.post('http://127.0.0.1:8000/myapp/login/', this.login)
    .then(response => {

      this.$router.push({ name: 'userTable' });
      toast.success("good")
    })
    .catch(error => {
      toast.error("bad");

    });
},
signup(){

  this.$router.push({ name: 'registrationForm' });

}
  }
};
</script>

<style>

</style>
