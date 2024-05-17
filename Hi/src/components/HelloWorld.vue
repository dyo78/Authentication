<template>
  <div>
    <form >
     <div v-if="currentStep===1">
      <label>Username</label>
      <input type="text" v-model="info.uname">
    </div>
    <div v-if="currentStep===2">
      <label>Email</label>
      <input type="email" v-model="info.email">
     </div>
     <div v-if="currentStep===3">
      <label>Phone</label>
      <input type="tel" v-model="info.phone">
      </div>
      <div v-if="currentStep===4">
      <button >
        Submit
      </button>
      </div>

      <div class="stepnav">
        <button v-if="currentStep>1" @click="prev">Prev</button>
        <button v-if="currentStep<4" @click="next">Next</button>

      </div>
    </form>
  </div>
</template>
<script>
export default{
 data(){
  return{
  info:{
    uname:'',
    email:'',
    phone:''
  },currentStep:1.
 } ;},
methods:{
 prev(){
 this.currentStep--;
}, 
next(){
 this.currentStep++;
}
}
};

</script>