import { createStore } from "vuex";
import router from "../router";
import axios from "axios";

export default createStore({
  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false,
  },
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    }
  },
  actions: {
    login(dispatch, loginObj) {
      axios.post("http://127.0.0.1:8000/api/rest-auth/login/", loginObj)
        .then(res => {
          let token = res.data.token;
          localStorage.setItem("access_token", token);
          this.dispatch("getMemberInfo");
          router.push({ name: "Home" });
          console.log(res);
        }).catch(() => {
          alert("Check Username & Password");
        });
    },
    logout({ commit }) {
      commit("logout");
      router.push({ name: "login" });
    },
    signup(dispatch, loginObj) {
      axios.post("http://127.0.0.1:8000/api/rest-auth/registration/", loginObj)
        .then(res => {
          alert("Success");
          router.push({ name: "login" });
          console.log(res);
        })
        .catch(() => {
          alert("Check Username & Password");
        });
    },
    getMemberInfo({ commit }) {
      let token = localStorage.getItem("access_token");
      let config = {
        headers: {
          "WWW-Authenticate": token
        }
      };

      console.log(config)

      axios.get("/users", config)
        .then(res => {
          let userInfo = {
            pk: res.data.data.pk,
            username: res.data.data.username,
            name: res.data.data.name,
            email: res.data.data.email,
          };
          console.log('sus2');
          commit("loginSuccess", userInfo);
        })
        .catch(() => {
          alert("Check Username & Password2");
        });
    }
  },
  modules: {},
});
