import { createRouter, createWebHashHistory } from 'vue-router';
import RegistrationForm from '../components/RegistrationForm.vue';
import UserTable from '../components/UserTable.vue';
import ShowDeletedUsers from '../components/ShowDeletedUsers.vue';
import Login from '../components/Login.vue';
import Blog from '../components/Blog.vue';
import BlogView from '../components/BlogView.vue';
import myProfile from '../components/MyProfile.vue'
// import logout from '../components/Logout.vue'


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
    component: UserTable,
  
  },
  // {
  //   path: '/edit/:userId',
  //   name: 'editUser',
  //   component: RegistrationForm
  // },
  {
    path: '/deleted-users',
    name: 'showDeletedUsers',
    component: ShowDeletedUsers,
  
  },
  {
    path: '/showblog',
    name: 'showblog',
    component: BlogView,
  
  },
  {
    path: '/myprofile',
    name: 'myprofile',
    component: myProfile,
  
  },
  // {
  //   path: '/logout',
  //   name: 'logout',
  //   component: logout
  // },
  {
    path: '/createblog',
    name: 'blog',
    component: Blog,
  

  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

// router.beforeEach((to, from, next) => {
//   const token = localStorage.getItem('token');
//   if (to.path !== '/login'&& '!token') {
//     next('/createblog');
//   } else {
//     next();
//   }
// });

export default router;
