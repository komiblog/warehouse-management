<template>
    <div class="front">
        <el-row>
            <el-col :span="6" style="min-height: 1px;"></el-col>
            <el-col :span="12">
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
                    <el-form-item label="数量">
                        <el-input v-model.number="form.p_count"></el-input>
                    </el-form-item>
                    <el-form-item label="描述">
                        <el-input type="textarea" v-model="form.p_depiction"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="upload">发送</el-button>
                        <el-button @click="$router.push('/dashboard/product')">取消</el-button>
                    </el-form-item>

                </el-form>
            </el-col>
            <el-col :span="6"></el-col>
        </el-row>
    </div>
</template>

<script>
export default {
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
        upload() {

            this.$http.post("/manage/product", this.form)
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
