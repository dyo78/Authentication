<template>
  <div>
    <div class="form-container">
      <form @submit.prevent="submitForm">
        <!-- Step 1: Name -->
        <div v-if="currentStep === 1">
          <label>Name</label>
          <input type="text" v-model="info.name" />
        </div>
        <!-- Step 2: Email -->
        <div v-if="currentStep === 2">
          <label>Email</label>
          <input type="email" v-model="info.email" />
        </div>
        <!-- Step 3: Phone -->
        <div v-if="currentStep === 3">
          <label>Phone</label>
          <input type="tel" v-model="info.phone" />
        </div>
        <!-- Step 4: Submit Button -->
        <div v-if="currentStep === 4">
          <button type="submit">Submit</button>
        </div>
        <!-- Step Navigation Buttons -->
        <div class="step-navigation">
          <button v-if="currentStep > 1" @click="prevStep">Previous</button>
          <button v-if="currentStep < 4" @click="nextStep">Next</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import axios from 'axios';

export default {
  data() {
    return {
      info: {
        id: null,
        name: '',
        email: '',
        phone: ''
      },
      currentStep: 1 // Step 1 is the initial step
    };
  },
  methods: {
    async submitForm() {
      // if (!this.info.name && !this.info.email && !this.info.phone) {
      //   toast.error('Please Fill form correctly');
      //   return;
      // }

      try {
        const response = await axios.post('http://127.0.0.1:8000/myapp/user/', this.info);
        if (response.status === 201) {
          this.clearForm();
          toast.success('User created successfully');
        
        }
        } catch (error) {
       

     
      }
    },
    prevStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
      }
    },
    nextStep() {
      if (this.currentStep < 4) {
        this.currentStep++;
      }
    },
    clearForm() {
      this.info = { id: null, name: '', email: '', phone: '' };
      this.currentStep = 1; // Reset step to initial step after submission
    }
  }
};
</script>


<style scoped>
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
  box-shadow: 0px 0px 5px #4a7c59;
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
  margin-bottom: 10px;
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
</style>
