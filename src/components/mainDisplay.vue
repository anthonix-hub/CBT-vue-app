<template>
    <div id="mainDisplay">
      <v-main>
        {{message}}: {{numInstance}}
        <h4
          v-for="context in filtered_quest(Question_Log, numInstance)"
          :key="context"
          v-html='context.quest'
          >
        </h4>
        <div class="row" v-for="ans in answer_filtered(Question_Log, numInstance)" :key="ans.id">
          <select multiple>
            <option
              id="ans_options"
              v-for=" (opt,index) in ans.opts"
              :key="opt.id"
              :value="opt.value"
              @click="answersIndex(index)"
              >
              {{opt.value}}
            </option>
          </select>
          <span class="quest_label">
            <ul v-for="(ans_opts,index) in ans.answers" :key="ans_opts.id">
              <label @click="optionIndex(index)">
                {{ans_opts}}
              </label>
            </ul>
          </span>
        </div>
        <!--<v-container>-->
            <!--<v-row>
              <v-col>
                <v-divider class="purple"></v-divider>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro similique tempore
                  dolore assumenda et
                  ab neque officia, enim alias omnis
                  eveniet dolor impedit harum officiis doloremque natus repellendus facere unde!
                <span v-for="log in Question_Log" :key="log">
                  <h3>{{log.quest3}}</h3>
                </span>
              </v-col>
            </v-row>-->
      </v-main>
      </div>
    <!--</v-container>-->
</template>
<script>
export default {
  name: 'mainDisplay',
  props: {
    msg: String,
    numInstance: String,
    answer_log: Array
  },
  data: () => ({
    isActive: true,
    focused: false,
    selected: [],
    // answer_log: [],
    Question_Log: [
      {
        id: 1,
        quest: 'what is the capital of Germany',
        answers: ['Jeniver', 'Damascus', 'Berlin', 'lorem'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 2,
        quest: 'what is the capital of Island',
        answers: [':Prem', 'Damascus', 'fiji', 'moriteus'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 3,
        quest: 'what is the capital of japan',
        answers: ['yokohama', 'Tokyo', 'Nairobi', 'Adis Ababa'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 4,
        quest: 'what is the capital of Quwait',
        answers: ['torem', 'Damascus', 'lorem', 'dorem'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 5,
        quest: 'what is the capital of senegal',
        answers: ['kinshaha', 'popoli', 'cusmos', 'dasande'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 6,
        quest: 'what is the capital of Eygpt',
        answers: ['Jeniver', 'Damascus', 'lorem', 'Berlin'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 7,
        quest: 'what is the capital of Congo',
        answers: ['Jeniver', 'Damascus', 'lorem', 'Berlin'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 8,
        quest: 'what is the capital of Liberial',
        answers: ['Lesoto', 'FreeTown', 'sosrem', 'Swahili'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 9,
        quest: 'what is the capital of Brazil',
        answers: ['Jeniver', 'Damascus', 'lorem', 'Berlin'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 10,
        quest: 'what is a tsunami ?',
        answers: ['An Atom', 'A japaniss Food', 'A contagious desease', 'An earth quake that occurs at the sea or occean bed'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 11,
        quest: 'who is the president of Poland',
        answers: ['Jeniver', 'Damascus', 'lorem', 'Berlin'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 12,
        quest: 'who is the president of America',
        answers: ['Donald Tramp', 'Donad Trumb', 'Donald Trump', 'hilty salio'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 13,
        quest: 'who is the prime minister of India',
        answers: ['Angelina Markel', 'Putin', 'Boris Johnson', 'Mondi'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 14,
        quest: 'what is the capital of Switzerland',
        answers: ['Jeniver', 'Damascus', 'lorem', 'Berlin'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      },
      {
        id: 15,
        quest: 'Which is the best option to fill the blank?<br> the house is _____ painted for the event to take place',
        answers: ['Being', 'Been', 'Not sure', 'None of the mentioned'],
        opts: [
          { value: 'A' },
          { value: 'B' },
          { value: 'C' },
          { value: 'D' }
        ]
      }
    ],
    context: [
      { option1: 'roginpon' },
      { option2: 'champion' },
      { option3: 'poopion' }
    ],
    message: 'the current question log',
    selected_opt: null
  }),
  methods: {
    filtered_quest: function (quests, numInstance) {
      return quests.filter(function (quest) {
        return quest.id === parseInt(numInstance)
      })
    },
    answer_filtered: function (ansLog, numInstance) {
      return ansLog.filter(function (ans) {
        return ans.id === parseInt(numInstance)
      })
    },
    answersIndex: function (index) {
      this.selected_opt = index
      if (this.selected_opt === 0) {
        this.selected_opt = 'A'
      };
      if (this.selected_opt === 1) {
        this.selected_opt = 'B'
      };
      if (this.selected_opt === 2) {
        this.selected_opt = 'C'
      };
      if (this.selected_opt === 3) {
        this.selected_opt = 'D'
      };
      // this.selected_opt = null
      console.log(this.selected_opt)
      this.$emit('checked', this.selected_opt)

      this.selected.push({ ans_index: this.numInstance, opt: this.selected_opt })
      this.answer_log.forEach(element => {
        // this.quest_count = this.answer_log.length;
        if (this.numInstance) {
          document.getElementById(this.numInstance).style.backgroundColor = 'red'
        };
      })
      // this.selected.forEach(element => {
      // if (this.selected.includes(element.this.ans_index)) {
      //     alert('option already answered')
      // }
      // else {
      //     this.selected.push({ans_index:this.numInstance, opt:this.selected_opt})
      //     alert(element.this.ans_index)
      // }
      // });
      for (const keyIndex in this.selected) {
        if (this.selected.includes(keyIndex.this.ans_index)) {
          // alert('option already answered')
          alert(keyIndex.this.ans_index)
        } else {
          this.selected.push({ ans_index: this.numInstance, opt: this.selected_opt })
          alert(keyIndex.this.ans_index)
        };
      }
    },
    optionIndex: function (index) {

    },
    answer_logFunc: function () {
      // this.answer_log =
    }
  },
  watch: {
    optionIndex () {
      this.selected_opt = null
    }
  }
}
</script>
<style scoped>

</style>
