<template>
    <div class="front">
        <el-form ref="form" :model="form" label-width="80px" style="width: 400px">
            <el-form-item label="名称">
                <el-input v-model="form.p_name"></el-input>
            </el-form-item>
            <el-form-item label="类别">
                <el-input v-model="form.p_type"></el-input>
            </el-form-item>
            <el-form-item label="价格">
                <el-input v-model.number="form.p_price"></el-input>
            </el-form-item>
            <el-form-item label="描述">
                <el-input type="textarea" v-model="form.p_depiction"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="update">发送</el-button>
                <el-button @click="$router.push('/dashboard/product')">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    mounted() {
        this.form.p_id = parseInt(this.$route.query.p_id);
        this.form.p_name = this.$route.query.p_name;
        this.form.p_type = this.$route.query.p_type;
        this.form.p_price = parseInt(this.$route.query.p_price);
        this.form.p_depiction = this.$route.query.p_depiction;
    },
    data() {
        return {
            form: {
                p_id: 0,
                p_name: "",
                p_type: "",
                p_depiction: "",
                p_price: 0,
                p_count: 0
            },
            fileList: [],
        };
    },
    methods: {
        update() {
            this.$http.put("/manage/product/" + this.form.p_id, this.form)
                .then((res) => {
                    if (res.status === 200) {
                        this.$message.success(res.data.message);
                        this.$router.push("/dashboard/product");
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.$message.warning(err.response.data.message);
                });
        },
    },
};
</script>

<style scoped></style>
