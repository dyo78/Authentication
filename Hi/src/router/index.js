import { createRouter, createWebHashHistory } from 'vue-router';
import RegistrationForm from '../components/RegistrationForm.vue';
import UserTable from '../components/UserTable.vue';
import ShowDeletedUsers from '../components/ShowDeletedUsers.vue';
import Login from '../components/Login.vue';

const routes = [


  {
    path: '/',
    name: 'registrationForm',
    component: RegistrationForm
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/table',
    name: 'userTable',
    component: UserTable
  },
  {
    path: '/edit/:userId',
    name: 'editUser',
    component: RegistrationForm
  },
  {
    path: '/deleted-users',
    name: 'showDeletedUsers',
    component: ShowDeletedUsers
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
