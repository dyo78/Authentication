<template>
     <div class="navbar m-0 p-0 bg-white overflow-hidden flex justify-center" >
        <router-link to="/login" class="nav-link block text-blue  px-4 m-3  duration-100  hover:text-black  hover:text-lg hover:bg-pink-200"  > Login</router-link>
        <router-link to="/" class="nav-link block text-blue  px-4 m-3 duration-300  hover:text-amber-800  hover:text-lg">Create Form</router-link>
        <router-link to="/table" class="nav-link block text-blue  px-4 m-3  duration-300  hover:text-amber-800  hover:text-lg">Table</router-link>
        <router-link to="/deleted-users" class="nav-link block text-blue  px-4 m-3  duration-300  hover:text-green-800  hover:text-lg">Deleted Users</router-link>

    </div>
</template>

<script>
import { routeLocationKey } from 'vue-router';

export default {
}
</script>
<!-- 
<style scoped>
/* Add your CSS styles here */
.navbar {
    margin:0;
    padding:0;
    background-color: #fff;
    overflow: hidden;
    display: flex;
    justify-content: center;
}

.nav-link {
    display: block;
    color: #4a7c59;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    margin: 0 10px;
    border-radius: 8px;
    transition: background-color 0.3s;
}

.nav-link:hover {
    background-color: #4a7c59;
    color: #eeffdb;
}
</style> -->
