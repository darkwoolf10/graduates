<template>
  <v-card>
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
      aspect-ratio="1"
    ></v-img>

    <v-card-title primary-title>
      <div>
        <h3 class="headline mb-0">{{curator.name}} {{curator.surname}}</h3>
        <div> {{curator.description}} </div>
      </div>
    </v-card-title>

    <v-card-actions>
      <v-btn flat color="orange">Показать</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
    export default {
        name: "CuratorCard",
        props: {
          curator: null
        }
    }
</script>

<style scoped>

</style>
