<template>
  <div class="hello">
    <h1>Hello world</h1>
    <ul>
      <li><h2><router-link to="/students">Students</router-link></h2></li>
      <li><h2><router-link to="/groups">Group</router-link></h2></li>
      <li><h2><router-link to="/curators">Curators</router-link></h2></li>
      <li><h2><router-link to="/diplomas">Diplomas</router-link></h2></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.hello {
  display: flex;
  align-items: center;
  justify-content: center;
}
.hello h2 {
}
</style>
