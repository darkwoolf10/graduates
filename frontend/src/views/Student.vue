<template>
  <v-container>
    <v-layout row class="content">
      <v-flex md5 class="photo">

      </v-flex>
      <v-flex md1 ></v-flex>
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

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Рік випуску: {{ student.year_end }}</v-list-tile-title>
                </v-list-tile-content>
              <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Математика: {{ student.ball.math }}</v-list-tile-title>
                </v-list-tile-content>
                <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Фізика: {{ student.ball.physical }}</v-list-tile-title>
                </v-list-tile-content>
                <v-divider></v-divider>
            </template>
          </v-list>

          <v-list>
            <template>
              <v-list-tile-content>
                  <v-list-tile-title>Програмування: {{ student.ball.programing }}</v-list-tile-title>
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
  .photo {
    background: linear-gradient(135deg, orange, orange 60%, cyan);
    border-radius: 10px;
  }
</style>
