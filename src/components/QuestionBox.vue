<template>
  <div class='question-box-container'>
    <b-jumbotron >
    <template v-slot:lead>
      {{ currentQuestion.question }}
    </template>
    <hr class="my-4" />
    <p>
      list of  answers
    </p>
    <b-button variant="primary" href="#">Submit</b-button>
    <b-button variant="success" href="#" @click="next">
      Next
    </b-button>
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  props: {
    currentQuestion: Object,
    next: Function
  },
  // computed () {
  // answers () {
  //   let answers = [...currentQuestion.incorrect_answers]
  //   answers.push(currentQuestion.correct_answer)
  // }
  // }
  mounted () {
    console.log(this.currentQuestion)
  }
}
</script>
