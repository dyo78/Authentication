<template>
     <div class="navbar m-0 p-0 bg-white overflow-hidden flex justify-center" >
        <router-link to="/createblog" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-pink-800  hover:text-lg">Create Blog</router-link>
        <router-link to="/showblog" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-pink-800  hover:text-lg">Blog</router-link>
        <router-link to="/login" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-pink-800  hover:text-lg">Login</router-link>
        <router-link to="/" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-pink-800  hover:text-lg">Signup</router-link>
        <router-link to="/logout" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-pink-800  hover:text-lg" @click.prevent="logout">Logout</router-link> 



    </div>
</template>

<script>

export default {
methods:{
    logout(){

    localStorage.removeItem('access_token');
    this.$router.push({ name: 'login' });

}}



}
</script>
