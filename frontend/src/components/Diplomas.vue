<template>
  <v-container>
    <v-card v-for="diplom in diplomas" :key="diplom.id" class="mx-auto" color="#26c6da" dark ma-2>
      <v-card-text class="headline font-weight-bold">
        "{{ diplom.title }}."
      </v-card-text>

      <v-card-actions>
        <v-list-tile class="grow">
          <v-list-tile-avatar color="grey darken-3">
            <v-img
              class="elevation-6"
              src="https://cdn3.iconfinder.com/data/icons/education-1-28/49/139-512.png"
            ></v-img>
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>{{diplom.curator.name}} {{diplom.curator.surname}}</v-list-tile-title>
          </v-list-tile-content>
<!--          <router-link to="/diplom/"><v-btn color="primary">Детальніше</v-btn></router-link>-->
        </v-list-tile>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
    export default {
        name: "Diplomas",
        data() {
          return {
            diplomas: null,
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/diplomas/').then((response) => {
            vm.diplomas = response.data;
            console.log(response.data);
          })
        },
    }
</script>

<style scoped>

</style>
