<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <label>Name</label>
      <input type="text" v-model="info.name" required /><br>

      <label>Email</label>
      <input type="email" v-model="info.email" required /><br>

      <label>Phone</label>
      <input type="tel" v-model="info.phone" /><br>

      <button type="submit">{{ submitButtonText }}</button>
    </form>
  </div>
  <div class="table">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in Record" :key="user.id">
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.phone }}</td>
          <td>
            <button @click="editUser(user)">Edit</button>
            <button @click="deleteUser(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: {
        id: null,
        name: '',
        email: '',
        phone: ''
      },
      Record: [],
      errorMessage: ''
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/myapp/user/');
        if (!response.ok) throw new Error('Network response was not ok');
        
        this.Record = await response.json();
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async submitForm() {
      const url = this.info.id ? `http://127.0.0.1:8000/myapp/user/${this.info.id}/` : 'http://127.0.0.1:8000/myapp/user/';
      const method = this.info.id ? 'PUT' : 'POST';

      try { 
        const response = await fetch(url, {
          method: method,
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.info)
        });

        if (!response.ok) throw new Error('Network response was not ok');
        
        const newData = await response.json();
        if (method === 'POST') {
          this.Record.push(newData);
        } else {
          const index = this.Record.findIndex(user => user.id === newData.id);
          if (index !== -1) this.Record.splice(index, 1, newData);
        }

        this.clearForm();
        this.$toast.open('Success: Data saved successfully!');
      } catch (error) {
        console.error('Error:', error);
        this.errorMessage = 'Error: ' + error.message;
      }
    },
    editUser(user) {
      this.info.id = user.id;
      this.info.name = user.name;
      this.info.email = user.email;
      this.info.phone = user.phone;
    },
    async deleteUser(userId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/myapp/user/${userId}/`, {
          method: 'DELETE'
        });

        if (!response.ok) throw new Error('Network response was not ok');
        
        this.Record = this.Record.filter(user => user.id !== userId);
        this.clearForm();
        this.$toast.open('Success: User deleted successfully!');
      } catch (error) {
        console.error('Error:', error);
        this.errorMessage = 'Error: ' + error.message;
      }
    },
    clearForm() {
      this.info = { id: null, name: '', email: '', phone: '' };
    }
  },
  computed: {
    submitButtonText() {
      return this.info.id ? 'Update' : 'Submit';
    }
  }
}
</script>

<style scoped>
/* Add your CSS styles here */
</style>
