<template>

  <div id="app">
    <!-- <Navbar/> -->
    <router-view/>
  </div>

</template>


<script>
// import Navbar from './components/Navbar.vue'; 
import Step from './components/StepForm.vue'
import Hello from './components/HelloWorld.vue'
import hi from './components/Example.vue'
export default {
  name: 'App',
  components: {
    // Navbar,
    Step,
    Hello,
    hi,
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  
}
body{
  margin: 0;
  padding:0;
 
   

}
</style>
