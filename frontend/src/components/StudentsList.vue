<template>
  <div>
    <router-link :to="{path: '/create-curator'}" style="text-decoration: none">
    <v-btn fab dark color="blue">
      <v-icon dark>add</v-icon>
    </v-btn>
  </router-link>
    <v-layout align-space-around justify-space-around row wrap>
    <v-flex xs10 sm4 md-3 ma-2 v-for="student in students" :key="student.id">
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
      <StudentCard :student="student"/>
    </v-flex>
  </v-layout>
  </div>

</template>

<script>
    import StudentCard from './StudentCard';

    export default {
        name: "StudentsList",
        data() {
          return {
            students: null,
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/students/').then((response) => {
            vm.students = response.data;
            console.log(vm.students);
          })
        },
        components: {
          StudentCard
        }
    }
</script>

<style scoped>

</style>
