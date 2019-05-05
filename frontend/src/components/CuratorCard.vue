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
      <router-link :to="{path: '/curator/' + curator.id, params: {curatorId: curator.id}}" style="text-decoration: none">
          <v-btn flat color="orange">Показать</v-btn>
        </router-link>
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
