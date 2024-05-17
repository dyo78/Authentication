<template>
 
  <h3>User Table</h3>

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
            <button @click="editUserClicked(user)">Edit</button>
            <button @click="deleteUserClicked(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Modal overlay -->
  <div class="modal-overlay" v-if="editUserId !== null">
    <!-- Modal content -->
    <div class="modal">
      <span class="close" @click="cancelEdit">&times;</span>
      <h2>Edit User</h2>
      <form @submit.prevent="saveChanges">
        <label>Name</label>
        <input type="text" v-model="editUserForm.name" />
        
        <label>Email</label>
        <input type="email" v-model="editUserForm.email" />
        
        <label>Phone</label>
        <input type="tel" v-model="editUserForm.phone" />
        
        <div class="btn-group">
          <button type="button" @click="cancelEdit">Cancel</button>
          <button type="submit">Save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { toast } from 'vue3-toastify'; 
import 'vue3-toastify/dist/index.css'
import axios from 'axios';

export default {
  data() {
    return {
      Record: [],
      editUserId: null,
      editUserForm: {
        id: null,
        name: '',
        email: '',
        phone: ''
      }
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:8000/myapp/user/')
        .then(response => {
          this.Record = response.data;
        })
        .catch(error => {
          toast.error('unable to load datas');
        });
    },
    editUserClicked(user) {
      this.editUserId = user.id;
      this.editUserForm = { ...user };
    },
    saveChanges() {
      axios.put(`http://127.0.0.1:8000/myapp/user/${this.editUserForm.id}/`, this.editUserForm)
        .then(response => {
          if (response.status === 200) {
            const index = this.Record.findIndex(user => user.id === this.editUserForm.id);
            if (index !== -1) {
              this.Record.splice(index, 1, this.editUserForm);
              toast.success('Updated user');
            }
          }
        })
        .catch(error => {
          toast.error('unable to update');
        })
        .finally(() => {
          this.cancelEdit();
        });
    },
    cancelEdit() {
      this.editUserId = null;
      this.editUserForm = {
        id: null,
        name: '',
        email: '',
        phone: ''
      };
    },
    deleteUserClicked(userId) {
      axios.delete(`http://127.0.0.1:8000/myapp/user/${userId}/`)
      .then(response => {
          if (response.status === 204) {
            this.Record = this.Record.filter(user => user.id !== userId);
            toast.success('user deleted');
          }
        })
        .catch(error => {
          toast.error('unable to delete');
        });
    }
  }
}
</script>

<style scoped>
h3 {
  text-align: center;
  margin-top: 20px;
  background-color: #fff;
}

.table {
  margin-top: 20px;
  border:1px solid #4a7c59;
  background-color: #fff;
  width: 100%;
}

.table table {
  width: 100%;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: 8px;
  border-bottom: 1px solid #4a7c59;
  text-align: left;
}

.table th {
  background-color: #4a7c59;
  color: #fff;
}

.table button {
  margin-right: 5px;
  background-color: #4a7c59;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.table button:hover {
  background-color: #070707;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3); /* Shadow */
  position: relative;
  width: 400px;
}

.close {
  position: absolute;
  top: 5px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}

form {
  margin-top: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #4a7c4a;
  border-radius: 4px;
}

.btn-group {
  text-align: right;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #4a7c59;
  color: #fff;
  cursor: pointer;
}

button[type="button"] {
  background-color: #4a7c59;
  margin-right: 10px;
}

button[type="submit"] {
  background-color: #4a7c59;
}

button:hover {
  background-color: #070707;
}
</style>
