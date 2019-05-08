import HelloWorld from '@/components/HelloWorld'
import StudentsList from "@/components/StudentsList"
import Curators from "@/components/Curators"
import Groups from "@/components/Groups";
import Diplomas from "@/components/Diplomas";
import Student from "@/views/Student";
import Curator from "@/views/Curator";
import CreateGroup from "@/views/CreateGroup";

export const routes = [
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
      path: '/student/:id',
      name: 'Student',
      component: Student
    },
    {
      path: '/curators',
      name: 'Curators',
      component: Curators
    },
    {
      path: '/curator/:id',
      name: 'Curator',
      component: Curator
    },
    {
      path: '/groups',
      name: 'Groups',
      component: Groups
    },
    {
      path: '/create-group',
      name: 'CreateGroup',
      component: CreateGroup
    },
    {
      path: '/diplomas',
      name: 'Diplomas',
      component: Diplomas
    },
    {
      path: '*',
      component: StudentsList
    }
  ];
