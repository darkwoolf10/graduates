<template>
  <v-layout align-space-around justify-space-around row wrap>
      <Card />
      <Card />
      <Card />
      <Card />
      <Card />
      <Card />
  </v-layout>
</template>

<script>
    import Card from './Card';

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
          Card
        }
    }
</script>

<style scoped>

</style>
