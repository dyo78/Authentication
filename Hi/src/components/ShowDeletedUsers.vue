<template>
  <div>
    <h3>Soft deleted Users</h3>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in deletedUser" :key="user.id">
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.phone }}</td>
          <td><button @click="restoreUser(user.id)">Restore</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {toast} from 'vue3-toastify'; 
import 'vue3-toastify/dist/index.css'
import axios from 'axios';

export default {
 
  data() {
    return {
      deletedUser: [],
    };
  },
  created() {
    this.fetchDeletedUser();
  },
  methods: {
    fetchDeletedUser() {
      axios.get('http://127.0.0.1:8000/myapp/deletedusers/')
        .then(response => {
          this.deletedUser = response.data;
        })
        .catch(error => {
          toast.error('Error loading user');

        });
    },
    restoreUser(userId) {
      axios.put(`http://127.0.0.1:8000/myapp/restore/${userId}/`)
        .then(response => {
          if (response.status === 200) {
            this.deletedUser = this.deletedUser.filter(user => user.id !== userId);
            toast.success('User restored');
          }
        })
        .catch(error => {
          toast.error('Error restoring user');
        });
    }
  }
};
</script>

<style scoped>
template{
  background-color: #fff;

}
h3 {
  text-align: center;
  margin-top: 20px;
    background-color: #fff;

}
.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #4a7c59;
  background-color: #fff;
}

.table th,
.table td {
  padding: 8px;
  border-bottom: 1px solid #4a7c59;
;
  text-align: left;
}

.table th {
  background-color: #4a7c59;
  color: #eeffdb;
}

.table button {
  background-color: #4a7c59;
  color: #eeffdb;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.table button:hover {
  background-color: #070707;
}
</style>
