<template>
    <v-card>
      <v-img
        src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
        aspect-ratio="1"
      ></v-img>

      <v-card-title primary-title>
        <div>
          <h3 class="headline mb-0">{{student.name}} {{student.surname}}</h3>
          <div> </div>
        </div>
      </v-card-title>

      <v-card-actions>
        <v-btn flat color="orange">Показать</v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "StudentsCard",
        props: {
          student: null
        }
    }
</script>

<style scoped>

</style>
