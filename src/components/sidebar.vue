<template>
  <div id="sidebar">
    <span class='row'>
      <span class='col'>
        <h3 class="text-info">
          <slot>{{title}}</slot>
        </h3>
        <p> {{body}} </p>
        <p>
          answered: <b>{{quest_count}}/100</b>
        </p>
      </span>
      <span class="col">
        <img :src='img' id="personal_img">
      </span>
    </span>
  </div>
</template>
<script>

// import Header from './Header.vue'
export default {
  name: 'sidebar',
  components: {
    // Header
  },
  props: [
    'title',
    'body',
    'img',
    'gotten_child_index',
    'quest_count'
  ],
  data: () => ({
    context: [
      'sloted context',
      'computed-context'
    ]
  })
}
</script>
<style>
</style>
