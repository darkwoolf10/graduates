<template>
  <v-card
    flat
    tile
  >
    <v-toolbar
      color="cyan"
      dark
    >
      <v-toolbar-side-icon></v-toolbar-side-icon>

      <v-toolbar-title>
        <router-link to="/">Application</router-link>
      </v-toolbar-title>

      <v-spacer></v-spacer>

<!--      <v-btn icon>-->
<!--        <v-icon>search</v-icon>-->
<!--      </v-btn>-->
    </v-toolbar>

    <router-view/>
  </v-card>
</template>

<script>
  export default {
    name: 'App',
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto');
* {
    font-family: 'Roboto';
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

}
.router-link-active {
  text-decoration: none;
  color: whitesmoke;
}
</style>
