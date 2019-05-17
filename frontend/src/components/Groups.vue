<template>
    <div class="container">
      <router-link :to="{path: '/create-group'}" style="text-decoration: none">
        <v-btn fab dark color="indigo">
          <v-icon dark>add</v-icon>
        </v-btn>
      </router-link>

      <v-list>
        <v-list-group v-for="item in items" :key="item.name" v-model="item.id" :prepend-icon="item.name" no-action>
          <template v-slot:activator>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title></v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
          <v-list-tile v-for="group in item.group" :key="group.name" @click="">

            <v-list-tile-content>
              <v-list-tile-title>{{ group.name }}</v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-action>
              <v-icon>{{ item.action }}</v-icon>
            </v-list-tile-action>

          </v-list-tile>
        </v-list-group>
      </v-list>
    </div>
</template>

<script>
    export default {
        name: "Groups",
        mounted () {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/faculty/').then((response) => {
            vm.items = response.data;
          })
        },
        data () {
        return {
          items: []
        }
      }
    }
</script>

<style scoped>
</style>
