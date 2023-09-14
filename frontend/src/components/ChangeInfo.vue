<template>
  <div class="front">
    <el-form
      status-icon
      ref="form"
      :model="form"
      :rules="rules"
      label-width="80px"
    >
      <el-form-item label="真实姓名" prop="name">
        <el-input type="text" v-model="form.name"></el-input>
      </el-form-item>

      <el-form-item label="手机号" prop="phone">
        <el-input type="tel" v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item label="电子邮箱" prop="email">
        <el-input type="email" v-model="form.email"></el-input>
      </el-form-item>

      <el-form-item label="性别">
        <el-radio-group v-model="form.sex">
          <el-radio label="0">不明</el-radio>
          <el-radio label="1">男</el-radio>
          <el-radio label="2">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="部门">
        <el-input type="text" v-model="form.department"></el-input>
      </el-form-item>
      <el-form-item label="地区">
        <el-cascader
          size="large"
          :options="options"
          v-model="form.selectedOptions"
          @change="handleChange"
        >
        </el-cascader>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
        <el-button @click="$router.push('/dashboard/addressbook')"
          >取消</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { regionData } from "element-china-area-data";

export default {
  mounted() {
    this.form.userid = this.$route.query.userid;
    this.form.name = this.$route.query.name;
    this.form.phone = this.$route.query.phone;
    this.form.email = this.$route.query.email;
  },
  data() {
    return {
      form: {
        userid: "",
        name: "",
        phone: "",
        email: "",
        sex: "0",
        department: "",
        selectedOptions: [],
      },
      options: regionData,
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],

        name: [{ required: true, message: "请输入真实姓名", trigger: "blur" }],
        phone: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          {
            pattern: "^1[0-9]{10}$",
            message: "请输入格式正确的中国大陆11位手机号",
            trigger: "blur",
          },
        ],
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            pattern: "^([a-zA-Z0-9]+[-_.]?)+@[a-zA-Z0-9]+.[a-z]+$",
            message: "邮箱格式错误",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    onSubmit() {
      this.$refs["form"].validate((valid) => {
        if (valid) {
          let query = [];
          query.push("userid=" + this.form.userid);
          query.push("name=" + this.form.name);
          query.push("phone=" + this.form.phone);
          query.push("email=" + this.form.email);
          let sex =
            (this.form.sex == this.form.sex) === "不明"
              ? 0
              : this.form.sex === "女"
              ? 1
              : 2;
          query.push("sex=" + sex);
          if (this.form.department != "") {
            query.push("department=" + this.form.department);
          }
          if (this.form.selectedOptions[-1] != null) {
            query.push("postalcode=" + this.form.selectedOptions[-1]);
          }
          var postdata = query.join("&");
          this.$http({
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            method: "post",
            url: "profile/edit",
            data: postdata,
          }).then((res) => {
            if (res.data.code === 1) {
              this.$message.success("修改成功!");
              this.$router.push("/dashboard/addressbook");
            } else {
              this.$message.warning("没有数据被修改!");
            }
          });
        } else {
          this.$message.warning("请输入必填项!");
        }
      });
    },
    // 控制地区选择
    handleChange(value) {
      console.log(value);
    },
  },
};
</script>

<style scoped>
.front {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

