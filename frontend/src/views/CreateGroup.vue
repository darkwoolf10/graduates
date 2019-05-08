<template>
  <v-container data-app>
    <form>
    <v-text-field
      v-model="group"
      label="Group"
    ></v-text-field>
    <v-select
      v-model="select"
      :items="faculty"
      label="Select faculty"
    ></v-select>

    <v-btn >submit</v-btn>
  </form>
  </v-container>
</template>

<script>
    export default {
        name: "CreateGroup",
        data () {
          return {
            faculty: null,
            group: null,
            select: null
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/faculty/')
            .then((response) => {
            console.log(response.data);
            response.data.forEach(function(element) {
              vm.faculty = element.name;
            });
          })
        }
    }
</script>

<style scoped>

</style>
