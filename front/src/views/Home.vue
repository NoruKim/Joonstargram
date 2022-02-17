<template>
  <!-- Header -->
  <div class="header">
    <div class="header-box">
      <div class="logo-img">
        <router-link :to="{ name: 'Home' }">
          <img src="../assets/logo_joonstar.png" alt="logo" />
        </router-link>
      </div>

      <div class="search-box">
        <input type="text" v-model="searchName" placeholder="Search" />
      </div>

      <div class="header-right">
        <div>
          <i class="fas fa-home fa-2x"></i>
        </div>
        <div>
          <i class="fas fa-plus-circle fa-2x"></i>
        </div>
        <div class="dropdown">
          <a
            href="#"
            role="button"
            id="dropdownMenuLink"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <i class="fas fa-user fa-2x"></i>
          </a>

          <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <li>
              <a class="dropdown-item" href="#">Profile</a>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <li>
              <a class="dropdown-item" href="#">Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Container -->
  <div v-for="post in posts" :key="post" class="post-box">
    <div class="header">
      <div class="profile">
        <img
          v-if="post.author.profile_photo"
          :src="post.author.profile_photo"
        />
        <img v-else src="../assets/default_profile.png" />
        <div>{{ post.author.username }}</div>
      </div>

      <div class="icon">
        <a href="#">
          <i class="fas fa-pencil-alt fa-lg"></i>
        </a>
        <a href="#">
          <i class="fas fa-trash-alt fa-lg"></i>
        </a>
      </div>
    </div>

    <v-img
      class="post-image"
      :src="post.image"
      contain
      height="300px"
      width="400px"
    />

    <div class="like-icon">
      <a href="#">
        <i class="fas fa-heart fa-2x" style="color: red"></i>
        <i class="far fa-heart fa-2x"></i>
      </a>
      {{ post.image_likes.length }} likes
    </div>

    <div class="desc-box">
      <div class="caption">
        <b>{{ post.author.username }}</b>
        {{ post.caption }}
      </div>

      <!-- <div class="comment">
        {% for comment in post.comment_post %}
        <div>
          <b>{{ comment.author.username }}</b>
          {{ comment.content }} {% if user.id == comment.author.id %}
          <a href="{% url 'posts:comment_delete' comment.id %}">
            <i class="fas fa-trash-alt" style="color: #0095f6"></i>
          </a>
          {% endif %}
        </div>
        {% endfor %}
      </div> -->
    </div>

    <!-- <div class="comment-input">
      <form method="post" action="{% url 'posts:comment_create' post.id %}">
        {% csrf_token %} {{ comment_form }}
        <input type="submit" value="作成" />
      </form>
    </div> -->
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "Home",
  data() {
    return {
      searchName: "",
      posts: null,
    };
  },
  mounted() {
    this.getPost();
  },
  methods: {
    getPost() {
      this.axios.get(`http://127.0.0.1:8000/posts/`).then((res) => {
        this.posts = res.data;
      });
    },
  },
};
</script>

<style>
/* Header CSS */
.header {
  height: 60px;
  background-color: white;
  border: solid 1px #f0f0f5;
  display: flex;
  justify-content: center;
}

.header-box {
  width: 1000px;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.logo-img img {
  width: 150px;
  height: 50px;
}

.header-box input {
  border: solid 1px #f0f0f5;
  text-align: center;
}

.header-box input[type="text"] {
  background-color: #f0f0f5;
  width: 200px;
  height: 25px;
}

.header-right {
  display: flex;
  flex-direction: row;
  justify-content: end;
}

.header-right div {
  margin: 10px;
}

.header-right a {
  color: black;
}

/* Main Container CSS */
.post-box {
  background-color: white;
  border: solid 1px #f0f0f5;
  width: 1000px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: auto;
  margin-right: auto;
}

.post-box .header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border: none;
}

.post-box .header .profile {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  column-gap: 10px;
  margin-left: 10px;
}

.post-box .header .profile img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.post-box .header .icon {
  margin-right: 10px;
}

.post-box .header .icon i {
  margin-right: 10px;
  color: black;
}

.post-box .header .icon a {
  text-decoration: none;
}

.post-box img.post-image {
  width: 100%;
  height: auto;
}

.post-box .desc-box {
  margin-top: 16px;
  margin-left: 16px;
  margin-bottom: 22px;
}

.post-box .caption {
  font-size: 20px;
}

.post-box .comment {
  margin-top: 10px;
}

.post-box .comment-input {
  height: 70px;
  border: 2px solid #f0f0f5;
}

.post-box .comment-input form {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.post-box .comment-input form textarea {
  height: 100%;
  width: 90%;
  box-sizing: border-box;
  border: none;
  margin: 5px;
}

.post-box .comment-input form input {
  height: 50%;
  box-sizing: border-box;
  border: none;
  margin-right: 10px;
  background: #fafafa;
  color: #0095f6;
  font-weight: bolder;
  font-size: 18px;
  cursor: pointer;
}

.post-box .like-icon a {
  text-decoration: none;
  color: inherit;
}
</style>