<template>
    <div class="front">
        <el-form :model="form" status-icon :rules="rules" ref="form" label-width="100px">
            <el-form-item label="用户名" prop="username">
                <el-input type="text" v-model="form.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="login">登录</el-button>
                <!-- <el-button @click="$router.push('/signup')">注册</el-button> -->
            </el-form-item>
        </el-form>
    </div>
</template>



<script>
import qs from "qs";
export default {
    data() {
        return {
            form: {
                username: "",
                password: "",
            },
            rules: {
                username: [
                    { required: true, message: "请输入用户名", trigger: "blur" },
                ],
                password: [
                    { required: true, message: "请输入密码", trigger: "blur" },
                    {
                        min: 6,
                        max: 12,
                        message: "长度在 6 到 12 个字符",
                        trigger: "change",
                    },
                ],
            },
        };
    },
    methods: {
        login() {
            if (this.form.username === "" || this.form.password === "") {
                this.$alert("账号或密码不能为空", "登录错误");
            } else {
                this.$http({
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    method: "post",
                    url: "login",
                    data: qs.stringify(this.form),
                })
                    .then((res) => {
                        if (res.data.code === 1) {
                            this.$message.success(res.data.message);
                            document.cookie = res.cookie;

                            this.$router.push("/dashboard");
                        } else if (res.data.code === 0) {
                            this.$message.warning(res.data.message);
                        }
                    })
                    .catch((err) => {
                        console.log(err);
                        this.$message.warning("请求失败");
                    });
            }
        },
    },
};
</script>


<style scoped>
/* div动态居中 */
.front {
    z-index: 1;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
}
</style>