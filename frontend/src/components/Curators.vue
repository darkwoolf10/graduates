<template>
  <v-layout align-space-around justify-space-around row wrap>
    <v-flex xs10 sm3 md-3 ma-2 v-for="curator in curators" :key="curator.id">
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
      <CuratorCard :curator="curator"/>
    </v-flex>
  </v-layout>
</template>

<script>
    import CuratorCard from './CuratorCard'
    export default {
        name: "Curators",
        data() {
          return {
            curators: null,
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/curators/').then((response) => {
            vm.curators = response.data;
            console.log(vm.curators);
          })
        },
        components: {
          CuratorCard
        }
    }
</script>

<style scoped>

</style>
