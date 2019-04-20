import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import StudentsList from "@/components/StudentsList"
import Curators from "@/components/Curators"
import Groups from "@/components/Groups";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/students',
      name: 'StudentList',
      component: StudentsList
    },
    {
      path: '/curators',
      name: 'Curators',
      component: Curators
    },
    {
      path: '/groups',
      name: 'Groups',
      component: Groups
    }
  ]
})
