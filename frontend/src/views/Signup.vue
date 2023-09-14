<template>
    <div class="front">
        <el-form status-icon ref="form" :model="form" :rules="rules" label-width="80px">
            <el-form-item label="用户名" prop="username">
                <el-input type="text" v-model="form.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkpass">
                <el-input type="password" v-model="form.checkpass" autocomplete="off"></el-input>
            </el-form-item>
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
                    <el-radio label="不明"></el-radio>
                    <el-radio label="男"></el-radio>
                    <el-radio label="女"></el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="部门">
                <el-input type="text" v-model="form.department"></el-input>
            </el-form-item>
            <el-form-item label="地区">
                <el-cascader size="large" :options="options" v-model="form.postalcode" @change="handleChange">
                </el-cascader>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="signup">立即注册</el-button>
                <el-button @click="$router.push('/login')">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import qs from "qs";
import { regionData } from "element-china-area-data";

export default {
    data() {
        var validatePass = (rule, value, callback) => {
            if (value === "") {
                callback(new Error("请再次输入密码"));
            } else if (value !== this.form.password) {
                callback(new Error("两次输入密码不一致!"));
            } else {
                callback();
            }
        };
        return {
            form: {
                username: "",
                password: "",
                checkpass: "",
                name: "",
                phone: "",
                email: "",
                sex: "不明",
                department: "",
                postalcode: [],
            },

            options: regionData,
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
                checkpass: [
                    {
                        required: true,
                        validator: validatePass,
                        trigger: "blur",
                    },
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
        signup() {
            this.$http({
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                method: "post",
                url: "register",
                data: qs.stringify(this.form),
            })
                .then((res) => {
                    if (res.data.code === 1) {
                        this.$message.success(res.data.message);

                        this.$router.push("/login");
                    } else if (res.data.code === 0) {
                        this.$message.warning(res.data.message);
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.$message.warning("请求失败");
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
    color: #5c5151;
}
</style>

