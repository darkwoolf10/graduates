<template>
  <v-container data-app>
    <form>
    <v-text-field
      v-model="group"
      label="Group"
    ></v-text-field>
    <v-select
      v-model="facylty"
      :items="facultys"
      label="Выбрать факультет"
      item-text="name"
      item-value="id"
    ></v-select>
    <v-select
      v-model="curator"
      name="curator"
      :items="curators"
      label="Выбрать куратора"
      item-text="name"
      item-value="id"
    ></v-select>
    <p class="text-xs-right">
      <v-btn large @click="createGroup">Создать</v-btn>
    </p>
  </form>
  </v-container>
</template>

<script>
    export default {
        name: "CreateGroup",
        data () {
          return {
            facultys: null,
            curators: null,
            curator: null,
            group: null,
            facylty: null
          }
        },
        async mounted() {
          let vm = this;
          await this.axios.get('http://127.0.0.1:8000/api/faculty/')
            .then((response) => {
              vm.facultys = response.data;
          });
          await this.axios.get('http://127.0.0.1:8000/api/curators/')
            .then((response) => {
              vm.curators = response.data;
            })
        },
        methods: {
          createGroup: function () {
            this.axios.post('http://127.0.0.1:8000/api/groups/', {
              
            })
              .then(response => response.data)
              .catch(error => console.log(error));
          }
        }
    }
</script>

<style scoped>

</style>
