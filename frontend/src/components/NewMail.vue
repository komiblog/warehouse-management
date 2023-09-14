<template>
    <div class="front">
        <el-form ref="form" :model="form" label-width="80px" style="width: 400px">
            <el-form-item label="名称">
                <el-input v-model="form.toid"></el-input>
            </el-form-item>
            <el-form-item label="类别">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="价格">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="数量">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="描述">
                <el-input type="textarea" v-model="form.content"></el-input>
            </el-form-item>
            <!-- <el-form-item label="附件">
                <el-upload class="upload-demo" action="#" :auto-upload="false" multiple :limit="1" :on-change="handleChange"
                    :on-remove="beforeRemove" :on-exceed="handleExceed" :file-list="fileList">
                    <el-button size="small" type="primary">上传<i class="el-icon-upload el-icon--right"></i></el-button>

                    <div slot="tip" class="el-upload__tip">
                        只能上传jpg/png文件，且不超过500kb
                    </div>
                </el-upload>
            </el-form-item> -->

            <el-form-item>
                <el-button type="primary" @click="upload">发送</el-button>
                <el-button @click="$router.push('/dashboard/product')">取消</el-button>
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
                fromid: "",
                toid: "",
                title: "",
                content: "",
                file: "",
            },
            fileList: [],
        };
    },
    methods: {
        upload() {
            let fd = new FormData();
            fd.append("file", this.form.file.raw);
            this.$http.get("/profile/show").then((res) => {
                this.form.fromid = res.data.userid;
            });
            fd.append("content", this.form.content);
            fd.append("fromid", this.form.fromid);
            fd.append("toid", this.form.toid);
            fd.append("title", this.form.title);
            this.$http({
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                method: "post",
                url: "/mail/sendmail",
                data: fd,
            })
                .then((res) => {
                    if (res.data.code === 1) {
                        this.$message.success(res.data.message);
                        this.$router.push("/dashboard/outbox");
                    } else if (res.data.code === 0) {
                        this.$message.warning(res.data.message);
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.$message.warning("请求失败");
                });
        },
        // 获取文件
        handleChange(file, fileList) {
            console.log(fileList[0]);
            this.form.file = fileList[0];
        },

        handleExceed(files, fileList) {
            this.$message.warning(
                `当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length
                } 个文件`
            );
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${file.name}？`);
        },
    },
};
</script>

<style scoped>
.front {
    text-align: left;

    margin: 0 auto;
    width: 50%;
}
</style>
