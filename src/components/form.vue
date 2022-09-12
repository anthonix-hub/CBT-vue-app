<template>

<div id='form'>
    {{feedback}}~{{Fname}}
    <form action="" class="form" v-show="feedback == 11">
        <template >
            <input placeholder="first-Name" v-model="Fname" type="text" v-bind:class="[Fname.length < 3 ? 'red' : 'green']"  >
            <input placeholder="last-Name" type="text" v-model="Lname">
            <input placeholder=" enter @email" type="email" v-model="email" >
            <input placeholder="country" type="text">
            <input placeholder="Mobile-number" type="text" >
            <input placeholder="password" type="password" >
            <input placeholder="reEnter-password " type="password">
            <v-button class="btn" type="submit">submit</v-button>
        </template>
        <template>
            <input placeholder="first-Name" type="text" v-model="Fname" >
            <input placeholder="password" type="password" v-model="Fname" >
        </template>
    </form>
</div>
</template>

<script>
export default {
  name: 'Form',
  data: () => ({
    Fname: 'Fname',
    Lname: '',
    email: '',
    password1: '',
    password2: '',
    feedback: 12
  })
}
</script>
<style >
.form{
    display: -moz-groupbox;
    background-color: #e6f3f6;
    width:80%;
    background:linear-gradient(rgba(31, 203, 225, 10)50%,rgba(15, 120, 134, 0.75)80%) ;
}
.form input{
    display: block;
    margin-inline: 40px;
    margin-top: 30px;
    width:30%;
    height:40px;
    font-size: 20px;
    padding: 5px;
}
.form input:nth-child(odd){
    width:30%;
    border-block-color: green;
}
.btn{
    margin-left: 350px;
    height:40px;
    width:10%
    }
</style>
