
<template>
  <div>
    <el-card class="box-card" v-model="form">
      <div slot="header" class="clearfix">
        <span>标题：{{ form.title }}</span>
      </div>
      <div class="text item">
        <p>{{ form.read }}：{{ form.name }}</p>
        <p>时间：{{ form.time }}</p>
        <p>{{ form.content }}</p>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  mounted() {
    this.form.title = this.$route.query.title;
    this.form.name = this.$route.query.name;
    this.form.time = this.$route.query.time;
    this.form.content = this.$route.query.content;
    this.form.read = this.$route.query.read;
    // this.form.attachment = this.$router.query.attachment;
  },
  data() {
    return {
      form: { name: "", title: "", content: "", time: "", read: "" },
    };
  },
};
</script>

<style>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 480px;
  margin: auto;
}
</style>