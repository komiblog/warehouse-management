<template>
  <div class="front" border>
    <el-row :gutter="0">
      <el-col :span="14">
        <el-descriptions :column="1" border title="个人信息">
          <el-descriptions-item label="姓名">
            {{ form.name }}</el-descriptions-item
          >

          <el-descriptions-item label="性别">
            {{ form.sex }}</el-descriptions-item
          >
          <el-descriptions-item label="部门">
            {{ form.depment }}</el-descriptions-item
          >
          <el-descriptions-item label="地区">
            {{ form.address }}</el-descriptions-item
          >
        </el-descriptions>
      </el-col>
      <el-col :span="8" style="align-items: stretch">
        <br />
        <div class="imgBox">
          <el-image fit="cover" :src="form.pic" alt="未上传头像!"></el-image>
        </div>
      </el-col>
    </el-row>
    <el-descriptions :column="1" border>
      <el-descriptions-item label="手机">
        {{ form.phone }}</el-descriptions-item
      >

      <el-descriptions-item label="邮箱">
        {{ form.email }}</el-descriptions-item
      >
    </el-descriptions>
  </div>
</template>

<script>
export default {
  name: "PersonalInfo",
  created: function () {
    this.$http.get("/profile/show").then((resp) => {
      let userdata = resp.data[0];
      this.form.name = userdata.name;
      this.form.phone = userdata.phone;
      userdata.pic = "data:image/jpeg;base64," + userdata.pic;
      this.form.pic = userdata.pic;
      this.form.email = userdata.email;
      if (userdata.sex == 0) {
        this.form.sex = "未知";
      } else if (userdata.sex == 1) {
        this.form.sex = "男";
      } else {
        this.form.sex = "女";
      }
      this.form.depment = userdata.depment;
      this.form.address = userdata.address;
    });
  },
  data() {
    return {
      form: {
        userid: "",
        username: "",
        name: "",
        phone: "",
        email: "",
        sex: "",
        depment: "",
        address: "",
        pic: "",
      },
    };
  },
};
</script>


<style>
.front {
  width: 50%;
  margin: auto;
}
</style>