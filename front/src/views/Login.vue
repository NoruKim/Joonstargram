<template>
  <div class="formContainer">
    <div class="logo-box">
      <img class="logo" src="../assets/logo_joonstar.png" />
    </div>
    <form class="login-box">
      <input
        type="input"
        v-model="username"
        name="username"
        placeholder="Username"
      />
      <input
        type="password"
        v-model="password"
        name="password"
        placeholder="Password"
      />
    </form>
    <div class="login-btn">
      <input
        type="submit"
        class="btn btn-primary"
        name="submit"
        value="Login"
        @click="login({ username, password })"
      />
    </div>
    <div class="login-btn-txt">
      <a>
        <router-link :to="{ name: 'signup' }">Sign Up</router-link>
      </a>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"]),
  },
  methods: {
    ...mapActions(["login"]),
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
.login-box {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 200px;
  margin: auto;
}
.login-box input {
  width: 100%;
  margin-bottom: 10px;
}
</style>