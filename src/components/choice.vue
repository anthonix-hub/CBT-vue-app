<template>
    <div id="choice">
      <!--<v-container>-->
        <v-row>
          <v-col lg="12">
            <!-- <h3>{{btn_select}}</h3> -->
            <v-btn-toggle v-for="(btn, index) in btnRange" :key="btn-id" class="primary" multiple>
              <v-btn
                :title="title"
                :id="btn"
                ref="numref"
                v-on:click="inputFunc(index)"
                variant="outline-primary"
                >
                {{index}}:{{btn}}
              </v-btn>
            </v-btn-toggle>
              <v-btn
                v-b-modal.calledmodal
                variant="success"
                v-on:click="cancleQuest"
                class="warning"
                >
                terminate
              </v-btn>
          </v-col>
        </v-row>
        <v-container>
          <v-alert
            dark
            class="blue-grey"
            dense elevation="10"
            outline
            border="left"
            bordered-color
            >
            are you sure you want to close the questions?
          </v-alert>
        </v-container>
      <!--</v-container>-->
    </div>
</template>
<script>
// import sideOption from './components/sideOption.vue'
export default {
  name: 'choice',
  components: {
  },
  data: () => ({
    btn_select: '',
    title: 'question',
    num_instance: null

  }),
  props: ({
    btnRange: Number
  }),
  methods: {
    cancleQuest: () => {
      this.btnRange = ''
      // alert('cancle')
    },
    inputFunc (index) {
      var questId = this.$refs.numref[index].id
      console.log(questId)
      alert('this is questtion with the id of ' + questId)
      this.num_instance = questId
      this.$emit('questId_gotten', this.num_instance)
    }
  }
}
</script>
