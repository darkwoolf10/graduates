<template>
  <v-container>
    <v-layout row class="content">
      <v-flex md6>
        PHOTO
      </v-flex>
      <v-flex md6>
        <v-card>
          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>ФІО: {{ student.name }} {{student.surname}} {{student.patronymic}}</v-list-tile-title>
                </v-list-tile-content>
              <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Тема дипломної роботи: {{ student.diploma.title }}</v-list-tile-title>
                </v-list-tile-content>
              <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Група: {{ student.group.name }}</v-list-tile-title>
                </v-list-tile-content>
              <v-divider></v-divider>
            </template>
          </v-list>


<!--          <v-list>-->
<!--            <template>-->
<!--              <v-list-tile-content>-->
<!--                  <v-list-tile-title>Теперішнє місце роботи: {{student.work.city}}(місто) {{ student.work.title }}</v-list-tile-title>-->
<!--                </v-list-tile-content>-->
<!--              <v-divider></v-divider>-->
<!--            </template>-->
<!--          </v-list>-->

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Рік випуску: {{ student.year_end }}</v-list-tile-title>
                </v-list-tile-content>
              <v-divider></v-divider>
            </template>
          </v-list>

          <v-list v-for="subject in student.ball" :key="subject.id">
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>{{subject.subject}} : {{subject.assessment}}</v-list-tile-title>
                </v-list-tile-content>
                <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Опис: {{ student.description }}</v-list-tile-title>
                </v-list-tile-content>
            </template>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
    export default {
        name: "Student",
        data() {
          return {
            student: {
              name: null,
              surname: null,
              patronymic: null,
              diploma: {
                title: null,
              },
              work: {
                city: null,
                title: null
              }
            }
          }
        },
        mounted() {
          let vm = this;
          this.axios.get('http://127.0.0.1:8000/api/students/' + this.$route.params.id + '/')
            .then((response) => {
            vm.student = response.data;
          })
        }
    }
</script>

<style scoped>
.content {
  height: 80vh;
}
</style>
