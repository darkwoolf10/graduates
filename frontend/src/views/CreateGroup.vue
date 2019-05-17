<template>
  <v-container data-app>
    <form>
    <v-text-field
      v-model="group"
      label="Group"
    ></v-text-field>
    <v-select
      v-model="selectedFacylty"
      :items="faculty"
      label="Выбрать факультет"
    ></v-select>
    <v-select
      v-model="selectedCurator"
      :items="curators"
      label="Выбрать куратора"
      item-text="name"
    ></v-select>
    <p class="text-xs-right">
      <v-btn large>Создать</v-btn>
    </p>
  </form>
  </v-container>
</template>

<script>
    export default {
        name: "CreateGroup",
        data () {
          return {
            faculty: null,
            curators: null,
            group: null,
            selectedFacylty: null,
            selectedCurator: null
          }
        },
        async mounted() {
          let vm = this;
          await this.axios.get('http://127.0.0.1:8000/api/faculty/')
            .then((response) => {
            response.data.forEach(function(element) {
              vm.faculty = element.name;
            });
          });
          await this.axios.get('http://127.0.0.1:8000/api/curators/')
            .then((response) => {
              vm.curators = response.data;
              // console.log(response.data);
              // response.data.forEach(function (element) {
              //   vm.curators = element.name + element.surname;
              // })
            })
        }
    }
</script>

<style scoped>

</style>
