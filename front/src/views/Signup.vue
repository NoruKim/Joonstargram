<template>
  <div class="formContainer">
    <div class="logo-box">
      <img class="logo" src="../assets/logo_joonstar.png" />
    </div>
    <form class="signup-box">
      <input
        type="text"
        v-model="username"
        name="username"
        placeholder="Username"
      />
      <input type="text" v-model="email" name="email" placeholder="Email" />
      <input
        type="password"
        v-model="password1"
        name="password1"
        placeholder="Password"
      />
      <input
        type="password"
        v-model="password2"
        name="password2"
        placeholder="Confirm Password"
      />
    </form>
    <div class="signup-btn">
      <input
        type="submit"
        class="btn btn-primary"
        name="submit"
        value="Sign Up"
        @click="signup({ username, email, password1, password2 })"
      />
    </div>
    <div class="signup-btn-txt">
      <a>
        <router-link :to="{ name: 'login' }">Log in</router-link>
      </a>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    ...mapActions(["signup"]),
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"]),
  },
};
</script>

<style>
.formContainer {
  width: 100%;
  padding-top: 0.5rem;
  padding: auto;
}
.logo {
  width: 250px;
  height: 150px;
  margin-bottom: 30px;
}
.signup-box {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 200px;
  margin: auto;
}
.signup-box input {
  width: 100%;
  margin-bottom: 10px;
}
</style>