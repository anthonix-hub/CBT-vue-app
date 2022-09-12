<template>
  <div>
    <v-app-bar fixed densed>
      <v-navigation-drawer app>
        <v-toolbar-title class="green--text">CBT app</v-toolbar-title>
      </v-navigation-drawer>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn active mx-2 class="error--text"><b>Fancy Quiz App</b></v-btn>
      <v-btn  disabled>Counter: 6/10</v-btn>
      <v-btn class="blue--text" :key='item' v-for="item in context"> {{item.item}} </v-btn>
      <v-btn  disabled  v-text="new Date()"></v-btn>
      <v-btn active>
        {{item}}
      </v-btn>
      <!-- <v-nav-item >{{item}}</v-nav-item> -->
      <!-- <router-link :to=""></router-link> -->
    </v-app-bar>
  </div>
</template>
<script>
export default {
  name: 'Header',
  data: () => ({
    msg: ''
  }),
  props: {
    context: Object,
    item: Object,
    btn_range: Object
  }
}
</script>
<style>
</style>
