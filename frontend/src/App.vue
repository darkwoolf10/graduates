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

      <v-toolbar-title>Application</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
