<template>
    <v-container>
       <v-card>
          <v-card-title><h4>Куратор курсової роботи</h4></v-card-title>
          <v-divider></v-divider>
          <v-list dense>
            <v-list-tile>
              <v-list-tile-content>ID:</v-list-tile-content>
              <v-list-tile-content class="align-end"><h3>{{ curator.id }}</h3></v-list-tile-content>
            </v-list-tile>
            <v-divider />
            <v-list-tile>
              <v-list-tile-content>Імя:</v-list-tile-content>
              <v-list-tile-content class="align-end"><h3>{{ curator.name }}</h3></v-list-tile-content>
            </v-list-tile>
            <v-divider />
            <v-list-tile>
              <v-list-tile-content>Фамілія:</v-list-tile-content>
              <v-list-tile-content class="align-end"><h3>{{ curator.surname }}</h3></v-list-tile-content>
            </v-list-tile>
            <v-divider />
            <v-list-tile>
              <v-list-tile-content>Опис: {{curator.description}}</v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: "Curator",
        data() {
          return {
            curator: {
              id: null,
              name: '',
              surname: '',
              description: ''
            }
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/curators/' + this.$route.params.id + '/')
            .then((response) => {
            console.log(response.data);
            vm.curator = response.data;
          })
        }
    }
</script>

<style scoped>

</style>
