<template>
    <v-app>
      <div id="geoApp">
      <br>
      <br>
        <v-row>
          <v-col lg="12">
            <Header
              :context="context"
              :btn_range="btn_range"
            />
          </v-col>
        </v-row>
        <v-spacer></v-spacer>
        <!--<v-row>
          <v-col lg='1'>
            <b-select
              :items="items"
              v-model.number="btnRange"
              label="select no"
              type="number"
              >
              <option value=25>25</option>
              <option value=30>30</option>
              <option value=45>35</option>
              <option value=45>40</option>
              <option value=45>50</option>
              <option value=60>60</option>
              <option value=100>100</option>
            </b-select>
            {{new_id}}
          </v-col>
        </v-row>-->
        <!--<v-container class="bv-example-row">
          <v-row>
            <v-col lg="9" >
              <v-card elevation="6" class="grey">
                <QuestionBox
                  v-if="questions.length"
                  :currentQuestion="questions[index]"
                  :next="next"
                  >
                </QuestionBox>
              </v-card>
            </v-col>
          </v-row>
        </v-container>-->
        <div class="container quest_section">
          <div class="row">
            <!--Question and answer section-->
            <div class="col-lg-8 col-md-8 col-sm-6">
              <transition name="fade">
                <mainDisplay
                  @checked="checked_quest($event)"
                  :msg="msg"
                  :numInstance="numInstance"
                  :answer_log="answer_log"
                />
              </transition>
                Answer each question that appears, you can skip current question you are nit sure of and ccome back later to attemp it rather than wasting time on sure questoin.
                <!-- <h4>API{{question_API}}</h4> -->
            </div>
            <!--*******Q & A ends********-->
            <div class="col-lg-4 offset-lg-2" id="task">
              <div class="jumbotron bg-muted " id="root">
                <sidebar
                  title="personal info"
                  body="component section"
                  :img='img'
                  :gotten_child_index="gotten_child_index"
                  :quest_count="quest_count"
                />
              </div>
            </div>
          </div>
        </div>
        <!--_<choice
          :btnRange="btnRange"
          :instagram="instagram"
          @questId_gotten="gotten_id()"
          class="grey"
          >
        </choice>-->
        <!--button section-->
        <div class="row">
          <div class="col-lg-12">
            <div class="btn-style">
              <div class="jumbotron" >
                <div class="row">
                  <div class="col-lg-12 col-md-12 ">
                    <span class="btn btn-group " v-for="(numID,index) in num" :key="index" id="quest_btns">
                      <button
                        class="btn btn-md btn-dark"
                        :id="numID"
                        ref="numref"
                        :title="btn_msg"
                        @click="inputFunc(index)"
                        >
                        {{numID}}
                      </button>
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!--**************-->
      </div>
    </v-app>
</template>
<script>
// import QuestionBox from './components/QuestionBox.vue'
import Header from './components/Header.vue'
import sidebar from './components/sidebar.vue'
// import choice from './components/choice.vue'
import mainDisplay from './components/mainDisplay.vue'
import axios from 'axios'
export default {
  name: 'geoApp',
  components: {
    // QuestionBox,
    Header,
    sidebar,
    // choice,
    mainDisplay
  },
  data: () => ({
    questions: [],
    index: 0,
    context: [
      { item: 'folly' },
      { item: 'polly' },
      { item: 'molly' },
      { item: 'holly' }
    ],
    social: [
      { Email: 'person@gmail.com' },
      { twitter: '@person.twitter' },
      { instagram: 'person.insta' }
    ],
    btnRange: '',
    numInstance: null,
    new_id: null,
    msg: 'vue todo',
    todo_items: [
      { item: 'wew' },
      { item: 'raap' }
    ],
    num: 100,
    type: null,
    lorem: ['folly', 'polly', 'molly', 'holly'],
    show: true,
    gotten_child_index: '',
    require: '',
    btn_msg: 'click to load question',
    img: '../CBT-app/default-avatar.png',
    quest_id: null,
    answer_log: [],
    isfocus: false,
    numID: '',
    quest_count: null,
    answers: [
      { index: '', opt: '' }
    ],
    question_API: []
  }),
  methods: {
    inputFunc (index) {
      this.questId = this.$refs.numref[index].id
      console.log(this.questId)
      this.numInstance = this.questId

      if (this.answer_log.includes(this.numInstance)) {
        console.log('already present')
        // document.getElementById("task").style.backgroundColor = "blue";
      } else {
        this.answer_log.push(this.numInstance)
      };
      // const log = 0
      this.answer_log.forEach(element => {
        this.quest_count = this.answer_log.length
        if (this.numInstance) {
          // document.getElementById(this.numInstance).style.backgroundColor = "blue"
        };
      })
    },
    checked_quest (selectedOpt) {
      this.gotten_child_index = selectedOpt
    }
  },
  mounted: function () {
    fetch('https://opentdb.com/api.php?amount=10&category=27&type=multiple', {
      method: 'get'
    })
      .then((response) => {
        return response.json()
      })
      .then((jsonData) => {
  },
  computed () {
    // answer_logFunc: function (numInstance) {
    //   return {
    //   }
    // },
    axios.get('http://localhost:8000/Questions/?format=api')
      .then(res => (this.question_API = res.data))
      // .then(res => (console.log(res.data)))
      .catch(err => console.log(err))
      console.log(this.question_API)
  },
  watch: {
    answer_log: function () {
      // this.quest_count = this.answer_log.count()
    }
  }
}
</script>
<style scoped>
  .fade-enter-active, .fade-leave-active {
        transition: opacity .5s ;
    }
    .fade-enter, .fade-leave-to{
        opacity: 0;
    }
    #quest_btns {
        padding:6px;
        padding-top:2px;
        margin-bottom: -3px;
    }
    .btn-style{
        background-color: #9578aa;
    }
    .btn-style .jumbotron{
        position: fixed;
        height:330px;
        margin-top: 40px;
    }
    #task{
        margin-right: -310px;
    }
    .quest_section{
        margin-left: 50px;
        /* border-radius: 2px solid red; */
    }
    select{
        width: 20%;
        font-size: 20px;
        border:none
    }
    .btn-groups, .quest_label {
        display: inline-block;
        /* border-right:1px solid black; */
        margin: 2px;
        font-size: 18px;
        color:#ff0000;
    }
    .selected{
        background-color: #ff0000;
    }
    .answered_quests {
        background-color: blue;
    }
    .not_answered_quests{
        background-color: #91d45e;
    }
    #personal_img{
        width: 35%;
        height: 80px;
    }
    #ans_options{
        background-color: #61eee9;
        padding: 5px;
        width: 26px;
        margin: 13px;
    }
    #ans_options:hover{
        background:yellow
    }
    #task{
        height: 160px;
    }
    
</style>